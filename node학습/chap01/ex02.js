let output = '';

for (var i = 0; i <= 5; i++) {
    for (j = 0; j < i; j++) {
        output += "*";
    }
    output += "\n"
}
console.log(output);

