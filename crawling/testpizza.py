from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\coding\chromedriver.exe'
## selenium에 필요한 크롬드라이버 위치

driver = webdriver.Chrome(chromedriver)
## 크롬 드라이버 실행

baseUrl = 'https://www.pizzahut.co.kr/menu/pizza/pizzaList/B02'
## 기본적인 url

driver.get(baseUrl)
## 페이지 이동

time.sleep(1)

for i in range(12):
    menuList = driver.find_elements_by_class_name('thumb_img_wrap')
    menuList[i].click()
    time.sleep(1)

    title = driver.find_element_by_class_name('wh_section_header').find_element_by_tag_name('h2').text
    ##short_info = driver.find_element_by_class_name('menu_txt').text
    ##topping = driver.find_element_by_class_name('basic_topping_desc').text
    print(title)
    driver.get(baseUrl)
    time.sleep(1)

time.sleep(3)

driver.quit()