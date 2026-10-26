# web-scraper-demo

A tiny, single-file Python scraper that pulls every book on the first
catalogue page of [books.toscrape.com](https://books.toscrape.com) — title,
price, rating, availability — and writes them to `books.csv`.

It is the **free demo** of a config-driven scraping engine. The selectors and
the target site are hardcoded on purpose: it shows the basic mechanics
(fetch politely → parse with BeautifulSoup → write CSV) in ~60 lines, with
no framework and no config files.

## Quickstart

```bash
git clone https://github.com/mahuan2928/web-scraper-demo
cd web-scraper-demo
pip install -r requirements.txt   # Python 3.10+
python scrape.py
```

Output: `books.csv` (20 rows) next to the script. A committed
`sample_output.csv` shows the first rows of a real run.

## What it does

- Sends a real `User-Agent` header and pauses briefly — scraping politely
  is the default, not an afterthought.
- Parses each `article.product_pod` card: `h3 a[title]` for the title,
  `p.price_color` for the price, the `p.star-rating` class for the rating,
  and `p.availability` for stock status.
- Writes clean UTF-8 CSV with the columns
  `title, price, rating, availability`.

## Responsible use

Only scrape data you have the right to collect. Respect each site's terms
of service and robots rules, keep request rates low, and cache pages instead
of re-fetching. This demo targets books.toscrape.com, a site built
specifically for scraping practice — don't point the pattern at a real shop
without checking its terms first.

## Free demo vs Full version

| | This demo (free) | [Full version — Config-Driven Web Scraper Engine ($39)](https://mahuan220.gumroad.com/l/zknkka) |
|---|---|---|
| Target sites | 1 hardcoded site | **Any site, described in a YAML config — no code changes** |
| Pagination | Page 1 only | **Next-link, page-number, and infinite-scroll pagination** |
| JavaScript pages | Not supported | **Playwright mode for JS-rendered pages** |
| Data quality | Raw rows | **Deduplication + invalid-row handling, with dropped-row counts** |
| Output | CSV | **CSV and Excel (.xlsx)** |
| Extras | — | **Optional Google Sheets export, retry/backoff, cron-friendly scheduled runs** |

👉 **Get the full version: [Config-Driven Web Scraper Engine — $39 on Gumroad](https://mahuan220.gumroad.com/l/zknkka)**

If you scrape more than one site, the demo's approach breaks down fast:
every new site means new hardcoded selectors, new pagination logic, new
edge cases. The full version moves all of that into a config file — a new
site is a new YAML, not a new program.

## Author

Built by **Marty Ma** — Senior AI & Data Engineer (Tokyo).

## License

MIT — see [LICENSE](LICENSE).
