import re
import json
import logging
from my_toolkit.my_tools.logger_tools import setup_logging

setup_logging()

def get_url(soup):
    urls = []
    # Βρίσκουμε όλα τα blocks των προϊόντων
    tag = soup.find_all('div', class_='product-layout')

    if tag:
        logging.info(f"Found {len(tag)} models")
        for model in tag:
            # Βρίσκουμε το <a> μέσα στο <h3>
            link_tag = model.find('h3', class_='product-name').find('a')

            if link_tag:
                full_name = link_tag.text.strip()
                # Μετατρέπουμε σε κεφαλαία για να μην έχουμε θέμα με το ταίριασμα
                if full_name.upper().startswith('APPLE IPHONE'):
                    data = {
                        'name': full_name,
                        'url': link_tag.get('href')
                    }

                    urls.append(data)
    return urls


def extract_json_data(soup_obj):
    """Εξάγει δεδομένα από το dataLayer script του myshop"""
    scripts = soup_obj.find_all('script')
    for script in scripts:
        if 'gtin' in script.text:
            # Ψάχνουμε το κομμάτι που ξεκινάει από {"id":"... και τελειώνει σε }
            match = re.search(r'\{"id":"\d+".*?"gtin":"(\d+)"', script.text)
            if match:
                # Επιστρέφουμε το Barcode (GTIN)
                gtin = match.group(1)
                return {"barcode": gtin}
    return {"barcode": None}

def get_category_from_script(soup):
    html_str = str(soup)
    match = re.search(r"['\"]category['\"]\s*:\s*['\"](.*?)['\"]", html_str)

    if match:
        raw_cat = match.group(1)
        # Αυτό το μαγικό κόλπο μετατρέπει το \u039a σε "Κ"
        clean_cat = raw_cat.encode().decode('unicode_escape')
        return clean_cat

    return "N/A"

def get_id_product(soup):
    tag = soup.select_one('.sku')
    if tag:
        text = tag.get_text(strip=True)
        try:
            return text.split(":")[1].strip()
        except:
            return "N/A"
    return "N/A"

def brand_name(soup):
    tag = soup.select_one('.manufimage a')
    val = tag.get_text(strip=True) if tag else "N/A"
    return  val

def get_model_from_url(url):
    split_url = url.split('/')
    slug = split_url[-1]
    match = re.search(r'(.*?)-(?:\d+gb|black|white|blue|green|pink|yellow|natural|titanium|ultramarine|lavender)', slug,re.IGNORECASE)

    if match:
        model = match.group(1).replace('-', ' ').upper()
        return model if model else "N/A"
    else:
        clean_model = re.sub(r'-(?:\d+gb|black|white|eu|mtp\d+).*$', '', slug, flags=re.IGNORECASE)
        model_error = clean_model.replace('-', ' ').upper()
        return model_error

def get_availability(soup):
    availability_tag = soup.find('div', class_='stock')
    if availability_tag:
        text =  availability_tag.get_text(strip=True)
        return text if text else "N/A"
    return None

def get_price(soup):
    price_tag = soup.select_one('.product-price-container')
    if price_tag:
        text = price_tag.get_text(strip=True)
        clean_val = text.replace('€', '').replace('.', '').replace(',', '.').strip()
        try:
            price_final = float(clean_val)
            return price_final if price_final else "N/A"
        except ValueError:
            price_final = 0.0
    return 0.0

def no_vat_price(soup):
    no_vat_price_tag = soup.select_one('.novat_price')
    if no_vat_price_tag:
        text = no_vat_price_tag.get_text(strip=True)
        clean_nv = re.sub(r'[^\d,.]', '', text)
        clean_nv = clean_nv.replace('.', '').replace(',', '.')
        try:
            clean_nv = float(clean_nv)
            no_vat_price_final = clean_nv
            return no_vat_price_final if no_vat_price_final else 0.0
        except ValueError:
            no_vat_price_final = 0.0
    return 0.0


