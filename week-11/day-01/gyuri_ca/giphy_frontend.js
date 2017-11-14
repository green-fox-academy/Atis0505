'use strict'
console.log("hello");

let giphy_url = "https://api.giphy.com/v1/gifs/trending?api_key=Ta2MhJolb79qoH6FBWDi6yNqBAx0Ovdg&q=cat&limit=10&rating=G";

function ajax(method, URL, data, callback){
    var ajax = new XMLHttpRequest();
    ajax.onload = function(){
        console.log("Onload");
        callback(JSON.parse(ajax.responseText).data);
        console.log("parse data");
        console.log(JSON.parse(ajax.responseText).data);
        };
        
    ajax.open(method, URL, true);
    console.log("Open");
    ajax.send(data);
    console.log("Data sent");
}

//readystate => 0, 1, 2, 3, 4 
var loaded_gifs = null;
function handle_data(data){
    console.log(data);
    data.forEach(function(element) {
        pasteImg(element.images.fixed_height.url);
    });
    
}

function pasteImg(url){
    let img = document.createElement('img');
    img.src = url;
    document.body.appendChild(img);
}

ajax('GET', giphy_url, null, handle_data );
