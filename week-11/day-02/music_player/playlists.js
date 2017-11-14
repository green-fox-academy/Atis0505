'use strict'

const PlaylistModule = function(dialog) {
    return {
        create: function(playlistName) {
            let li = document.createElement('li')
            li.textContent = playlistName
            document.querySelector('ul').appendChild(li);
            dialog.close();
        }
    }
}

const Load = function(responseList) {
    responseList.forEach(function(title, i) {
        n = i+1;      
        if(i%2==0){
             Render(title,"#EAEAEA;");
        }else{
           Render(title, "#F5F5F5;");
        }
    });
}

const Render = function(itemOfList, color){
    let trackDiv = document.createElement('div');
    trackDiv.textContent = n+"  "+ title;
    trackDiv.style.backgroundColor = color;
    document.querySelector('.track_list').appendChild(trackDiv);
    
}