'use strict';

var shop_items = ["Cupcake", 2, "Brownie", false]
var shop_items02 = ["Cupcake", 2, "Brownie", false]

// Accidentally we added "2" and "false" to the array. 
// Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
// No, don't just remove the items :)
shop_items[1] = "Croissant";
shop_items[3] = "Ice cream";
console.log(shop_items)
shop_items02[shop_items02.indexOf(2)] = "Croissant";
shop_items02[shop_items02.indexOf(false)] = "Ice cream";
console.log(shop_items02)