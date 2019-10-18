from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\coding\chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

menu = 'http://www.redcappizza.com/menu/pizza.jsp'

driver.get(menu)

time.sleep(1)

menuArray = []

menuList = driver.find_element_by_class_name('gdslist').find_element_by_tag_name('ul')
menuList = menuList.find_elements_by_tag_name('li')

for menu in menuList:
    idx = menu.get_attribute('idx')
    if idx:
        menuArray.append(idx)

menuView = 'http://www.redcappizza.com/menu/menu_view.jsp?pdid='

print(menuArray)
for url in menuArray:
    menuUrl = ''
    menuUrl = menuView + url
    
    driver.get(menuUrl)
    time.sleep(2)
    
    title = driver.find_element_by_class_name('pdname').text
    topping = driver.find_element_by_class_name('poscode4').text
    print("-------------------------------")
    print(title)
    print(topping)


driver.quit()
