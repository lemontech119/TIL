function add(a, b, callback){
    console.log("--> add함수");
    let result = a+b;
    callback(result);
    console.log("<-- add함수");
}

// function callback2(result){
    
//     console.log('콜백함수');
//     console.log('result= ', result);
// }

//add (10, 20, callback2);

add(10, 20, function(result){
    console.log("--> callback()");
    console.log('콜백함수');
    console.log('result= ', result);
    console.log("<-- callback()");
})