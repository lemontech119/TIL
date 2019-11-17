var subject;
(function (subject) {
    subject[subject["Math"] = 1] = "Math";
    subject[subject["Science"] = 3] = "Science";
    subject[subject["History"] = 7] = "History";
})(subject || (subject = {}));
console.log(subject[3]);
