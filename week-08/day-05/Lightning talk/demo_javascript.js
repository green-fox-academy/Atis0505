//this is the list of numbers
var list_of_number = [1,2,3,4,5,6,7,8,9,10]
//Whats happening if var missing?
//print method
console.log("Fifth element:"+list_of_number[5])

//print first number
console.log("First element:"+list_of_number[0])

//print last number
console.log("Last element:"+list_of_number[list_of_number.length-1])
//Why -1?
//print length of list
console.log("Length of list:"+list_of_number.length)

//for loop in javascript
for(var i = 0; i < list_of_number.length;i++){
    console.log(list_of_number[i])
}