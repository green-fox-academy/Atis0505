//Apple testing file

'use strict'

var test = require('tape');
var apple_object = require('./apples');

test('apple object test',function(t){
    t.equal(apple_object.getApple,'apple');
    t.end();
});