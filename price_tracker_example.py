import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"  # Practice site - no real scraping restrictions

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

print("Top 5 books with prices:")
for i, book in enumerate(books[:5], 1):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    print(f"{i}. {title} - {price}")
