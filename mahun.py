
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

def choice_date(driver, day):
  driver.implicitly_wait(2)
  driver.find_element(By.PARTIAL_LINK_TEXT, day).click()

def choice_time(driver, isAm, time, duration):
  driver.implicitly_wait(2)
  parent = driver.find_element(By.PARTIAL_LINK_TEXT, '오후')
  if isAm:
    parent = driver.find_element(By.PARTIAL_LINK_TEXT, '오전')
    
  # 시간 고르기
  possibleElements = parent.find_elements(By.CLASS_NAME, 'anchor')
  isCheck = False
  for element in possibleElements:
    # if time and time+duration 존재 ?
    timedElement = element.find_element(By.PARTIAL_LINK_TEXT, time)
    if timedElement.isDisplayed():
      timedElement.click()
      isCheck = True
      break
  
  if isCheck:
    driver.find_element(By.CLASS_NAME, 'btn_srch on').click()
    driver.implicity_wait(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, '다음단계').click()
    driver.implicity_wait(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, '결제하기').click()



def main():
  driver.get(url)
# xpath = '//태그[@속성="속성값"]'
  driver.implicitly_wait(2)
  login.naver_login(driver, 'gnb_btn_login') # 로그인 class name 

  # 코트 선택
  driver.implicitly_wait(2)
  elements = driver.find_elements(By.CLASS_NAME, 'lnk_item_book')
  for element in elements:
    element.click()
     # 날짜 선택
    choice_date(driver, '12')

    # 시간 선택
    choice_time(driver, True, '12:00', 1)
    driver.back()

  

  time.sleep(5)

if __name__ == '__main__':
  main()

