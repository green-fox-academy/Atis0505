let express = require('express');
let app = express();
app.use('/example',express.static('./example'));

app.get('/hello', function(req, rep){
    rep.sendFile(__dirname + '/server.html');
});

app.get('/hello', function(req, rep){
    rep.json({"hello":"bello"});
});

app.post('/hello',function(req, rep){
    rep.json({"hello":"mr postman!"});
});



app.listen(3000);