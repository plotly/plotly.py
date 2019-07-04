var http = require('http');
var url = require('url');
var fs = require('fs');
var path = require('path');

var ecstatic = require('ecstatic');
var browserify = require('browserify');
var cheerio = require('cheerio');
var tapParser = require('tap-parser');
var chrome = require('chrome-launch');

var PORT = 8080;
var PATH_ROOT = path.join(__dirname, '..');
var PATH_INDEX_STUB = path.join(PATH_ROOT, 'index.tmp.html');
var PATH_TEST_BUNDLE = path.join(PATH_ROOT, 'test.tmp.js');

var URL = 'http://localhost:' + PORT + '/index.tmp.html';
var EXIT_CODE = 0;

if(process.argv.length !== 4) {
    throw new Error('must provide path to html and js files');
}

var PATH_INDEX = process.argv[2];
var PATH_TEST_FILE = process.argv[3];

main();

function main() {
    scanInput();

    stubIndex()
        .then(bundleTests)
        .then(startServer)
        .then(launch);
}

function scanInput() {
    var reqFiles = [PATH_INDEX, PATH_TEST_FILE];

    reqFiles.forEach(function(filePath) {
        if(!doesFileExist(filePath)) {
            throw new Error(filePath + ' does not exist');
        }
    });
}

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

function doesFileExist(filePath) {
    try {
        if(fs.statSync(filePath).isFile()) return true;
    }
    catch(e) {
        return false;
    }

    return false;
}
