const http = require('http');
const url = require('url');
const querystrubg = require('querystring');

let port = 3000;
const server = http.createServer();

server.listen(port, function () {
    console.log('web server waiting... : %d', port);
});

server.on('connection', function (socket) {
    let addr = socket.address();
    console.log('client: ' + addr.address + ' : ' + addr.port + ' connection.')
});

server.on('close', function () {
    console.log('web server close.');
});

server.on('request', function (req, res) {
    let urlp = url.parse(req.url, true);
    if (urlp.pathname == '/login') {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.write('<p>test</p>')
        res.end();
    } else {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.write('<h1>집가고 싶다</h1>');
        res.end();
    }

})