def get_product_specs(soup_obj):

    spec_table = soup_obj.find('table', class_='table-bordered')

    if not spec_table:
        return {
            "status": "success",
            "value": {},
            "error_message": "No specification table found on this page"
        }

    specs_dict = {}
    try:
        # 2. Λούπα σε κάθε γραμμή του πίνακα
        rows = spec_table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 2:
                # Καθαρισμός κλειδιού (π.χ. "Επεξεργαστής:") και τιμής
                key = cols[0].get_text(strip=True).replace(':', '')
                value = cols[1].get_text(strip=True)
                specs_dict[key] = value

        return {
            "status": "success",
            "value": specs_dict,
            "error_message": None
        }

    except Exception as e:
        return {
            "status": "error",
            "value": {},
            "error_message": f"Error parsing specs: {str(e)}"
        }


def transform_specs(specs_dict):
    """
    Μετατρέπει τα ακατέργαστα specs σε καθαρά δεδομένα.
    Διαχειρίζεται δεκαδικά με κόμμα, μονάδες MB/GB/TB και καθαρίζει τα strings.
    """
    transformed = {
        "storage_gb": 0.0,
        "ram_gb": 0.0,
        "screen_size": 0.0,
        "battery_mah": 0,
        "cpu_model": "N/A",
        "main_camera_mp": 0.0
    }

    # Helper για μετατροπή κειμένου σε float 
    def parse_to_float(text):
        if not text: return 0.0
        # Αντικατάσταση κόμματος με τελεία και εύρεση αριθμού (ακέραιου ή δεκαδικού)
        match = re.search(r'(\d+[.,]?\d*)', text.replace(',', '.'))
        return float(match.group(1)) if match else 0.0

    # 1. Εσωτερική Μνήμη (Storage & RAM)
    # Παράδειγμα: "0,032 GB +RAM 0,032 GB" ή "128GB 4GB RAM"
    mem_raw = specs_dict.get('Εσωτερική Μνήμη', '').replace(',', '.')

    # regex που βρίσκει συνδυασμούς αριθμού και μονάδας
    mem_matches = re.findall(r'(\d+\.?\d*)\s*(GB|MB|TB)', mem_raw, re.IGNORECASE)

    for i, (val, unit) in enumerate(mem_matches):
        num = float(val)
        # Μετατροπή όλων σε GB για ομοιομορφία στη βάση
        if unit.upper() == "TB": num *= 1024
        if unit.upper() == "MB": num /= 1024

        # Λογική διαχωρισμού:
        # Αν το string περιέχει "RAM" κοντά στον αριθμό ή αν είναι η δεύτερη μέτρηση
        if "RAM" in mem_raw.upper() and i > 0:
            transformed["ram_gb"] = round(num, 3)
        elif i == 0:
            transformed["storage_gb"] = round(num, 3)
        elif i == 1:  # Αν βρει δεύτερο νούμερο χωρίς "RAM" label, συνήθως είναι η RAM
            transformed["ram_gb"] = round(num, 3)

    # 2. Μέγεθος Οθόνης (π.χ. "6.1 inches" ή "2,4 \"")
    screen_raw = specs_dict.get('Μέγεθος Οθόνης', '')
    transformed["screen_size"] = parse_to_float(screen_raw)

    # 3. Μπαταρία (π.χ. "3240 mAh" ή "1400mAh")
    battery_raw = specs_dict.get('Μπαταρία', '')
    battery_match = re.search(r'(\d+)', battery_raw)
    if battery_match:
        transformed["battery_mah"] = int(battery_match.group(1))

    # 4. Επεξεργαστής (Κρατάμε μόνο την πρώτη γραμμή/μοντέλο)
    cpu_raw = specs_dict.get('Επεξεργαστής', 'N/A')
    # Καθαρισμός από αλλαγές γραμμής και περιττά κενά
    transformed["cpu_model"] = cpu_raw.split('\n')[0].split('\r')[0].strip()

    # 5. Ανάλυση Κάμερας (π.χ. "50 MP" ή "0.08MP")
    camera_raw = specs_dict.get('Ανάλυση Κάμερας', '0')
    transformed["main_camera_mp"] = parse_to_float(camera_raw)

    return transformed


