let express = require('express');
let app = express();

app.get('/hello', function(req, rep){
    rep.json({"hello":"bello"});
});

app.post('/hello',function(req, rep){
    rep.json({"hello":"mr postman!"});
});


app.listen(3000);