'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];
var max_match_length = (boys.length>girls.length)?girls.length:boys.length;
for(var i =0; i < max_match_length; i++){
    order.push(girls[i]) 
    order.push(boys[i])
}

console.log(order);