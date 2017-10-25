'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(max_number){
    var sum = 0;
    for(var i=0;i<=max_number;i++){
        sum += i;
    }
    return sum
}

console.log(sum(5))