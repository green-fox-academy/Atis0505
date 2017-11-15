'use strict'
let password_string = 'Alga19890505';
let mysql = require('mysql');
let express = require('express');
let app = express();

express.json.type = "application/json";

app.use(express.json());
app.use('/',express.static('./'));

var sqlConnection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: password_string,
    database: 'Music'
});

function getList(typeList){
    let data = [];
    sqlConnection.query("Select * from "+typeList+";", function(err, results, fields){
        results.forEach(function(element){data.push(element)
        })
        response.send(data);
    })
}

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html');
    console.log(__dirname);
});

app.get("/playlists", function(request, response){
    let data = [];
    sqlConnection.query("Select * from PlayList;", function(err, results, fields){
        results.forEach(function(element){data.push(element)
        })
        response.send(data);
    })
    
});

app.get("/tracklists", function(request, response){
    let data = [];
    sqlConnection.query("Select * from Music;", function(err, results, fields){
        results.forEach(function(element){data.push(element)
        })
        response.send(data);
    })
    
});

app.post("/playlists", function(req, res){
    console.log(req.body);
    let data = [];
    // sqlConnection.query("INSERT INTO PlayList (name) VALUES ('"+ req.body.title +"')");
    // res.json({result : "ok"});
    // data.push({"status" : "ok"});
    res.json(data);
});

app.post("/tracklists", function(req, res){
    console.log(req.body);
    let data = [];
    // sqlConnection.query("INSERT INTO Music (name) VALUES ('"+ req.body.title +"')");
    // res.json({result : "ok"});
    // data.push({"status" : "ok"});
    res.json(data);
});

app.delete("/playlists/:id", function(req, res){
    let data = [];
    sqlConnection("DELETE FROM PlayList WHERE id="+req.params.id+";", function(err, results, fields){
        results.forEach(function(element){data.push(element)
        })
    res.json(data);
    })
});

app.delete("/tracklists/:id", function(req, res){
    let data = [];
    sqlConnection("DELETE FROM Music WHERE id="+req.params.id+";", function(err, results, fields){
        results.forEach(function(element){data.push(element)
        })
    res.json(data);
    })
});


app.listen(4500);