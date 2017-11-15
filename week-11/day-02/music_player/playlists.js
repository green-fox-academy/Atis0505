'use strict'

const playListModule = (function(){

    const PlaylistDialog = function(dialog) {
        return {
            create: function(playlistName) {
                let li = document.createElement('li')
                li.textContent = playlistName
                document.querySelector('ul').appendChild(li);
                dialog.close();
            }
        }
    }

    const Create = function(playListName){
        let postData = { "title" : playListName};
        ajax("POST", "/playlists", Render, postData);
    };

    const Load = function() {
        ajax("GET", "/playlists", Render)
    };

    const Delete = function(index){
        ajax("DELETE", "/playlists", index)
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
            listsDiv.style.color = "#BEBEBE";      
            listsDiv.classList.add = i;
            listsDiv.innerHTML = playListItem.name;
            
            if(i % 2 == 0){
                listsDiv.style.backgroundColor = "rgb(234, 234, 234)";
            }else{
                
                listsDiv.style.backgroundColor = "rgb(245, 245, 245)";
            }
            listsDiv.addEventListener('click', function(){
                let old_color = listsDiv.style.backgroundColor;
                if(!listsDiv.style.backgroundColor === "rgb(171, 231, 229)"){
                    listsDiv.style.backgroundColor = "rgb(171, 231, 229)";
                }else{
                    listsDiv.style.backgroundColor = old_color;
                }
                
                // Highlight(i--, listsDiv.style.backgroundColor);
            });
            play_list.appendChild(listsDiv);
        });
    }

    const Highlight = function(index, old_color){
        console.log(old_color);
        let listsDiv = document.querySelectorAll('.play_lists.div');
        console.log(old_color);
        listsDiv.forEach(function(div, i){
            console.log("régi",old_color);
            if(!div.style.backgroundColor == "rgb(171, 231, 229)"){
                div.style.backgroundColor = "rgb(171, 231, 229)"
            }else{
                div.style.backgroundColor = old_color;
            }
            console.log("új",div.style.backgroundColor);
        });
    }

    return {
        create : Create,
        load : Load
    }

})();

playListModule.load();
playListModule.create("New song");