// user 스키마
const mongoose = require('mongoose');
// user 스키마 정의
const { Schema } = mongoose;
const userSchema = new Schema({
    name: {
        type: String,
        required: true,
        unique: true
    },
    age: {
        type: Number,
        required: true
    },
    married: {
        type: Boolean
    },
    comment: {
        type: String
    },
    createAt: {
        type: Date,
        default: Date.now
    }
});
module.exports = mongoose.model('User', userSchema);
