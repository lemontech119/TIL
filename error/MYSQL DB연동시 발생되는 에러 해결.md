## MYSQL DB연동시 발생되는 에러 해결

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