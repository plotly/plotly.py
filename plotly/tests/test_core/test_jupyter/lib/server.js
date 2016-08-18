var http = require('http');
var url = require('url');
var fs = require('fs');
var path = require('path');
var ecstatic = require('ecstatic');
var browserify = require('browserify');
var cheerio = require('cheerio');
var chrome = require('chrome-launch');
var tapParser = require('tap-parser');

var PORT = 8080;
var PATH_ROOT = path.join(__dirname, '..');
var PATH_FIXTURES = path.join(PATH_ROOT, 'fixtures');
var PATH_INDEX = path.join(PATH_FIXTURES, 'test.html');
var PATH_INDEX_STUB = path.join(PATH_FIXTURES, 'test.tmp.html');
var PATH_TEST_FILE = path.join(PATH_ROOT, 'test.js');
var PATH_TEST_BUNDLE = path.join(PATH_ROOT, 'test.tmp.js');
var URL = 'http://localhost:' + PORT + '/fixtures/test.tmp.html';
var EXIT_CODE = 0;

// main
stubIndex()
    .then(bundleTests)
    .then(startServer)
    .then(launch)

function stubIndex() {
    return new Promise(function(resolve, reject) {
        var html = fs.readFileSync(PATH_INDEX, 'utf-8');
        var $ = cheerio.load(html);

        $('body').append('<script type="text/javascript" src="../test.tmp.js"></script>');

        fs.writeFile(PATH_INDEX_STUB, $.html(), resolve);
    });
}

function bundleTests() {
    return new Promise(function(resolve, reject) {
        var wsBundle = fs.createWriteStream(PATH_TEST_BUNDLE);

        browserify(PATH_TEST_FILE, { debug: true })
            .bundle()
            .pipe(wsBundle);

        wsBundle.on('close', resolve);
    });
}

function startServer() {
    return new Promise(function(resolve, reject) {
        var server = http.createServer(ecstatic({ root: PATH_ROOT }));

        server.on('request', handle);

        server.listen(PORT, resolve);
    });
}

function handle(req, res) {
    var query = url.parse(req.url).query || '';
    var parser = tapParser();

    function is(query, root) {
        return query.indexOf(root) !== -1;
    }

    if(is(query, 'data')) handleData(req, res);
    if(is(query, 'done')) handleDone();

    function handleData(req, res) {
        req.pipe(parser);
        req.pipe(process.stdout);
    }

    parser.on('assert', function(assert) {
        if(EXIT_CODE === 0 && assert.ok === false) EXIT_CODE = 1;
    })

    function handleDone() {
        removeBuildFiles();
        process.exit(EXIT_CODE);
    }
}

function launch() {
    chrome(URL);
}

function removeBuildFiles() {
    fs.unlinkSync(PATH_INDEX_STUB);
    fs.unlinkSync(PATH_TEST_BUNDLE);
}
