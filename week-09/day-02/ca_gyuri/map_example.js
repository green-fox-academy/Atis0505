'use strict'

let nums = [1,2,3,4,5,6,7,8,9];

let evens = [];
//for meg minden más kellene hozzá, map-el egyszerűbb

function isEven(num) {
    return num % 2 === 0;
}

let evensNum = nums.filter(isEven);

evens = nums.filter(function(num){
    return num % 2 === 0;
});

let doubledNum = nums.map(function(num){
    return num * 2;
})

console.log(evens)
console.log(doubledNum)
console.log(evensNum)
