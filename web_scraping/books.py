import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url)
response.encoding = 'utf-8'   # <-- add this line

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    total = 0
    number_books = len(books)

    for products in books:
        book_title = products.find('h3').find('a')['title']
        book_price = products.find('p', class_='price_color').text 

        price_value = float(book_price.replace('£',''))

        total = total + price_value
        

        print(f'Name: {book_title} | Price: {book_price}')

    average = total / number_books
    

    print(f'Total price: £{total}')
    print(f'Average price: £{average}')

else:
    print('Failed')