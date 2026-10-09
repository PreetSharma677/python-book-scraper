import requests
import csv
from bs4 import BeautifulSoup

all_books = []
failed_pages = []

for page in range(1, 6):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Page {page} failed: {e}")
        failed_pages.append(page)
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
      
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        all_books.append([title, price])

    print(f"Page {page} completed | Books: {len(all_books)}")

with open("books_day3.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(all_books)

print("Done! Total books:", len(all_books))
print("Saved to books_day3.csv") 
print("Failed pages:", failed_pages)
print("Unique books:", len(set(book[0] for book in all_books)))
 