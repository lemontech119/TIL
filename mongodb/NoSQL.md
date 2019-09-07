## NoSQL

NoSQL 이란? 관계형 데이터베이스가 아닌 데이터 베이스



#### NoSQL의 장점

- 클라우트 컴퓨팅 환경에 적합
  - 하드웨어 확장에 유연한 대처가 가능
  - RDBMS보다 저렴하게 분산 처리 및 병렬 처리 가능
- 유연한 데이터 모델
  - 비정형 데이터 구조 설계로 설계 비용이 감소
- 빅데이터 처리에 효과적



#### MongoDB의 특징

- 고성능
  - 문서 안에 문서를 넣어서 저장하는 임베디드 방식이라 join에 의한 성능저하가 없다





#### 쿼리

``` sql
show dbs;
-- 전체 데이터베이스 확인
mongod --version
-- 몽고db 버전 확인
mongod --dbpath c:\mongodb\data
-- 특정 데이터 저장 장소 지정 가능


use user;
-- 데이터베이스 사용
db.stats();
-- 데이터베이스 상태 확인
show collections;
-- 전체 콜렉션 확인

-- 콜렉션 생성 명령
db.things.insert({empno: 1102});
-- 콜렉션이 없어서 자동으로 things라는 콜렉션이 생성
db.createCollection("employees", {capped: true. size: 10000});
-- 콜렉션 생성 capped true, size값을주면 collection이 size 만큼 커지지 않는다.

db.things.drop();
-- 해당 콜렉션 삭제
db.things.save({empno: 1234});
-- 해당 db에 데이터 저장
m = {empno:12345}
db.things.save(m);
-- 변수로 해서 저장도 가능

db.things.find();
-- sql의 select문입니다. 
db.things.find({}, {_id:0});
-- _id값을 제외하고 데이터 출력

-- insert 방법
db.things.insert({});
-- insert는 중복 데이터를 넣을 경우 에러가 나지만
-- save는 중복 데이터를 넣을 경우 최신화를 해줌
db.things.save({});
-- 두 가지 방법으로 추가가 가능

-- 데이터 수정
db.things.update({변경할 부분 조건}, {변경 내용});
db.things.insert({_id: 1, data:"value"});
-- 이렇게 추가된 데이터를 아래 방식으로 update 가능
db.things.update({_id:1}, {data: "test"});
-- 위의 방식이면 변경할 경우 다른 데이터도 다 사라짐
db.userinfo.update({ename:"kim"}, {$set : {ename:"lee"}});
-- set을 통하여 원하는 부분만 변경되도록 해야한다.
db.userinfo.updatemany({ename:"kim"}, {$set : {ename:"lee"}});
-- 여러개 변경하고 싶을때는 요렇게~

-- 데이터 삭제
db.userinfo.remove({ename:"kim"})

-- 조건 조회
db.employees.find({empno:{$gt: 7500, $lte: 7600}});
-- empno가 7500~7600 사이의 값
 db.employees.find({empno:{$gt: 7500, $lte: 7600}}, {_id:0, empno:1, ename:2});
-- _id: 0 같이 0을 주면 그 값을 안본다는 명령
db.employees.find({$or: [{empno:7782}, {empno:7844}]}, {_id:0});
-- or조건

db.employees.distinct('job');
-- job이라는 key값의 value를 중복없이 보여주는 것


db.employees.find({}, {_id:0, ename:1, job:1}).sort({ename:1});
-- order by 
db.employees.find({}, {_id:0, ename:1, job:1}).sort({ename:-1});
-- 역순으로 하는 것

-- 조건부 검색
db.employees.find({deptno: {$in: [10,30]}}, {_id:0, empno:1, ename:1, deptno:1});
-- 10과 20사이 출력
db.employees.find({comm: {$exists: true}}, {_id:0});
-- exists
-- comm 이라는 key값에 value가 있는 애들만 출력해줘
```

