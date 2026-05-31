# E-commerce Data Synchronization Pipeline (Python)

An automated, high-performance Python data pipeline designed for e-commerce synchronization. The system seamlessly scrapes product information across multiple brands, manages a dual-database architecture (SQLite + MySQL) in real-time, monitors price and stock deviations, and executes optimized updates to a WooCommerce store via its REST API by utilizing smart record filtering.

## Key Features
* **Automated Web Scraping:** Multi-brand data extraction using BeautifulSoup4 with robust HTML parsing.
* **Dual Database Synchronization:** Parallel real-time replication to a local SQLite cache and a production-ready MySQL database.
* **Smart Sync (Delta Updates):** Performance-optimized logic that tracks modifications and skips unmodified SKUs to reduce WooCommerce API overhead.
* **WooCommerce REST API Integration:** Dynamic updates of pricing, live variations, and stock statuses.
* **Professional Logging:** Rotational logging system keeping track of sync metrics and execution times.

---

## System Architecture & Previews

### 1. Database Management (Dual-Sync)

*
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (312)" src="https://github.com/user-attachments/assets/c701e02d-ab13-457f-ab0c-85835107df47" />
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (313)" src="https://github.com/user-attachments/assets/e449b479-4dbc-4dd5-a63d-762b1309e610" />
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (314)" src="https://github.com/user-attachments/assets/9ac7c91e-b109-4081-9b04-dd2a07b2fc36" />
*

### 2. Live E-shop Integration (WooCommerce)
Successfully processed product updates, prices, and variations rendered directly on the live store.
*
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (315)" src="https://github.com/user-attachments/assets/3bb885d0-d868-4368-ab8a-e45dc4239ee0" />
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (316)" src="https://github.com/user-attachments/assets/9072f5cf-0e9b-46c6-982e-a1fb1e1157c0" />
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (317)" src="https://github.com/user-attachments/assets/78af3704-cb92-49a7-ac4c-daa4cbcd83d0" />
<img width="1920" height="1080" alt="Στιγμιότυπο οθόνης (318)" src="https://github.com/user-attachments/assets/57fdf255-581e-4456-9a93-b5d645c67430" />
*
---

## Περιγραφή Project  

Ένας αυτοματοποιημένος αγωγός (pipeline) σε Python υψηλής απόδοσης για τον συγχρονισμό δεδομένων ηλεκτρονικού εμπορίου. Το σύστημα συλλέγει (scrapes) δεδομένα προϊόντων για πολλαπλά brands, εκτελεί ταυτόχρονο διπλό συγχρονισμό βάσεων δεδομένων σε πραγματικό χρόνο (SQLite + MySQL), καταγράφει μεταβολές τιμών/αποθεμάτων και πραγματοποιεί έξυπνες live ενημερώσεις σε κατάστημα WooCommerce μέσω REST API, παρακάμπτοντας τις αμετάβλητες εγγραφές για εξοικονόμηση πόρων.

## Κύρια Χαρακτηριστικά
* **Αυτοματοποιημένο Web Scraping:** Εξαγωγή δεδομένων από πολλαπλά brands με χρήση BeautifulSoup4 και εξελιγμένο HTML parsing.
* **Διπλός Συγχρονισμός Βάσεων Δεδομένων:** Παράλληλη εγγραφή σε πραγματικό χρόνο σε τοπική SQLite (cache) και σε παραγωγική βάση MySQL.
* **Έξυπνος Συγχρονισμός (Delta Updates):** Βελτιστοποίηση απόδοσης με έλεγχο μεταβολών και παράκαμψη (skipping) αμετάβλητων SKU για ελαχιστοποίηση των κλήσεων στο WooCommerce API.
* **Διασύνδεση με WooCommerce REST API:** Ζωντανή ενημέρωση τιμών, αποθεμάτων και παραλλαγών προϊόντων.
* **Επαγγελματικό Σύστημα Καταγραφής:** Δημιουργία αναλυτικών logs με χρονική σήμανση, metrics συγχρονισμού και αναφορές εργασίας (Job Reports).

---

## Execution Logs / Ιστορικό Εκτέλεσης

