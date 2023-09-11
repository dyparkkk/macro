from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip

def naver_login(driver, login_class):
  driver.find_element(By.CLASS_NAME, login_class).click()

  driver.implicitly_wait(2)
  pyperclip.copy("dkdlel1z")
  driver.find_element(By.ID, 'id').send_keys(Keys.COMMAND, 'v')

  pyperclip.copy("do15964")
  driver.find_element(By.ID, 'pw').send_keys(Keys.COMMAND, 'v')
  driver.find_element(By.CLASS_NAME, 'btn_login').click()