def parse_product(name, brand):
    import re

    s = name
    brand = brand.upper()

    if s.startswith(brand):
        s = s[len(brand):].strip()

    # storage
    storage_match = re.search(r'(\d+)\s?GB', s)
    storage = int(storage_match.group(1)) if storage_match else None

    # colors
    colors = [
        'BLACK','WHITE','BLUE','RED','MIDNIGHT','STARLIGHT','PINK',
        'TEAL','ULTRAMARINE','LAVENDER','SAGE','GOLD','SILVER'
    ]

    color = None
    for c in colors:
        if c in s:
            color = c
            break

    # clean model
    s = re.sub(r'\d+\s?GB', '', s)
    s = re.sub(r'\b(INDIA|INDIAN SPEC|SPEC|NATURAL|REFURBISHED|GRADE|A|COSMIC|TITANIUM|DEEP|5G|ORANGE|MIST)\b', '', s)
    s = re.sub(r'\b\d{6,}\b', '', s)

    for c in colors:
        s = s.replace(c, '')

    model = ' '.join(s.split()).strip()

    return {
        "model": model,
        "storage": storage,
        "color": color
    }




def clean_model_name(model_str, brand):
    """Καθαρίζει το όνομα μοντέλου από brand, SKU και σκουπίδια."""
    model_str = model_str.upper().replace('-', ' ')
    brand = brand.upper()

    # Αφαίρεση του brand αν υπάρχει στην αρχή
    if model_str.startswith(brand):
        model_str = model_str[len(brand):].strip()

    # Αφαίρεση SKU (π.χ. LAM113164)
    model_str = re.sub(r'[A-Z]{2,}\d{3,}', '', model_str)

    # Αφαίρεση λέξεων που χαλάνε την ομαδοποίηση
    junk = ['DUAL SIM', 'MOBILE PHONE', 'SIM', 'RED', 'BLUE', 'BLACK', 'WHITE', 'GOLD', 'SILVER']
    for word in junk:
        model_str = model_str.replace(word, '')

    return ' '.join(model_str.split()).strip()

def extract_color_from_url(url):
    """Βγάζει το χρώμα από το slug του URL."""
    slug = url.split('/')[-1]
    match = re.search(r'mobile-phone-(.*)-[a-z]+\d+', slug)
    if match:
        return match.group(1).replace('-', ' ').title()
    return "Standard"


def get_image_url(soup):
    """
    [EL] Περιγραφή: Εξάγει το URL της κεντρικής εικόνας του προϊόντος.
    [EN] Description: Extracts the main product image URL.
    """
    # Δοκιμάζουμε πρώτα το αριστερό column που βρήκαμε ότι δουλεύει
    container = soup.select_one(".product-column-left")

    if container:
        # Ψάχνουμε το πρώτο img με κλάση img-responsive
        img_tag = container.select_one("img.img-responsive")
        if img_tag:
            url = img_tag.get("src")
            # Καθαρισμός αν το URL είναι σχετικό (relative)
            if url and url.startswith('//'):
                url = "https:" + url
            return url

    return "N/A"


def product_creator(soup_obj, url):
    """
    Συναρμολογεί όλα τα δεδομένα χρησιμοποιώντας τους Scrapers & Parsers.
    """
    # 1. Παίρνουμε τα δύο βασικά containers
    right_container = soup_obj.select_one('.product-column-right')
    left_container = soup_obj.select_one('.product-column-left')  # photo

    if not right_container:
        return {"status": "error", "error_message": "Right layout container missing"}

    try:
        # Χρήση των Scrapers/Parsers
        raw_specs = get_product_specs(right_container).get('value', {})
        clean_specs = transform_specs(raw_specs)
        brand = brand_name(right_container)

        # Καθαρισμός ονόματος για την οικογένεια (Family)
        model_base = clean_model_name(get_model_from_url(url), brand)
        family_model = f"{brand} {model_base}".upper()

        return {
            "status": "success",
            "data": {
                # Στοιχεία για Products Table
                "family_model": family_model,
                "product_brand": brand,
                "screen_size": clean_specs["screen_size"],
                "battery_mah": clean_specs["battery_mah"],
                "cpu_model": clean_specs["cpu_model"],
                "main_camera_mp": clean_specs["main_camera_mp"],

                # Στοιχεία για Variants Table
                "external_id": get_id_product(right_container),
                "storage_gb": clean_specs["storage_gb"],
                "ram_gb": clean_specs["ram_gb"],
                "color": extract_color_from_url(url),
                "product_availability": get_availability(right_container),
                "product_link": url,

                # Στοιχεία για φωτογραφία
                "image_url": get_image_url(soup_obj),

                # Στοιχεία για Price History
                "product_price": get_price(right_container),
                "product_no_vat": no_vat_price(right_container)
            }
        }

    except Exception as e:
        return {"status": "error", "error_message": f"Mapping error: {str(e)}"}


