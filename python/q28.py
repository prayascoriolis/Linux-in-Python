'''28. Implement a web scraper that saves data into a database and handles pagination.'''
# https://stackoverflow.com/questions

import requests
from bs4 import BeautifulSoup
import sqlite3

def save_to_db(title, link):
    """Save the scraped data into the SQLite database."""
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (title, link) VALUES (?, ?)", (title, link))
    conn.commit()
    conn.close()

def scrape_page(url):
    """Scrape data from a single page."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    question_section = soup.find('div', class_='flush-left', id="questions")
    for data in question_section.find_all('div'):
        description = data.find('div', class_='s-post-summary--content-excerpt')
        title = data.find('h3')
        owner = data.find('div', class_='s-user-card--link')
        li_tags = data.find('ul')
        # question hyper link also
        if description not in [-1, None]:
            print('description', description.get_text().strip())
        if title not in [-1, None]:
            print('title', title.get_text().strip())
        if owner not in [-1, None]:
            print('owner',owner.get_text().strip())
        if li_tags not in [-1, None]:
            print('tags')
            print([li.get_text().strip() for li in li_tags])
        # break
        # Save the data to the database
        # save_to_db(title, link)

def scrape_website(base_url):
    """Scrape the entire website, handling pagination."""
    page_num = 1
    while True:
        if page_num == 2:
            print("No more pages to scrape.")
            break
        print(f"Scraping page {page_num}...")
        url = f"{base_url}@page={page_num}"
        response = requests.get(url)
        scrape_page(url)
        page_num += 1

def get_in_the_news(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        news_section = soup.find('div', class_='questions', id="flush-left")
        if news_section:
            # Extract and clean the text
            headlines = [item.get_text() for item in news_section.find_all('li')]
            news_content = "\n".join(headlines)
            return news_content
        else:
            print("The 'In the news' section was not found.")
    except Exception as e:
        print(f"An error occurred while making the request: {e}")

if __name__ == "__main__":
    base_url = 'https://stackoverflow.com/questions?tab=newest'
    scrape_website(base_url)
