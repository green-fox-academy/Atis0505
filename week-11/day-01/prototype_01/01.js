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


let cat = new Animals("meow");
cat.say();
dog.say();

function talk(){
    console.log(this.sound);
}

let animal = {
    talk
}

let bear = {
    sound: "grrr"
}

Object.setPrototypeOf(bear, animal);
bear.talk();
