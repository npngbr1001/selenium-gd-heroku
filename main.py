from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("GOOGLE_CHROME_PATH"), options=options)

driver.get("https://www.google.com")
print(driver.page_source)