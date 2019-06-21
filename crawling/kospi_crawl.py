import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

# 1. python requests를 통해 요청 보내기
response = requests.get(url).text
print(type(response))
# 2. 크롬브라우저로 보는 것을 대신해서,
# 문자열을 DOM 구조(html)로 변환한다.
soup = BeautifulSoup(response, 'html.parser')
print(type(soup))

# 3. 선택자를 활용해서 내가 원하는 값을 가져온다.
kospi = soup.select_one('#KOSPI_now').text
print(kospi)
