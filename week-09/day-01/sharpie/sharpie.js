// We should know about each sharpie:
//      color (which should be a string)
//      width (which will be a number)
//      inkAmount (another number)
// When instantiating a Sharpie, we need to specify the color and the width
// Every sharpie is created with a default 100 as inkAmount
// We can use() the sharpie objects
//      which decreases inkAmount by the width
// Write a loop that consumes all the sharpie's ink, but don't hardcode the 
// required iteration count to your code

function Sharpie(color, width){
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
    this.use = function(){
        this.inkAmount -= this.width;
        return this.inkAmount;
    }
}

var sharpie = new Sharpie('black',5);
console.log(sharpie.inkAmount);
while(sharpie.inkAmount > 0){
    sharpie.use();
}
console.log(sharpie.inkAmount);
