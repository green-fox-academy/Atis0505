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
j-=2
for(i=1; i<= lineCount; i++){
    j -= 2;
    stars += "*".repeat(j);
    spaces += " ".repeat(i);
    console.log(spaces + stars);
    stars = ""
    spaces = ""

}
