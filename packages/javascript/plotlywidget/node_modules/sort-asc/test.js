/*!
 * sort-asc <https://github.com/jonschlinkert/sort-asc>
 *
 * Copyright (c) 2014 Jon Schlinkert, contributors.
 * Licensed under the MIT License
 */

'use strict';

var assert = require('assert');
var sortAsc = require('./');

describe('sort object', function () {
  it('should sort keys in ascending order.', function () {
    var actual = (['a', 'b', 'c', 'd']).sort(sortAsc);
    assert.deepEqual(actual, ['d', 'c', 'b', 'a']);
  });
});
