## nginx와 haproxy에서 로드 밸런싱 해보기

#### 1. nginx에서 로드밸런싱 (ubuntu 16.04)

- 기본 설정

``` bash
$ sudo apt-get update
$ sudo apt-get install -y build-essential
$ sudo apt-get install curl
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash --
$ sudo apt-get install -y nodejs
## node 설치

$ apt-get install -y nginx
## nginx 설치

## 추가적으로 테스트를 위해 포트 3000, 3001, 3002로 테스트 서버 오픈
```

- git 설치(안해도 됨)

``` bash
$ sudo add-apt-repository ppa:git-core/ppa
$ sudo apt-get update && sudo apt-get dist-upgrade
$ sudo apt-get install git-core
 
$ git version
```



- 테스트 서버 코드

``` javascript
// /test1/app.js //3개 오픈
const express = require('express');
const app = express();

app.get('/test1', (req, res) => {
  res.send('PORT 3000 /test1');
});
app.get('/test3', (req, res) => {
  res.send('PORT 3000 /test3');
});
app.get('/', (req, res) => {
  res.send('PORT 3000');
});
app.listen(3000);
```



- Nginx 설정 

``` bash
$ cd /etc/nginx/sites-available/
$ sudo vi default
```

Default 기본 세팅

``` 
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name example.com;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

}
```

> Listen 부분으로 port 설정이 되어있습니다. 
>
> location에 추가하게 되먼 80으로 접근한 경우 연결해줍니다.
>
> 아래의 내용을 추가해주면 로드 밸런싱이 가능해집니다.

``` 
upstream node_proxy{
	server localhost:3000;
	server localhost:3001;
	server localhost:3002;
}

location / {
		proxy_pass http://node_proxy;
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
}
```

- 결과적으로 최종은 아래와 같이 작성해주시면 됩니다. 

``` 
upstream node_proxy{
	server localhost:3000;
	server localhost:3001;
	server localhost:3002;
}
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name example.com;

	location / {
		proxy_pass http://node_proxy;
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
	}

}
```

- 그 이후 사용해야 할 명령어

``` bash
$ nginx -t
## 설정 확인 ok가 나오면 제대로 작성된 것입니다. 
$ sudo systemctl restart nginx 
## nginx 재시작
```

이 후 80으로 여러번 요청 해보면 확인이 가능합니다.

----------------



#### 2. Haproxy로 로드 밸런싱 해보기

``` bash
$ sudo add-apt-repository ppa:vbernat/haproxy-1.8
$ sudo apt-get update
$ sudo apt-get install haproxy
```

- Haproxy 설정

``` bash
$ cd /etc/haproxy
$ sudo vi haproxy.cfg
```

> 테스트 서버 코드는 동일함

- 기본 서정

``` cfg
global
	log /dev/log	local0
	log /dev/log	local1 notice
	chroot /var/lib/haproxy
	stats socket /run/haproxy/admin.sock mode 660 level admin
	stats timeout 30s
	user haproxy
	group haproxy
	daemon

	# Default SSL material locations
	ca-base /etc/ssl/certs
	crt-base /etc/ssl/private

	# Default ciphers to use on SSL-enabled listening sockets.
	# For more information, see ciphers(1SSL). This list is from:
	#  https://hynek.me/articles/hardening-your-web-servers-ssl-ciphers/
	ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS
	ssl-default-bind-options no-sslv3

defaults
	log	global
	mode	http
	option	httplog
	option	dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
	errorfile 400 /etc/haproxy/errors/400.http
	errorfile 403 /etc/haproxy/errors/403.http
	errorfile 408 /etc/haproxy/errors/408.http
	errorfile 500 /etc/haproxy/errors/500.http
	errorfile 502 /etc/haproxy/errors/502.http
	errorfile 503 /etc/haproxy/errors/503.http
	errorfile 504 /etc/haproxy/errors/504.http
```

- 추가 해야 될 내용

``` 
frontend Local_Server
	bind *:80
	default_backend My_Web_Servers

backend My_Web_Servers
	balance roundrobin
	server s1 127.0.0.1:3000 check
	server s2 127.0.0.1:3001 check
	server s3 127.0.0.1:3002 check
```



- 마지막에 실행

``` bash
$ sudo service haproxy restart
```

