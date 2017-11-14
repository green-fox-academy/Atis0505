'use strict'
let password_string = 'Alga19890505';
let express = require('express');
let mysql = require('mysql');
let app = express();
express.json.type = "application/json";
app.use('/assets', express.static("./assets"));

var sqlConnection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Alga19890505',
    database: 'bookstore'
})

sqlConnection.connect();

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html');
});

function getDatabase(tableName, what){
    let searchQuery = 'SELECT' + what + " FROM " + tableName;
    sqlConnection.query(searchQuery, function(err, results, fields){
        callback(results);
    })
}


app.get('/books', function(request, response, callback){
    let data = [];
    sqlConnection.query("Select book_name from book_mast;", function(err, results, fileds){
        results.forEach(function(element){data.push(element.book_name)})
            response.send({'books':data});
        })
});

app.listen('3000',()=>console.log("Futok wazzee!!"));