'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(input_number){
    return (input_number<2)?1:factorio(input_number-1)*input_number;
}

console.log(factorio(5))