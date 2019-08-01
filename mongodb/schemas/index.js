// mongodb 연결

// Using Node.js `require()`
const mongoose = require('mongoose');

module.exports = () => {
    mongoose.connect('mongodb://localhost/nodejs', {
        useNewUrlParser: true
    }, (err) => {
        if (err) {
            console.log('mongodb 연결 오류');
        } else {
            console.log('mongodb 연결 성공');
        }
    });

    mongoose.connection.on('error', (err) => {
        console.log('mongodb 연결 에러 : ', err);
    });
    mongoose.connection.on('disconnected', () => {
        console.log('mongodb 연결 끊어짐');
    });
}
