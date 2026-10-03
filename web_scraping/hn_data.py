import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

base_url = "https://news.ycombinator.com/"
current_url = base_url

with open('hn_data.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['News Title', 'Author'])
    page_number = 1

    while current_url:
        print(f'Scraping page {page_number}: {current_url}')

        response = requests.get(current_url)

        if response.status_code != 200:
            print("Failed to load page")
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        all_story_boxes = soup.select('tr.athing')

        for box in all_story_boxes:
            title_tag = box.select_one('span.titleline > a')
            news_title = title_tag.get_text() if title_tag else "Unknown"

            subtext_box = box.find_next_sibling('tr')
            author_tag = subtext_box.select_one('a.hnuser') if subtext_box else None
            author_name = author_tag.get_text() if author_tag else "Unknown"

            writer.writerow([news_title, author_name])

        next_button = soup.select_one('a.morelink')

        if next_button:
            next_page_link = next_button['href']
            current_url = urljoin(base_url, next_page_link)
            page_number = page_number + 1
        else:
            current_url = None

print("Finished Scraping")