'use strict';
// Accidentally I messed up this quote from Richard Feynman.
// Two words are out of place
// Your task is to fix it by swapping the right words with code

// Also, log the sentence to the console with spaces in between.

var words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."];

Array.prototype.move = function(from,to){
    this.splice(to,0,this.splice(from,1)[0]);
    return this;
  };

[words[2],words[5]] = [words[5],words[2]]
console.log(words)