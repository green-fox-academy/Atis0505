var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecb015029b20462fbfa4d244b3bd797c&begin_date=19690416&end_date=19690421";

var myRequest = new XMLHttpRequest();
myRequest.open("GET", url, false);
myRequest.send(null);

var myContent = JSON.parse(myRequest.response);
console.log(myContent);


var contentUl = document.querySelector('ul');

myContent.response.docs.forEach(function(article) {
    if(article['snippet'].search('a') != -1){
        var br = document.createElement('br');
        var newLi = document.createElement('li');
        newLi.innerText = article['headline'].main+ "\n" + article['snippet'] +"\n"+ article['pub_date'];
        newLi.appendChild(br);
        contentUl.appendChild(newLi);
        contentUl.appendChild(br);
    }
    
});


