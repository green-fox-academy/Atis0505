'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(input_parameters){
    console.log(arguments)
    console.log("Well hi there,",input_parameters)
}

printer("Attila")