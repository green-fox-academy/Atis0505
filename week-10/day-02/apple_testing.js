//Apple testing file

'use strict'

var test = require('tape');
var apple_object = require('./apples');
// console.log(apple_object.getApple);

test('apple object test',function(t){
    t.equal(apple_object.getApple,'apple');
    t.end();
});