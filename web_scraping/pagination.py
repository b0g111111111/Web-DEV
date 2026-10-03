import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

base_url = "https://quotes.toscrape.com/"
current_url = base_url

with open('quotes_data.csv', mode = 'w', newline= '', encoding= 'utf-8')as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])
    page_number = 1




    while current_url:
        print(f'Scraping page {page_number}: {current_url}')

        response = requests.get(current_url)

        if response.status_code != 200:
            print("Failed to load page")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')

        all_quotes_box = soup.select('div.quote')

        for box in all_quotes_box:
            quote_text = box.select_one('span.text').get_text()
            author_name = box.select_one('small.author').get_text()

            writer.writerow([quote_text, author_name])
        next_button = soup.select_one('li.next a')

        if next_button:
            next_page_link = next_button['href']
            current_url = urljoin(base_url, next_page_link)
            page_number = page_number + 1
        else:
            current_url = None


print("Finished Scraping")