var btn = document.querySelector('button');

btn.addEventListener('click', function(){
    var myInput = document.querySelector('input');
    var url = 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=';
        url += myInput.value;
        console.log(btn.value);

    var myFrame = document.querySelector('iframe');
        
    var myRequest = new XMLHttpRequest();
    myRequest.open("GET", url, false);
    myRequest.setRequestHeader('X-Mashape-Key','eDobuIitKbmshmCL4exbA4iNROQip1tmFLyjsnuXvgZoVBKl1A');
    myRequest.setRequestHeader('Accept','application/json');
    myRequest.send(null);
    var myData = JSON.parse(myRequest.response);

    var lblLat = document.querySelector('.lat');
    lblLat.textContent = myData.Results[0].lat;
    var lblLon = document.querySelector('.lon');
    lblLon.textContent = myData.Results[0].lon;
    myFrameSrcString = myFrame.src;
    let XY = lblLat.textContent +","+lblLon.textContent;
    myFrame.setAttribute('src',myFrameSrcString.substr(0,120)+XY);
    console.log(myFrame.src);

});
