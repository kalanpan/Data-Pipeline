"""
Example Configuration File
==========================
"""

from woocommerce import API
import os

# --- WooCommerce API Configuration ---
# [EN] WooCommerce REST API credentials
# [EL] Διαπιστευτήρια WooCommerce REST API
wcapi = API(
    url='https://your-store.com',  # Change to your store URL
    consumer_key='ck_your_consumer_key_here',  # From WooCommerce > Settings > Advanced > REST API
    consumer_secret='cs_your_consumer_secret_here',  # From WooCommerce > Settings > Advanced > REST API
    version='wc3'
)

# --- Database Configuration ---
# [EN] SQLite database path
# [EL] Διαδρομή βάσης δεδομένων SQLite
DB_PATH = os.path.join(os.path.dirname(__file__), 'db', 'my_database.db')

# --- MySQL Configuration (Optional) ---
# [EN] MySQL connection settings
# [EL] Ρυθμίσεις σύνδεσης MySQL
mysql_config = {
    'host': 'localhost',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'your_database_name'
}

# --- Scraping Configuration ---
# [EN] URLs and categories to scrape
# [EL] URLs και κατηγορίες για scraping
scraping_urls = [
    {
        'title': 'Category 1',
        'url': 'https://example-shop.com/category-1'
    },
    {
        'title': 'Category 2',
        'url': 'https://example-shop.com/category-2'
    }
]

# --- Notification Settings (Optional) ---
# [EN] Telegram/Email notifications
# [EL] Ειδοποιήσεις Telegram/Email
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_telegram_chat_id'
