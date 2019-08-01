// comment 스키마
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectId = Schema.Types.ObjectId;
// const ObjectId = {Types: {ObjectId}} = Schema;


const commentSchema = new Schema({
    commenter: {
        type: ObjectId,
        required: true,
        ref: 'User'
    },
    comment : {
        type: String,
        required: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }

});

module.exports = mongoose.model('Comment', commentSchema);