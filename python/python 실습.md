# Python을 통한 컴퓨터 조작

## 1. webbrowser

``` python
import webbrowser
webbrowser.open('https://www.naver.com')
```



## 2. [os](https://docs.python.org/ko/3/library/os.html)

> os는 파이썬 코드를 통해 운영체제를 조작할 수 있다.

``` python
import os 
# 1. getcwd : get current working directory
print(os.getcwd())
os.chdir(r'디렉토리 경로')
print(os.getcwd())

```

* 파일명 변경하기

  ``` python
  import os 
  for filename in os.listdir():
      os.rename(filename, '이력서_'+filename)
  ```

  `listdir()`: shell에서 `ls` 명령어와 동일하다.

  `rename(원래이름, 변경명)`

## 3. file 조작

* 기본 코드

  ``` python
  # 1. 텍스트 파일 읽기
  with open('파일명', 'r', encoding='utf-8') as f:
      lines = f.readlines()
  for line in lines:
      print(line)
      
  # 2. 텍스트 파일 쓰기(w: 덮어쓰기, a: 추가하기)
  with open('파일명.txt', 'w', encoding='utf-8') as f:
      f.write('파일 써지나요?')
      
  # 3. csv 파일 읽기
  import csv
  with open('파일명.csv', 'r', encoding='utf-8') as f:
      reader = csv.reader(f)
      for line in reader:
          print(line) # list
          
  # 4. csv 파일 쓰기
  import csv 
  with open('파일명.csv', 'w', encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow(('안동원', 'ado119@naver.com'))
  ```

  

# python을 활용한 크롤링

## 1. 기본설정

* `requests`, `bs4` 모듈 설치

  ``` bash
  $ pip install requests
  $ pip install bs4
  
  
  ```

*  기본 코드

  ``` python
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

  * `select_one` : 선택자를 이용하여 특정 태그를 select함.
    * 리턴값 : beautifulsoup object
    * 여러 값이 있어도, 가장 첫번째 값만 가져옴

  * `select` : 선택자를 이용항 해당 태그들을 모두 select함
    * 리턴값: list / list 원소 : beautifulsoup object 
    * 해당되는 내용을 모두 가져옴  



# python을 활용한 email 전송

> 이메일을 보내기 위한 규약은 SMTP를 활용하는 것이다. 
>
> SMTP(간이 우편 전송 프로토콜/Simple Mail Transfer Protocol)
>
> 이메일을 받기 위한 규약은 POP3/IMAP을 활용하는 것이다. 
>
> POP3(Post Office Protocol), IMAP(Internet Message Access Protocol)

## 1. 네이버 메일 설정

네이버 메일 환경 설정에서 POP3/SMTP 설정을 반드시 해야함

설정 이후에는 SMTP 서버는 `smtp.naver.com`포트는 `465` 이다.

## 2. 기본 메일 보내기

```python 
import getpass
import smtplib
from email.message import EmailMessage
# 1. 비밀번호 저장
password = getpass.getpass('비밀번호를 입력하세요: ')
# 2. 이메일 메세지 만들기
msg = EmailMessage()
msg['From'] = 'ado119@naver.com'
msg['To'] = 'ado119@naver.com'
msg['Subject'] = '제목입니다.'
msg.set_content('안녕하세요 내용입니다!!!')
# 3. smtp 서버 활용해서 보내기
server = smtplib,SMTP_SSL('smtp.naver.com', 465)
server.login('ado119', password)
server.send_message(msg)
print('전송완료')
```

