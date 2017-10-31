'use strict';

function factorialTillLimitWithCallback(limit, callback) {
  var factorial = 1;
  for (var i = 1; i <= limit; ++i) {
    callback(factorial);
    factorial *= i;
  }
  console.log(factorial);
}

function printNumber( number ) {
    console.log("the number: ", number);
}


// Create a function and pass it as a parameter to the factorialTillLimitWithCallback
// function, and print all the factorial numbers till 20
const myFactorial = factorialTillLimitWithCallback(5, printNumber);


console.log(myFactorial)