'use strict';
// Saturn is missing from the planetList
// Insert it into the correct position
// bonus for using some built in methods

var planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"];
Array.prototype.insert = function (index, item){
    this.splice(index, 0, item)
};
planetList.insert(5,"Saturn");
console.log(planetList)