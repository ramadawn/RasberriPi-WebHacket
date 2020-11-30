const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
var path = require('path');


const app = express();

const USERNAME = "test"
const PASSWORD = "test"

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

app.get('/', function (request, response) {
    response.sendFile(path.join(__dirname + '/login.html'));
});

app.post('/auth', function (request, response) {
    const username = request.body.username;
    const password = request.body.password;
    if (username && password) {
        if (username === USERNAME && password === PASSWORD) {
            response.redirect('/home');
        } else {
            response.status(403);
            response.send('Incorrect Username and/or Password!');
        }
    } else {
        response.status(403)
        response.send('Please enter Username and Password!');
    }
    response.end();
});

app.get('/home', function (request, response) {
    response.send('Welcome back, ' + USERNAME + '!');
    response.end();
});

app.listen(3000);