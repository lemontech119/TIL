let a = 'test';
let b = 10;
let c = true;
console.log(`${a} ${b} ${c}`);

const obj = {
    outside: {
        inside: {
            key: 'value',
        },
    },
}

console.log(obj);
console.dir(obj, {
    depth: 1
})