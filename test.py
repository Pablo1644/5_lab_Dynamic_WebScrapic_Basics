from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)

driver = webdriver.Chrome(
    options=option, executable_path="path-of-driver\chromedriver.exe"
)
driver.get('https://www.elektroda.pl/rtvforum/forum510.html')
time.sleep(10)