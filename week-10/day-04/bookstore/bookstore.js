'use strict'
let password_string = 'Alga19890505';
const mysql = require('mysql');
let express = require('express');
let app = express();
let sql_query_book_title = "SELECT book_name FROM book_mast;";
let sql_query_to_table =`SELECT book_name, aut_name, cate_descrip, pub_name, book_price
                        FROM book_mast
                        INNER JOIN author ON book_mast.aut_id = author.aut_id 
                        INNER JOIN category ON book_mast.cate_id = category.cate_id 
                        INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id`;
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
    console.log(__dirname);
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
        response.send(rows);
    });

});


app.get('/table', function(request, response) {
    connection.query(sql_query_to_table, function(err, rows){
        if(err){
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        response.send(rows);
    });

});


app.listen(4000);