# crawling 공부
# python을 활용한 크롤링

## 1. 기본설정

- `requests`, `bs4` 모듈 설치

  ```bash
  $ pip install requests
  $ pip install bs4
  
  
  ```

- 기본 코드

  ```python
  # 1. 모귤 import 
  import requests
  from bs4 import Beautifulsoup
  # 2. url 설정
  url = 'https://finance.naver.com/site/'
  # 3. requests를 통한 요청
  response = requests.get(url).text
  # 4. BeautifulSoup을 통한 html 구조화
  soup = BeautifulSoup(response, 'html.parser')
  # 5. 선택자(selector)를 활용한 값 추출
  kospi = soup.select_one ('#KOSPI_now')
  # 6. 해당 태그에 담긴 내용 출력
  print(kospi.text)
  ```

  - `select_one` : 선택자를 이용하여 특정 태그를 select함.
    - 리턴값 : beautifulsoup object
    - 여러 값이 있어도, 가장 첫번째 값만 가져옴
  - `select` : 선택자를 이용항 해당 태그들을 모두 select함
    - 리턴값: list / list 원소 : beautifulsoup object 
    - 해당되는 내용을 모두 가져옴  

