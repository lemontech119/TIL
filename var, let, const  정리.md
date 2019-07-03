## var, let, const  정리

#### var, let, const 요약 설명

- var, let은 변수를 선언하는 키워드이고, const는 상수를 선언하는 키워드이다. 

- var, let은 변수선언 키워드이므로 리터럴 값의 재할당이 가능하지만, const는 리터럴 값의 재할당이 불가능합니다.
- var는 재선언이 가능하지만 let은 재선언이 불가능합니다. 
- const 키워드는 선언과 동시에 리터럴 값을 할당해줘야합니다.

```javascript
var name="선언"
name="재할당가능"
var name="재선언가능"

let test="선언"
test="재할당가능"
let test="재선언불가능" //SyntaxError: Identifier 't' has already been declared

const PI="3.14" //const는 상수선언 키워드이므로 값 재할당이 불가능합니다.
//선언과 동시에 값을 할당해줘야 합니다.
```



#### var와 let, const의 차이점은 크게 유효 범위(scope)라고 볼 수 있습니다. 

- var는 Function-scope이고, let, const는 Block-scope입니다.

  - scope를 직역하면 영역, 범위라는 뜻입니다. 하지만 프로그램 언어에서의 유효범위는 어느 범위까지 참조하는지. 즉 변수와 매개변수의 **접근성**과 **생존기간**을 뜻합니다.

  - Function-scope는 변수의 참조가 function 단위부터 막히는 것입니다.

    ```javascript
    // var는 function-scope이기 때문에 for문이 끝난다음에 i를 호출하면 값이 출력이 잘 된다.
    for (var j = 0; j < 3; j++) {
        console.log('j', j)
    }
    console.log('after loop j is ', j) // after loop j is 3
    
    
    // 아래의 경우에는 에러가 발생한다.
    // function-scope이기에 i가 출력되지 않는다.
    function counter() {
        for (var i = 0; i < 3; i++) {
            console.log('i', i)
        }
    }
    counter()
    console.log('after loop i is', i) // ReferenceError: i is not defined
    ```

    

  - Block-scope는 변수의 참조가 Block단위부터 막히는 것입니다. 

    ```javascript
    for (let j = 0; j < 3; j++) {
        console.log('j', j)
    }
    console.log('after loop j is ', j) //ReferenceError: j is not defined
    ```



#### var를 쓰면 안되는 이유(var, let 비교)

- var 키워드는 변수명을 재선언해도 아무런 문제가 발생하지 않습니다.
  반면 let 키워드는 변수명 재선언시 에러가 발생합니다.
- var 키워드는 호이스팅(hoisting)이라는 매커니즘을 통해 끌어 올려진다. 

``` javascript
console.log(var_test); //에러가 발생되지 않음 undefined 출력됨
var var_test =1;
consolo.log(var_test);

console.log(let_test); //ReferenceError: let_test is not defined
let let_test = 1;
console.log(let_test);
```

위의 예제를 자바스크립트가 실행할 때 호이스팅을 하여 아래와 같이 정리되며 실행한다.

```javascript
var var_test;
console.log(var_test);
var_test = 1;
console.log(var_test);

console.log(let_test);
let let_test = 1;
console.log(let_test);
```

- 호이스팅을 통하여 위와 같이 정리되는데 let과 달리 var키워드는 선언만 문서 맨 위로 올라갑니다. 
- 선언만 올라가고 할당 자체는 개발자가 작성한 위치에서 실행되기 때문에 var를 주로 사용하게 되면 개발자가 상정하지 못한 문제가 발생할 수 있습니다. 
- 그렇기에 es6에서는 var를 사용하지 않고 let을 사용하는 것이 좀 더 좋다고 생각합니다. 



#### const!!

- const로 선언한 변수는 값의 변경이 절대 불가능합니다.
- 하지만 객체, 배열 같은 경우는 const로 선언하여도 내부의 값 변경이 가능합니다.

``` javascript
const PI="3.14";
PI="3.15" //Uncaught TypeError: Assignment to constant variable.

const arr = [];
arr.push(1);
console.log(arr); //[ 1 ]

const object = {value : 1};
object.value = 2;
console.log(object.value); // 2
```

위의 예제를 실행하게 되면 변수 재할당은 안되지만 배열과 객체 같은 경우는 되는 것을 확인할 수 있습니다. 

- 이게 가능한 이유는 자바스크립트에서 배열과 객체 같은 경우는 배열, 객체 자체가 할당 되는 것이 아닌 
  배열과 객체의 **주소**가 할당되기 때문입니다. 

```javascript
const object2 = {value : 1};
const object3 = {value : 1};

console.log(object2 == object3); //false
console.log(object2 === object3); //false
```

- 객체 자체가 아닌 주소를 할당해주는 것을 확인 할 수 있는 예제입니다. 



#### es6에서의 변수 사용법

1. 우선 변수 선언은 **const**로 합니다.
2. 재할당이 필요한 변수 같은 경우는 let으로 선언합니다.
3. es6에서 var는 쓰지 않습니다. 

위와 같이 변수를 사용하는 이유는 기본적으로 const를 사용하고 재할당이 필요한 경우에 let을 사용하게 되면 

코드를 확인하는데 더 수월하며 개발자의 시선 밖의 에러가 날 확률이 더 줄어듭니다.