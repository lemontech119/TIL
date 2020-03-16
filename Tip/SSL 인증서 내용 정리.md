## SSL 인증서 내용 정리

> 회사에서 다른 분이 만들어 놓고 간 프로젝트를 관리하던 와중에 아래 이미지와 같은 사태가 벌어졌다.
> 그에 관련된 내용 정리입니다. 서버는 Node로 돌리고 있었고, ssl 설정은 이미 되어 있어 https로 서비스를 사용하고 있었습니다. 
>
> 구성환경
> -GCP Computer engine (was ec2와 비슷)
> -Ubuntu.16.04
> -Node.js 10

![스크린샷 2020-03-16 오전 11 11 32](https://user-images.githubusercontent.com/52039625/76725911-04680200-6793-11ea-9d11-ad4c7af74afd.png)

1. 일단 해당 서버내에 있는 인증서 유효 기간을 확인했습니다

``` bash
### 인증서 최종 기간 체크하는 문법
$ openssl x509 -enddate -noout -in fullchain.pem 
notAfter=Mar 14 13:52:48 2020 GMT
```

- 이 문제를 체크한 시점은 월요일이었습니다. 주말에 만료가 되서 월요일에 사용을 못한거 같습니다.



2. 검색을 진행했습니다. (검색 키워드 ssl 인증서 수동 갱신)

> <https://swiftcoding.org/lets-encrypt-renew>
>
> <https://sjwiq200.tistory.com/3>
>
> <https://blog.lael.be/post/5107>
> 외에도 여러 블로그 및 stackover

- 검색결과를 따라했지만 해당 서버는 certbot-auto가 없었고 수동 갱신또한 에러가 발생했습니다.
  - 에러가 나는 이유를 문제해결이 우선이기에 미뤄놨다가 찾아보려 했지만 로그를 잃어버렸습니다ㅠㅠ

``` bash
## 따라했지만 저는 실패했습니다. 이 방법은 검색해서 느꼈던 점은 ssl 인증서가 만료된 경우가 아닌 경우 재발급을 해주는 느낌이었습니다.
$ cd /etc/letsencrypt/renewal
## 해당 위치에 있는 conf 파일에서 renew_before_expiry = 30 days
## 라고 나와 있는 주석을 제거하고 뒤에 30을 90으로 변경
$ letsencrypt renew
## 재발급을 진행합니다. 
## 다만 전 여기에 에러가 발생했습니다. 
```



3. 검색을 진행하면서 새롭게 배운 점

> 저는 보통 node.js를 쓰면서 nginx를 같이 사용했습니다. 
> 이유는 로드밸런싱을 할때 편하고, 개인적으로 사용할때는 처음 시작할때 그렇게 해서 였습니다.(최악의 이유…)

> 근데 검색한 많은 자료 같은 경우 nginx 또는 apache를 사용했는데
> 저희 서비스는 그렇게 안되어 있더라고요. 정식 서비스가 아닌 실험을 위한 웹사이트 였지만요.
> 찾아보니깐 express 자체에 내장이 되어 있어서 써도 되지만 안써도 된다고 합니다...

- 리눅스에서 파일 찾기 

``` bash
$ find / -name letsencrypt
/usr/bin/letsencrypt
/opt/eff.org/certbot/venv/bin/letsencrypt
/opt/eff.org/certbot/venv/lib/python2.7/site-packages/letsencrypt
/var/lib/letsencrypt
/var/log/letsencrypt
/etc/letsencrypt
```



4. 인증서 재발급

> 현재 인증서를 가지고 하는 것이 힘들다고 판단되어 재 설치를 하기로 했습니다. 
>
> <https://medium.com/@sejongdekang/node-js%EC%97%90%EC%84%9C-lets-encrypt-%EB%AC%B4%EB%A3%8C-ssl-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0-fe337b87bfbb>
>
> 해당 블로그를 참고하였습니다.

- 저는 이미 세팅이 되어 있었습니다. (Certbot-auto가 필요합니다.)

``` bash
$ ./certbot-auto certonly
Requesting to rerun ./certbot-auto with root privileges...
Saving debug log to /var/log/letsencrypt/letsencrypt.log

How would you like to authenticate with the ACME CA?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: Spin up a temporary webserver (standalone)
2: Place files in webroot directory (webroot)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 

## standalone 을 선택하면 됩니다. 

please enter in your domain name(s) 
## 이런 내용이 나올껍니다. 제가 로그를 날려버려서 검색해서 대충 정리합니다....
## 도메인명 적어주시면 됩니다. 

 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/${도메인명 들어가는 자리}/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/${도메인명 들어가는 자리}/privkey.pem
   Your cert will expire on 2020-06-14. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - If you like Certbot, please consider supporting our work by:
 
 ## 성공하면 위 처럼 나옵니다. 
 ## 해당 위치에 있는 pem 파일을 사용하면 됩니다. 
```



5. 에러 (주의할 점)

> 이제 되겠지 하면서 즐겁게 테스트를 했습니다. 
>
> 하지만 서버가 죽었습니다. 저는 당시 pm2를 사용했는데 에러가 발생해 있었습니다

발생한 에러

``` 
{ Error: EACCES: permission denied, open '/etc/letsencrypt/live/${도메인면}/privkey.pem'
    at Object.openSync (fs.js:443:3)
    at Object.readFileSync (fs.js:343:35)
    at Object.<anonymous> (/home/bbomi_haii/saemi.ehwa-admin/app.js:30:19)
    at Module._compile (internal/modules/cjs/loader.js:776:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:787:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Object.<anonymous> (/home/bbomi_haii/.nvm/versions/node/v10.16.0/lib/node_modules/pm2/lib/ProcessContainerFo
rk.js:27:21)
    at Module._compile (internal/modules/cjs/loader.js:776:30)
  errno: -13,
  syscall: 'open',
  code: 'EACCES',
  path: '/etc/letsencrypt/live/${도메인면}/privkey.pem' }
```

- 전에 있던 인증서를 지우고 재발급을 받았는데 권한 설정을 안해줘서 권한 설정을 해줬습니다. 