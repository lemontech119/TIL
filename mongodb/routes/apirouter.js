var express = require('express');
var router = express.Router();
var Users = require('../schemas/user');
var Comments = require('../schemas/comment');

/* GET users listing. */
router.get('/', function (req, res, next) {
    res.send('api router');
});

/* GET users listing. */
router.get('/users', function (req, res, next) {
    Users.find({}, (err, result) => {
        if (err) console.log(err);
        else {
            console.log(result);
            res.json(result);
        }
    })


});

router.post('/users', function (req, res, next) {
    const user = new Users({
        name: req.body.name,
        age: req.body.age,
        married: req.body.married,
    });
    user.save((err, result) => {
        if (err) console.log(err);
        else {
            console.log(result);
            res.status(201).json(result);
        }
    })
});

/* GET users listing. */
router.get('/comments/:id', function (req, res, next) {
    // Comments.find({}, (err, result) => {
    //     if (err) console.log(err);
    //     else {

    //         console.log(result);
    //         res.json(result);
    //     }
    // })
    Comments.find({commenter: req.params.id}).populate('commenter').exec((err, results) =>{
            if(err) console.log(err);
            else {
                console.log(results);
                res.json(results);
            }
        })

});

router.post('/comments', function (req, res, next) {
    const comment = new Comments({
        commenter: req.body.id,
        comment: req.body.comment
    });
    comment.save((err, result) => {
        if (err) console.log(err);
        else {
            console.log(result);
            res.status(201).json(result);
        }
    })
});

router.patch('/comments/:id', (req, res)=>{
    Comments.updateOne({_id: req.params.id}, 
        {comment: req.body.comment}, (err, result) =>{
            if(err) console.log(err);
            else {
                res.json(result);
            }
    })
})

router.delete('/comments/:id', (req, res)=>{
    Comments.deleteOne({_id: req.params.id},
        (err, result) =>{
            if(err) console.log(err);
            else{
                res.json(result);
            }
        })
})


module.exports = router;
