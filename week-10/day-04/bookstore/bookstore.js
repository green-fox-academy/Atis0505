'use strict'
let password_string = 'Alga19890505';
const mysql = require('mysql');
let express = require('express');
let app = express();
let sql_query_book_title = "SELECT book_name FROM book_mast;";
express.json.type = "application/json";

app.use(express.json());
app.use('/assets',express.static('./assets'));

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: password_string,
    database: 'bookstore'
});

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html');
});

connection.connect(function(err){
    if(err){
      console.log(err, "Error connecting to Db");
      return;
    }
    console.log("Connection established");
});



app.get('/list', function(request, response) {
    connection.query(sql_query_book_title, function(err, rows){
        if(err){
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        // console.log(rows);
        // var htmlString = '<ul>';
        // rows.forEach(function(row) {
            
        //     htmlString = htmlString + '<li>' + row.book_name + '</li>';
        // });
        // htmlString = htmlString + '</ul>';
        response.send(rows);
    });

});


// app.get('/all', function(request, response){
//     connection.query(sql_query_book_title, function(err, rows){
//         if(err){
//             console.log(err.toString());
//         }
//         console.log("Data received from Db:\n");
//         let htmlString = '<table><ul>';
//         rows.forEach(function(row) {
//             htmlString = htmlString + '<li>' + row.book_name + '<li>';
//         });
//         htmlString = htmlString + '<ul>';
//     })
//     response.send(htmlString);
// });

app.listen(4000);