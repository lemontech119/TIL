import requests
from bs4 import BeautifulSoup

base_url = 'https://web.dominos.co.kr/goods/'
base_list = 'list'

url = base_url+ base_list

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
category = soup.select(".lst_prd_type ")

href_list = []
for i in category:
    li_list = i.select("li")
    for j in li_list:
        href = j.select_one("a")
        href = href.get('href')
        href_list.append(href)
############### 리스트에서 필요한 href 받아오기 끝

for menu in href_list:
    menu_url = base_url + menu
    menu_url = requests.get(menu_url).text
    menu_soup = BeautifulSoup(menu_url, 'html.parser')

    print("-----------------------------")
    title = menu_soup.select_one(".prd_title").text
    title = title.strip()
    ##price_large = menu_soup.select_one(".price_large").text
    ##price_medium = menu_soup.select_one(".price_medium").text

    tab_content = menu_soup.select(".tab_content")
    main_topping = tab_content[1].select_one(".tbl_type").select_one("tbody").select_one("tr").select_one("td").text
    print(title)
    ##print('라지 가격은: ', price_large)
    ##print('미들 가격은: ', price_medium)
    print('토핑: ', main_topping)
