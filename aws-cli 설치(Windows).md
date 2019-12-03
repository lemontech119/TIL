## aws-cli 설치(Windows)

- 파이썬 설치 확인

``` bash
C:\Users\ado94>python --version
Python 3.7.4

C:\Users\ado94>pip3 --version
pip 19.0.3 from c:\users\ado94\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
```

- aws-cli 설치

``` bash
C:\Users\ado94>pip3 install awscli
```

- 확인

``` bash
C:\Users\ado94>aws --version
aws-cli/1.16.292 Python/3.7.4 Windows/10 botocore/1.13.28
```

- 최신버전 업데이트 

``` bash
C:\Users\ado94>pip3 install --user --upgrade awscli
```

- 설치 확인

``` bash
C:\Users\ado94>where aws
C:\Users\ado94\AppData\Local\Programs\Python\Python37\Scripts\aws
C:\Users\ado94\AppData\Local\Programs\Python\Python37\Scripts\aws.cmd
```

- aws configure

``` bash
C:\Users\ado94>aws configure
AWS Access Key ID [None]: ###########################
AWS Secret Access Key [None]: #########################
Default region name [None]: dongwon-0
Default output format [None]: json
```

> Access key 생성 필요

- configure 확인

``` bash
C:\Users\ado94>aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************LKFA shared-credentials-file
secret_key     ****************usWn shared-credentials-file
    region                dongwon-0      config-file    ~/.aws/config
```

- EB CLI 설치

``` bash
C:\Users\ado94>pip install awsebcli --upgrade --user
```

- 환경변수 설정

``` bash
%USERPROFILE%\AppData\roaming\Python\Python37\scripts
## 환경설정 
```



