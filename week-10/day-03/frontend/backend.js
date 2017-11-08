let express = require('express');
let app = express();

app.use("/assets", express.static('./assets'));


app.get('/',function(req, rep){
    rep.sendFile(__dirname + '/index.html');
});

app.get('/doubling',function(req, res){
    let response_number = {"received": req.query.input, "result":req.query.input*2};
    res.send(JSON.stringify(response_number));
});


app.listen(8080);