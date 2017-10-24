var lineCount = 4;
var char = "*";
// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

//draw_dymond
var lineCount = 4;
var stars = "";
var spaces = "";
var j = 1;
for(i=0; i<= lineCount; i++){
    stars += "*".repeat(j);
    spaces += " ".repeat(lineCount-i);
    console.log(spaces + stars);
    stars = ""
    spaces = ""
    j += 2;
}