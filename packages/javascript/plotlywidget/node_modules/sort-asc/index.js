/*!
 * sort-asc <https://github.com/helpers/sort-asc>
 *
 * Copyright (c) 2014 Jon Schlinkert, contributors.
 * Licensed under the MIT License
 */

'use strict';

module.exports = function (a, b) {
  return b < a ? -1 : 1;
};