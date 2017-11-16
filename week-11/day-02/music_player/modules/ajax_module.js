'use strict'



function ajax(request_type, end_point, callback, reqBody){
    
    let xhr = new XMLHttpRequest();
    let url = "http://localhost:4500";

   
    xhr.open(request_type, url+end_point,true);

    xhr.setRequestHeader("accept", "application/json");
    xhr.setRequestHeader("content-type", "application/json");
    xhr.onload = function(){
        callback(JSON.parse(xhr.responseText));
    }
    let bodyDataText = null;
    if(reqBody){
        bodyDataText = JSON.stringify(reqBody);
    }
    xhr.send(bodyDataText);
}
