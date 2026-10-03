import requests
from bs4 import BeautifulSoup

url ='https://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    all_quotes = soup.select('dev.quote')

    for box in all_quotes:
        quote_text = box.select_one('span.text').get_text()
        author_name = box.select_one('small.author').get_text()

        tags_list = box.select_one("div.tags a.tag")

        tags = [tag.get_text() for tag in tags_list]

        print(f'Quote: {quote_text}')
        print(f'Author: {author_name}')
        print(f'{tags}')

else:
    print('Failed to load website!')