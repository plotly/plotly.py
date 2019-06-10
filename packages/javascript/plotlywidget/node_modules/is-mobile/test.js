var test = require('tape');
var isMobile = require('./');

var iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3';
var chrome = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36';
var ffos = 'Mozilla/5.0 (Mobile; rv:18.0) Gecko/18.0 Firefox/18.0';
var ipad = 'Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1'

test('is mobile', function (t) {
  t.ok(isMobile({ ua: iphone }));
  t.ok(isMobile({ ua: ffos }));
  t.notOk(isMobile({ ua: ipad }));
  t.ok(isMobile({ ua: ipad, tablet: true }));
  t.ok(isMobile({ ua: { headers: { 'user-agent': iphone } } }));
  t.notOk(isMobile({ ua: chrome }));
  t.notOk(isMobile({ ua: { headers: { 'user-agent': chrome } } }));
  t.notOk(isMobile());
  t.notOk(isMobile({ ua: { headers: null } }));
  t.notOk(isMobile({ ua: { headers: { 'user-agent': null } } }));

  global.navigator = {};

  global.navigator.userAgent = iphone;
  t.ok(isMobile());
  t.ok(isMobile({ tablet: true }));

  global.navigator.userAgent = chrome;
  t.notOk(isMobile());
  t.notOk(isMobile({ tablet: true }));

  global.navigator.userAgent = ipad;
  t.notOk(isMobile());
  t.ok(isMobile({ tablet: true }));

  t.end();
});
