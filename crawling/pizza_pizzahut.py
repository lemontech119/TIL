from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\coding\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

pizzaHut = 'https://www.pizzahut.co.kr/menu/pizza/pizzaList/B02'

driver.get(pizzaHut)

time.sleep(2)

menuList = driver.find_elements_by_class_name('thumb_img_wrap')

for menu in menuList:
    menuList.click()
    time.sleep(2)
    currntUrl = driver.page_source
    
    driver.back()

driver.quit()