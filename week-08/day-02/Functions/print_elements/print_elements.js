'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(input_parameters){
    var param_string = ""
    for(var i=0; i<=arguments.length-1;i++){
        param_string += arguments[i] + " "
    }
    console.log("Well hi there,",param_string)
}

printer("Attila","Peti","Zsuzsi","Laci")