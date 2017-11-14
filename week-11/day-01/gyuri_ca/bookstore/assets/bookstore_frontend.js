'use strict'

let xhr = new XMLHttpRequest();
let url = "http://localhost:3000";


function talkToApi(request_type, end_point, callback){
    xhr.open(request_type, url+end_point, true);
    xhr.onload = function(){
        callback(xhr.response);
    }
    xhr.send();
}

talkToApi("GET", "/books", createList);

function createList(response){
    console.log(response);
    let listOfElement = parseResponse(response);
    console.log(listOfElement);
}

function parseResponse(responseText){
    return JSON.parse(responseText);
}