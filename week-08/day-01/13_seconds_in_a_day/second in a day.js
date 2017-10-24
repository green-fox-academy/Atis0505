var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

let leftSeconds = ((24-currentHours)*60*60) + ((60-currentMinutes)*60) + 60-currentSeconds;
console.log(leftSeconds);