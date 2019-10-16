import requests
from bs4 import BeautifulSoup

## 도미노피자 크롤링

base_url = 'https://web.dominos.co.kr/goods/'
base_list = 'list'

url = base_url+ base_list

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
## 맨 처음 url를 html로 파싱

category = soup.select(".lst_prd_type ")
## 내부 들어가서 체크 할 수 있도록 모든 피자 가져오기
href_list = []
## 피자들을 담을 리스트
for i in category:
    li_list = i.select("li")
    for j in li_list:
        href = j.select_one("a")
        ## a태그만 가져오기
        href = href.get('href')
        ## 가져온 a태그의 href 속성값 가져오기
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
    ## 가격 가져오기는 실패...
    tab_content = menu_soup.select(".tab_content")
    main_topping = tab_content[1].select_one(".tbl_type").select_one("tbody").select_one("tr").select_one("td").text
    print(title)
    ##print('라지 가격은: ', price_large)
    ##print('미들 가격은: ', price_medium)
    print('토핑: ', main_topping)
    ## 체크를 위한 print
