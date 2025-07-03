from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import random

def scrape_amazon(search_term, max_pages=3, output_csv='amazon_products.csv'):
    chrome_options = Options()
    # No headless so you can see browser
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    data = []
    for page in range(1, max_pages + 1):
        url = f"https://www.amazon.com/s?k={search_term}&page={page}"
        driver.get(url)

        # Add random delay (3-7 seconds) to mimic human behavior
        time.sleep(random.randint(3, 7))

        # Check for Captcha (simple check: is there "Enter the characters" text?)
        if "Enter the characters" in driver.page_source:
            print("⚠️ Captcha detected! Please solve it manually in the browser...")
            while "Enter the characters" in driver.page_source:
                time.sleep(25)  # Wait for you to solve the Captcha
            print("✅ Captcha solved. Continuing...")

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

        print(f"✅ Scraped page {page}, found {len(products)} products")

    driver.quit()

    # Save to CSV
    if data:
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"✅ Scraped {len(data)} products across {max_pages} page(s) and saved to {output_csv}")
    else:
        print("❌ No products found.")

if __name__ == '__main__':
    scrape_amazon("laptop", max_pages=3)
