'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() 
// that returns its circumference

function Rectangles( aside, heihgt){
    this.aside = aside;
    this.heihgt = heihgt;
}

Rectangles.prototype.getArea = function(aside, heihgt){
    return this.aside*this.heihgt;
}

Rectangles.prototype.getCircumference = function(aside,heihgt){
    return (this.aside+this.heihgt)*2;
}

let rect = new Rectangles(2,10);
console.log(rect.getArea());
console.log(rect.getCircumference());
let rect02 = new Rectangles(20,100);
console.log(rect02.getArea());
console.log(rect02.getCircumference());