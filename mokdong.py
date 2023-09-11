from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = "https://www.ycs.or.kr/fmcs/33"
driver.get(url)
# xpath = '//태그[@속성="속성값"]'
xpath_login = '//a[@id="process_login"]'
driver.find_element(By.XPATH, xpath_login).click()

xpath_id = '//input[@id="user_id"]'
driver.find_element(By.XPATH, xpath_id).send_keys("id")
time.sleep(3)