import re
import json


def extract_datalayer_data(soup_obj):
    """
    Αναζητά και εξάγει δεδομένα από το Google/Facebook DataLayer script.
    Λειτουργεί ως fallback αν οι selectors αποτύχουν.
    """
    fallback_data = {
        'external_id': None,
        'barcode': None,
        'price': None,
        'name': None,
        'brand': None
    }

    scripts = soup_obj.find_all('script')
    for script in scripts:
        content = script.text
        # Ψάχνουμε το σημείο που περιέχει το GTIN ή το Product ID
        if 'gtin' in content or '"id":' in content:
            try:
                # 1. Regex για να απομονώσουμε το πρώτο JSON object που μοιάζει με προϊόν
                # Ψάχνει το μοτίβο {"id":"...", "name":"...", ... "gtin":"..."}
                match = re.search(
                    r'\{"id":"(?P<id>\d+)","name":"(?P<name>.*?)","price":"(?P<price>.*?)".*?"gtin":"(?P<gtin>\d+)"',
                    content)

                if match:
                    fallback_data['external_id'] = match.group('id')
                    fallback_data['name'] = match.group('name')
                    fallback_data['price'] = float(match.group('price'))
                    fallback_data['barcode'] = match.group('gtin')

                    # 2. Προσπάθεια για Brand (συχνά είναι λίγο πιο μετά στο script)
                    brand_match = re.search(r'"brand":"(?P<brand>.*?)"', content)
                    if brand_match:
                        fallback_data['brand'] = brand_match.group('brand')

                    return fallback_data
            except Exception:
                continue

    return fallback_data


def product_creator_2(soup_obj, url):
    """
    Εξάγει RAW δεδομένα από τη σελίδα.
    Δεν παίρνει αποφάσεις για το schema, απλώς μαζεύει πληροφορία.
    """
    right_container = soup_obj.select_one('.product-column-right')

    if not right_container:
        return {"status": "error", "error_message": "Right layout container missing"}

    try:
        # 1. Μαζεύουμε τα RAW δεδομένα (χωρίς μετασχηματισμούς ακόμα)
        raw_specs = get_product_specs(right_container).get('value', {})
        brand = brand_name(right_container)

        # 2. Επιστρέφουμε ένα flat dictionary με "πρώτη ύλη"
        return {
            "status": "success",
            "data": {
                "product_brand": brand,
                "family_model": get_model_from_url(url),  # Το ακατέργαστο όνομα από το URL
                "raw_specs": raw_specs,  # Σημαντικό: Τα στέλνουμε όλα πακέτο
                "external_id": get_id_product(right_container),
                "product_availability": get_availability(right_container),
                "image_url": get_image_url(soup_obj),
                "product_price": get_price(right_container),
                "product_no_vat": no_vat_price(right_container),
                # Προσθέτουμε τυχόν κωδικούς μοντέλου αν υπάρχουν
                "model_code": None  # Συμπληρώνεται αν βρεις MPN/SKU
            }
        }
    except Exception as e:
        return {"status": "error", "error_message": f"Extraction error: {str(e)}"}



