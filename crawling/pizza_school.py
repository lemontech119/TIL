import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

file_data = OrderedDict()

## 피자스쿨 menu 리스트 url
base_url = 'http://pizzaschool.net/menu/'

## 피자만 구분 해 놓은 페이지 부재로 미리 리스트 뺴놓음
menu_list = ['허니비프피자', '더블갈릭바베큐피자', '고르곤졸라피자', '직화파인애플피자',
'치즈피자', '페퍼로니피자', '콤비네이션피자', '고구마피자', '포테이토피자',
'핫치킨피자', '불고기피자', '나폴리피자', '446', '까르보네피자', 
'아이리쉬포테이토피자', '461', '도이치바이트피자', '멕시칸바이트피자', '직화홀릭바이트피자',
'야채퀘사디아피자', '치킨퀘사디아피자', '비프퀘사디아피자', '465', '닭안심살피자']

for menu in menu_list:
    url = base_url + menu
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    ## 피자 스쿨 3개 피자만 번호로 되어 있어요...
    if menu == '446' :
        menu = '스테이크피자'
    elif menu == '465' :
        menu = '떡갈비피자'
    elif menu == '461' :
        menu = '깐쇼새우피자'
    
    li_list = soup.select(".article-icon-entry")
    short_info = li_list[0].select_one(".iconlist_content ").select_one("p").text
    topping = li_list[1].select_one(".iconlist_content ").select_one("p").text
    
    file_data["brand"] = "피자스쿨"
    file_data["pizza_name"] = menu
    file_data["short_info"] = short_info
    file_data["topping"] = topping

    with open('school.json', 'a', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


    print('------------------------')
    