import os
import requests
 
key = ''
#본인 key 발급 이후 넣어주면 됨
targetDt = '20190226'
url=f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={targetDt}'

response = requests.get(url).json()
# 박스오피스 API json으로 받아오기
top10_list = response.get("boxOfficeResult").get("dailyBoxOfficeList")
# 필요한 데이터를 위해 dailyBoxOfficeList 까지 추출
print(type(top10_list))
# list확인

for top in top10_list:
    print(top.get("rank")+ "위 " + top.get("movieNm") + " "+ top.get("audiAcc"))

# 현재 영화 순위, 제목, 누적관객수 출력
