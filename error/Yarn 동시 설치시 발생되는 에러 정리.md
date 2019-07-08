## Yarn 동시 설치시 발생되는 에러 정리

동빈나님의 강의인 React와 Node.js를 활용한 고객 관리 시스템 개발 강의를 보고 따라 실행한 경우 

발생한 에러 해결 방안

``` json
//package.json 파일
{
    "name": "management",
    "version": "1.0.0",
    "scripts": {
        "client": "cd client && yarn start",
        "server": "nodemon server.js",
        "dev": "concurrently --kill-others-on-fail \"yarn server\" \"yarn client\""
    },
    "dependencies": {
        "body-parser": "^1.18.3",
        "express": "^4.16.4"
    },
    "devDependencies": {
        "concurrently": "^4.0.1"
    }
}
```

``` javascript
$yarn dev
```

![yarn error](https://user-images.githubusercontent.com/52039625/60782549-13b59b00-a182-11e9-80bc-ac70cd36d15c.PNG)

위와 같이 설치 시에 nodemon 글로벌 에러 발생(npm install -g nodemon 설치 한 이후)

>package.json 이 있을 경우 --save 옵션을 주지 않아도 되는지 알아서
>
>npm install -g nodemon 설치이후 위와 같이 진행 결과 에러 발생
>
>> npm install nodemon --save로 설치하니깐 dependencies 에 nodemon 버전 추가되고 에러 없이 무사히 실행
>
>문제 발생 추정 npm global 설치한 nodemon의 경로가 꼬였던 걸로 보임...

```json
{
    "name": "management",
    "version": "1.0.0",
    "scripts": {
        "client": "cd client && yarn start",
        "server": "nodemon server.js",
        "dev": "concurrently --kill-others-on-fail \"yarn server\" \"yarn client\""
    },
    "dependencies": {
        "body-parser": "^1.18.3",
        "express": "^4.16.4",
        "nodemon": "^1.19.1"
    },
    "devDependencies": {
        "concurrently": "^4.0.1"
    }
}
```

