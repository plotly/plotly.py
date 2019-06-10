'use strict'


var isBrowser = require('is-browser');
var toAB = require('./');
var t = require('tape')
var toString =  require('arraybuffer-to-string')



t('bare-bones Data URIs', t => {
    var uri = 'data:,Hello%2C%20World!';

    var buf = toAB(uri);
    t.equal('Hello, World!', toString(buf));

    t.end()
});

t('bare-bones "base64" Data URIs', t => {
    var uri = 'data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D';

    var buf = toAB(uri);

    t.equal('text/plain', buf.type);
    t.equal('Hello, World!', toString(buf));

    t.end()
});

t('plain-text Data URIs', t => {
    var html = '<!DOCTYPE html>'+
               '<html lang="en">'+
               '<head><title>Embedded Window</title></head>'+
               '<body><h1>42</h1></body>'+
               '</html>';

    // Escape the HTML for URL formatting
    var uri = 'data:text/html;charset=utf-8,' + encodeURIComponent(html);

    var buf = toAB(uri);
    t.equal('text/html', buf.type);
    t.equal('utf-8', buf.charset);
    t.equal(html, toString(buf));

    t.end()
});

// the next 4 tests are from:
// https://bug161965.bugzilla.mozilla.org/attachment.cgi?id=94670&action=view

t('"ISO-8859-8 in Base64" URIs', t => {
    var uri = 'data:text/plain;charset=iso-8859-8-i;base64,+ezl7Q==';

    var abuf = toAB(uri);

    t.equal('text/plain', abuf.type);
    t.equal('iso-8859-8-i', abuf.charset);
    var buf = Buffer.from(abuf)

    t.equal(4, buf.length);
    t.equal(0xf9, buf[0]);
    t.equal(0xec, buf[1]);
    t.equal(0xe5, buf[2]);
    t.equal(0xed, buf[3]);

    t.end()
});

t('"ISO-8859-8 in URL-encoding" URIs', t => {
    var uri = 'data:text/plain;charset=iso-8859-8-i,%f9%ec%e5%ed';

    var abuf = toAB(uri)
    var buf = Buffer.from(abuf);
    t.equal('text/plain', abuf.type);
    t.equal('iso-8859-8-i', abuf.charset);
    t.equal(4, buf.length);
    t.equal(0xf9, buf[0]);
    t.equal(0xec, buf[1]);
    t.equal(0xe5, buf[2]);
    t.equal(0xed, buf[3]);

    t.end()
});

t('"UTF-8 in Base64" URIs', t => {
    var uri = 'data:text/plain;charset=UTF-8;base64,16nXnNeV150=';

    var abuf = toAB(uri);
    t.equal('text/plain', abuf.type);
    t.equal('UTF-8', abuf.charset);
    t.equal(8, abuf.byteLength);
    t.equal('שלום', toString(abuf, 'utf8'));

    t.end()
});

t('"UTF-8 in URL-encoding" URIs', t => {
    var uri = 'data:text/plain;charset=UTF-8,%d7%a9%d7%9c%d7%95%d7%9d';

    var abuf = toAB(uri);
    t.equal('text/plain', abuf.type);
    t.equal('UTF-8', abuf.charset);
    t.equal(8, abuf.byteLength);
    t.equal('שלום', toString(abuf, 'utf8'));

    t.end()
});

// this next one is from Wikipedia IIRC

t('"base64" Data URIs with newlines', t => {
    var uri = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA\n' +
      'AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO\n' +
      '9TXL0Y4OHwAAAABJRU5ErkJggg==';

    var abuf = toAB(uri);
    t.equal('image/png', abuf.type);
    t.equal('iVBORw0KGgoAAAANSUhEUgAAAAUA' +
      'AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO' +
      '9TXL0Y4OHwAAAABJRU5ErkJggg==', toString(abuf, 'base64'));

    t.end()
});

t('a plain-text URI with a space character in it', t => {
    var uri = 'data:,foo bar';

    var buf = toAB(uri);
    t.equal('text/plain', buf.type);
    t.equal('foo bar', toString(buf));

    t.end()
});

t('data with a "," comma char', t => {
    var uri = 'data:,a,b';
    var buf = toAB(uri);
    t.equal('text/plain', buf.type);
    t.equal('a,b', toString(buf));

    t.end()
});

t('data with traditionally reserved characters like ";"', t => {
    var uri = 'data:,;test';
    var buf = toAB(uri);
    t.equal('text/plain', buf.type);
    t.equal(';test', toString(buf));

    t.end()
});


t('base64 string', t => {
    var str = Buffer.from('12345', 'binary').toString('base64')

    var buf = toAB(str)
    t.equal(toString(buf), '12345')

    t.end()
})

t('plain string', t => {
    var buf = toAB('Hello World!')
    t.equal(toString(buf), 'Hello World!')

    t.end()
})

t('unicode data-uri', t => {
    t.equal(toAB('uuLMhh').byteLength, 6)
    t.end()
})

