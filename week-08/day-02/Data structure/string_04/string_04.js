'use strict';
// When saving this quote a disk error has occured. Please fix it.
// Add "always takes longer than" to between the words "It" and "you"

var quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
var src_string = "It"
var start = quote.search(src_string);
var inserted = "always takes longer than"
quote = quote.slice(0,start+src_string.length) + " " + inserted + quote.slice(start+src_string.length)
console.log(start)
console.log(quote);