var http = require('http'),
    server = http.createServer(sourcehandler),
    fs = require("fs"),
    httpProxy = require('http-proxy');

server.listen(8080);

function sourcehandler (req, res) {

    console.log('request! url: ', req.url);

    if (req.method !== "POST") {
       console.log(JSON.stringify({msg: "Bad Request Method: " + req.method,
        code: 406}));
       req.destroy();
    }

    req.once('error', function (e) {
       console.log(JSON.stringify(({err:e, msg: "Request Stream Error", code: 500})));
    });

    req.once('close', function (haderror) {
       console.log("REQUEST CLOSING");
    });

    req.setEncoding('utf8');

    if(req.url.indexOf('/successful_write') === 0) {
      console.log('successful_write URLZ.');
      req.pipe(fs.createWriteStream("request.txt", {flags: 'a'}));
    }

    if(req.url==='/5s_timeout') {
        // Keep connection open for 5s, close with a 408
        req.pipe(fs.createWriteStream("request.txt", {flags: 'a'}));
        setTimeout(function(){
          console.log("\nclosing");
          res.writeHead(408);
          res.end("timeout on active data");
          req.destroy();
        }, 5000);
    }
}

//
// Create a proxy server with latency
//
var proxy = httpProxy.createProxyServer();

proxy.on('error', function(err, req, res) {
    res.end();
});

//
// Create your server that makes an operation that waits a while
// and then proxies the request
//
http.createServer(function (req, res) {
  // This simulates an operation that takes 10s to execute
  setTimeout(function () {
    proxy.web(req, res, {
      target: 'http://localhost:8080/successful_write'
    });
  }, 10000);
}).listen(9008);
