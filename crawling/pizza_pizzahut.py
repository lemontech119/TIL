import requests
import time
from bs4 import BeautifulSoup


# chromedriver = 'C:\coding\chromedriver.exe'

# driver = webdriver.Chrome(chromedriver)

base_url = 'https://www.pizzahut.co.kr/menu/pizza/pizzaDetail'
based_id = ['CA', 'RG', 'CA', 'CA', 'RG', 'RG', 'RG', 'RG', 'RG', 'RG', 'RG', 'RG']
product_id = ['JC', 'KC', 'AI', 'GB', 'RL', 'AL', 'RT', 'HK', 'EP', 'PG', 'SS', 'OA']

num = 0
for base in based_id:
    
    url = base_url
    data  = {'menuCd': 'B02', 'selectedPromotionCode': 'P000000005', 'classId': 'P', 'baseId': base, 'productId': product_id[num] , '_csrf': '6e385d0c-5b10-4b10-a11f-e8e60177f4c5'}
    num = num + 1
    # driver.post(url, data=data)
    response = requests.post(url, data=data).text
    soup = BeautifulSoup(response, 'html.parser')
    
    body = soup.select_one('.wh_Container')
    print(body)
    

    # title = soup.select_one('.wh_section_header').select_one('h2').text
    # item = soup.select('.item_txt').text

    # print(title)
    # print(item)
    exit()
    
    print('------------------------')
    