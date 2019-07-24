## 간단 MYSQL 문법

1. 데이터베이스

   ```sql
   SHOW databases; #데이터베이스 조회
   CREATE DATABASE test_db default character set UTF8; # 데이터베이스 생성
   use test_db; # 해당 사용자가 test_db를 사용한다는 뜻
   exit; #연결된 데이터베이스를 닫음 
   ```

   

2. CREATE TABLE 

   ```sql
   CREATE TABLE test
   (
   	idx INT PRIMARY KEY auto_increment,
   	name VARCHAR(20) NOT NULL,
       level INT default 1,
       noshow INT default 0
   );
   describe test;
   ```

   > auto_increment 자동 증가 설정 부여
   >
   > NOT NULL 자료 입력할 때 항상 value를 넣어주어야 함
   >
   > default 넣어준 value가 없다면 뒤에 있는 값을 자동으로 넣어줌
   >
   > describe test; 테이블 구조 확인 (DESC test; #줄여서 사용 가능)



3. INSERT TABLE

   ```sql
   INSERT INTO test (idx, name, level, noshow) VALUES('1', 'test', 1, 0);
   ```

   > 첫 번째 나오는 칼럼명 명시 해주는 내용은 생략 가능

4. SELECT TABLE

   ```sql
   SELECT * from test;
   ```

   > *는 테이블이 가지는 모든 필드를 뜻합니다. 

   ```sql
   select * from employees order by first_name ASC, last_name DESC;
   -- ASC 오름차순 DESC 내림차순
   
   select * from employees limit 10;
   -- 가져오는 갯수를 제한할 수 있음
   
   select * from employees limit 10 OFFSET 10;
   -- 앞에서 몇개 스킵하고 가져오는것
   
   select distinct first_name from employees; 
   -- 중복된 내용은 빼고 출력 
   
   select * from employees where first_name like 'K%';
   -- like는 패턴 검색임
   -- 위의 like는 k로 시작하는 것을 찾아줘
   ```

   

5. DROP TABLE

   ```sql
   DROP * test;
   ```

   > DROP * 테이블명; 으로 제거 가능
   >
   > 제거시 복구가 불가능 하므로 신중히 제거 해야됨.

6. DELETE TABLE

   ```sql
   delete from employees where emp_no= 10001;
   ```

   
