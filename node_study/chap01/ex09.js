let foo = ["one", "two", "three"];

let a = foo[0];
let b = foo[1];
let c = foo[2];

let [x, y, z] = foo;
console.log(a);
console.log(b);
console.log(c);
console.log(x);
console.log(y);
console.log(z);

let [aa, bb, ...cc] = [1, 2, 3, 4, 5];
console.log(aa);
console.log(bb);
console.log(cc);

let obj = {p: 10, q:true};
let {p, q} = obj;
console.log(p);
console.log(q);