from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import random
import mysql.connector

def human_scroll(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    scroll_pause = random.uniform(1, 2)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
        if new_height >= last_height:
            break

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-webgl")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def save_to_mysql(data):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deepika@464",
            database="scraping_db"
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO amazon_products (title, price, rating, reviews, link)
        VALUES (%s, %s, %s, %s, %s)
        """

        for item in data:
            cursor.execute(insert_query, (
                item["Title"],
                item["Price"],
                item["Rating"],
                item["Reviews"],
                item["Link"]
            ))

        conn.commit()
        print(f"✅ Saved {len(data)} products to MySQL database")

    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def scrape_amazon(search_term, max_pages=3):
    data = []

    for page in range(1, max_pages + 1):
        url = f"https://www.amazon.com/s?k={search_term}&page={page}"
        print(f"🌟 Loading: {url}")

        try:
            driver = get_driver()
            driver.get(url)
            human_scroll(driver)
            time.sleep(random.randint(3, 6))

            if "Enter the characters" in driver.page_source:
                print("⚠️ Captcha detected! Please solve it manually...")
                while "Enter the characters" in driver.page_source:
                    time.sleep(10)
                print("✅ Captcha solved.")

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            products = soup.select('div.s-main-slot div[data-component-type="s-search-result"]')

            for product in products:
                title = product.select_one('h2 a span')
                title = title.get_text(strip=True) if title else "N/A"

                price = product.select_one('.a-price .a-offscreen')
                price = price.get_text(strip=True) if price else "N/A"

                rating = product.select_one('.a-icon-alt')
                rating = rating.get_text(strip=True) if rating else "N/A"

                reviews = product.select_one('.a-size-base')
                reviews = reviews.get_text(strip=True) if reviews else "N/A"

                link = product.select_one('h2 a')
                link = "https://www.amazon.com" + link['href'] if link else "N/A"

                data.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Reviews": reviews,
                    "Link": link
                })

            print(f"✅ Scraped {len(products)} products from page {page}")

        except Exception as e:
            print(f"❌ Error on page {page}: {e}")
        finally:
            driver.quit()

    if data:
        save_to_mysql(data)
    else:
        print("❌ No products found.")

if __name__ == '__main__':
    scrape_amazon("laptop", max_pages=3)


#   to run in mysql use the following query:
""" USE scraping_db;
SELECT * FROM amazon_products;"""