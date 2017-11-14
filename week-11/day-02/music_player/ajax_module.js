'use strict'

let xhr = new XMLHttpRequest();
let url = "http://localhost:4500";

function talkToApi(request_type, end_point, callback){
    xhr.open(request_type, url+end_point,true);
    xhr.onload() = function(){
        callback(xhr.response);
    }
    xhr.send();
}

talkToApi("GET", "/Playlists", parseResponse);

function parseResponse(musicResponse){
    let musicTitles = JSON.parse(musicResponse);
    console.log(musicTitles);
}