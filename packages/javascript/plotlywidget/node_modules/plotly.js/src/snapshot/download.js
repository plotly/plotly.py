/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var toImage = require('../plot_api/to_image');
var Lib = require('../lib');
var fileSaver = require('./filesaver');

/** Plotly.downloadImage
 *
 * @param {object | string | HTML div} gd
 *   can either be a data/layout/config object
 *   or an existing graph <div>
 *   or an id to an existing graph <div>
 * @param {object} opts (see ../plot_api/to_image)
 * @return {promise}
 */
function downloadImage(gd, opts) {
    var _gd;
    if(!Lib.isPlainObject(gd)) _gd = Lib.getGraphDiv(gd);

    // check for undefined opts
    opts = opts || {};
    // default to png
    opts.format = opts.format || 'png';

    return new Promise(function(resolve, reject) {
        if(_gd && _gd._snapshotInProgress) {
            reject(new Error('Snapshotting already in progress.'));
        }

        // see comments within svgtoimg for additional
        //   discussion of problems with IE
        //   can now draw to canvas, but CORS tainted canvas
        //   does not allow toDataURL
        //   svg format will work though
        if(Lib.isIE() && opts.format !== 'svg') {
            reject(new Error('Sorry IE does not support downloading from canvas. Try {format:\'svg\'} instead.'));
        }

        if(_gd) _gd._snapshotInProgress = true;
        var promise = toImage(gd, opts);

        var filename = opts.filename || gd.fn || 'newplot';
        filename += '.' + opts.format;

        promise.then(function(result) {
            if(_gd) _gd._snapshotInProgress = false;
            return fileSaver(result, filename);
        }).then(function(name) {
            resolve(name);
        }).catch(function(err) {
            if(_gd) _gd._snapshotInProgress = false;
            reject(err);
        });
    });
}

module.exports = downloadImage;
