/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

/*
* substantial portions of this code from FileSaver.js
* https://github.com/eligrey/FileSaver.js
* License: https://github.com/eligrey/FileSaver.js/blob/master/LICENSE.md
* FileSaver.js
* A saveAs() FileSaver implementation.
* 1.1.20160328
*
* By Eli Grey, http://eligrey.com
* License: MIT
*   See https://github.com/eligrey/FileSaver.js/blob/master/LICENSE.md
*/

'use strict';

var fileSaver = function(url, name) {
    var saveLink = document.createElement('a');
    var canUseSaveLink = 'download' in saveLink;
    var isSafari = /Version\/[\d\.]+.*Safari/.test(navigator.userAgent);
    var promise = new Promise(function(resolve, reject) {
        // IE <10 is explicitly unsupported
        if(typeof navigator !== 'undefined' && /MSIE [1-9]\./.test(navigator.userAgent)) {
            reject(new Error('IE < 10 unsupported'));
        }

        // First try a.download, then web filesystem, then object URLs
        if(isSafari) {
            // Safari doesn't allow downloading of blob urls
            document.location.href = 'data:application/octet-stream' + url.slice(url.search(/[,;]/));
            resolve(name);
        }

        if(!name) {
            name = 'download';
        }

        if(canUseSaveLink) {
            saveLink.href = url;
            saveLink.download = name;
            document.body.appendChild(saveLink);
            saveLink.click();
            document.body.removeChild(saveLink);
            resolve(name);
        }

        // IE 10+ (native saveAs)
        if(typeof navigator !== 'undefined' && navigator.msSaveBlob) {
            // At this point we are only dealing with a SVG encoded as
            // a data URL (since IE only supports SVG)
            var encoded = url.split(/^data:image\/svg\+xml,/)[1];
            var svg = decodeURIComponent(encoded);
            navigator.msSaveBlob(new Blob([svg]), name);
            resolve(name);
        }

        reject(new Error('download error'));
    });

    return promise;
};

module.exports = fileSaver;
