## Ubuntu 내에 yarn 글로벌 세팅

- 저장소 등록

```bash
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

- yarn 설치하기

``` bash
$ sudo apt-get update && sudo apt-get install yarn
```

- yarn 버전 확인(설치 완료 확인)

``` bash
$ yarn --version
```



- 글로벌 설정

``` bash
$ yarn config get prefix
## undefined가 뜨는게 맞음
$ yarn config set prefix ~/.yarn-global

$ yarn config get prefix
## 글로벌 세팅 값이 나와야함

$ vi ~/.bashrc
## 아래 한줄 추가
export PATH="$PATH:`yarn global bin`"
```

- restart shell

``` bash
$ bash -l
```

