## 인텔리j 커뮤니티 버전에서 스프링 부트 세팅

File - New - New project - Maven 선택 후 Next 클릭

![00](https://user-images.githubusercontent.com/52039625/60958145-db0ff000-a340-11e9-8d87-ba325072c933.PNG)

GroupId는 기본 package명 

ArtifactId는 프로젝트명 작성

![01](https://user-images.githubusercontent.com/52039625/60958154-dcd9b380-a340-11e9-9f67-1e2e439c5750.PNG)

프로젝트 설치할 디렉토리 설정 후 Finish 클릭

![02](https://user-images.githubusercontent.com/52039625/60958163-df3c0d80-a340-11e9-84e0-9f0e1e192df6.PNG)

이후 우측 하단에 Maven projects need to be imported에서 Enable Auto-import 를 클릭해주면 됩니다. 이후에 자동으로 import 해주는 설정입니다. 

![04](https://user-images.githubusercontent.com/52039625/60958168-e105d100-a340-11e9-97fb-b5b63b4e99ae.PNG)

 이제 spring boot를 위한 maven 기본 설정을 세팅해주면 됩니다. 

<https://docs.spring.io/spring-boot/docs/2.0.3.RELEASE/reference/htmlsingle/#getting-started-maven-installation>

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.example</groupId>
	<artifactId>myproject</artifactId>
	<version>0.0.1-SNAPSHOT</version>

	<!-- Inherit defaults from Spring Boot -->
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.0.3.RELEASE</version>
	</parent>

	<!-- Add typical dependencies for a web application -->
	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
	</dependencies>

	<!-- Package as an executable jar -->
	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>
```

공식 레퍼런스에 있는 Maven pom.xml에 작성해야할 기본 설정입니다. 

groupid, artifactid, version은 생성한 프로젝트에 맞춰 다른 것들은 공식 레퍼런스에 있는 것을 가져와 사용해주면 됩니다. 

>**POM의 속성 간단 설명**
>
>gourpId - 일반적으로 프로젝트의 패키지 명칭
>
>artifactId - 아티팩트의 명칭, groupId범위 내에서 유일해야 한다. 
>
>version - 아티팩트의 현재 버전
>
>parent - 프로젝트이 계층 정보
>
>dependencies - 의존성 정의 및 설정 영역



src - main - java에 package를 만들어주고 그 안에 class 파일을 만들어주면 됩니다. 

![05](https://user-images.githubusercontent.com/52039625/60958176-e3682b00-a340-11e9-9470-fdf1464bfdba.PNG)

생성한 class 파일에 아래와 같이 작성하면 됩니다. (Application은 제가 생성한 class명입니다.)

``` java
package test.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

```

그 후 run application 실행(ctrl + shift + F10) 그 후 localhost:8080 들어가 에러페이지 확인 - 에러페이지가 나오는 이유는 아무것도 작성하지 않았기 때문입니다. 

![06](https://user-images.githubusercontent.com/52039625/60958185-e5ca8500-a340-11e9-9857-76afe86ac8f8.PNG)

위와 같이 나오지 않고 ''사이트에 연결할 수 없음''이 나오면 포트 충돌의 가능성이 크기 때문에 8080포트 끄고 다시 테스트 해주세요. 

에러페이지가 잘 나오면 멈춰주고 Terminal을 열어서 mvn package 실행

mvn이 실행되지 않는 경우 mvn이 설치가 되어 있지 않은 경우이기에 mvn 설치 이후 환경설정을 해주면 됩니다. (jdk 환경설정하는 것처럼 진행하면 됩니다. )

mvn package를 실행하면 jar 파일이 프로젝트 디렉터리 내부 target폴더 안에 생성될 것입니다. 

![07](https://user-images.githubusercontent.com/52039625/60958195-e7944880-a340-11e9-9796-d251924de8f3.PNG)

그 후 터미널에서 java -jar target\spring-boot-getting-st-1.0-SNAPSHOT.jar 실행해주면 됩니다. 

그러면 run application 하던 것 처럼 실행될 것입니다. 

