import logging
from urllib.parse import urljoin


# --- [1] URL FILTERS ---

def is_valid_url(url, domain="example-shop.com"):
    """
    [EN] Validates if URL belongs to the target domain.
    [EL] Ελέγχει αν το URL ανήκει στο domain που μας ενδιαφέρει.
    
    Args:
        url (str): The URL to validate
        domain (str): The target domain (default: "example-shop.com")
    
    Returns:
        bool: True if valid, False otherwise
    """
    if not url: return False
    return domain in url and "community" not in url


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
def organize_category_map(data, custom_mapping=None):
    """
    [EN] Organizes categories into logical groups based on URL keywords.
    [EL] Οργανώνει τις κατηγορίες σε λογικές ομάδες βάσει λέξεων-κλειδιών URL.
    
    Args:
        data (list): List of category dictionaries with 'title' and 'url'
        custom_mapping (dict, optional): Custom category mapping. Defaults to generic mapping.
    
    Returns:
        dict: Organized categories with items grouped by type
    """
    # Default generic mapping (can be overridden)
    default_mapping = {
        "Electronics": ["electronics", "devices", "gadgets"],
        "Mobile": ["mobile", "phones", "smartphones"],
        "Computing": ["computers", "laptops", "gaming"],
        "Accessories": ["accessories", "cases", "chargers"]
    }
    
    mapping = custom_mapping if custom_mapping else default_mapping
    organized = {key: [] for key in mapping.keys()}
    organized["Uncategorized"] = []

    for item in data:
        assigned = False
        url_lower = item['url'].lower()
        for cat, keywords in mapping.items():
            if any(kw in url_lower for kw in keywords):
                organized[cat].append(item)
                assigned = True
                break
        if not assigned:
            organized["Uncategorized"].append(item)
    
    return organized
