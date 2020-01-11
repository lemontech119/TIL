## PM2 명령어

- start 명령어

``` bash
# 서버 실행
$ pm2 start app.js

# 프로세스 이름 지정
$ pm2 start app.js --name servername

# 아웃풋 로그와 에러로그의 위치를 지정
$ pm2 start app.js -e err.log -o out.log

# 로그의 시간데이터 포맷을 지정
$ pm2 start app.js --log-data-format "YYYY-MM-DD HH:mm z"

# 노드 start 등과 같이 명령어를 통해 실행할 때
$ pm2 start servername -- run start
```

- 그 외 알아두면 좋은 명령어

``` bash
# 현재 실행되고 있는 리스트
$ pm2 list

# 서버 재실행
$ pm2 restart servername

# 서버 제거
$ pm2 delete servername

# 로그 출력
$ pm2 logs
```

