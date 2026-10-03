import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    all_countries = soup.select('div.country')

    with open('countries_detailed_data.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Country Name', 'Capital', 'Population', 'Area'])

        for box in all_countries:
            country_name = box.select_one('h3.country-name').get_text().strip()
            capital_name = box.select_one('span.country-capital').get_text().strip()
            population = box.select_one('span.country-population').get_text()
            area = box.select_one('span.country-area').get_text()

            writer.writerow([country_name, capital_name, population, area])

    print('Finished Scraping')

else:
    print('Failed to load website!')