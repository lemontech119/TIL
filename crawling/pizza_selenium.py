from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

## 파파존스 크롤링은 request와 BeautifulSoup으로 데이터를 가져오는 데 무리가 있을 것이라고 판단되어 selenium활용

chromedriver = 'C:\coding\chromedriver.exe'
## selenium에 필요한 크롬드라이버 위치

driver = webdriver.Chrome(chromedriver)
## 크롬 드라이버 실행

baseUrl = 'https://www.pji.co.kr/menu/menuList.jsp?'
## 기본적인 url

driver.get(baseUrl)
## 페이지 이동

time.sleep(1)
## page loading을 위한 대기 시간

menuArray = []

menuList = driver.find_element_by_id('menuListContent').find_elements_by_tag_name('li')
## 피자 페이지로 이동을 위해 피자에서 필요한 부분만 빼놓음 리스트형태
for menu in menuList:
    
    onclick = menu.find_element_by_class_name('btn_goview').get_attribute('onclick')
    onclick = onclick[22 :26] 
    ## 필요한 데이터만 빼오는데 문제가 있어 빼온 다음에 숫자만 빼온 것
    menuArray.append(onclick)
    

for i in menuArray:
    menuUrl = 'https://www.pji.co.kr/menu/menuView.jsp?pd_id='
    
    lastUrl = menuUrl + i
    driver.get(lastUrl)
    time.sleep(2)
    title = driver.find_element_by_class_name('product_title').find_element_by_tag_name('h4').text
    topping = driver.find_element_by_class_name('basic_topping_desc').text
    print(title)
    print(topping)
    print("--------------------------------")



time.sleep(3)

driver.quit()