"""28. Implement a web scraper that saves data into a database and handles pagination."""

import os
import requests
from bs4 import BeautifulSoup
import sqlite3
import mysql.connector

DB_NAME = "web_scraper"
TABLE_NAME = "scraped_data"
PAGE_NUM = 1
HOST = "localhost"
USER = "colama"
PASSWORD = "prayas7@P"

# Connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host=HOST,  # MySQL host
        user=USER,  # MySQL username
        password=PASSWORD,  # MySQL password
        database=DB_NAME,
    )


def save_to_db(db_data_dict):
    """Save the scraped data into the SQLite database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO {TABLE_NAME} (title, description, owner, tags) VALUES (%s, %s, %s, %s)",
        (
            db_data_dict["title"],
            db_data_dict["description"],
            db_data_dict["owner"],
            db_data_dict["tags"],
        ),
    )
    conn.commit()
    conn.close()


def scrape_page(url):
    """Scrape data from a single page."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    question_section = soup.find("div", class_="flush-left", id="questions")
    for data in question_section.find_all("div"):
        description = data.find("div", class_="s-post-summary--content-excerpt")
        title = data.find("h3", class_="s-post-summary--content-title")
        owner = data.find("div", class_="s-user-card--link")
        li_tags = data.find("ul", class_="js-post-tag-list-wrapper")
        db_data_dict = {"description": "", "title": "", "owner": "", "tags": ""}
        if description not in [-1, None]:
            db_data_dict["description"] = description.get_text().strip()
        if title not in [-1, None]:
            db_data_dict["title"] = title.get_text().strip()
        if owner not in [-1, None]:
            db_data_dict["owner"] = owner.get_text().strip()
        if li_tags not in [-1, None]:
            db_data_dict["tags"] = ", ".join([li.get_text().strip() for li in li_tags])
        # Save the data to the database
        if all(value != "" for value in db_data_dict.values()):
            save_to_db(db_data_dict)


def create_new_database(DB_NAME, TABLE_NAME):
    """Create a new database and table in MySQL."""
    try:
        # Connect to MySQL server
        con = mysql.connector.connect(
            host=HOST,  # MySQL host
            user=USER,  # MySQL username
            password=PASSWORD,  # MySQL password
        )
        cursor = con.cursor()
        # Drop the database if it exists (optional)
        cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' deleted (if it exsisted).")
        # Create a new database
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created.")
        # Select the database to use
        cursor.execute(f"USE {DB_NAME}")
        # Create the table
        cursor.execute(
            f"""
                CREATE TABLE {TABLE_NAME} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description TEXT,
                    owner VARCHAR(255),
                    tags TEXT
                )
            """
        )
        print(f"Table '{TABLE_NAME}' created in database '{DB_NAME}'.")
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        print(f"Error: {e}")


def scrape_website(base_url, PAGE_NUM):
    """Scrape the entire website, handling pagination."""
    # Database and table setup
    create_new_database(DB_NAME, TABLE_NAME)
    page = 1
    while True:
        if PAGE_NUM < page:
            print("No more pages to scrape.")
            break
        print(f"Scraping page {page}...", end=" ")
        url = f"{base_url}@page={page}"
        response = requests.get(url)
        scrape_page(url)
        print("done")
        page += 1

def read_records():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    records = cursor.fetchall()
    print("Questions in the database:")
    for record in records:
        print(record)
    db.close()

if __name__ == "__main__":
    base_url = "https://stackoverflow.com/questions?tab=newest"
    scrape_website(base_url, PAGE_NUM)
    read_records()
