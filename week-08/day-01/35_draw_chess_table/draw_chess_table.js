// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//
var line ="";
for(i=1;i<=8;i++){
    for(j=1;j<=8;j++){
        if((i%2===0 && j%2===0) || (i%2===1 && j%2===1)){
            line += "%";
        }else{
            line += " ";
        }
    }
    console.log(line);
    line ="";
}