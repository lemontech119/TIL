## MYSQL DB연동시 발생되는 에러 정리

> Error: Cannot enqueue Handshake after already enqueuing a Handshake.

위와 같은 에러 발생은 이미 db연동이 된 상태에서 또 다시 db연결을 시도할 경우 발생하는 에러입니다. 

db연결을 한번만 하도록 코드를 변경하면 됩니다.

```javascript
let pool = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '1234',
    port: 3306,
    database: 'moim_db',
    insecureAuth : true
});
let db_conn = true;

if(db_conn){
        pool.connect();
        db_conn = false;
}
```

위와 같은 방식으로도 한번만 연결을 할 수 있도록 구현 가능



----------



- 주로 local에서 테스트할 때 아래와 같은 에러가 많이 발생하는데 이 문제는 패스워드 관련 문제일 확률이 많습니다.

> querySqlSync : Error: ER_NOT_SUPPORTED_AUTH_MODE: Client does not support authentication protocol requested by server; consider upgrading MySQL client

일단 우선적으로 패스워드가 맞는지 부터 확인해야합니다.

그래도 동일한 에러가 발생할 경우는 

```mysql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '패스워드'
```

위의 명령어를 실행하면 됩니다. root 자리에 userId, 패스워드 자리에 사용하는 패스워드를 입력하면 됩니다. 