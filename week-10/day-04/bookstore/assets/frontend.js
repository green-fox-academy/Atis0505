'use strict'

let url = 'http://localhost:4000';
let bodyElement = document.querySelector('body');
let connectionObject = new XMLHttpRequest();

function talkToApi(method, resource){
    connectionObject.open(method, url+resource, true);
    connectionObject.onload = function(){
        let div = document.createElement('div');
        div.innerHTML = connectionObject.response;
        bodyElement.appendChild(div);
    }
    connectionObject.send();

}

talkToApi("GET", "/list");
// talkToApi("GET", "/all");