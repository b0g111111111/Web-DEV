import requests
from bs4 import BeautifulSoup

url ='https://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    first_quote = soup.find('span', class_='text').text
    first_author = soup.find('small', class_='author').text

    print(f'Quote: {first_quote}')
    print(f'Author: {first_author}')

else:
    print('Failed to load website!')