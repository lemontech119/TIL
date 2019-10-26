from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict
import time
import json

with open('allTopping.json', encoding="utf-8") as json_file:
    allTopping = json.load(json_file)

file_data = OrderedDict()

chromedriver = 'C:\coding\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

baseUrl = 'https://www.pizzaalvolo.co.kr/pizzadetail/'
menuList = ['1059', '1028', '4536', '1033', '1016', '1025', '1009', '1002', '1043', '1021', '1017', '4531', '1037', '1001', '1003', '1004', '1005', '1006', '1007', '1008', '1010', '1012', '1019', '1020', '1023', '1024', '1018']

allTopping = []
for menu in menuList:
    topping = ''
    menuUrl = baseUrl + menu
    driver.get(menuUrl)
    time.sleep(1)
    title = driver.find_element_by_class_name('pizza-item-name').text
    shortInfo = driver.find_element_by_class_name('pizza-item-description').text
    largePrice = driver.find_elements_by_class_name('pizza-item-price')[0].text
    regularPrice = driver.find_elements_by_class_name('pizza-item-price')[1].text
    toppingList = driver.find_elements_by_class_name('pizza-topping-text-name')
    trashList = []
    for j in toppingList:
        trashList.append(j.text)


    for i in trashList:
        if i in allTopping:
            print("이게 포함되네 2")
        else:
            allTopping.append(i)

    file_data["brand"] = "피자알볼로"
    file_data["pizza_name"] = title
    file_data["short_info"] = shortInfo
    file_data["topping"] = trashList

    with open('alvolo.json', 'a', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    
with open('alvoloTopping.json', 'w', encoding="utf-8") as make_files:
    json.dump(allTopping, make_files, ensure_ascii=False, indent="\t")


driver.quit()
