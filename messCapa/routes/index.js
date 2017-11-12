var express = require('express');
var router = express.Router();
var mongo = require('mongodb');
var db = require('monk')('localhost:57085/messCapa');

/* GET home page. */
router.get('/', function(req, res, next) {
  var db = req.db;
  var posts = db.get('dataTable');
  posts.find({}, {}, (err,posts)=>{
    res.render('index', { posts: posts });
  });
});

module.exports = router;
