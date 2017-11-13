'use strict'

let url = "http://localhost:5000";
let bodyElement = document.querySelector('body');
let connectionObject = new XMLHttpRequest();

function talkToApi(method, resource, callback){
    connectionObject.open(method, url+resource, true);
    connectionObject.onload = function(){
        callback(connectionObject.response);
    }
    connectionObject.send();
}
