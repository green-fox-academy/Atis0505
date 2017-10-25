'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average
var sum_candies = 0;
for(var item in students){
    let line = students[item];
    for(var key in line){
        var candies = line['candies']
    }  
    sum_candies += candies;
}
console.log("Students have " + sum_candies + " candies!")
