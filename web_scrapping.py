import requests
from bs4 import BeautifulSoup
import csv
with open("books_data.csv", "w", newline='', encoding='utf-8') as data:
    writer = csv.writer(data)
    writer.writerow(["Category", "Book Name", "Rating", "Price"])
    base_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    response = requests.get(base_url)
    if response.status_code == 200:
        print("Successfully fetched the main page!")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        exit()
    soup = BeautifulSoup(response.text, 'html.parser')
    category_section = soup.find('ul', {'class': 'nav nav-list'})
    categories = category_section.find_all('a')
    category_links = []
    for category in categories[1:]:
        category_name = category.text.strip()
        category_url = base_url.rsplit('/', 1)[0] + "/" + category['href']
        category_links.append((category_name, category_url))
    for category_name, category_url in category_links:
        while category_url:
            category_response = requests.get(category_url)
            category_soup = BeautifulSoup(category_response.text, 'html.parser')
            books = category_soup.find_all('article', {'class': 'product_pod'})
            for book in books:
                book_name = book.find('h3').find('a')['title']
                rating_class = book.find('p', {'class': 'star-rating'})['class'][1]
                rating = rating_class.capitalize()
                price = book.find('p', {'class': 'price_color'}).text.strip()
                writer.writerow([category_name, book_name, rating, price])
            next_page = category_soup.find('li', {'class': 'next'})
            if next_page:
                next_page_url = next_page.find('a')['href']
                category_url = category_url.rsplit('/', 1)[0] + "/" + next_page_url
            else:
                category_url = None
        print(f"Finished scraping books from the category: {category_name}")
with open("books_data.csv", "r", encoding='utf-8') as new_data:
    print(new_data.read())
