from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\coding\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

baseUrl = 'https://www.pji.co.kr/menu/menuList.jsp?'

driver.get(baseUrl)
time.sleep(1)

menuArray = []

menuList = driver.find_element_by_id('menuListContent').find_elements_by_tag_name('li')
for menu in menuList:
    
    onclick = menu.find_element_by_class_name('btn_goview').get_attribute('onclick')
    onclick = onclick[22 :26] 
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