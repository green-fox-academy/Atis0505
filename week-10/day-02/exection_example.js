'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2, printStr){
    if(typeof str1 !== 'string' ){
        throw new TypeError("First input is not string!");
    }else if(typeof str2 !== 'string'){
        throw new TypeError("Second input is not string!");
    }else if(typeof printStr !== 'function'){
        throw new TypeError("This is not a function!");
    }
  let newStr = str1 + str2;
  printStr(newStr);
}

let printStr = function(str) {
  console.log(str);
}
try{
    addString('1234', '56789', printStr);
} catch (error_object) {
    console.log("Catch error!");
    console.log(error_object.message);
}
