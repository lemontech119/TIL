import requests
import time
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

file_data = OrderedDict()

# chromedriver = 'C:\coding\chromedriver.exe'

# driver = webdriver.Chrome(chromedriver)

base_url = 'http://www.mrpizza.co.kr/menu/productView'

menu_list = ['0101011140', '0126011120', '0126011110', '0101011070', '0101011060', '0126010890', '0125010860', '0125010870', '0125010880', '0101010740', '0101010770', '0101010760', '0102010020']
print(len(menu_list))
# '0126011120'
gubun = ['MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP01', 'MP02']
print(len(gubun))
gubun_num = 0
for menu in menu_list:
    
    url = base_url
    data  = {'product_case': 'MP01', 'product_key': menu, 'product_gubun': gubun[gubun_num], 'dough_id': '', 'option_id': '', 'pasta_option_id': '', 'class_id_0': '01', 'base_id_0': '01', 'size_id_0': '01', 'product_id_0': '1140', 'menu_group1_0': 'MP01', 'menu_group2_0': 'MP0158', 'menu_group3_0': 'x', 'option_group2_0': 'OP0201', 'option_group3_0': 'x', 'option_group6_0': 'x', 'p_item_0': '0101021140|||37500|||1', 'class_id_1': '01', 'base_id_1': '26', 'size_id_1': '01', 'product_id_1': '1120', 'menu_group1_1': 'MP01', 'menu_group2_1': 'MP0157', 'menu_group3_1': 'x', 'option_group2_1': 'OP0211', 'option_group3_1': 'x', 'option_group6_1': 'x', 'p_item_1': '0126021120|||36500|||1', 'class_id_2': '01', 'base_id_2': '26', 'size_id_2': '01', 'product_id_2': '1110', 'menu_group1_2': 'MP01', 'menu_group2_2': 'MP0156', 'menu_group3_2': 'x', 'option_group2_2': 'OP0211', 'option_group3_2': 'x', 'option_group6_2': 'x', 'p_item_2': '0126021110|||36500|||1', 'class_id_3': '01', 'base_id_3': '01', 'size_id_3': '01', 'product_id_3': '1070', 'menu_group1_3': 'MP01', 'menu_group2_3': 'MP0151', 'menu_group3_3': 'x', 'option_group2_3': 'OP0201', 'option_group3_3': 'x', 'option_group6_3': 'x', 'p_item_3': '0101021070|||35900|||1', 'class_id_4': '01', 'base_id_4': '01', 'size_id_4': '01', 'product_id_4': '1060', 'menu_group1_4': 'MP01', 'menu_group2_4': 'MP0150', 'menu_group3_4': 'x', 'option_group2_4': 'OP0201', 'option_group3_4': 'x', 'option_group6_4': 'x', 'p_item_4': '0101021060|||33900|||1', 'class_id_5': '01', 'base_id_5': '26', 'size_id_5': '01', 'product_id_5': '0890', 'menu_group1_5': 'MP01', 'menu_group2_5': 'MP0138', 'menu_group3_5': 'x', 'option_group2_5': 'OP0211', 'option_group3_5': 'x', 'option_group6_5': 'x', 'p_item_5': '0126020890|||31900|||1', 'class_id_6': '01', 'base_id_6': '25', 'size_id_6': '01', 'product_id_6': '0860', 'menu_group1_6': 'MP01', 'menu_group2_6': 'MP0135', 'menu_group3_6': 'x', 'option_group2_6': 'OP0210', 'option_group3_6': 'x', 'option_group6_6': 'x', 'p_item_6': '0125020860|||34900|||1', 'class_id_7': '01', 'base_id_7': '25', 'size_id_7': '01', 'product_id_7': '0870', 'menu_group1_7': 'MP01', 'menu_group2_7': 'MP0136', 'menu_group3_7': 'x', 'option_group2_7': 'OP0210', 'option_group3_7': 'x', 'option_group6_7': 'x', 'p_item_7': '0125020870|||35900|||1', 'class_id_8': '01', 'base_id_8': '25', 'size_id_8': '01', 'product_id_8': '0880', 'menu_group1_8': 'MP01', 'menu_group2_8': 'MP0137', 'menu_group3_8': 'x', 'option_group2_8': 'OP0210', 'option_group3_8': 'x', 'option_group6_8': 'x', 'p_item_8': '0125020880|||31900|||1', 'class_id_9': '01', 'base_id_9': '01', 'size_id_9': '01', 'product_id_9': '0740', 'menu_group1_9': 'MP01', 'menu_group2_9': 'MP0131', 'menu_group3_9': 'x', 'option_group2_9': 'OP0201', 'option_group3_9': 'OP0701', 'option_group6_9': 'x', 'p_item_9': '0101020740|||35900|||1', 'class_id_10': '01', 'base_id_10': '01', 'size_id_10': '01', 'product_id_10': '0770', 'menu_group1_10': 'MP01', 'menu_group2_10': 'MP0133', 'menu_group3_10': 'x', 'option_group2_10': 'OP0201', 'option_group3_10': 'x', 'option_group6_10': 'x', 'p_item_10': '0101020770|||35900|||1', 'class_id_11': '01', 'base_id_11': '01', 'size_id_11': '01', 'product_id_11': '0760', 'menu_group1_11': 'MP01', 'menu_group2_11': 'MP0132', 'menu_group3_11': 'x', 'option_group2_11': 'OP0201', 'option_group3_11': 'x', 'option_group6_11': 'x', 'p_item_11': '0101020760|||34900|||1'}
    gubun_num = gubun_num + 1
    # driver.post(url, data=data)
    response = requests.post(url, data=data).text
    soup = BeautifulSoup(response, 'html.parser')
    # product = driver.find_elements_by_class_name('product_cont').text
    title = soup.select_one('.product_top').select_one('h1').text
    short_info = soup.select_one('.product_top').select_one('div').text
    short_info = short_info.replace("\n", "")
    short_info = short_info.replace("\t", "")
    short_info = short_info.replace("\r", "")    
    product = soup.select_one('.product_summary').text
    product = product.replace("\n", "")
    product = product.replace("\t", "")
    product = product.replace("\r", "")
    
    file_data["brand"] = "미스터피자"
    file_data["pizza_name"] = title
    file_data["short_info"] = short_info
    file_data["topping"] = product
    with open('mr.json', 'a', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    

    
    print('------------------------')
    