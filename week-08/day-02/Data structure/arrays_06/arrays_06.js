'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

var listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]
var checkList = [4,8,12,16]

function numChecker(list_of_number){
    var count_number = list_of_number.length;
    var found_nembur = 0;
    for(var i=0;i<=count_number-1;i++){
        for(var j = 0; j<= checkList.length-1;j++){
            (list_of_number[i]==checkList[j])?found_nembur=found_nembur+1:found_nembur=found_nembur+0;
        }
    }
    console.log(found_nembur)
    return (found_nembur===checkList.length)?true:false;
}

console.log(numChecker(listOfNumbers))