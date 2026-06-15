import logging
import config
from my_toolkit.my_tools.sqlite3_tools import connect_db
from database import bulk_sync_action, sync_product_entry, sync_variant_entry, sync_price_entry
from my_toolkit.my_tools.my_sql_tools import db_transaction_wrapper, insert_many


def dual_sync(grouped_data):
    """
    [EN] Unified synchronization to both SQLite and MySQL databases.
    Both databases use the same smart bulk_sync_action logic.
    
    [EL] Ενοποιημένος συγχρονισμός σε SQLite και MySQL.
    Και οι δύο βάσεις χρησιμοποιούν την ΙΔΙΑ έξυπνη λογική bulk_sync_action.
    
    Args:
        grouped_data (dict): Grouped product data to synchronize
    
    Returns:
        dict: {"status": "success", "data": {"sqlite": bool, "mysql": bool}, "error_message": None}
              OR {"status": "fail", "data": None, "error_message": str}
    
    ---
    Ενοποιημένος συγχρονισμός σε SQLite και MySQL.
    Και οι δύο βάσεις χρησιμοποιούν πλέον την ΙΔΙΑ έξυπνη λογική bulk_sync_action.
    """
    if not grouped_data:
        logging.warning("No Data for Synchronization")
        return

    # --- 1. SQLITE SYNC ---
    res_sqlite = connect_db(config.DB_PATH)
    if res_sqlite.get('status') == 'success':
        conn = res_sqlite.get('connection')
        try:
            # Η bulk_sync_action περιέχει τα "ταληράκια" (sync_product_entry, κλπ)
            bulk_sync_action(conn, grouped_data)
            logging.info("SQLite: Synchronization completed.")
        except Exception as e:
            logging.error(f"SQLite Error: {e}")
        finally:
            conn.close()

    # --- 2. MYSQL SYNC ---
    logging.info("MySQL: Starting Synchronization...")
    try:
        # ΚΑΛΟΥΜΕ ΤΗΝ ΙΔΙΑ ΣΥΝΑΡΤΗΣΗ bulk_sync_action ΜΕΣΩ ΤΟΥ WRAPPER
        # Αυτό θα εκτελέσει τα 3 στάδια (Product -> Variant -> Price) με έλεγχο τιμής!
        db_transaction_wrapper(config.mysql_config, bulk_sync_action, grouped_data)
        logging.info("MySQL: Synchronization completed.")
    except Exception as e:
        logging.error(f"MySQL Sync Error: {e}")

    logging.info("Double Synchronization completed!")
