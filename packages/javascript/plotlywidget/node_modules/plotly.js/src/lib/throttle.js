/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var timerCache = {};

/**
 * Throttle a callback. `callback` executes synchronously only if
 * more than `minInterval` milliseconds have already elapsed since the latest
 * call (if any). Otherwise we wait until `minInterval` is over and execute the
 * last callback received while waiting.
 * So the first and last events in a train are always executed (eventually)
 * but some of the events in the middle can be dropped.
 *
 * @param {string} id: an identifier to mark events to throttle together
 * @param {number} minInterval: minimum time, in milliseconds, between
 *   invocations of `callback`
 * @param {function} callback: the function to throttle. `callback` itself
 *   should be a purely synchronous function.
 */
exports.throttle = function throttle(id, minInterval, callback) {
    var cache = timerCache[id];
    var now = Date.now();

    if(!cache) {
        /*
         * Throw out old items before making a new one, to prevent the cache
         * getting overgrown, for example from old plots that have been replaced.
         * 1 minute age is arbitrary.
         */
        for(var idi in timerCache) {
            if(timerCache[idi].ts < now - 60000) {
                delete timerCache[idi];
            }
        }
        cache = timerCache[id] = {ts: 0, timer: null};
    }

    _clearTimeout(cache);

    function exec() {
        callback();
        cache.ts = Date.now();
        if(cache.onDone) {
            cache.onDone();
            cache.onDone = null;
        }
    }

    if(now > cache.ts + minInterval) {
        exec();
        return;
    }

    cache.timer = setTimeout(function() {
        exec();
        cache.timer = null;
    }, minInterval);
};

exports.done = function(id) {
    var cache = timerCache[id];
    if(!cache || !cache.timer) return Promise.resolve();

    return new Promise(function(resolve) {
        var previousOnDone = cache.onDone;
        cache.onDone = function onDone() {
            if(previousOnDone) previousOnDone();
            resolve();
            cache.onDone = null;
        };
    });
};

/**
 * Clear the throttle cache for one or all timers
 * @param {optional string} id:
 *   if provided, clear just this timer
 *   if omitted, clear all timers (mainly useful for testing)
 */
exports.clear = function(id) {
    if(id) {
        _clearTimeout(timerCache[id]);
        delete timerCache[id];
    } else {
        for(var idi in timerCache) exports.clear(idi);
    }
};

function _clearTimeout(cache) {
    if(cache && cache.timer !== null) {
        clearTimeout(cache.timer);
        cache.timer = null;
    }
}
