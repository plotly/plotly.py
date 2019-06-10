'use strict';

var expect = require('chai').expect;
var parser = require('../');

// var a = parser.parse('//top\n{// top a\n/* abc */"a":1,//right\n/* bcd */"b":{"a":1}}//bottom');
// // var a = parser.parse('{/*top*/"a":1,//right\n/*abc*/"b":{"a":1}}');
// console.log(a);

var cases = [
  {
    d: 'comment at the top',
    s: '//top\n{"a":1}',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect(obj['//^']).to.deep.equal(['//top']);
    }
  },
  {
    d: 'multiple comments at the top, both line and block',
    s: '//top\n/*abc*/{"a":1}',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect(obj['//^']).to.deep.equal(['//top', '/*abc*/']);
    }
  },
  {
    d: 'comment at the bottom',
    s: '{"a":1}\n//bot',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect(obj['//$']).to.deep.equal(['//bot']);
    }
  },
  {
    d: 'multiple comments at the bottom, both line and block',
    s: '{"a":1}\n//top\n/*abc*/',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect(obj['//$']).to.deep.equal(['//top', '/*abc*/']);
    }
  },
  {
    d: 'comment for properties',
    s: '{//a\n"a":1}',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect('// a' in obj).to.equal(true);
      expect(obj['// a']).to.deep.equal([['//a']]);
    }
  },
  {
    d: 'comment for properties, multiple at the top',
    s: '{//a\n/*b*/"a":1}',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect('// a' in obj).to.equal(true);
      expect(obj['// a']).to.deep.equal([['//a', '/*b*/']]);
    }
  },
  {
    d: 'comment for properties, both top and right',
    s: '{//a\n"a":1//b\n}',
    o: '{"a":1}',
    e: function (obj) {
      expect(obj.a).to.equal(1);
      expect('// a' in obj).to.equal(true);
      expect(obj['// a']).to.deep.equal([['//a'], ['//b']]);
    }
  },
  {
    // #8
    d: 'support negative numbers',
    s: '{//a\n"a": -1}',
    o: '{"a": -1}',
    e: function (obj) {
      expect(obj.a).to.equal(-1);
      expect('// a' in obj).to.equal(true);
    }
  }
]


cases.forEach(function (c) {
  describe("parse()", function(){
    var _it = c.only
      ? it.only
      : it;

    _it(c.d, function(){
      c.e(parser.parse(c.s));
    });

    _it(c.d + ', removes comments', function(){
      expect(parser.parse(c.s, null, true)).to.deep.equal(parser.parse(c.o));
    });
  });
});



var invalid = [
  '{',
  '}',
  '[',
  '',
  '{a:1}',
  '{"a":a}',
  '{"a":undefined}'
];

// ECMA262 does not define the standard of error messages.
// However, we throw error messages the same as JSON.parse()
describe("error messages", function(){
  invalid.forEach(function (i) {
    it('error message:' + i, function(){
      var error;
      var err;

      try {
        parser.parse(i);
      } catch(e) {
        error = e;
      }

      try {
        JSON.parse(i);
      } catch(e) {
        err = e;
      }

      expect(!!(err && error)).to.equal(true);
      expect(error.message).to.equal(err.message);
    });
  });
});
