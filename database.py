import re
import config
import logging
import sqlite3
from my_toolkit.my_tools.sqlite3_tools import (
    connect_db, init_schema, close_connection,
    insert_many, query_db, update_record
)

# --- CONFIGURATION (Schemas) ---
SCHEMAS = [
    """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL UNIQUE,
        screen_size REAL,
        battery_mah INTEGER,
        cpu_model TEXT,
        main_camera_mp REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS variants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        external_id TEXT UNIQUE, 
        storage_gb REAL,
        ram_gb REAL,
        color TEXT,
        product_link TEXT,
        availability TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        variant_id INTEGER,
        price REAL NOT NULL,
        price_no_vat REAL,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (variant_id) REFERENCES variants(id) ON DELETE CASCADE
    );
    """
]


MYSQL_SCHEMAS = [
    """
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        brand VARCHAR(100) NOT NULL,
        model VARCHAR(255) NOT NULL UNIQUE,
        screen_size DECIMAL(5,2),
        battery_mah INT,
        cpu_model VARCHAR(255),
        main_camera_mp DECIMAL(5,2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    """,
    """
    CREATE TABLE IF NOT EXISTS variants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        external_id VARCHAR(255) UNIQUE, 
        storage_gb DECIMAL(10,2),
        ram_gb DECIMAL(10,2),
        color VARCHAR(100),
        product_link VARCHAR(750),
        availability VARCHAR(100),
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
    ) ENGINE=InnoDB;
    """,
    """
    CREATE TABLE IF NOT EXISTS price_history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        variant_id INT,
        price DECIMAL(10,2) NOT NULL,
        price_no_vat DECIMAL(10,2),
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (variant_id) REFERENCES variants(id) ON DELETE CASCADE
    ) ENGINE=InnoDB;
    """
]

def init_new_db():
    db_path = r'C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db'
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        for sql in SCHEMAS:
            cursor.execute(sql)

        conn.commit()
        conn.close()
        print("Η βάση δημιουργήθηκε επιτυχώς με το νέο schema!")
    except Exception as e:
        print(f"Σφάλμα κατά τη δημιουργία: {e}")




# --- INFRASTRUCTURE ---

def db_transaction_wrapper(action_func, *args, **kwargs):
    """Lifecycle Management της σύνδεσης."""
    db_resp = connect_db(config.DB_PATH)
    if db_resp.get("status") != "success":
        logging.error(f"DB Connection Error: {db_resp.get('message')}")
        return None

    conn = db_resp.get("connection")
    try:
        result = action_func(conn, *args, **kwargs)
        return result
    except Exception as e:
        logging.error(f"Transaction Error: {e}")
        return None
    finally:
        close_connection(conn)


def db_init(conn):
    """Αρχικοποιεί τους πίνακες. ΔΕΝ κλείνει τη σύνδεση εδώ."""
    logging.info("Αρχικοποίηση πινάκων...")
    try:
        for s in SCHEMAS:
            init_schema(conn, s)
        logging.info("Η δομή της βάσης αρχικοποιήθηκε επιτυχώς.")
        return True
    except Exception as e:
        logging.error(f"Σφάλμα στο init: {e}")
        return False


def erase_all_db(conn):
    """Καθαρίζει τα δεδομένα. Καλούμε μέσω wrapper."""
    tables = ['price_history', 'variants', 'products']
    for table in tables:
        try:
            conn.execute(f"DELETE FROM {table}")
            conn.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'")
            logging.info(f"Πίνακας {table} καθαρίστηκε.")
        except Exception:
            pass
    conn.commit()


def sync_product_entry(cursor, info, is_mysql=True):
    # 1. Καθαρισμός δεδομένων
    brand = str(info.get('brand', 'UNKNOWN')).upper().strip()
    raw_model = info.get('model', info.get('model_name', 'UNKNOWN'))
    clean_name = "".join(c for c in str(raw_model).strip().upper() if c.isalnum() or c.isspace())

    p = "%s" if is_mysql else "?"

    # 2. Εκτέλεση Insert
    if is_mysql:
        sql_insert = f"""
            INSERT INTO products (brand, model, screen_size, battery_mah, cpu_model, main_camera_mp)
            VALUES ({p}, {p}, {p}, {p}, {p}, {p})
            ON DUPLICATE KEY UPDATE brand=brand
        """
    else:
        sql_insert = (f"INSERT OR IGNORE INTO products (brand, model, screen_size, battery_mah, cpu_model, main_camera_mp) "
                      f"VALUES ({p},{p},{p},{p},{p},{p})")

    params = (
        brand, clean_name,
        info.get('screen_size'), info.get('battery_mah'),
        info.get('cpu_model'), info.get('main_camera_mp')
    )

    #logging.info(f"DEBUG: Executing Insert for {clean_name}...")
    cursor.execute(sql_insert, params)

    # 3. Εκτέλεση Select
    sql_select = f"SELECT id FROM products WHERE model = {p}"
    #logging.info(f"DEBUG: Executing Select with param: '{clean_name}'")
    cursor.execute(sql_select, (clean_name,))

    res = cursor.fetchone()

    # Εδώ είναι η παγίδα: Αν το res είναι None, το res[0] θα πετάξει το error που είδες
    if res is None:
        logging.info(f"ERROR: Product '{clean_name}' was NOT found in DB after insert!")
        return {"status": "error", "message": f"Model {clean_name} not found after insert"}

    #logging.info(f"Found ID {res[0]}")
    return {"status": "success", "product_id": res[0], "model": clean_name}


