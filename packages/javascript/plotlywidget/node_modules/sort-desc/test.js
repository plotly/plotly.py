/*!
 * sort-desc <https://github.com/jonschlinkert/sort-desc>
 *
 * Copyright (c) 2014 Jon Schlinkert, contributors.
 * Licensed under the MIT License
 */

'use strict';

var assert = require('assert');
var sortDesc = require('./');

describe('sort object', function () {
  it('should sort keys in descending order.', function () {
    var actual = (['d', 'c', 'b', 'a']).sort(sortDesc);
    assert.deepEqual(actual, ['a', 'b', 'c', 'd'] );
  });
});
