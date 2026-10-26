# Testing

Smoke test run on 2026-10-26 (Python 3.12.3 venv; pinned deps
`requests==2.32.3`, `beautifulsoup4==4.12.3`).

## Commands

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scrape.py
```

## Live-site result

The live site was reachable and the test **passed**:

```
Fetching https://books.toscrape.com/catalogue/page-1.html ...
Wrote 20 books to books.csv
```

Validation of the generated `books.csv` (via `csv.DictReader`):

- **Rows: 20** (all books on catalogue page 1) ✅
- **Columns: `title, price, rating, availability`** ✅
- **Rows with any empty field: 0** ✅
- First row: `A Light in the Attic, £51.77, Three, In stock`
- `sample_output.csv` in the repo is the header + first 5 rows of this run.

## Issue found and fixed during the test

The first run produced mojibake prices (`Â£51.77`) because `requests`
guessed the wrong encoding from the response headers. Fixed by setting
`response.encoding = "utf-8"` in `scrape.py` before parsing; the re-run
produced correct `£` prices in all 20 rows.

## Not tested

- Behaviour when the site is down or its markup changes (the demo has no
  retry logic by design — that is one of the full version's features).
