E-Shop Data Synchronizer
[EN]

A Python-based automation tool designed to synchronize product data from e-shop sources to a local database and a live WooCommerce store. It minimizes manual effort by automating data extraction, normalization, and synchronization processes.
[EL]

Ένα εργαλείο αυτοματισμού σε Python, σχεδιασμένο για να συγχρονίζει δεδομένα προϊόντων από πηγές e-shop σε τοπική βάση δεδομένων και στο live κατάστημα WooCommerce. Μειώνει τη χειροκίνητη εργασία αυτοματοποιώντας τις διαδικασίες εξαγωγής, κανονικοποίησης και συγχρονισμού δεδομένων.
Project Highlights / Τεχνικά Χαρακτηριστικά

    ✅ Web Scraping: Engineered to extract data from complex layouts, featuring robust URL filtering and category navigation to ensure only relevant products are processed.
    (Σχεδιασμένο για την άντληση δεδομένων από σύνθετες σελίδες, με μηχανισμούς φιλτραρίσματος URL και πλοήγησης για τη διασφάλιση της ακρίβειας των δεδομένων.)

    ✅ Data Normalization & Cleaning: Implements automated processing to sanitize product titles, format pricing, and standardize technical specifications like RAM, Storage, and CPU models.
    (Εφαρμόζει αυτοματοποιημένη επεξεργασία για τον καθαρισμό τίτλων, τη διαμόρφωση τιμών και την ομογενοποίηση τεχνικών χαρακτηριστικών.)

    ✅ Dual-Database Architecture (SQLite + MySQL): Supports simultaneous synchronization, using SQLite for local development and MySQL for production-ready reliability.
    (Υποστηρίζει ταυτόχρονο συγχρονισμό, χρησιμοποιώντας SQLite για τοπικό development και MySQL για αξιοπιστία σε περιβάλλον παραγωγής.)

    ✅ WooCommerce REST API Integration: Automates product creation, HTML description formatting, and attribute assignment (e.g., color, memory) directly to your store.
    (Αυτοματοποιεί τη δημιουργία προϊόντων, τη διαμόρφωση περιγραφών HTML και την ανάθεση χαρακτηριστικών απευθείας στο eshop σας.)

    ✅ Smart Sync Logic (Delta Updates): Optimizes API usage by detecting changes; it updates only pricing and stock levels if they have changed, avoiding unnecessary full-product overwrites.
    (Βελτιστοποιεί τη χρήση του API εντοπίζοντας αλλαγές. Ενημερώνει μόνο τιμές και αποθέματα αν υπάρξει αλλαγή, αποφεύγοντας περιττές ενημερώσεις.)

    ✅ Professional Logging System: Comprehensive action tracking with 7-day rotation, enabling easy debugging and verification of synchronization success.
    (Πλήρης καταγραφή ενεργειών με 7-day rotation, διευκολύνοντας τον εντοπισμό σφαλμάτων και την επιβεβαίωση της επιτυχίας του συγχρονισμού.)

Getting Started / Πώς να ξεκινήσετε

    Install Dependencies / Εγκατάσταση:
    Bash

    pip install -r requirements.txt

    Configuration / Ρύθμιση:
    Copy config.example.py to config.py and input your database and API credentials.
    (Αντιγράψτε το config.example.py στο config.py και εισάγετε τα στοιχεία για τη βάση δεδομένων και τα API credentials σας.)

    Execution / Εκτέλεση:
    Bash

    python main.py
