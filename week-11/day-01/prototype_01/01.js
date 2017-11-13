'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(say) {
    this.say = function(){
        console.log(say);
    }
}

let dog = new Animals("woof");
dog.say();

let cat = new Animals("meow");
cat.say();