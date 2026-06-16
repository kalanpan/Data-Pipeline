
# E-commerce Product Synchronization Pipeline


Automated product discovery, normalization,

database synchronization and WooCommerce integration.


## Features

- Product discovery from category pages

- Product data extraction and normalization

- SQLite storage

- MySQL synchronization

- Historical price tracking

- WooCommerce product creation

- WooCommerce inventory updates

- Duplicate detection

- Change detection

  
- ## Workflow

1. Discover product URLs

2. Extract product information

3. Normalize technical specifications

4. Synchronize SQLite database

5. Synchronize MySQL database

6. Track price changes

7. Update WooCommerce catalog

## Tech Stack


- Python

- SQLite

- MySQL

- BeautifulSoup

- Requests


```mermaid
graph TD
    A[Category Pages] --> B[URL Discovery]
    B --> C[Product Scraping]
    C --> D[Data Normalization]
    D --> E[Product Grouping]
    E --> F{Database Sync}
    F --> G[SQLite Local]
    F --> H[MySQL Production]
    G --> I[Price History Tracking]
    H --> J[WooCommerce API Update]
    
    style F fill:#f9f,stroke:#333,stroke-width:2px
```
### REPORT

```text
========================================
 JOB REPORT
========================================
Categories Scanned : 3
Total URLs Found: 78
Products Approved : 35
Database Updated : OK
WooCommerce Updated : OK
Status : Success
Duration of job  : 14.93 mins
========================================
```


Built with Python and enhanced through AI-assisted development.

