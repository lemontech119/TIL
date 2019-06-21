## 영화관입장권통합전산망 오픈 API활용

### 제공 서비스 

영화권입장권 통합 전산망이 제공하는 오픈 API 서비스

* 박스 오피스 : `일별 박스오피스` / `주간/주말 박스오피스`
* 공통코드조회 : `공통코드 조회`
* 영화정보 : `영화목록` / `영화 상세정보`
* 영화사정보 : `영화사목록` / `영화사 상세정보`
* 영화인정보 : `영화인목록` / `영화인 상세정보`

`movie.py`는 박스 오피스 중 일별 박스오피스의 데이터 중 영화 순위 및 누적 관객을 뽑아온 소스입니다.



1. REST 방식

   * 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml (또는 .json)

   ```python
   url = '기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
   key = ''
   #key값은 발급 받은 키 대입
   targetDt = '20190227'
   
   real_url = url + key + '&' + targetDt
   # 위와 같은 방식으로 url 동적으로 구성하여 활용
   
   ```

   