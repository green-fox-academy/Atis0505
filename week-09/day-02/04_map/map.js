
'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.
var newArray = fruits.map(function(fruit){
    var letter_number = 0;
    var chars_list = fruit.split("");
    for(var i = 0; i < chars_list.length; i++){
        if(chars_list[i] === 'e'){
            letter_number ++;
        }
    }
    return letter_number;
})

console.log(newArray)