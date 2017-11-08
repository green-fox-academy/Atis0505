let express = require('express');
let app = express();
express.json.type = "application/json";


app.use("/assets", express.static('./assets'));


app.get('/',function(req, rep){
    rep.sendFile(__dirname + '/index.html');
});

app.get('/doubling',function(req, res){
    let response_answer = {"error": "Please provide an input!"}  ;
    if(req.query.input !== undefined){
        response_answer = {"received": req.query.input*1, "result":req.query.input*2};       
    }
    res.json(response_answer);
});


app.listen(8080);