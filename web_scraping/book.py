import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    print('All Books Name and Price')

    book1_title = books[0].find('h3').text
    book1_price = books[0].find('p', class_='price_color').text
    print(f'Name: {book1_title} | Price: {book1_price}')

    book2_title = books[1].find('h3').text
    book2_price = books[1].find('p', class_='price_color').text
    print(f'Name: {book2_title} | Price: {book2_price}')

    book3_title = books[2].find('h3').text
    book3_price = books[2].find('p', class_='price_color').text
    print(f'Name: {book3_title} | Price: {book3_price}')

    book4_title = books[3].find('h3').text
    book4_price = books[3].find('p', class_='price_color').text
    print(f'Name: {book4_title} | Price: {book4_price}')

    book5_title = books[4].find('h3').text
    book5_price = books[4].find('p', class_='price_color').text
    print(f'Name: {book5_title} | Price: {book5_price}')

    book6_title = books[5].find('h3').text
    book6_price = books[5].find('p', class_='price_color').text
    print(f'Name: {book6_title} | Price: {book6_price}')

    book7_title = books[6].find('h3').text
    book7_price = books[6].find('p', class_='price_color').text
    print(f'Name: {book7_title} | Price: {book7_price}')

    book8_title = books[7].find('h3').text
    book8_price = books[7].find('p', class_='price_color').text
    print(f'Name: {book8_title} | Price: {book8_price}')

    book9_title = books[8].find('h3').text
    book9_price = books[8].find('p', class_='price_color').text
    print(f'Name: {book9_title} | Price: {book9_price}')

    book10_title = books[9].find('h3').text
    book10_price = books[9].find('p', class_='price_color').text
    print(f'Name: {book10_title} | Price: {book10_price}')

    book11_title = books[10].find('h3').text
    book11_price = books[10].find('p', class_='price_color').text
    print(f'Name: {book11_title} | Price: {book11_price}')

    book12_title = books[11].find('h3').text
    book12_price = books[11].find('p', class_='price_color').text
    print(f'Name: {book12_title} | Price: {book12_price}')

    book13_title = books[12].find('h3').text
    book13_price = books[12].find('p', class_='price_color').text
    print(f'Name: {book13_title} | Price: {book13_price}')

    book14_title = books[13].find('h3').text
    book14_price = books[13].find('p', class_='price_color').text
    print(f'Name: {book14_title} | Price: {book14_price}')

    book15_title = books[14].find('h3').text
    book15_price = books[14].find('p', class_='price_color').text
    print(f'Name: {book15_title} | Price: {book15_price}')

    book16_title = books[15].find('h3').text
    book16_price = books[15].find('p', class_='price_color').text
    print(f'Name: {book16_title} | Price: {book16_price}')

    book17_title = books[16].find('h3').text
    book17_price = books[16].find('p', class_='price_color').text
    print(f'Name: {book17_title} | Price: {book17_price}')

    book18_title = books[17].find('h3').text
    book18_price = books[17].find('p', class_='price_color').text
    print(f'Name: {book18_title} | Price: {book18_price}')

    book19_title = books[18].find('h3').text
    book19_price = books[18].find('p', class_='price_color').text
    print(f'Name: {book19_title} | Price: {book19_price}')

    book20_title = books[19].find('h3').text
    book20_price = books[19].find('p', class_='price_color').text
    print(f'Name: {book20_title} | Price: {book20_price}')

else:
    print('Failed to load website!')