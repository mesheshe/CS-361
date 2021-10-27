var express = require('express');

var app = express();

app.set('port', 3000);

app.get('/', function(req,res){
    res.send('A message from CS361');
});



app.listen(app.get('port'), function(){
    console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});