```text
2026-05-31 09:15:04,072 - root - INFO - Logging system initialized (7-day rotation enabled).
2026-05-31 09:15:06,938 - root - INFO - --- STARTING SCRAPING ---
2026-05-31 09:15:06,938 - root - INFO - 
>>> CATEGORY-BRAND: Apple
2026-05-31 09:15:17,780 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple)
2026-05-31 09:15:17,906 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:15:17,913 - root - INFO - Processing 13 items for Apple...
2026-05-31 09:15:17,916 - root - INFO - Scraping starts for 13 URLs...
2026-05-31 09:15:28,625 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-256gb-cosmic-orange-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-256gb-cosmic-orange-eu)
2026-05-31 09:15:28,932 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:15:28,959 - root - INFO - Processed: apple-iphone-17-pro-max-256gb-...
2026-05-31 09:15:28,959 - root - INFO - Data is ready
2026-05-31 09:15:35,431 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu](https://www.kaizershop.gr/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu)
2026-05-31 09:15:35,552 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:15:35,581 - root - INFO - Processed: samsung-galaxy-s26-ultra-s948-...
2026-05-31 09:15:35,585 - root - INFO - Data is ready
2026-05-31 09:15:41,626 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-16-pro-max-256gb-black-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-16-pro-max-256gb-black-eu)
2026-05-31 09:15:41,864 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:15:41,887 - root - INFO - Processed: apple-iphone-16-pro-max-256gb-...
2026-05-31 09:15:41,887 - root - INFO - Data is ready
2026-05-31 09:15:49,755 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-256gb-deep-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-256gb-deep-blue-eu)
2026-05-31 09:15:49,990 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:15:50,011 - root - INFO - Processed: apple-iphone-17-pro-max-256gb-...
2026-05-31 09:15:50,012 - root - INFO - Data is ready
2026-05-31 09:15:55,678 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu)
2026-05-31 09:15:55,767 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:15:55,790 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:15:55,790 - root - INFO - Data is ready
2026-05-31 09:16:02,174 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-13-128gb-blue-eu-mlpk3](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-13-128gb-blue-eu-mlpk3)
2026-05-31 09:16:02,557 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:02,583 - root - INFO - Processed: apple-iphone-13-128gb-blue-eu-...
2026-05-31 09:16:02,583 - root - INFO - Data is ready
2026-05-31 09:16:09,686 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-512gb-cosmic-orange-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-512gb-cosmic-orange-eu)
2026-05-31 09:16:09,910 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:09,934 - root - INFO - Processed: apple-iphone-17-pro-max-512gb-...
2026-05-31 09:16:09,934 - root - INFO - Data is ready
2026-05-31 09:16:18,312 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu](https://www.kaizershop.gr/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu)
2026-05-31 09:16:18,402 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:18,434 - root - INFO - Processed: xiaomi-pocophone-x8-pro-max-51...
2026-05-31 09:16:18,435 - root - INFO - Data is ready
2026-05-31 09:16:25,863 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-256gb-mist-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-256gb-mist-blue-eu)
2026-05-31 09:16:26,168 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:26,189 - root - INFO - Processed: apple-iphone-17-256gb-mist-blu...
2026-05-31 09:16:26,189 - root - INFO - Data is ready
2026-05-31 09:16:34,143 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-14-pro-max-256gb-black-eu-mq9u3](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-14-pro-max-256gb-black-eu-mq9u3)
2026-05-31 09:16:34,353 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:34,377 - root - INFO - Processed: apple-iphone-14-pro-max-256gb-...
2026-05-31 09:16:34,377 - root - INFO - Data is ready
2026-05-31 09:16:40,638 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu)
2026-05-31 09:16:40,773 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:40,803 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:16:40,803 - root - INFO - Data is ready
2026-05-31 09:16:47,040 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-512gb-silver-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-512gb-silver-eu)
2026-05-31 09:16:47,276 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:47,297 - root - INFO - Processed: apple-iphone-17-pro-max-512gb-...
2026-05-31 09:16:47,297 - root - INFO - Data is ready
2026-05-31 09:16:54,792 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-512gb-deep-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-apple/apple-iphone-17-pro-max-512gb-deep-blue-eu)
2026-05-31 09:16:55,159 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:16:55,182 - root - INFO - Processed: apple-iphone-17-pro-max-512gb-...
2026-05-31 09:16:55,182 - root - INFO - Data is ready
2026-05-31 09:16:56,197 - root - INFO - Successfully connected to database: C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db
2026-05-31 09:16:56,221 - root - INFO - Sync Summary: 8 Products, 13 Variants, 0 New Prices.
2026-05-31 09:16:56,222 - root - INFO - Database connection closed successfully.
2026-05-31 09:16:56,222 - root - INFO - Synchronization completed!
2026-05-31 09:16:56,223 - root - INFO - Successfully connected to database: C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db
2026-05-31 09:16:56,236 - root - INFO - Sync Summary: 8 Products, 13 Variants, 0 New Prices.
2026-05-31 09:16:56,236 - root - INFO - SQLite: Synchronization completed.
2026-05-31 09:16:56,236 - root - INFO - MySQL: Starting Synchronization...
2026-05-31 09:16:57,385 - root - INFO - Successfully connected to MySQL database: kaizer_test
2026-05-31 09:16:57,543 - root - INFO - Sync Summary: 8 Products, 13 Variants, 0 New Prices.
2026-05-31 09:16:57,543 - root - INFO - Transaction committed successfully.
2026-05-31 09:16:57,566 - root - INFO - MySQL connection closed successfully.
2026-05-31 09:16:57,567 - root - INFO - MySQL: Synchronization completed.
2026-05-31 09:16:57,568 - root - INFO - Double Synchronization completed!
2026-05-31 09:16:57,568 - root - INFO - --- Έναρξη Έξυπνου Συγχρονισμού με WooCommerce ---
2026-05-31 09:17:08,471 - root - INFO - ⚡ Price/Stock Updated: 40791 (1527.9€)
2026-05-31 09:17:10,467 - root - INFO - No changes for SKU 40790. Skipping...
2026-05-31 09:17:12,453 - root - INFO - No changes for SKU 40794. Skipping...
2026-05-31 09:17:14,403 - root - INFO - No changes for SKU 40795. Skipping...
2026-05-31 09:17:17,027 - root - INFO - No changes for SKU 40793. Skipping...
2026-05-31 09:17:19,113 - root - INFO - No changes for SKU 42224. Skipping...
2026-05-31 09:17:22,874 - root - INFO - ⚡ Price/Stock Updated: 38910 (1344.9€)
2026-05-31 09:17:24,514 - root - INFO - No changes for SKU 42235. Skipping...
2026-05-31 09:17:26,497 - root - INFO - No changes for SKU 42236. Skipping...
2026-05-31 09:17:30,001 - root - INFO - ⚡ Price/Stock Updated: 29913 (549.9€)
2026-05-31 09:17:31,945 - root - INFO - No changes for SKU 42192. Skipping...
2026-05-31 09:17:33,643 - root - INFO - No changes for SKU 40878. Skipping...
2026-05-31 09:17:35,317 - root - INFO - No changes for SKU 32990. Skipping...
2026-05-31 09:17:35,317 - root - INFO - 
========================================
 JOB REPORT
========================================
Categories Scanned : 1
Total URLs Found: 13
Products Approved : 8
Database Updated : OK
WooCommerce Updated : OK
Status : Success
Duration of job  : 2.47 mins
========================================
2026-05-31 09:17:35,317 - root - INFO - 
>>> CATEGORY-BRAND: Samsung
2026-05-31 09:17:44,060 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung)
2026-05-31 09:17:44,245 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:17:44,267 - root - INFO - Processing 30 items for Samsung...
2026-05-31 09:17:44,267 - root - INFO - Scraping starts for 30 URLs...
2026-05-31 09:17:51,922 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-8gb-5g-dual-awesome-lavender-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-8gb-5g-dual-awesome-lavender-eu)
2026-05-31 09:17:52,010 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:17:52,045 - root - INFO - Processed: samsung-galaxy-a37-a376-256gb-...
2026-05-31 09:17:52,045 - root - INFO - Data is ready
2026-05-31 09:18:01,572 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-17-pro-max-512gb-silver-eu](https://www.kaizershop.gr/apple-iphone-17-pro-max-512gb-silver-eu)
2026-05-31 09:18:01,836 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:01,861 - root - INFO - Processed: apple-iphone-17-pro-max-512gb-...
2026-05-31 09:18:01,861 - root - INFO - Data is ready
2026-05-31 09:18:08,135 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-sky-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-sky-blue-eu)
2026-05-31 09:18:08,582 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:08,613 - root - INFO - Processed: samsung-galaxy-s26-plus-s947-2...
2026-05-31 09:18:08,613 - root - INFO - Data is ready
2026-05-31 09:18:15,749 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-cobalt-violet-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-cobalt-violet-eu)
2026-05-31 09:18:15,847 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:15,871 - root - INFO - Processed: samsung-galaxy-s26-plus-s947-2...
2026-05-31 09:18:15,871 - root - INFO - Data is ready
2026-05-31 09:18:24,714 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu)
2026-05-31 09:18:24,837 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:24,859 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:18:24,861 - root - INFO - Data is ready
2026-05-31 09:18:30,523 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-14-pro-max-256gb-black-eu-mq9u3](https://www.kaizershop.gr/apple-iphone-14-pro-max-256gb-black-eu-mq9u3)
2026-05-31 09:18:30,732 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:30,763 - root - INFO - Processed: apple-iphone-14-pro-max-256gb-...
2026-05-31 09:18:30,763 - root - INFO - Data is ready
2026-05-31 09:18:37,546 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-17-pro-max-512gb-cosmic-orange-eu](https://www.kaizershop.gr/apple-iphone-17-pro-max-512gb-cosmic-orange-eu)
2026-05-31 09:18:37,871 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:37,894 - root - INFO - Processed: apple-iphone-17-pro-max-512gb-...
2026-05-31 09:18:37,895 - root - INFO - Data is ready
2026-05-31 09:18:43,574 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-white-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-white-eu)
2026-05-31 09:18:43,666 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:43,687 - root - INFO - Processed: samsung-galaxy-a37-a376-128gb-...
2026-05-31 09:18:43,687 - root - INFO - Data is ready
2026-05-31 09:18:50,968 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-navy-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-navy-eu)
2026-05-31 09:18:51,057 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:51,082 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:18:51,083 - root - INFO - Data is ready
2026-05-31 09:18:57,038 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-ultra-s948-256gb-12gb-5g-dual-sky-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-ultra-s948-256gb-12gb-5g-dual-sky-blue-eu)
2026-05-31 09:18:57,130 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:18:57,152 - root - INFO - Processed: samsung-galaxy-s26-ultra-s948-...
2026-05-31 09:18:57,152 - root - INFO - Data is ready
2026-05-31 09:19:05,552 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-17-pro-max-512gb-deep-blue-eu](https://www.kaizershop.gr/apple-iphone-17-pro-max-512gb-deep-blue-eu)
2026-05-31 09:19:05,863 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:05,907 - root - INFO - Processed: apple-iphone-17-pro-max-512gb-...
2026-05-31 09:19:05,908 - root - INFO - Data is ready
2026-05-31 09:19:12,791 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu)
2026-05-31 09:19:13,175 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:13,206 - root - INFO - Processed: samsung-galaxy-s26-ultra-s948-...
2026-05-31 09:19:13,206 - root - INFO - Data is ready
2026-05-31 09:19:21,740 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-8gb-5g-dual-awesome-white-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-8gb-5g-dual-awesome-white-eu)
2026-05-31 09:19:21,838 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:21,862 - root - INFO - Processed: samsung-galaxy-a37-a376-256gb-...
2026-05-31 09:19:21,862 - root - INFO - Data is ready
2026-05-31 09:19:31,034 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-8gb-5g-dual-awesome-graygreen-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-8gb-5g-dual-awesome-graygreen-eu)
2026-05-31 09:19:31,144 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:31,164 - root - INFO - Processed: samsung-galaxy-a37-a376-256gb-...
2026-05-31 09:19:31,166 - root - INFO - Data is ready
2026-05-31 09:19:39,812 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu](https://www.kaizershop.gr/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu)
2026-05-31 09:19:39,929 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:39,947 - root - INFO - Processed: xiaomi-pocophone-x8-pro-max-51...
2026-05-31 09:19:39,947 - root - INFO - Data is ready
2026-05-31 09:19:50,765 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-256gb-8gb-5g-dual-awesome-navy-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-256gb-8gb-5g-dual-awesome-navy-eu)
2026-05-31 09:19:50,874 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:50,894 - root - INFO - Processed: samsung-galaxy-a57-a576-256gb-...
2026-05-31 09:19:50,894 - root - INFO - Data is ready
2026-05-31 09:19:59,124 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu)
2026-05-31 09:19:59,237 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:19:59,257 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:19:59,257 - root - INFO - Data is ready
2026-05-31 09:20:05,029 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu)
2026-05-31 09:20:05,125 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:05,148 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:20:05,148 - root - INFO - Data is ready
2026-05-31 09:20:13,487 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-lavender-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-lavender-eu)
2026-05-31 09:20:13,728 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:13,753 - root - INFO - Processed: samsung-galaxy-a37-a376-128gb-...
2026-05-31 09:20:13,753 - root - INFO - Data is ready
2026-05-31 09:20:20,336 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu)
2026-05-31 09:20:20,436 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:20,458 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:20:20,458 - root - INFO - Data is ready
2026-05-31 09:20:29,836 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-charcoal-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-charcoal-eu)
2026-05-31 09:20:29,975 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:30,002 - root - INFO - Processed: samsung-galaxy-a37-a376-128gb-...
2026-05-31 09:20:30,002 - root - INFO - Data is ready
2026-05-31 09:20:37,493 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-s942-256gb-12gb-5g-dual-cobalt-violet-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-s942-256gb-12gb-5g-dual-cobalt-violet-eu)
2026-05-31 09:20:37,769 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:37,790 - root - INFO - Processed: samsung-galaxy-s26-s942-256gb-...
2026-05-31 09:20:37,791 - root - INFO - Data is ready
2026-05-31 09:20:44,345 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-graygreen-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-graygreen-eu)
2026-05-31 09:20:44,459 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:44,479 - root - INFO - Processed: samsung-galaxy-a37-a376-128gb-...
2026-05-31 09:20:44,479 - root - INFO - Data is ready
2026-05-31 09:20:53,941 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu](https://www.kaizershop.gr/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu)
2026-05-31 09:20:54,142 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:20:54,170 - root - INFO - Processed: samsung-galaxy-s26-ultra-s948-...
2026-05-31 09:20:54,172 - root - INFO - Data is ready
2026-05-31 09:21:04,198 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-17-256gb-mist-blue-eu](https://www.kaizershop.gr/apple-iphone-17-256gb-mist-blue-eu)
2026-05-31 09:21:04,482 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:21:04,510 - root - INFO - Processed: apple-iphone-17-256gb-mist-blu...
2026-05-31 09:21:04,510 - root - INFO - Data is ready
2026-05-31 09:21:13,357 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-lilac-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-lilac-eu)
2026-05-31 09:21:13,484 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:21:13,507 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:21:13,507 - root - INFO - Data is ready
2026-05-31 09:21:18,682 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-6gb-5g-dual-awesome-charcoal-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-a37-a376-256gb-6gb-5g-dual-awesome-charcoal-eu)
2026-05-31 09:21:18,779 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:21:18,800 - root - INFO - Processed: samsung-galaxy-a37-a376-256gb-...
2026-05-31 09:21:18,802 - root - INFO - Data is ready
2026-05-31 09:21:24,719 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-black-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-black-eu)
2026-05-31 09:21:24,963 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:21:24,985 - root - INFO - Processed: samsung-galaxy-s26-plus-s947-2...
2026-05-31 09:21:24,985 - root - INFO - Data is ready
2026-05-31 09:21:34,176 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-13-128gb-blue-eu-mlpk3](https://www.kaizershop.gr/apple-iphone-13-128gb-blue-eu-mlpk3)
2026-05-31 09:21:34,579 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:21:34,611 - root - INFO - Processed: apple-iphone-13-128gb-blue-eu-...
2026-05-31 09:21:34,611 - root - INFO - Data is ready
2026-05-31 09:21:43,215 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-white-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-samsung/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-white-eu)
2026-05-31 09:21:43,385 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:21:43,410 - root - INFO - Processed: samsung-galaxy-s26-plus-s947-2...
2026-05-31 09:21:43,410 - root - INFO - Data is ready
2026-05-31 09:21:44,429 - root - INFO - Successfully connected to database: C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db
2026-05-31 09:21:44,455 - root - INFO - Sync Summary: 11 Products, 30 Variants, 0 New Prices.
2026-05-31 09:21:44,455 - root - INFO - Database connection closed successfully.
2026-05-31 09:21:44,455 - root - INFO - Synchronization completed!
2026-05-31 09:21:44,455 - root - INFO - Successfully connected to database: C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db
2026-05-31 09:21:44,469 - root - INFO - Sync Summary: 11 Products, 30 Variants, 0 New Prices.
2026-05-31 09:21:44,469 - root - INFO - SQLite: Synchronization completed.
2026-05-31 09:21:44,469 - root - INFO - MySQL: Starting Synchronization...
2026-05-31 09:21:44,578 - root - INFO - Successfully connected to MySQL database: kaizer_test
2026-05-31 09:21:44,655 - root - INFO - Sync Summary: 11 Products, 30 Variants, 0 New Prices.
2026-05-31 09:21:44,655 - root - INFO - Transaction committed successfully.
2026-05-31 09:21:44,659 - root - INFO - MySQL connection closed successfully.
2026-05-31 09:21:44,659 - root - INFO - MySQL: Synchronization completed.
2026-05-31 09:21:44,659 - root - INFO - Double Synchronization completed!
2026-05-31 09:21:44,659 - root - INFO - --- Έναρξη Έξυπνου Συγχρονισμού με WooCommerce ---
2026-05-31 09:21:50,306 - root - INFO - ⚡ Price/Stock Updated: 42068 (339.9€)
2026-05-31 09:21:54,164 - root - INFO - ⚡ Price/Stock Updated: 42067 (296.9€)
2026-05-31 09:21:57,686 - root - INFO - ⚡ Price/Stock Updated: 42061 (368.9€)
2026-05-31 09:22:01,457 - root - INFO - ⚡ Price/Stock Updated: 42069 (363.9€)
2026-05-31 09:22:04,963 - root - INFO - ⚡ Price/Stock Updated: 42066 (299.9€)
2026-05-31 09:22:08,570 - root - INFO - ⚡ Price/Stock Updated: 41931 (289.9€)
2026-05-31 09:22:12,410 - root - INFO - ⚡ Price/Stock Updated: 42065 (299.9€)
2026-05-31 09:22:17,369 - root - INFO - ⚡ Price/Stock Updated: 41932 (363.9€)
2026-05-31 09:22:19,179 - root - INFO - No changes for SKU 40795. Skipping...
2026-05-31 09:22:20,987 - root - INFO - No changes for SKU 40794. Skipping...
2026-05-31 09:22:22,669 - root - INFO - No changes for SKU 40793. Skipping...
2026-05-31 09:22:26,454 - root - INFO - ⚡ Price/Stock Updated: 41945 (899.0€)
2026-05-31 09:22:29,978 - root - INFO - ⚡ Price/Stock Updated: 41943 (899.0€)
2026-05-31 09:22:33,921 - root - INFO - ⚡ Price/Stock Updated: 41905 (899.0€)
2026-05-31 09:22:38,005 - root - INFO - ⚡ Price/Stock Updated: 41906 (899.0€)
2026-05-31 09:22:39,689 - root - INFO - No changes for SKU 42235. Skipping...
2026-05-31 09:22:43,591 - root - INFO - ⚡ Price/Stock Updated: 41933 (362.9€)
2026-05-31 09:22:47,411 - root - INFO - ⚡ Price/Stock Updated: 41934 (409.9€)
2026-05-31 09:22:49,148 - root - INFO - No changes for SKU 42236. Skipping...
2026-05-31 09:22:51,014 - root - INFO - No changes for SKU 42236. Skipping...
2026-05-31 09:22:52,703 - root - INFO - No changes for SKU 42235. Skipping...
2026-05-31 09:22:54,541 - root - INFO - No changes for SKU 42146. Skipping...
2026-05-31 09:22:56,481 - root - INFO - No changes for SKU 32990. Skipping...
2026-05-31 09:22:58,338 - root - INFO - No changes for SKU 41833. Skipping...
2026-05-31 09:23:00,218 - root - INFO - No changes for SKU 42224. Skipping...
2026-05-31 09:23:02,108 - root - INFO - No changes for SKU 42224. Skipping...
2026-05-31 09:23:03,776 - root - INFO - No changes for SKU 42192. Skipping...
2026-05-31 09:23:07,577 - root - INFO - ⚡ Price/Stock Updated: 41832 (729.9€)
2026-05-31 09:23:09,610 - root - INFO - No changes for SKU 40878. Skipping...
2026-05-31 09:23:13,085 - root - INFO - ⚡ Price/Stock Updated: 29913 (549.9€)
2026-05-31 09:23:13,085 - root - INFO - 
========================================
 JOB REPORT
========================================
Categories Scanned : 2
Total URLs Found: 43
Products Approved : 19
Database Updated : OK
WooCommerce Updated : OK
Status : Success
Duration of job  : 8.1 mins
========================================
2026-05-31 09:23:13,085 - root - INFO - 
>>> CATEGORY-BRAND: Xiaomi
2026-05-31 09:23:23,185 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi)
2026-05-31 09:23:23,411 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:23:23,426 - root - INFO - Processing 31 items for Xiaomi...
2026-05-31 09:23:23,426 - root - INFO - Scraping starts for 31 URLs...
2026-05-31 09:23:30,981 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-256gb-8gb-5g-dual-blue-2510era8bg](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-256gb-8gb-5g-dual-blue-2510era8bg)
2026-05-31 09:23:31,500 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:23:31,539 - root - INFO - Processed: xiaomi-redmi-note-15-pro-plus-...
2026-05-31 09:23:31,539 - root - INFO - Data is ready
2026-05-31 09:23:40,231 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-5g-dual-titanium-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-5g-dual-titanium-eu)
2026-05-31 09:23:40,411 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:23:40,437 - root - INFO - Processed: xiaomi-redmi-note-15-pro-256gb...
2026-05-31 09:23:40,437 - root - INFO - Data is ready
2026-05-31 09:23:48,860 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-black-eu](https://www.kaizershop.gr/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-black-eu)
2026-05-31 09:23:49,102 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:23:49,143 - root - INFO - Processed: samsung-galaxy-s26-plus-s947-2...
2026-05-31 09:23:49,143 - root - INFO - Data is ready
2026-05-31 09:23:58,895 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-black-2602bpc18g](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-black-2602bpc18g)
2026-05-31 09:23:59,167 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:23:59,192 - root - INFO - Processed: xiaomi-pocophone-x8-pro-max-51...
2026-05-31 09:23:59,192 - root - INFO - Data is ready
2026-05-31 09:24:05,276 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-4g-nfc-dual-purple](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-4g-nfc-dual-purple)
2026-05-31 09:24:05,525 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:05,560 - root - INFO - Processed: xiaomi-redmi-note-15-256gb-8gb...
2026-05-31 09:24:05,560 - root - INFO - Data is ready
2026-05-31 09:24:15,063 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-5g-dual-black-25080rabdg](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-5g-dual-black-25080rabdg)
2026-05-31 09:24:15,481 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:15,504 - root - INFO - Processed: xiaomi-redmi-note-15-pro-256gb...
2026-05-31 09:24:15,519 - root - INFO - Data is ready
2026-05-31 09:24:22,463 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-128gb-6gb-4g-nfc-dual-purple](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-128gb-6gb-4g-nfc-dual-purple)
2026-05-31 09:24:22,839 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:22,865 - root - INFO - Processed: xiaomi-redmi-note-15-128gb-6gb...
2026-05-31 09:24:22,865 - root - INFO - Data is ready
2026-05-31 09:24:30,163 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-256gb-8gb-5g-dual-black-2510era8bg](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-256gb-8gb-5g-dual-black-2510era8bg)
2026-05-31 09:24:30,636 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:30,703 - root - INFO - Processed: xiaomi-redmi-note-15-pro-plus-...
2026-05-31 09:24:30,703 - root - INFO - Data is ready
2026-05-31 09:24:38,602 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-15-256gb-8gb-5g-dual-green-25057rn09e](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-15-256gb-8gb-5g-dual-green-25057rn09e)
2026-05-31 09:24:38,935 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:38,953 - root - INFO - Processed: xiaomi-redmi-15-256gb-8gb-5g-d...
2026-05-31 09:24:38,953 - root - INFO - Data is ready
2026-05-31 09:24:45,586 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu)
2026-05-31 09:24:45,705 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:45,729 - root - INFO - Processed: xiaomi-pocophone-x8-pro-max-51...
2026-05-31 09:24:45,729 - root - INFO - Data is ready
2026-05-31 09:24:55,547 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-512gb-12gb-5g-dual-blue](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-512gb-12gb-5g-dual-blue)
2026-05-31 09:24:56,034 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:24:56,049 - root - INFO - Processed: xiaomi-redmi-note-15-pro-plus-...
2026-05-31 09:24:56,049 - root - INFO - Data is ready
2026-05-31 09:25:05,343 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu](https://www.kaizershop.gr/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-white-eu)
2026-05-31 09:25:05,522 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:05,549 - root - INFO - Processed: xiaomi-pocophone-x8-pro-max-51...
2026-05-31 09:25:05,549 - root - INFO - Data is ready
2026-05-31 09:25:14,529 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-white-eu](https://www.kaizershop.gr/samsung-galaxy-s26-plus-s947-256gb-12gb-5g-dual-white-eu)
2026-05-31 09:25:14,741 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:14,773 - root - INFO - Processed: samsung-galaxy-s26-plus-s947-2...
2026-05-31 09:25:14,774 - root - INFO - Data is ready
2026-05-31 09:25:20,549 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-blue-eu](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-pocophone-x8-pro-max-512gb-12gb-dual-blue-eu)
2026-05-31 09:25:20,803 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:20,851 - root - INFO - Processed: xiaomi-pocophone-x8-pro-max-51...
2026-05-31 09:25:20,851 - root - INFO - Data is ready
2026-05-31 09:25:26,681 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-5g-nfc-dual-black](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-5g-nfc-dual-black)
2026-05-31 09:25:26,955 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:26,975 - root - INFO - Processed: xiaomi-redmi-note-15-256gb-8gb...
2026-05-31 09:25:26,975 - root - INFO - Data is ready
2026-05-31 09:25:35,980 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-icy-blue-eu)
2026-05-31 09:25:36,202 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:36,233 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:25:36,233 - root - INFO - Data is ready
2026-05-31 09:25:45,699 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-gray-eu)
2026-05-31 09:25:45,826 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:45,852 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:25:45,852 - root - INFO - Data is ready
2026-05-31 09:25:54,676 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-4g-nfc-dual-black](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-4g-nfc-dual-black)
2026-05-31 09:25:54,910 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:25:54,942 - root - INFO - Processed: xiaomi-redmi-note-15-256gb-8gb...
2026-05-31 09:25:54,942 - root - INFO - Data is ready
2026-05-31 09:26:03,726 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-512gb-12gb-5g-dual-black](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-512gb-12gb-5g-dual-black)
2026-05-31 09:26:04,069 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:04,118 - root - INFO - Processed: xiaomi-redmi-note-15-pro-plus-...
2026-05-31 09:26:04,120 - root - INFO - Data is ready
2026-05-31 09:26:13,723 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-graygreen-eu](https://www.kaizershop.gr/samsung-galaxy-a37-a376-128gb-6gb-5g-dual-awesome-graygreen-eu)
2026-05-31 09:26:13,883 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:13,914 - root - INFO - Processed: samsung-galaxy-a37-a376-128gb-...
2026-05-31 09:26:13,914 - root - INFO - Data is ready
2026-05-31 09:26:22,763 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a37-a376-256gb-6gb-5g-dual-awesome-charcoal-eu](https://www.kaizershop.gr/samsung-galaxy-a37-a376-256gb-6gb-5g-dual-awesome-charcoal-eu)
2026-05-31 09:26:22,965 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:22,981 - root - INFO - Processed: samsung-galaxy-a37-a376-256gb-...
2026-05-31 09:26:22,992 - root - INFO - Data is ready
2026-05-31 09:26:31,345 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-256gb-8gb-5g-dual-brown-2510era8bg](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-plus-256gb-8gb-5g-dual-brown-2510era8bg)
2026-05-31 09:26:31,751 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:31,789 - root - INFO - Processed: xiaomi-redmi-note-15-pro-plus-...
2026-05-31 09:26:31,791 - root - INFO - Data is ready
2026-05-31 09:26:37,407 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu](https://www.kaizershop.gr/samsung-galaxy-s26-ultra-s948-1tb-16gb-5g-dual-pink-gold-eu)
2026-05-31 09:26:37,605 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:37,628 - root - INFO - Processed: samsung-galaxy-s26-ultra-s948-...
2026-05-31 09:26:37,628 - root - INFO - Data is ready
2026-05-31 09:26:47,164 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-17-256gb-mist-blue-eu](https://www.kaizershop.gr/apple-iphone-17-256gb-mist-blue-eu)
2026-05-31 09:26:47,597 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:47,623 - root - INFO - Processed: apple-iphone-17-256gb-mist-blu...
2026-05-31 09:26:47,623 - root - INFO - Data is ready
2026-05-31 09:26:57,229 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-lilac-eu](https://www.kaizershop.gr/samsung-galaxy-a57-a576-128gb-8gb-5g-dual-awesome-lilac-eu)
2026-05-31 09:26:57,484 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:26:57,522 - root - INFO - Processed: samsung-galaxy-a57-a576-128gb-...
2026-05-31 09:26:57,522 - root - INFO - Data is ready
2026-05-31 09:27:07,295 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-nfc-dual-black](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-nfc-dual-black)
2026-05-31 09:27:07,660 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:27:07,684 - root - INFO - Processed: xiaomi-redmi-note-15-pro-256gb...
2026-05-31 09:27:07,684 - root - INFO - Data is ready
2026-05-31 09:27:16,947 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-128gb-6gb-5g-nfc-dual-black](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-128gb-6gb-5g-nfc-dual-black)
2026-05-31 09:27:17,265 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:27:17,287 - root - INFO - Processed: xiaomi-redmi-note-15-128gb-6gb...
2026-05-31 09:27:17,287 - root - INFO - Data is ready
2026-05-31 09:27:25,123 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-128gb-6gb-4g-nfc-dual-blue](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-128gb-6gb-4g-nfc-dual-blue)
2026-05-31 09:27:25,450 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:27:25,479 - root - INFO - Processed: xiaomi-redmi-note-15-128gb-6gb...
2026-05-31 09:27:25,479 - root - INFO - Data is ready
2026-05-31 09:27:32,841 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/apple-iphone-13-128gb-blue-eu-mlpk3](https://www.kaizershop.gr/apple-iphone-13-128gb-blue-eu-mlpk3)
2026-05-31 09:27:33,154 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:27:33,179 - root - INFO - Processed: apple-iphone-13-128gb-blue-eu-...
2026-05-31 09:27:33,179 - root - INFO - Data is ready
2026-05-31 09:27:42,544 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-4g-nfc-dual-blue](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-256gb-8gb-4g-nfc-dual-blue)
2026-05-31 09:27:42,874 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:27:42,913 - root - INFO - Processed: xiaomi-redmi-note-15-256gb-8gb...
2026-05-31 09:27:42,921 - root - INFO - Data is ready
2026-05-31 09:27:48,634 - root - INFO - Successfully fetched: [https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-5g-dual-blue](https://www.kaizershop.gr/cell-phones-smartphones/cell-phones-smartphones-xiaomi/xiaomi-redmi-note-15-pro-256gb-8gb-5g-dual-blue)
2026-05-31 09:27:48,798 - root - INFO - HTML content successfully parsed into Soup object.
2026-05-31 09:27:48,830 - root - INFO - Processed: xiaomi-redmi-note-15-pro-256gb...
2026-05-31 09:27:48,831 - root - INFO - Data is ready
2026-05-31 09:27:49,834 - root - INFO - Successfully connected to database: C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db
2026-05-31 09:27:49,852 - root - INFO - Sync Summary: 11 Products, 31 Variants, 0 New Prices.
2026-05-31 09:27:49,852 - root - INFO - Database connection closed successfully.
2026-05-31 09:27:49,852 - root - INFO - Synchronization completed!
2026-05-31 09:27:49,852 - root - INFO - Successfully connected to database: C:\python_projects\toolkit\kaizer_eshop\db\kaizer_eshop.db
2026-05-31 09:27:49,876 - root - INFO - Sync Summary: 11 Products, 31 Variants, 0 New Prices.
2026-05-31 09:27:49,876 - root - INFO - SQLite: Synchronization completed.
2026-05-31 09:27:49,878 - root - INFO - MySQL: Starting Synchronization...
2026-05-31 09:27:49,895 - root - INFO - Successfully connected to MySQL database: kaizer_test
2026-05-31 09:27:49,963 - root - INFO - Sync Summary: 11 Products, 31 Variants, 0 New Prices.
2026-05-31 09:27:49,963 - root - INFO - Transaction committed successfully.
2026-05-31 09:27:49,963 - root - INFO - MySQL connection closed successfully.
2026-05-31 09:27:49,963 - root - INFO - MySQL: Synchronization completed.
2026-05-31 09:27:49,963 - root - INFO - Double Synchronization completed!
2026-05-31 09:27:49,963 - root - INFO - --- Έναρξη Έξυπνου Συγχρονισμού με WooCommerce ---
2026-05-31 09:27:55,330 - root - INFO - ⚡ Price/Stock Updated: 41544 (379.99€)
2026-05-31 09:27:58,916 - root - INFO - ⚡ Price/Stock Updated: 41644 (375.99€)
2026-05-31 09:28:00,778 - root - INFO - No changes for SKU 42141. Skipping...
2026-05-31 09:28:02,600 - root - INFO - No changes for SKU 41549. Skipping...
2026-05-31 09:28:06,561 - root - INFO - ⚡ Price/Stock Updated: 41545 (384.9€)
2026-05-31 09:28:14,141 - root - INFO - No changes for SKU 42149. Skipping...
2026-05-31 09:28:11,667 - root - INFO - ⚡ Price/Stock Updated: 41543 (299.99€)
2026-05-31 09:28:13,641 - root - INFO - No changes for SKU 42074. Skipping...
2026-05-31 09:28:15,359 - root - INFO - No changes for SKU 42140. Skipping...
2026-05-31 09:28:20,262 - root - INFO - ⚡ Price/Stock Updated: 41905 (899.0€)
2026-05-31 09:28:23,854 - root - INFO - ⚡ Price/Stock Updated: 41906 (899.0€)
2026-05-31 09:28:25,462 - root - INFO - No changes for SKU 42078. Skipping...
2026-05-31 09:28:27,136 - root - INFO - No changes for SKU 42192. Skipping...
2026-05-31 09:28:28,915 - root - INFO - No changes for SKU 42192. Skipping...
2026-05-31 09:28:30,705 - root - INFO - No changes for SKU 42191. Skipping...
2026-05-31 09:28:34,046 - root - INFO - ⚡ Price/Stock Updated: 41643 (204.9€)
2026-05-31 09:28:38,244 - root - INFO - ⚡ Price/Stock Updated: 41628 (177.0€)
2026-05-31 09:28:40,249 - root - INFO - No changes for SKU 41818. Skipping...
2026-05-31 09:28:43,627 - root - INFO - ⚡ Price/Stock Updated: 41641 (207.9€)
2026-05-31 09:28:47,394 - root - INFO - ⚡ Price/Stock Updated: 41817 (226.9€)
2026-05-31 09:28:51,486 - root - INFO - ⚡ Price/Stock Updated: 41542 (177.0€)
2026-05-31 09:28:55,126 - root - INFO - ⚡ Price/Stock Updated: 41642 (204.9€)
2026-05-31 09:28:56,945 - root - INFO - No changes for SKU 41816. Skipping...
2026-05-31 09:28:58,530 - root - INFO - No changes for SKU 42236. Skipping...
2026-05-31 09:29:00,266 - root - INFO - No changes for SKU 42235. Skipping...
2026-05-31 09:29:02,186 - root - INFO - No changes for SKU 42146. Skipping...
2026-05-31 09:29:05,810 - root - INFO - ⚡ Price/Stock Updated: 42065 (299.9€)
2026-05-31 09:29:10,376 - root - INFO - ⚡ Price/Stock Updated: 41932 (363.9€)
2026-05-31 09:29:12,264 - root - INFO - No changes for SKU 42224. Skipping...
2026-05-31 09:29:13,967 - root - INFO - No changes for SKU 40878. Skipping...
2026-05-31 09:29:19,039 - root - INFO - ⚡ Price/Stock Updated: 29913 (549.9€)
2026-05-31 09:29:19,039 - root - INFO - 
========================================
 JOB REPORT
========================================
Categories Scanned : 3
Total URLs Found: 74
Products Approved : 30
Database Updated : OK
WooCommerce Updated : OK
Status : Success
Duration of job  : 14.2 mins
========================================
