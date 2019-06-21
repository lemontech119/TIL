import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

# 1. python requests를 통해 요청 보내기
response = requests.get(url).text
# 2. 크롬브라우저로 보는 것을 대신해서,
# 문자열을 DOM 구조(html)로 변환한다.
soup = BeautifulSoup(response, 'html.parser')
# 3. 선택자를 활용해서 내가 원하는 값을 가져온다.

test1 = soup.select(".tit")
test2 = soup.select(".sale")
nation = []
sale = []
for i in test1:
    i = i.text
    i = i.strip()
    nation.append(i)
for j in test2:
    j = j.text
    sale.append(j)
for name, currency in zip(nation, sale):
    print(name, currency)
