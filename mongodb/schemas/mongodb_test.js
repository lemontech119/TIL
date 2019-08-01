// Using Node.js `require()`
const mongoose = require('mongoose');
// const Schema = mongoose.Schema;
const { Schema } = mongoose;

// mongodb 연결
mongoose.connect('mongodb://localhost/nodejs', {
    useNewUrlParser: true
});

// user 스키마 정의
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

const User = mongoose.model('user', userSchema);

User.find({}, (err,docs)=>{
    if(err){
        console.log(err);
    } else {
        console.log(docs);
    }
})

const user = new User({
    name: 'hong',
    age: 20,
    married: false
})
user.save((err, result) => {
    if(err)
        console.log(err);
    else {
        console.log(result);
    }
 }) 