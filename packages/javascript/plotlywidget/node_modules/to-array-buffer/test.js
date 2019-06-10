'use strict'

var NDArray = require('ndarray');
var isBrowser = require('is-browser');
var toAB = require('./');
var t = require('tape')

t('basics', t => {
	t.ok(toAB(1) instanceof ArrayBuffer);
	t.equal(toAB(1).byteLength, 1);
	t.end()
})

t('ArrayBuffer', t => {
	t.equal(toAB(new ArrayBuffer(2)).byteLength, 2);
	t.end()
})

t('Float32Array', t => {
	t.equal(toAB(new Float32Array(2)).byteLength, 8);
	t.end()
})

t('Buffer', t => {
    var u8ab = new Uint8Array(4)

    var b = Buffer.from(u8ab.buffer)
    var ab = toAB(b)
    t.equal(ab.byteLength, 4)

    var u8ab = new Uint8Array(ab)
    var u8b = new Uint8Array(b.buffer)

    t.deepEqual(u8ab, u8b)

    u8ab[0] = 100
    t.equal(u8b[0], 100, 'reference buffer instead of copy')

	t.end()
})

t('Array', t => {
	t.equal(toAB([1,2,3]).byteLength, 3);
	t.end()
})

t('data-uri bare-bones', t => {
	var uri = 'data:,Hello%2C%20World!';
    var buf = toAB(uri);
    t.equal('Hello, World!', String.fromCharCode.apply(null, new Uint8Array(buf)));

    t.end()
})
t('data-uri bare-bones base64', t => {
    var uri = 'data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D';
    var buf = toAB(uri);
    t.equal('Hello, World!', String.fromCharCode.apply(null, new Uint8Array(buf)));
    t.end()
})
t.skip('File, Blob', t => {
    if (!global.File || !global.Blob) return t.end()

	var uri = 'data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D';
    var file = new File([uri], 'hw.txt')
    var blob = new Blob([uri])

    t.equal(String.fromCharCode.apply(null, new Uint8Array(toAB(file))), 'Hello, World!')
    t.equal(String.fromCharCode.apply(null, new Uint8Array(toAB(blob))), 'Hello, World!')

    t.end()
})
t('plain-text Data URIs', t => {
	var html = '<!DOCTYPE html>'+
               '<html lang="en">'+
               '<head><title>Embedded Window</title></head>'+
               '<body><h1>42</h1></body>'+
               '</html>';

    // Escape the HTML for URL formatting
    var uri = 'data:text/html;charset=utf-8,' + encodeURIComponent(html);

    var buf = toAB(uri);
    t.equal(html, String.fromCharCode.apply(null, new Uint8Array(buf)));
    t.end()
})
t.skip('decode "ISO-8859-8 in Base64" URIs', t => {
	var uri = 'data:text/plain;charset=iso-8859-8-i;base64,+ezl7Q==';

    var buf = toAB(uri);
    t.equal(4, buf.byteLength);

    var arr = new Uint8Array(buf)
    t.equal(0xf9, arr[0]);
    t.equal(0xec, arr[1]);
    t.equal(0xe5, arr[2]);
    t.equal(0xed, arr[3]);

    t.end()
})
t('decode "ISO-8859-8 in URL-encoding" URIs')
t('decode "UTF-8 in Base64"')
t('base64')

t('non-decodable')

t.skip('unicode data-uri', t => {
    t.equal(toAB('uuLMhh').byteLength, 16)
    t.end()
})

t('nested arrays', t => {
    t.deepEqual(
        [0,0,0,0,1,1,1,1],
        new Uint8Array(toAB([[0,0,0,0], new Uint8Array([1,1,1,1])]))
    )

    t.end()
})

t('bad input', t => {
    t.notOk(toAB(null))
    t.notOk(toAB())
    t.notOk(toAB(/abc/))
    t.notOk(toAB(new Date))

    t.end()
})

t.skip('huge files', async t => {
    // save-file case of saving 2gb file
    // https://github.com/dy/save-file/issues/15

    // var fs = require('fs')
    // let a = fs.readFileSync('./test.mkv')
    let resp = await fetch('./test.mkv')
    let blob = await resp.blob()

    var ab = await new Promise(ok => {
        var fileReader = new FileReader();
        fileReader.onload = function(event) {
            ok(event.target.result);
        };
        fileReader.readAsArrayBuffer(blob);
    })

    let byteArray = new Int8Array(ab)

    // toAB(byteArray)
    // let data = new Blob([byteArray], {type: 'application/octet-stream'})

    // require('../save-file/src/to-blob')(byteArray, 'x.mkv')
    let save = require('../save-file')
    save(byteArray, 'x.mkv')

    t.end()
})
