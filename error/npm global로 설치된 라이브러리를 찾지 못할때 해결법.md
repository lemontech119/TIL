##  npm global로 설치된 라이브러리를 찾지 못할때 해결법

> OS는 Window7
>
> node: v10.16.0
>
> npm: v6.9.2 활용 상황입니다.

![error1](https://user-images.githubusercontent.com/52039625/61420839-5411d780-a93f-11e9-8467-bdf4850e9056.PNG)



위와 같이 문제 발생 시

```bash
npm prefix -g ##글로벌 설치된 라이브러리 저장 위치 
```

위 명령어를 실행하여 나온 위치에 글로벌 설치된 라이브러리 있는지 확인



있으면  path 설정 에러로 시스템 환경변수에 글로벌 설치된 라이브러리가 있는 주소 path에 추가

