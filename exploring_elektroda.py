import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import time

elements_to_json = []
# parameter - name of json file
# return data
# scrolling and clicking available

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-web-security")
options.add_argument('--disable-logging')
options.add_argument('ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

# service = Service('webdriver/chromedriver.exe')
service = Service('webdriver/chromedriver.exe')
driver = webdriver.Chrome(options = options,service=service)
driver.get('https://www.elektroda.pl/rtvforum/forum510.html')   # użyłem opcji szukaj ;)
time.sleep(8)

capabilities = webdriver.DesiredCapabilities().CHROME
capabilities['acceptSslCerts'] = True
elements = driver.find_elements(By.CSS_SELECTOR, 'h2')

print("Użyłem opcji szukaj :)")

def save_to_json(file):
    for element in elements:
        try:
            print(element.text)
            elements_to_json.append(element.text)
        except selenium.common.exceptions.StaleElementReferenceException:
            print("Elementy znajdują się na następnej stronie!")
            break
        time.sleep(0.1)

    for _ in range(5):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    print("See last posts")
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.sAH5RwMahEPB>li:nth-child(3)')))
    button.click()

    with open(file, 'w',encoding='utf-8') as f:
        json.dump(elements_to_json, f)

save_to_json('forum.json')
time.sleep(15)