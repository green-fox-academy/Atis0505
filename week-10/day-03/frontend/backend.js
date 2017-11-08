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

app.get('/greeter', function(req, rep){
    if(req.query.name === null){
        answer = { "error": "Please provide a name!"};
    }else if(req.query.title === null){
        answer = { "error": "Please provide a title!"};
    }else{
        answer = { "welcome_message": "Oh, hi there " +req.query.name+", my dear " +req.query.title + "!"};
    }
    rep.json(answer);
});

app.get('/appenda/:animal', function(req, rep){
    let appendA_answer = {"appended" : req.params.animal + "a"};  
    rep.json(appendA_answer);
});

app.post('/dountill/:what', function(req, res))


app.listen(8080);