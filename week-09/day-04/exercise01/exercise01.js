


var myRequest = new XMLHttpRequest();
myRequest.open("GET","https://api.giphy.com/v1/gifs/trending?api_key=Ta2MhJolb79qoH6FBWDi6yNqBAx0Ovdg&limit=25&rating=G",false);
myRequest.send(null);

var myData = JSON.parse(myRequest.response);

console.log(myData.data);

function Gif(){

}

var footer = document.querySelector('footer');
var mainContent = document.querySelector('content');
var mainImage = document.createElement('img');
var gifDownSize = myData.data[0].images.downsized_large.url;        
mainImage.src = gifDownSize;
mainContent.appendChild(mainImage);

for(var i = 0; i <= 12; i++){
    var gifUrl = myData.data[i].images.fixed_width_small_still.url;
    var newImage = document.createElement('img');
    newImage.src = gifUrl;
    footer.appendChild(newImage);
}

var smallImagesList = document.querySelectorAll('footer img');

smallImagesList.forEach(function(image, i){
    image.addEventListener('click', function(){
        mainImage.setAttribute('src', myData.data[i].images.downsized_large.url);
    });
});



