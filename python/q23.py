'''23. Create a script to scrape web content and extract data (e.g., “In the news” from Wiki).'''
# https://en.wikipedia.org/wiki/Main_Page

import requests
from bs4 import BeautifulSoup

def get_in_the_news(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        news_section = soup.find('div', class_='mp-contains-float', id="mp-itn")
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
    link = "https://en.wikipedia.org/wiki/Main_Page"
    news_content = get_in_the_news(link)
    if news_content:
        print(news_content)