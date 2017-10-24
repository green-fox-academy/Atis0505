// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

var cuboidSideSize = 10;
var surfaceArea = Math.pow(cuboidSideSize,2)*6;
var cuboidVolume = Math.pow(cuboidSideSize,3);

console.log("Surface Area: "+ surfaceArea +"\n"+
            "Volume: " + cuboidVolume);