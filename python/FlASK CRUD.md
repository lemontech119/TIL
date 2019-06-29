# FlASK CRUD

## 준비사항

1. sqlalchemy

   > SQLAlchemy는 Flask에서 사용하는 ORM이다.
   >
   > ORM(Object Relational Mapper) -파이썬 클래스(Object)와 데이터베이스(Relational) 연결 (Mapper)
   >
   > 쉡게 데이터베이스 설정을 할 수 있고, 간단한 쿼리문을 객체 메소드 조작으로 처리할 수 있다.
   >
   > 데이터베이스에 있는 레코드들을 객체로 조작 가능.

   ``` bash
   $ pip install flask_sqlalchemy
   ```

2. migrate

   > Migrate는 ORM을 사용할 때 flask에서 마이그레이션 작업을 위해 사용한다.
   >
   > 마이그레이션 : 일종의 데이터베이스 설계도

   ``` bash
   $pip intall flask_migrate
   ```

#### 1. 기본코드

``` python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

#### 2. 모델(class 정의)

``` python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'  
```



#### 3. DB 반영

``` bash
$ flask db init 
$ flask db migrate
$ flask db upgrade
```



#### 4. DB 확인

``` bash
$ sqlite3 db.sqlite3
> .schema post
```

