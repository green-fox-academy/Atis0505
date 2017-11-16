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

    const Create = function(playListName){
        let postData = { "title" : playListName};
        ajax("POST", "/playlists", Render, postData);
    };

    const Load = function() {
        ajax("GET", "/playlists", Render)
    };

    const Delete = function(index){
        ajax("DELETE", "/playlists/"+index, Render)
    };

    const Render = function(responsePlayLists){  
        console.log(responsePlayLists);
        let play_list = document.querySelector('.play_lists');
        while(play_list.firstChild){
            play_list.removeChild(play_list.firstChild);
        }
        responsePlayLists.forEach(function(playListItem, i) {
            let listsDiv = document.createElement('div');  
            listsDiv.classList.add('listItem'); 
            console.log(playListItem.name);  
            listsDiv.textContent = playListItem.name;
            listsDiv.addEventListener('click', function(){
                Highlight(i);
            });
            play_list.appendChild(listsDiv);
        });
    }

    const Highlight = function(index){
        let titleTag = document.querySelector('title');
        let trackDivs = document.querySelectorAll('.play_list div');
        trackDivs.forEach(function(div, i){
            if(i === index){
                div.setAttribute("style","background: lightgreen;");

            }else if(i % 2 == 0 ){
                div.setAttribute("style", "background-color: #EAEAEA;")
            }else{
                div.setAttribute("style", "background-color: #F5F5F5;")
            }
        })
    }


    return {
        create : Create,
        load : Load
    }

})();

playListModule.load();