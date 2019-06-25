function test() {
    var hangeul = prompt("국어 시험 성적은?");
    hangeul = Number(hangeul);
    var math = prompt("수학 시험성적은?");
    math = Number(math);
    var english = prompt("영어 시험성적은?");
    english = Number(english);
    var total = hangeul + math + english;
    var mean = total / 3;

    document.write("<tr><td>국어</td><td>" + hangeul + "</td></tr>");
    document.write("<tr><td>수학</td><td>" + math + "</td></tr>");
    document.write("<tr><td>영어</td><td>" + english + "</td></tr>");
    document.write("<tr><td>총점</td><td>" + total + "</td></tr>");
    document.write("<tr><td>평균</td><td>" + mean + "</td></tr>");
}