def sync_variant_entry(cursor, p_id, v_data, is_mysql=True):
    """
    Διαχειρίζεται το Variant, αποθηκεύει το Image URL και επιστρέφει το ID.
    """
    ext_id = str(v_data.get('external_id')).strip()
    img_url = v_data.get('image_url')
    p = "%s" if is_mysql else "?"

    try:
        # 1. Έλεγχος αν υπάρχει ήδη
        cursor.execute(f"SELECT id FROM variants WHERE external_id = {p}", (ext_id,))
        res = cursor.fetchone()

        if res:
            v_id = res[0]
            # UPDATE: Ενημερώνουμε διαθεσιμότητα ΚΑΙ το image_url (για να γεμίσει το NULL)
            sql_upd = f"UPDATE variants SET product_id = {p}, availability = {p}, image_url = {p} WHERE id = {p}"
            cursor.execute(sql_upd, (p_id, v_data['availability'], img_url, v_id))
        else:
            # INSERT: Προσθήκη νέου Variant με το Image URL
            sql_ins = f"""
                INSERT INTO variants (product_id, external_id, storage_gb, ram_gb, color, product_link, availability, image_url)
                VALUES ({p}, {p}, {p}, {p}, {p}, {p}, {p}, {p})
            """
            cursor.execute(sql_ins, (
                p_id, ext_id, v_data['storage_gb'], v_data['ram_gb'],
                v_data['color'], v_data['product_link'], v_data['availability'], img_url
            ))

            if is_mysql:
                cursor.execute("SELECT LAST_INSERT_ID()")
                v_id = cursor.fetchone()[0]
            else:
                v_id = cursor.lastrowid

        return {"status": "success", "variant_id": v_id}

    except Exception as e:
        logging.error(f"Variant Error for SKU {ext_id}: {e}")
        return {"status": "error", "message": str(e)}



def sync_price_entry(cursor, v_id, ext_id, current_p, price_no_vat, is_mysql=True):
    """
    Ελέγχει την τελευταία τιμή και κάνει insert ΜΟΝΟ αν υπάρχει διαφορά.
    """
    p = "%s" if is_mysql else "?"
    clean_ext_id = str(ext_id).strip()

    try:
        # 1. Φέρνουμε την τελευταία τιμή για αυτό το external_id
        sql_check = f"SELECT price FROM price_history WHERE external_id = {p} ORDER BY id DESC LIMIT 1"
        cursor.execute(sql_check, (clean_ext_id,))
        row = cursor.fetchone()

        should_insert = False

        if row:
            last_p = float(row[0])
            diff = abs(last_p - current_p)
            #logging.info(f"DEBUG: Found last price {last_p}€ for {clean_ext_id}. Current: {current_p}€. Diff: {diff:.4f}")

            if diff > 0.01:
                logging.info(f"DEBUG: Price changed! (Diff > 0.01)")
                should_insert = True
            #else:
               # logging.info(f"DEBUG: Price is the same. Skipping insert.")
        else:
            logging.info(f"DEBUG: No previous price found for {clean_ext_id}. First time insert.")
            should_insert = True

        # 2. Insert αν χρειάζεται
        if should_insert:
            sql_ins = f"INSERT INTO price_history (variant_id, external_id, price, price_no_vat) VALUES ({p}, {p}, {p}, {p})"
            cursor.execute(sql_ins, (v_id, clean_ext_id, current_p, price_no_vat))
            logging.info(f"New Price Record Created!")
            return {"status": "success", "action": "inserted"}

        return {"status": "success", "action": "skipped"}

    except Exception as e:
        logging.info(f"Price Error: {e}")
        return {"status": "error", "message": str(e)}


def bulk_sync_action(conn, grouped_data):
    if conn is None: return False
    cursor = conn.cursor()
    is_mysql = hasattr(conn, 'database') or 'mysql' in str(type(conn)).lower()

    counts = {"products": 0, "variants": 0, "prices": 0}

    for f_key, data in grouped_data.items():
        # --- ΣΤΑΔΙΟ 1: PRODUCT ---
        p_res = sync_product_entry(cursor, data['info'], is_mysql)
        if p_res['status'] != 'success': continue
        p_id = p_res['product_id']
        counts["products"] += 1

        for v in data['variants']:
            # --- ΣΤΑΔΙΟ 2: VARIANT ---
            v_res = sync_variant_entry(cursor, p_id, v, is_mysql)
            if v_res['status'] != 'success': continue
            v_id = v_res['variant_id']
            counts["variants"] += 1

            # --- ΣΤΑΔΙΟ 3: PRICE HISTORY ---
            pr_res = sync_price_entry(cursor, v_id, v['external_id'], float(v['price']), v['price_no_vat'], is_mysql)
            if pr_res.get('action') == 'inserted':
                counts["prices"] += 1

    conn.commit()
    logging.info(
        f"Sync Summary: {counts['products']} Products, {counts['variants']} Variants, {counts['prices']} New Prices.")
    return {"status": "success", "message": "Bulk sync completed successfully"}