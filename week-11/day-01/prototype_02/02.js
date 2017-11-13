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
console.log("With class" + rect.getArea());
console.log("With class" +rect.getCircumference());
let rect02 = new Rectangles(20,100);
console.log("With class" +rect02.getArea());
console.log("With class" +rect02.getCircumference());


function getArea02(){
    return this.a*this.b;
}

function getCircumference02(){
    return (this.a+this.b)*2
}


let Rectangle = {
    getArea02,
    getCircumference02
}

let firstRectangle = {
    a:2,
    b:10
}

Object.setPrototypeOf(firstRectangle, Rectangle);
console.log("With Prototype:"+firstRectangle.getArea02());
console.log("With Prototype:"+firstRectangle.getCircumference02());