## nodemailer를 활용하여 이메일 발송 하기

우선 nodemailer 모듈을 설치해줍니다.

```bash
npm install --save nodemailer
```

모듈 설치 후 서버로 활용할 js파일에 아래 명령어를 선언해줍니다.

```javascript
const nodemailer = require('nodemailer');
```

그리고 저는 추가적으로 원활한 테스트를 위해 express까지 선언하여서 테스트를 진행했습니다.

추가적으로 발송 이메일을 naver로 하여 테스트를 진행했습니다. 

```javascript
app.get('/test', (req, res) => {
    // 발송 메일 설정입니다. 
    let transporter = nodemailer.createTransport({
        service:'naver',
        auth: {
            user: '아이디@naver.com',
            pass: '비밀번호'
        }
    })

    // 이메일 기본 설정입니다.
    // test를 위해 받는 사람 이메일을 gmail로 진행했습니다.
    // 다른 이메일도 사용가능합니다. 
    let mailOptions = {
        from: '발송자아이디@naver.com',
        to: '받는사람아이디@gmail.com',
        subject: 'mailTest',
        text: '성공했나용???'
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if(error){
            console.log('에러발생 ㅠㅠ' + error)
        }else {
            console.log('이메일 발송 성공 우훗! : ' + info);
            res.send('성공');
        }

        transporter.close();
    })
    

});

```

발송 이메일을 네이버로 할 경우 추가적인 설정이 더 필요합니다. 

![emailtest](https://user-images.githubusercontent.com/52039625/61879274-b36a7b80-af2d-11e9-8a17-f5c2730b48a1.PNG)

naver 이메일에 들어가 POP3/SMTP 사용을 사용함으로 변경을 해주어야 합니다.




![emailtest2](https://user-images.githubusercontent.com/52039625/61879275-b36a7b80-af2d-11e9-9faf-e5df5baff0f0.PNG)

위 사진은 성공한 사진입니다. 

-----

저는 사용자가 비밀번호를 잃어버렸을 때 비밀번호 찾기 서비스를 위해 이메일 발송을 사용할 계획이라 

숫자와 알파벳을 랜덤으로 만들어서 보내줄 필요가 있습니다.

```javascript
function randNum() {
    let ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                 'w', 'x', 'y', 'z',
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    let rN = '';
    for (var i = 0; i < 8; i++) {
        var randTnum = Math.floor(Math.random() * ALPHA.length);
        rN += ALPHA[randTnum];
    }
    return rN;
}
```

위의 함수를 선언해둡니다. 위의 함수는 숫자와 알파벳이 랜덤으로 들어가 8글자의 단어가 랜덤으로 형성됩니다.

``` javascript
let mailOptions = {
        from: '발송자아이디@naver.com',
        to: '받는사람아이디@gmail.com',
        subject: 'new_password',
        text: '당신의 새 비밀번호는 ' + new_password + '입니다.'
    };
```

발송 설정을 위와 같은 방식으로 변경하면 됩니다.

추가적으로 해당 유저의 db를 update해주면 됩니다. 





