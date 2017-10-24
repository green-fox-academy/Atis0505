// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var lineCount = 6;
var line ="";
for(i=0; i<=lineCount; i++){
    for(j=0; j<=lineCount; j++){
        if(j===0 || i===0 || j===lineCount || i===lineCount || i===j){
            line += "%";
        }else{
            line += " ";
        }
    }
    console.log(line);
    line="";
}