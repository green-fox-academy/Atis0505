'use strict'

const trackListModule = (function(){

    // const PlaylistDialog = function(dialog) {
    //     return {
    //         create: function(playlistName) {
    //             let li = document.createElement('li')
    //             li.textContent = playlistName
    //             document.querySelector('ul').appendChild(li);
    //             dialog.close();
    //         }
    //     }
    // }

    const Create = function(trackListName){
        let postData = { "title" : trackListName};
        ajax("POST", "/tracklists", Render, postData);
    };

    const Load = function() {
        ajax("GET", "/tracklists", Render)
    };

    const Delete = function(index){
        ajax("DELETE", "/tracklists", index)
    };

    const Render = function(responseTrackLists){  
        console.log(responseTrackLists);
        let track_list = document.querySelector('.track_list');
        responseTrackLists.forEach(function(trackListItem, i) {
            let listsDiv = document.createElement('div');
            // listsDiv.style.height = "40px";
            listsDiv.style.fontSize = "20px";
            listsDiv.style.textAlign = "left";
            listsDiv.style.padding = "8px";
            listsDiv.textContent = trackListItem.title;
            listsDiv.addEventListener('mouseover', function(){
                listsDiv.style.backgroundColor = "#ABE7E5";
            });
            let index_string = i+1;
            listsDiv.className = index_string;
            if(i % 2 == 0){
                listsDiv.style.backgroundColor = "#EAEAEA";
            }else{
                listsDiv.style.backgroundColor = "#F5F5F5";
            }
            track_list.appendChild(listsDiv);
        });
    }

    return {
        create : Create,
        load : Load
    }

})();

trackListModule.load();