function changeBodyColor(){
    document.body.style.backgroundColor = 'tomato';
}

let myDialog = Dialog("Hello");

myDialog.onAction(changeBodyColor);