class ElevatorController{
    contructor(){      
        var myModel = new ElevatorModel(10,10);
        var myView = new ElevatorView;
        myView.drawElevator();
    }
}


class ElevatorModel{

    constructor(maxFloor, maxPeople){
        this.maxFloor = maxFloor;
        this.maxPeople = maxPeople;
        this.people_in_elevator = 0;
    }

    getActualPosition() {
        var actualLevel = document.querySelector('div.green');
        var levels = document.querySelectorAll('div.level');
        var actualPosition;
        levels.forEach(function(level, i){
            if(actualLevel === level){
                actualPosition = i;
            }
        });
        return actualPosition;
    }

    addPeople() {
        if(this.people_in_elevator < this.maxPeople){
            this.people_in_elevator++;
        }
    }

    removePeople() {
        if(this.people_in_elevator > 0){
            this.people_in_elevator--;
        }
    }
}


class ElevatorView{    

    drawElevator(){
        console.log(myModel.maxFloor);
        var content = document.querySelector('content');
        for(var i = 0; i <= myModel.maxFloor; i++){
            var newDiv = document.createElement('div');
            newDiv.classList.add('level'    );
            content.appendChild(newDiv);    
        }
        content.style.justifyContent = "center";
        content.alignItems = "center";
        
    }

    drawPeopleInElevator(index) {
        var levels = document.querySelectorAll('div');
        levels[index].classList.add("green");
        levels[index].textContent = myModel.people_in_elevator;
    }

    moveElevator(direction) {
        var levels = document.querySelectorAll('div');
        var currentPosition = myModel.getActualPosition ();
        if(direction === 'down' && currentPosition < myModel.maxFloor){
            levels[currentPosition].classList.remove('green');
            levels[currentPosition].textContent = "";
            this.drawPeopleInElevator(currentPosition+1);
        }else if(direction === 'up'){
            levels[currentPosition].classList.remove('green');
            levels[currentPosition].textContent = "";
            this.drawPeopleInElevator(currentPosition-1);
        }
    }

}

var myModel = new ElevatorModel(10,10);
var myView = new ElevatorView;
myView.drawElevator();
myView.drawPeopleInElevator(0);

let up_button = document.querySelector('.up');
let down_button = document.querySelector('.down');
let add_button = document.querySelector('.add');
let remove_button = document.querySelector('.remove');

add_button.addEventListener('click', function(){
    myModel.addPeople();
    myView.drawPeopleInElevator(myModel.getActualPosition());
});

remove_button.addEventListener('click', function(){
    myModel.removePeople();
    myView.drawPeopleInElevator(myModel.getActualPosition());
});

up_button.addEventListener('click', function(){
    myView.moveElevator('up');
});

down_button.addEventListener('click', function(){
    myView.moveElevator('down');
});
