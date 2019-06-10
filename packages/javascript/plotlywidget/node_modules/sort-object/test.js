/*!
 * sort-keys <https://github.com/helpers/sort-keys>
 *
 * Copyright (c) 2014 Brian Woodward, Jon Schlinkert, contributors.
 * Licensed under the MIT License
 */

'use strict';

var should = require('should');
var assert = require('assert');
var sortAsc = require('sort-asc');
var sortDesc = require('sort-desc');
var sortObj = require('./');

describe('sort object', function () {
  it('should create a new object with only the given keys.', function () {
    var o = {a: 1, c: 2, b: 3};
    var actual = sortObj(o, {keys: ['a', 'b']});

    Object.keys(actual)[0].should.equal('a');
    Object.keys(actual)[1].should.equal('b');
    actual.should.not.have.property('c');
  });

  it('should sort the keys on an object with alphabetical keys', function () {
    var o = {a: 1, c: 2, b: 3};
    var actual = sortObj(o);

    Object.keys(actual)[0].should.equal('a');
    Object.keys(actual)[1].should.equal('b');
    Object.keys(actual)[2].should.equal('c');
  });

  it('should sort the keys on an object with numerical keys', function () {
    var o = {1: 1, 3: 3, 2: 2};
    var actual = sortObj(o);

    Object.keys(actual)[0].should.equal('1');
    Object.keys(actual)[1].should.equal('2');
    Object.keys(actual)[2].should.equal('3');
  });

  it('should sort the keys on an object in descending order.', function () {
    var o = {a: 1, c: 2, b: 3};
    var actual = sortObj(o, {sortOrder: 'desc'});

    Object.keys(actual)[0].should.equal('a');
    Object.keys(actual)[1].should.equal('b');
    Object.keys(actual)[2].should.equal('c');
  });

  it('should sort the keys on an object in ascending order.', function () {
    var o = {a: 1, c: 2, b: 3};
    var actual = sortObj(o, {sortOrder: 'asc'});

    Object.keys(actual)[0].should.equal('c');
    Object.keys(actual)[1].should.equal('b');
    Object.keys(actual)[2].should.equal('a');
  });

  it('should sort the keys using a custom function.', function () {
    var o = {a: 1, c: 2, e: 5, d: 4, b: 3};
    var actual = sortObj(o, {
      sort: function (a, b) {
        return a < b ? -1 : 1;
      }
    });
    actual.should.eql({a: 1, b: 3, c: 2, d: 4, e: 5});

    Object.keys(actual)[0].should.equal('a');
    Object.keys(actual)[1].should.equal('b');
    Object.keys(actual)[2].should.equal('c');
  });

  it('should sort keys to the order in the given array.', function () {
    var o = sortObj({a: 'a', b: 'b', c: 'c'}, ['c', 'a', 'b']);

    Object.keys(o)[0].should.equal('c');
    Object.keys(o)[1].should.equal('a');
    Object.keys(o)[2].should.equal('b');
  });

  it('should use a function to sort keys in the given array.', function () {
    var o = sortObj({a: 'a', b: 'b', c: 'c'}, {
      keys: ['c', 'a'],
      sort: sortDesc
    });

    Object.keys(o)[0].should.equal('a');
    Object.keys(o)[1].should.equal('c');
    o.should.not.have.property('b');
  });

  it('should use a function to sort keys in the given array.', function () {
    var o = sortObj({a: 'a', b: 'b', c: 'c'}, {
      keys: ['b', 'a'],
      sort: sortAsc
    });

    Object.keys(o)[0].should.equal('b');
    Object.keys(o)[1].should.equal('a');
    o.should.not.have.property('c');
  });


  it('should use a `sortBy` function to return an array of keys to sort by.', function () {
    var old = {one: 'aa', two: 'bc', three: 'ab'};
    var o = sortObj(old, {
      sortBy: function (obj) {
        var arr = [];
        Object.keys(obj).filter(function(key) {
          if (/^a/.test(obj[key])) {
            arr.push(key);
          }
        });
        return arr.reverse();
      }
    });

    Object.keys(o).length.should.equal(2);
    Object.keys(o)[0].should.equal('three');
    Object.keys(o)[1].should.equal('one');
  });
});
