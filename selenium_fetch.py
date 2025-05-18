import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_page_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    logging.info(f"Setting up Chrome WebDriver for URL: {url}")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        logging.info("Fetching the webpage")
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
    except WebDriverException as e:
        logging.error(f"Error fetching the webpage: {e}")
        html = None
    finally:
        logging.info("Closing the WebDriver.")
        driver.quit()
    return html

if __name__ == "__main__":
    url = "https://airport.ee/lennuinfo/"
    html = fetch_page_html(url)
    if html:
        logging.info("Successfully fetched the webpage.")
    else:
        logging.error("Failed to fetch the webpage.")