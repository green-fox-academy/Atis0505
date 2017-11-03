'use strict'

var sellProduct = function() {
    var cash = 0;
    return function(price) {
        cash += price;
        console.log(cash);
        
    }
}

let sell = sellProduct();
sell(50)
sell(100)


//n kapszulációt a felső megoldás valósítja meg, ez nem jó mert a var cash elérhető kívülről!!!!
// var cash = 50;

// function sellProduct(price){
//     cash += price;
//     console.log(cash);
// }


// sellProduct(100);