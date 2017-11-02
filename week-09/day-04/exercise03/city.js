var btn = document.querySelector('button');

btn.addEventListener('click', function(){
    var myInput = document.querySelector('input');
    var url = 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=';
        url += myInput.value;
        console.log(btn.value);
        
    var myRequest = new XMLHttpRequest();
    myRequest.open("GET", url, false);
    myRequest.setRequestHeader('X-Mashape-Key','eDobuIitKbmshmCL4exbA4iNROQip1tmFLyjsnuXvgZoVBKl1A');
    myRequest.setRequestHeader('Accept','application/json');
    myRequest.send(null);
    var myData = JSON.parse(myRequest.response);
    console.log(myData);

    var lblLat = document.querySelector('.lat');
    console.log(myData.Results[0].lat);
    lblLat.textContent = myData.Results[0].lat;
    var lblLon = document.querySelector('.lon');
    lblLon.textContent = myData.Results[0].lon;
});
