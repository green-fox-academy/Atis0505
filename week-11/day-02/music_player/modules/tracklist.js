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
        ajax("DELETE", "/tracklists/"+index, Render)
    };

    const Render = function(responseTrackLists){  
        console.log(responseTrackLists);
        let track_list = document.querySelector('.track_list');
        while(track_list.firstChild){
            track_list.removeChild(track_list.firstChild);
        }
        responseTrackLists.forEach(function(trackListItem, i) {
            let listsDiv = document.createElement('div');
            listsDiv.classList.add('listItem');           
            listsDiv.addEventListener('click', function(){
                Highlight(i, trackListItem.title);
            });
            listsDiv.addEventListener('bdlclick', function(){
                Delete(i);
            })
            let index_string = i+1;
            listsDiv.classList.add(index_string);
            listsDiv.textContent = (i+1)+" "+trackListItem.title;
            track_list.appendChild(listsDiv);

        });
    }

    const Highlight = function(index, title){
        console.log(index+ "  "+title);
        let titleTag = document.querySelector('title');
        let trackDivs = document.querySelectorAll('.track_list div');
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

trackListModule.load();