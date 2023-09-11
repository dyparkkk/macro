from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = "https://www.naver.com/"
driver.get(url)
# xpath = '//태그[@속성="속성값"]'
driver.implicitly_wait(2)
xpath = '//a[@class="MyView-module__link_login___HpHMW"]'
driver.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW').click()

xpath2 = '//input[@id="id"]'
driver.find_element(By.XPATH, xpath2).send_keys("id")
time.sleep(3)

