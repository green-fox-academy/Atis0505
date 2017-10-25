'use strict';
// Things are a little bit messed up
// Your job is to decode the notSoCrypticMessage by using the hashmap as a look up table
// Assemble the fragments into the out variable

var out = "";
var out2 = "";
var notSoCrypticMessage = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11];

var hashmap = {
    7: "run around and desert you ",
    50: "tell a lie and hurt you ",
    49: "make you cry, ",
    2: "let you down",
    12: "give you up, ",
    1: "Never gonna ",
    11: "\n",
    3: "say goodbye "
};

for(var i = 0; i<= notSoCrypticMessage.length-1;i++){
    for(var key in hashmap){
        if(key==notSoCrypticMessage[i]){
            out+=hashmap[key]
        }
    }
}

notSoCrypticMessage.forEach(function(number){
    out2 += hashmap[number]
})

console.log(out)
console.log(out2)