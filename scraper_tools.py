import logging
from urllib.parse import urljoin


# --- [1] URL FILTERS ---

def is_valid_url(url):
    """Ελέγχει αν το URL ανήκει στο domain που μας ενδιαφέρει."""
    if not url: return False
    return "kaizershop.gr" in url and "community" not in url


def get_unique_urls(url_list):
    """Καθαρίζει τη λίστα από διπλάτυπα και άκυρα URLs."""
    return list(set([url for url in url_list if is_valid_url(url)]))


# --- [2] NAVIGATION TOOLS ---

def choose_category(soup_obj):
    """Βρίσκει όλες τις κατηγορίες από το κεντρικό μενού."""
    all_categories = []
    try:
        # Ψάχνουμε τα links του Megamenu
        links = soup_obj.find_all('a', class_='megamenu-category-title-inner')
        if not links:
            links = soup_obj.select('li > a')

        for link in links:
            title = link.get('title') or link.get_text(strip=True)
            url = link.get('href')
            if title and url:
                all_categories.append({"title": title, "url": url})

        return all_categories
    except Exception as e:
        logging.error(f"Error finding categories: {e}")
        return []


def get_urls_from_category_html(soup_obj):
    """Παίρνει τα URLs των προϊόντων από μια σελίδα κατηγορίας (λιστάνθιση)."""
    urls = []
    products = soup_obj.find_all('div', class_='product-layout')

    for product in products:
        link_tag = product.select_one('.product-name a')
        if link_tag and link_tag.get('href'):
            urls.append(link_tag.get('href'))

    return list(set(urls))


# --- [3] CATEGORY MAPPING (Optional) ---
def organize_kaizer_map(data):
    """Οργάνωση των κατηγοριών σε ομάδες (Smartphones, Accessories κλπ)."""
    mapping = {
        "Smartphones": ["cell-phones", "smartphones", "apple", "samsung", "xiaomi"],
        "Home_Appliances": ["gia-to-spiti", "tv", "vacuum", "kitchen"],
        "Computing_Gaming": ["consoles", "gaming", "perifereiaka"],
        "Accessories": ["accessories", "cases", "chargers"]
    }
    organized = {key: [] for key in mapping.keys()}
    organized["Uncategorized"] = []

    for item in data:
        assigned = False
        url_l = item['url'].lower()
        for cat, keywords in mapping.items():
            if any(kw in url_l for kw in keywords):
                organized[cat].append(item)
                assigned = True
                break
        if not assigned: organized["Uncategorized"].append(item)
    return organized