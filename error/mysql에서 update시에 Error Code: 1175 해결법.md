### mysql에서 update시에 Error Code: 1175 해결법

> Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.	0.182 sec



해당 작업은 mac에서 mysql workbench로 데이터 변경을 해야되는 부분이 있어서 update 할 경우 발생한 에러입니다.

에러내용은 primary key를 기준점이 아닌 방식으로 하여 안전하지 않기 때문에 에러가 발생한 상황입니다.



- 해결방법

해결방법은 여러 방법이 있겠지만 저는 아래의 코드를 실행하고 난 다음에 update 실행 시 해결이 됐습니다.

> SET SQL_SAFE_UPDATES = 0;

기본적으로 설정되어 있는 update 설정을 변경하여 update를 key를 기준으로 잡지 않아도 해결이 되는 상황이었습니다.
다만 이 방법은 안전하지 않기 때문에 그리 추천되는 방법은 아닙니다. 