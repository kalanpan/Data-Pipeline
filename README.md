
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   E-shops       │────▶│  Scraper Engine  │────▶│ Data Processing │
│  (E-shop, etc)  │     │  (BeautifulSoup) │     │  Normalization  │
└─────────────────┘     └──────────────────┘     └────────┬────────
                                                          │
                    ┌─────────────────────────────────────┼─────────────────────────────────────┐
                    │                                     │                                     │
                    ▼                                     ▼                                     ▼
          ┌─────────────────┐                   ┌─────────────────┐                   ┌─────────────────┐
          │   SQLite (Local)│                   │  MySQL (Prod)   │                   │  WooCommerce    │
          │   Cache & Dev   │                   │   Production    │                   │  Live Store     │
          └─────────────────┘                   └─────────────────┘                   └─────────────────┘


Built with ❤️ using Python & AI-Assisted Development

