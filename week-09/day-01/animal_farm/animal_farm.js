

class Animal{
    constructor(){
        this.hunger = 5;
        this.thirst = 5;
    }
    eat(){
        this.hunger -= 1
    }
    drink(){
        this.thirst -= 1
    }
    play(){
        this.hunger -= 1
        this.thirst -= 1
    }
}

class Farm{
    constructor(slot){
        this.slot = slot;
        this.animal_list= [];
    }
    
    breed(){
        if(this.slot > 0){
            var animal = new Animal();
            this.animal_list.push(animal)
        }else{
            console.log("No more place!");
        }
    }

    slaghter(){
        this.animal_list.sort(function(a, b) { 
            return b.hunger - a.hunger;
        })
        this.animal_list.splice(this.animal_list.length,1);
    }

    current_state(){
        console.log("The farm has "+this.animal_list.length+" living animals we are bankrupt");
    }

    progress(){
        for(var i = 0; i <= this.animal_list.length-1; i++){
            var num = Math.random();
            console.log(num);
            if( num > 0.5){
                this.animal_list.splice(this.animal_list[i],1);
            }
        }
        console.log("Animals number: ",this.animal_list.length)
        if(this.animal_list.length === this.slot){
            console.log("FULL");
        }else if(this.animal_list.length === 0){
            console.log("BANKRUPT");
        }else{
            console.log("OKAY")
        }
    }
}

var farm = new Farm(3);
farm.breed();
farm.breed();
farm.current_state();
farm.breed();
for(var i = 0; i < 100; i++){
    farm.current_state();
    farm.progress();
}