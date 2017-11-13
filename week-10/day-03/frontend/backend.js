let express = require('express');
let app = express();
express.json.type = "application/json";




app.use("/assets", express.static('./assets'));
app.use(express.json());


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
    if(req.query.name === undefined){
        answer = { "error": "Please provide a name!"};
    }else if(req.query.title === undefined){
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

app.post('/dountil/:what', function(req, res){
    let number = req.body.until;
    if(req.params.what === 'sum'){ 
        result = sum(number);
    }else if(req.params.what === 'factor'){
        result = factor(number);
    }else if(!req.body.until){
        result = {
            "error": "Please provide a number!"
          }
    }
    res.json(result);
});

app.post('/arrays', function(req, res){
    let result = 0;
    if(req.body.what === 'sum'){
        result = req.body.numbers.reduce(function(akkum, number){
            return akkum + number;
        });
    }else if(req.body.what === 'multiply'){
        result = req.body.numbers.reduce(function(number){
            return akkum * number;
        });
    }else if(req.body.what === 'doubling'){
        result = req.body.numbers.map((number) => number*2);
    }
    res.json(result);
});

function sum(number){
    var sum = 0;
    for(var i=0; i<number+1; i++ ){
        sum += i;
    }
    let result = {"result": sum};
    return result;
}

function factor(number){
    var fact = 1;
    for(var i = 1; i<number+1; i++ ){
        fact *= i;
    }
    result = {"result": fact};
    return result;
}

app.listen(8080);