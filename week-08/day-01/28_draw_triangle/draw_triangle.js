var lineCount = 4;
var char = "*";

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for(i=0;i<lineCount;i+=1){
    console.log(char.repeat(i+1));
}