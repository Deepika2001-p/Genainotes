from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

def scrape_naukri_jobs(output_csv='naukri_jobs.csv'):
    url = 'https://www.naukri.com/data-analyst-jobs-in-hyderabad-secunderabad?k=data%20analyst&l=hyderabad&experience=1&nignbevent_src=jobsearchDeskGNB'

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run visibly for debugging
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    driver.save_screenshot("naukri_debug.png")
    print("✅ Screenshot saved as naukri_debug.png")

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.jobTuple'))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_cards = soup.select('article.jobTuple')

        if not job_cards:
            print("⚠ No job data found after visible load!")
            return

        # (Continue as before to process and save jobs)

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()

scrape_naukri_jobs()
