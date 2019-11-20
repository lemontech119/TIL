## docker 사용하는 명령어 정리

- 도커 설치

``` bash
$ curl -s https://get.docker.com | sudo sh

$ sudo apt-get update
$ sudo apt-get install docker.io
$ sudo ln -sf /usr/bin/docker.io /usr/local/bin/docker

## docker 버전 확인
$ docker -v
```



- 도커 이미지 빌드

``` bash
$ sudo docker build -t <이미지명> .
```



- 도커 이미지 실행

``` bash
$ sudo docker run -it --rm -p 3000:3000 --entrypoint bash <이미지명>
```



- 현재 실행중인 이미지 확인

``` bash
$ sudo docker ps -a
```



- container 안의 명령 실행 

``` bash
$ sudo docker exec -it <컨테이너ID> /bin/bash
```



- 컨테이너 시작/재시작/정지

``` bash
$ sudo docker start <컨테이너 name>

$ sudo docker restart <컨테이너 name>

$ sudo docker stop <컨테이너 name>
```



- 컨테이너/이미지 삭제

``` bash
## 컨테이너 삭제
$ sudo docker rm <컨테이너 네임>

## 이미지 삭제
$ sudo docker rmi <이미지 네임>
```

