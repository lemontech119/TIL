let _ = require('lodash');
// https://lodash.com/ 참고 하여 학습


// array를 나눌때 사용 chunk
let array = ['a', 'b', 'c', 'd'];
let chunkTest = _.chunk(array, [2]);
console.log(chunkTest);


// array 내부에 원하는 값으로 채우기
array = [1, 2, 3];
_.fill(array, 'a');
console.log(array);
console.log(_.fill(Array(3), 2));
// index 기준으로 1<= index <3 설정해놓은 value 값으로 변경
console.log(_.fill([4, 6, 8, 10], "*", 1, 3));


// find
let users = [
    { 'user': 'barney',  'active': false },
    { 'user': 'fred',    'active': false },
    { 'user': 'pebbles', 'active': true }
  ];
_.find(users, (a) =>{
    if (a.active === true){
        // return 
        console.log(a.user)
    }
});
findTest = _.find(users, (a) => {return a.active === false});
console.log(findTest);
console.log(_.find(users, 'active'));

// findIndex
// 기본적으로 find와 사용법이 유사합니다.
// 다만 차이점은 find는 전체 object를 리턴해주지만 findIndex는 index를 리턴합니다. 
console.log(_.findIndex(users, ['active', false]));
console.log(_.findIndex(users, 'active'));


// concat
// array 합치는 용도로 사용할 수 있을 것 같습니다. 
array = [1];
let other = _.concat(array, 2, [3], [[4]]);


// uniq
// uniq는 array의 중복된 값 제거
array = [1, 1, 2, 3, 4, 4]
uniqTest = _.uniq(array)
console.log(uniqTest)


// map 
// map은 모든 array에 함수를 적용시키는 용도로 쓸 수 있을꺼 같다...
function square(n) {
    return n * n
}
array = [4, 8]
console.log(_.map(array, square))


// chain


// sumBy
// array의 Object의 데이터 합산 가능
const sumByTestData = [
    {"제품": "떡볶이", "가격": 3000},
    {"제품": "오뎅", "가격": 1000},
    {"제품": "족발", "가격": 30000}
]
console.log(_.sumBy(sumByTestData, "가격"));

// groupBy
// 원하는 기준 별로 재 배열 생성 가능 
const groupByTestData = [
    {"시장": "암사", "상호": "순수한찬"},
    {"시장": "암사", "상호": "섹시한떡복이"},
    {"시장": "오색", "상호": "엄마네식당"},
    {"시장": "오색", "상호": "낙원떡집"}
]
console.log(_.groupBy([6.1, 4.2, 6.3], Math.floor))
console.log(_.groupBy(groupByTestData, "시장"))


// size 
// array 의 길이 반환 length와 동일한 기능입니다. 
array = [1, 2, 3, 4]
console.log(_.size(array))