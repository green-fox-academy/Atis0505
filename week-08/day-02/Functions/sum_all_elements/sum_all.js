'use strict';
// - Create a variable named `ai` with the following content: `[3, 4, 5, 6, 7]`
// - Log the sum of the elements in `ai` to the console

var ai = [3, 4, 5, 6, 7];
for(var i = 0, sum = 0; i<ai.length; sum+=ai[i++] );
console.log(sum)