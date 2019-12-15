## window 한경에서 node 버전 문제 시 해결 방법

- window에서 node로 프로젝트를 할 경우 node 버전이 달라서 npm audit fix 등 여러 문제가 발생할 경우가 있습니다.
- 맥과 리눅스 환경에서는 이러한 문제해결이 상대적으로 쉬웠던 반면 window에서는 어려웠었다... (저만의 착각일 수도 있습니다.)



문제해결을 위해 nvm을 설치해야 합니다.

- https://github.com/coreybutler/nvm-windows/releases
  - 해당 주소로 접속하여 nvm-setup.zip 파일을 다운 받습니다.
- 해당 압축파일을 풀고 nvm을 설치한 이후 cmd를 실행합니다
- nvm version을 입력하여 설치된 것을 확인합니다.



사용하려고 하는 node버전을 node.js 공식 사이트에 들어가서 설치합니다. 

설치 이후 (node v12.13.1이라고 가정)

- nvm install v12.13.1
  - nvm install (해당 사용 버전)
- nvm ls 
  - 현재 설치된 nodejs 버전을 확인
- nvm use v12.13.1
  - 설치된 node 버전 사용 가능

위의 방식으로 node 버전을 정리하여 사용하면 됩니다. 