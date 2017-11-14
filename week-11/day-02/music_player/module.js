'use strict'

class App {
    constructor() {
        let myDialog = AddPlaylistDialog("Foxplayer playlist add")
        let playlist = PlaylistModule( myDialog );

        myDialog.onAction( playlist.create )
        myDialog.onClose( () => {
            alert('Very closed!')
        });

        document.querySelector('.openDialog').addEventListener('click', function(){
            myDialog.show();
        });
    }
}

const myApp = new App();