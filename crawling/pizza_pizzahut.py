#-*- coding:utf-8 -*-
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys


# chromedriver = 'C:\coding\chromedriver.exe'

# driver = webdriver.Chrome(chromedriver)

base_url = 'https://www.pizzahut.co.kr/menu/pizza/pizzaDetail'
based_id = ['CA', 'RG', 'CA', 'CA', 'RG', 'RG', 'RG', 'RG', 'RG', 'RG', 'RG', 'RG']
product_id = ['JC', 'KC', 'AI', 'GB', 'RL', 'AL', 'RT', 'HK', 'EP', 'PG', 'SS', 'OA']

num = 0
for base in based_id:
    
    url = base_url
    headers = {'Host' : 'www.pizzahut.co.kr', 'Connection' : 'keep-alive', 'Content-Length' : '119', 'Cache-Control' : 'max-age=0', 'Upgrade-Insecure-Requests' : '1', 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36', 'Sec-Fetch-Mode' : 'navigate', 'Sec-Fetch-User' : '?1', 'Origin' : 'https://www.pizzahut.co.kr', 'Content-Type' : 'application/x-www-form-urlencoded', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Sec-Fetch-Site' : 'same-origin' 'keep-alive', 'Content-Length' : '119', 'Cache-Control' : 'max-age=0', 'Upgrade-Insecure-Requests' : '1', 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36', 'Sec-Fetch-Mode' : 'navigate', 'Sec-Fetch-User' : '?1', 'Origin' : 'https://www.pizzahut.co.kr', 'Content-Type' : 'application/x-www-form-urlencoded', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Sec-Fetch-Site' : 'same-origin', 'Referer' : 'https://www.pizzahut.co.kr/menu/pizza/pizzaList/B02', 'Accept-Encoding' : 'gzip, deflate, br', 'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie' : 'WMONID=DtuzpZSiXYA; _ga=GA1.3.1782354048.1570713080; RB_PCID=1570713080438101281; adn_uid=MjE5LjI1NS4yMjAuMTM1XzE1NzA3MTMwODE=; RB_GUID=11fb6df9-e90f-4d66-b86c-feda527b0b3a; clientlanguage=ko; _gid=GA1.3.439378447.1571736310; etRemoteOptions=%7B%7D; etMachineId=et-4c537c04-06b6-4dee-8c5e-e28491a94914; etSessionId=et-4d05cd5a-a4e9-4ea0-85aa-95a06f54146e; floatingCookieCheck=Y; JSESSIONID=F4E97683223AA76359C9C3F26EDB0C12; _gac_UA-46023241-3=1.1571829620.CjwKCAjw9L_tBRBXEiwAOWVVCaozyMiWTTzL21iP0VYNowGEpETTEAq3xwnWDwRbZ6KU0LETgCrNYRoCd8QQAvD_BwE; wcs_bt=s_2dc859750f2:1571829660; RB_SSID=izGem6c6o3; adn_items=P_RG_KC|7^P_CA_JC|18^P_RG_OA|1^P_RG_SS|1^P_RG_PG|1^P_RG_EP|1^P_RG_HK|1^P_RG_RT|1^P_RG_AL|1^P_RG_RL|1^P_CA_GB|1^P_CA_AI|1; etPageInfo=%7B%22pathname%22%3A%22/menu/pizza/pizzaDetail%22%2C%22timestamp%22%3A1571829663696%7D; _gali=wh_Footer'}
    data  = {'menuCd': 'B02', 'selectedPromotionCode': 'P000000005', 'classId': 'P', 'baseId': 'RG', 'productId': 'kg'}#,'_csrf':'f164e308-1262-4538-ac32-7ad5c3ba2431'}  #product_id[num]}
    num = num + 1
    # driver.post(url, data=data)
    response = requests.post(url, data=data, headers=headers).text
    print(response)
    with open('pizz1.txt','w', encoding='utf-8') as f:
        f.write(response)
    soup = BeautifulSoup(response, 'html.parser')
    meta = soup.find("meta",  property="og:_csrf")
    print(meta)
    body = soup.select_one('.topping_ul')
    print(body)
    

    # title = soup.select_one('.wh_section_header').select_one('h2').text
    # item = soup.select('.item_txt').text

    # print(title)
    # print(item)
    exit()
    
    print('------------------------')
    