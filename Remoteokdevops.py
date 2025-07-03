from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

def scrape_remoteok_with_selenium(url='https://remoteok.com/remote-devops-jobs?location=region_NA', output_csv='all_devops_jobs.csv'):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run without opening browser
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Initialize WebDriver
    service = Service()  # or specify ChromeDriver path: Service("path/to/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the page
    driver.get(url) #method called get() is used to open the page
    time.sleep(5)  # wait for JS to load (adjust if needed)

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()  

    # Parse job rows
    job_rows = soup.select('tr.job[data-id]')
    jobs = []
    for row in job_rows:
        try:
            job_id = row['data-id']
            title = row.select_one('h2').get_text(strip=True)
            company = row.select_one('.companyLink h3').get_text(strip=True) if row.select_one('.companyLink h3') else ''
            location = row.select_one('.location')
            location = location.get_text(strip=True) if location else ''
            tags = [tag.get_text(strip=True) for tag in row.select('.tag')]
            date = row.get('data-date', '')
            link = 'https://remoteok.com' + row.get('data-href', '')

            jobs.append({
                'Job ID': job_id,
                'Title': title,
                'Company': company,
                'Location': location,
                'Tags': ', '.join(tags),
                'Date': date,
                'Link': link
            })
        except Exception as e:
            print(f"⚠️ Skipping one row due to error: {e}")
            continue

    # Save to CSV
    if jobs:
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
            writer.writeheader()
            writer.writerows(jobs)

        print(f"✅ Scraped {len(jobs)} jobs and saved to {output_csv}")
    else:
        print("❌ No jobs found.")

if __name__ == '__main__':
    scrape_remoteok_with_selenium()
