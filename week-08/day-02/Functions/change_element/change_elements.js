'use strict';
// - Create an array named `s` with the following content: `[1, 2, 3, 8, 5, 6]`
// - Change the 8 to 4 with the `.map` method 
// - Print the fourth element as a test

var s = [1, 2, 3, 8, 5, 6];
var result01 = s.map(function(a){
    return (a===8)? 4: a;
});

var result02 = s.map(function(a,i){
    return (i===4)? "test": a;
});

console.log(result01)
console.log(result02)