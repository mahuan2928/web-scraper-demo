"""web-scraper-demo: scrape page 1 of books.toscrape.com into books.csv.

A deliberately small, single-site demo. The full version of this tool is
config-driven (any site described in YAML, pagination, Playwright mode,
dedup, Excel/Sheets export): https://mahuan220.gumroad.com/l/zknkka

Usage:  python scrape.py
Output: books.csv with columns title, price, rating, availability.
Only scrape publicly available data you have the right to collect.
"""
import csv
import time

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/page-1.html"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0 Safari/537.36 "
        "web-scraper-demo/1.0 (educational demo)"
    )
}
DELAY_SECONDS = 1.0  # be polite: never hammer a site
RATING_WORDS = {"One", "Two", "Three", "Four", "Five"}


def parse_books(html: str) -> list[dict]:
    """Extract title, price, rating, availability from one catalogue page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for pod in soup.select("article.product_pod"):
        title = pod.select_one("h3 a")["title"]
        price = pod.select_one("p.price_color").get_text(strip=True)
        rating_el = pod.select_one("p.star-rating")
        rating = next((c for c in rating_el["class"] if c in RATING_WORDS), "")
        availability = " ".join(
            pod.select_one("p.availability").get_text(" ", strip=True).split()
        )
        books.append(
            {
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability,
            }
        )
    return books


def main() -> None:
    print(f"Fetching {URL} ...")
    response = requests.get(URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    response.encoding = "utf-8"  # the site is UTF-8; don't let requests guess
    time.sleep(DELAY_SECONDS)  # polite pause after the request

    books = parse_books(response.text)
    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["title", "price", "rating", "availability"]
        )
        writer.writeheader()
        writer.writerows(books)
    print(f"Wrote {len(books)} books to books.csv")


if __name__ == "__main__":
    main()
