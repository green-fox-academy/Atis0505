'use strict'
let password_string = 'Alga19890505';
const mysql = require('mysql');
let express = require('express');
let app = express();

express.json.type = "application/json";

app.use(express.json());
app.use('/assets',express.static('./assets'));

var sqlConnection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: password_string,
    database: 'Music'
});

app.get("/Playlists", function(request, response){
    let data = [];
    sqlConnection.query("Select title from Music;", function(err, results, fields){
        results.forEach(function(element){data.push(element.title)
            console.log(element.title);
        })
        response.send(data);
    })
    
});

app.listen(4500);