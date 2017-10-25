'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

var size = 5;

function drawMatrix(size_number){
    var line = "";
    var size = size_number;
    for(var i = 1; i<=size;i++){
        for(var j=1;j<=size;j++){
            if(j===size_number){
                line+="1"
            }else{
                line+="0"
            }
        }
        size_number--;
        console.log(line)
        line = ""
    }
}

drawMatrix(size)
