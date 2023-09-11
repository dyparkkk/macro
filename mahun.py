
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip
import src.component.login as login

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
url = "https://booking.naver.com/booking/10/bizes/210031"

def main():
  driver.get(url)
# xpath = '//태그[@속성="속성값"]'
  driver.implicitly_wait(2)
  login.naver_login(driver, 'gnb_btn_login') # 로그인 class name 

  # 코트 선택
  driver.implicitly_wait(2)
  driver.find_element(By.PARTIAL_LINK_TEXT, '9월 A코트(실내)').click() 

  # 날짜 선택
  driver.implicitly_wait(2)
  day = '12'
  driver.find_element(By.PARTIAL_LINK_TEXT, day).click()

  # 시간 선택
  driver.implicitly_wait(2)
  wanted_times = ['8:00', '9:00', '10:00', '11:00', '12:00']
  elements =  driver.find_elements(By.CLASS_NAME, 'anchor')
  print (elements)
  if len(elements) < 0:
    print('예약 가능한 시간이 없습니다.')

  # for element in elements:
  #   if driver.

  time.sleep(5)

if __name__ == '__main__':
  main()

