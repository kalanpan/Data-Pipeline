import config
import logging


def build_product_payload(brand, model_name, v, info):
    """
    [EL] Κατασκευάζει το πλήρες πακέτο (payload) για το WooCommerce.
    [EN] Builds the complete WooCommerce product payload.
    """

    # 1. Καθαρισμός Ονόματος (Αποφυγή π.χ. Apple APPLE iPhone)
    brand_clean = str(brand).strip().upper()
    model_clean = str(model_name).upper().replace(brand_clean, "").strip()

    storage = v.get('storage_gb', 'N/A')
    color = v.get('color', 'N/A')
    full_name = f"{brand_clean} {model_clean} {storage}GB {color}"

    # 2. Πλούσιο HTML Table για τα Specs (Στιγμιότυπο 238 Fix)
    description_html = f"""
    <h4>Τεχνικά Χαρακτηριστικά</h4>
    <table class='shop_attributes' style='width:100%; border-collapse:collapse;'>
        <tr style='background:#f9f9f9;'><th>Επεξεργαστής</th><td>{info.get('cpu_model', 'N/A')}</td></tr>
        <tr><th>Οθόνη</th><td>{info.get('screen_size', 'N/A')} ίντσες</td></tr>
        <tr style='background:#f9f9f9;'><th>Μπαταρία</th><td>{info.get('battery_mah', 'N/A')} mAh</td></tr>
        <tr><th>Κύρια Κάμερα</th><td>{info.get('main_camera_mp', 'N/A')} MP</td></tr>
        <tr style='background:#f9f9f9;'><th>Μνήμη RAM</th><td>{v.get('ram_gb', 'N/A')} GB</td></tr>
        <tr><th>Εσωτερική Μνήμη</th><td>{storage} GB</td></tr>
    </table>
    <p><small>Πηγή δεδομένων: {brand_clean} External ID: {v.get('external_id')}</small></p>
    """

    # 3. Payload Construction
    payload = {
        "name": full_name,
        "type": "simple",
        "regular_price": str(v.get('price', '0')).replace(',', '.'),
        "sku": str(v.get('external_id', '')),
        "description": description_html,
        "manage_stock": False,
        "stock_status": "instock" if "διαθέσιμο" in str(v.get('availability', '')).lower() else "outofstock",
        "images": [{"src": v.get('image_url')}] if v.get('image_url') and v.get('image_url') != "N/A" else [],
        "attributes": [
            {"name": "RAM", "options": [f"{v.get('ram_gb')}GB"], "visible": True},
            {"name": "Storage", "options": [f"{storage}GB"], "visible": True},
            {"name": "Color", "options": [color], "visible": True}
        ]
    }
    return payload


def sync_to_woocommerce(grouped_data):
    """
    [EL] Έξυπνος συγχρονισμός: Update μόνο αν χρειάζεται, αλλιώς Create.
    [EN] Smart sync: Update only price/stock if exists, else full Create.
    """
    logging.info("--- Έναρξη Έξυπνου Συγχρονισμού με WooCommerce ---")

    for model_key, content in grouped_data.items():
        brand = content['info'].get('brand', 'Example Store')
        info = content.get('info', {})

        for v in content['variants']:
            sku = str(v.get('external_id'))

            try:
                # 1. Αναζήτηση προϊόντος βάσει SKU
                res = config.wcapi.get("products", params={"sku": sku})
                found_products = res.json()

                if found_products:
                    # --- ΣΕΝΑΡΙΟ UPDATE (LIGHT PAYLOAD) ---
                    product_id = found_products[0]['id']
                    current_price = found_products[0].get('regular_price')
                    current_stock = found_products[0].get('stock_status')

                    new_price = str(v.get('price', '0')).replace(',', '.')
                    new_stock = "instock" if "διαθέσιμο" in str(v.get('availability', '')).lower() else "outofstock"

                    # Ενημέρωση ΜΟΝΟ αν άλλαξε η τιμή ή το απόθεμα
                    if current_price != new_price or current_stock != new_stock:
                        update_payload = {
                            "regular_price": new_price,
                            "stock_status": new_stock
                        }
                        config.wcapi.put(f"products/{product_id}", update_payload)
                        logging.info(f"⚡ Price/Stock Updated: {sku} ({new_price}€)")
                    else:
                        logging.info(f"No changes for SKU {sku}. Skipping...")

                else:
                    # --- ΣΕΝΑΡΙΟ CREATE (FULL PAYLOAD) ---
                    full_payload = build_product_payload(brand, model_key, v, info)
                    config.wcapi.post("products", full_payload)
                    logging.info(f"Full Product Created: {full_payload['name']}")

            except Exception as e:
                logging.error(f"Critical Sync Error for SKU {sku}: {e}")
