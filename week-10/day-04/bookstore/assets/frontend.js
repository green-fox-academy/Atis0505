'use strict'

let url = 'http://localhost:4000';
let bodyElement = document.querySelector('body');
let connectionObject = new XMLHttpRequest();

function talkToApi(method, resource, callback){
    connectionObject.open(method, url+resource, true);
    connectionObject.onload = function(){
        callback(connectionObject.response);      
    }
    connectionObject.send();
}

talkToApi("GET", "/list", createNameOfList);

function createNameOfList(response){
    let responseList = JSON.parse(response);
    console.log(responseList);   
    let div = document.createElement('div');
    div.innerHTML = "<ul>";
    responseList.forEach(function(row) {
        div.innerHTML+="<li>"+ row.book_name +"</li>"
    });
    div.innerHTML+="</ul>"
    // div.innerHTML = responseText;
    bodyElement.appendChild(div);
}




// talkToApi("GET", "/all");