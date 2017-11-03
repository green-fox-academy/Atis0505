'use strict'

let number = 1;

const printHello = function(greet) {
    console.log(greet);
}

const greetings = function(print) {
    print("Szevasz");
}

setTimeout(greetings, 1000, printHello);

console.log('Hallo!');