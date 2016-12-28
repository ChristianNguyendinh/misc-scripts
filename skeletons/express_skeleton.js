/*
(Install Node)
npm init
npm install --save express
node express_skeleton.js
*/

var express = require('express');
var app = express();

app.set('port', (process.env.port || 3000));

app.get('/', function(req, res) {
	res.send("hey");
	console.log("request recieved");
});

app.listen(app.get('port'), function() {
	console.log("Server started on port " + app.get('port'));
});