from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import OrderedDict
import time
import json

with open('allTopping.json', encoding="utf-8") as json_file:
    allTopping = json.load(json_file)

file_data = OrderedDict()

chromedriver = 'C:\coding\chromedriver.exe'
## selenium에 필요한 크롬드라이버 위치

driver = webdriver.Chrome(chromedriver)
## 크롬 드라이버 실행

baseUrl = 'https://www.pizzahut.co.kr/menu/pizza/pizzaList/B02'
## 기본적인 url

driver.get(baseUrl)
## 페이지 이동

time.sleep(3)

allTopping = []
for i in range(12):
    menuList = driver.find_elements_by_class_name('thumb_img_wrap')
    menuList[i].click()
    time.sleep(1)
    toppingNext = driver.find_element_by_class_name('bx-next')
    toppingNext.click()
    

    title = driver.find_element_by_class_name('wh_section_header').find_element_by_tag_name('h2').text
    toppingList = driver.find_elements_by_class_name('item_txt')
    result = []

    for i in toppingList:
        i = i.text
        if i == "":
            print("")
        else:
            result.append(i)

    result = list(set(result))
    for topping in result:
        if topping in allTopping:
            print("이게 포함되네 5")
        else:
            print(topping)
            allTopping.append(topping)

    file_data["barnd"] = "피자헛"
    file_data["pizza_name"] = title
    file_data["short_info"] = ""
    file_data["topping"] = result

    with open('hut.json', 'a', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

    driver.get(baseUrl)
    time.sleep(1)

with open('hutTopping.json', 'w', encoding="utf-8") as make_files:
    json.dump(allTopping, make_files, ensure_ascii=False, indent="\t")


time.sleep(3)


driver.quit()