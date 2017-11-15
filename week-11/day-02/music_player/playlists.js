'use strict'

const playListModule = (function(){

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

    let pass = function(){};
    const Create = function(playListName){
        let postData = { "title" : playListName};
        ajax("POST", "/playlists", Render, postData);
    };

    const Load = function() {
        ajax("GET", "/playlists", Render)
    };

    const Delete = function(index){
        ajax("DELETE", "/playlists/:id", index)
    };

    const Render = function(responsePlayLists){  
        console.log(responsePlayLists);
        let play_list = document.querySelector('.play_lists');
        while(play_list.firstChild){
            play_list.removeChild(play_list.firstChild);
        }
        responsePlayLists.forEach(function(playListItem, i) {
            let listsDiv = document.createElement('div');
            listsDiv.style.fontSize = "20px";
            listsDiv.style.textAlign = "left";
            listsDiv.style.padding = "8px";
            listsDiv.textContent = playListItem.name;
            let index_string = i+1;
            listsDiv.className = index_string;
            listsDiv.addEventListener('click', function(){
                listsDiv.style.backgroundColor = "#ABE7E5";
            });
            if(i % 2 == 0){
                listsDiv.style.backgroundColor = "#EAEAEA";
            }else{
                listsDiv.style.backgroundColor = "#F5F5F5";
            }
            play_list.appendChild(listsDiv);
        });
    }

    return {
        create : Create,
        load : Load
    }

})();

playListModule.load();
playListModule.create("New song");