def normalize_availability(raw_status):
    status = raw_status.lower()
    if any(x in status for x in ['άμεσα', 'διαθέσιμο', 'απόθεμα']):
        return "IN_STOCK"
    if any(x in status for x in ['παραγγελία', 'αναμένεται']):
        return "PREORDER"
    return "OUT_OF_STOCK"


def get_scrape_json_data(soup, url):
    """
    [EN] Extracts product data from embedded JSON dataLayer scripts.
    Combines HTML scraping with JSON parsing for comprehensive data extraction.
    
    [EL] Εξάγει δεδομένα προϊόντος από ενσωματωμένα JSON dataLayer scripts.
    Συνδυάζει HTML scraping με JSON parsing για ολοκληρωμένη εξαγωγή δεδομένων.
    
    Args:
        soup (BeautifulSoup): The parsed HTML object
        url (str): The product URL
    
    Returns:
        dict: Structured product data with products_table, variants_table, 
              store_details_table, and price_history_table
              OR None if extraction fails
    """
    target_script = soup.find('script', string=re.compile(r'gtin'))
    if not target_script: return None

    content = target_script.string
    match = re.search(r'"products"\s*:\s*(\[.*?\])', content)

    if match:
        try:
            products = json.loads(match.group(1))
            if not products: return None
            product = products[0]

            # 1. HTML Scraping & Internal Functions
            raw_specs = get_product_specs(soup).get('value', {})
            clean_specs = transform_specs(raw_specs)
            brand = product.get('brand', 'Apple').upper()
            raw_name = product.get('name', '').upper()
            name_data = parse_product(raw_name, brand)

            # 2. Logic για Condition & New Release
            condition = 'NEW'
            if any(x in raw_name for x in ['USED', 'METAXEIRISMENO', 'REFURBISHED']):
                condition = 'USED'

            is_new = 1 if 'NEW' in raw_name or '2026' in raw_name else 0

            # 3. ΤΕΛΙΚΗ ΔΟΜΗ (Αντιστοιχία 1:1 με το Schema)
            return {
                # Table: products
                "products_table": {
                    "brand": brand,
                    "model": name_data['model'],
                    "category": product.get('category'),
                    "is_new_release": is_new,
                    "screen_size": clean_specs["screen_size"],
                    "battery_mah": clean_specs["battery_mah"],
                    "cpu_model": clean_specs["cpu_model"],
                    "main_camera_mp": clean_specs["main_camera_mp"],
                    "specs_json": json.dumps(raw_specs, ensure_ascii=False)
                },

                # Table: variants
                "variants_table": {
                    "barcode": product.get('gtin'),
                    "external_id": str(product.get('id')),
                    "storage_gb": clean_specs["storage_gb"],
                    "ram_gb": clean_specs["ram_gb"],
                    "color": name_data['color'] if name_data['color'] else extract_color_from_url(url),
                    "condition": condition,
                    "image_url": get_image_url(soup)
                },

                # Table: store_details
                "store_details_table": {
                    "store_name": "example_store",
                    "source_scraper": "generic_json_hybrid",
                    "product_link": url,
                    "availability_raw": get_availability(soup),
                    "availability_normalized": normalize_availability(get_availability(soup) or "")
                },

                # Table: price_history
                "price_history_table": {
                    "price": float(product.get('price', 0)),
                    "price_no_vat": no_vat_price(soup),
                    "discount_amount": float(product.get('discount', 0)),
                    "coupon_code": product.get('coupon')
                }
            }
        except Exception as e:
            logging.error(f"Error: {e}")
            return None
    return None


def fallback_manual_parse(content):
    # Εμπλουτίζουμε και το fallback για να μην κρασάρει το Insert
    gtin = re.search(r'"gtin"\s*:\s*"(\d+)"', content)
    price = re.search(r'"price"\s*:\s*"([\d.]+)"', content)
    name = re.search(r'"name"\s*:\s*"([^"]+)"', content)

    if gtin and price:
        return {
            'gtin': gtin.group(1),
            'price': price.group(1),
            'name': name.group(1) if name else "Unknown",
            'condition': 'NEW',
            'is_new_release': 0,
            'is_active': 1
        }
    return None

