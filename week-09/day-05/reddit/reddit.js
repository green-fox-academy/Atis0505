'use strict'
var myRequestObject = new XMLHttpRequest();
var postsUrl = 'http://secure-reddit.herokuapp.com/simple/posts';
myRequestObject.open("GET", postsUrl);

function getPost(callback){
    myRequestObject.onreadystatechange = function() {
        if(myRequestObject.readyState == 4) {
            let postsDetails = JSON.parse(myRequestObject.responseText).posts;
            postsDetails.forEach(function(element) {
                createNewPost(element);
            }, this);
            callback(postsDetails);
        }
    }
    myRequestObject.send(null);
}

let logPost = function (postObject) {
    console.log(postObject);
}

var content= document.querySelector('content');

function createNewPost(item){
    let postDiv = document.createElement('article');
    let articleContent = `<div class = "first_column">
                            <div class="upArrow"><\div>
                            <div class = "score"><\div>
                          <\div>
                          <div class = "second_column">
                            <div class ="post_title"><\div>
                            <div class = "post_content"><\div>
                          <\div>`;
    postDiv.className = "post";
    postDiv.innerHTML = articleContent;
    content.appendChild(postDiv);
}

getPost(logPost);