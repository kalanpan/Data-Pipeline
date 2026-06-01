import os
import logging
import config
import time
import db_manager
from wp_sync import sync_to_woocommerce
from scraper_tools import get_urls_from_category_html, get_unique_urls
from pipline import run_pipeline
from my_toolkit.my_tools.web_tools import fetch_html, parse_html
from my_toolkit.my_tools.logger_tools import setup_logging

# --- [1] CONTROL PANEL (Διακόπτες) ---
SETTINGS = {
    "SYNC_DB": True,  # Ενημέρωση SQLite/MySQL
    "SYNC_WOO": True,  # Ενημέρωση WooCommerce
    "LIMIT_PER_CAT": None,  # Βάλε αριθμό (π.χ. 2) για γρήγορο τεστ, αλλιώς None
    "SLEEP_BETWEEN": 3  # Δευτερόλεπτα αναμονής μεταξύ requests
}

setup_logging()
start_time = time.time()

def main():
    logging.info("--- STARTING SCRAPING ---")

    # --- [2] STATISTICS TRACKER ---
    global_stats = {
        "categories_processed": 0,
        "total_urls_found": 0,
        "total_final_data": 0,
        "status": "Success"
    }

    for item in config.scraping_urls:
        brand = item['title']
        url = item['url']

        logging.info(f"\n>>> CATEGORY-BRAND: {brand}")
        global_stats["categories_processed"] += 1

        try:
            # 1. Discovery
            raw_html = fetch_html(url)
            if raw_html.get('status') != 'success':
                logging.error(f"Fail to connect to  {brand}")
                continue

            parse_result = parse_html(raw_html['data'])
            soup = parse_result.get('soup')
            if not soup: continue

            raw_urls = get_urls_from_category_html(soup)
            clean_urls = get_unique_urls(raw_urls)

            # Εφαρμογή ορίου για δοκιμές (LIMIT_PER_CAT)
            if SETTINGS["LIMIT_PER_CAT"]:
                clean_urls = clean_urls[:SETTINGS["LIMIT_PER_CAT"]]

            global_stats["total_urls_found"] += len(clean_urls)

            if clean_urls:
                logging.info(f"Processing {len(clean_urls)} items for {brand}...")

                # 2. Pipeline (Scraping & Internal Logic)
                final_data = run_pipeline(clean_urls)

                if final_data:
                    global_stats["total_final_data"] += len(final_data)

                    # 3. Database Control
                    if SETTINGS["SYNC_DB"]:
                        db_manager.dual_sync(final_data)
                    else:
                        logging.info("DB Sync: SKIPPED (By User Settings)")

                    # 4. WooCommerce Control
                    if SETTINGS["SYNC_WOO"]:
                        sync_to_woocommerce(final_data)
                    else:
                        logging.info("WooCommerce Sync: SKIPPED (By User Settings)")

        except Exception as e:
            logging.error(f"Problem at {brand}: {e}")
            global_stats["status"] = "Partial Error"

        # --- [3] FINAL SUMMARY REPORT ---
        db_status = "OK" if SETTINGS['SYNC_DB'] else "Base is out of sync"
        woo_status = "OK" if SETTINGS['SYNC_WOO'] else "WooCommerce is out of sync"
        end_time = time.time()
        duration = round((end_time - start_time) / 60, 2)

        summary_report = (
            f"\n{'=' * 40}\n"
            f" JOB REPORT\n"
            f"{'=' * 40}\n"
            f"Categories Scanned : {global_stats['categories_processed']}\n"
            f"Total URLs Found: {global_stats['total_urls_found']}\n"
            f"Products Approved : {global_stats['total_final_data']}\n"
            f"Database Updated : {db_status}\n"
            f"WooCommerce Updated : {woo_status}\n"
            f"Status : {global_stats['status']}\n"
            f"Duration of job  : {duration} mins\n"
            f"{'=' * 40}"
        )

        # Το γράφουμε στο Log (INFO level)
        logging.info(summary_report)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()

