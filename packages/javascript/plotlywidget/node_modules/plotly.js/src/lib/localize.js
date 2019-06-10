/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var Registry = require('../registry');

/**
 * localize: translate a string for the current locale
 *
 * @param {object} gd: the graphDiv for context
 *  gd._context.locale determines the language (& optional region/country)
 *  the dictionary for each locale may either be supplied in
 *  gd._context.locales or globally via Plotly.register
 * @param {string} s: the string to translate
 */
module.exports = function localize(gd, s) {
    var locale = gd._context.locale;

    /*
     * Priority of lookup:
     *     contextDicts[locale],
     *     registeredDicts[locale],
     *     contextDicts[baseLocale], (if baseLocale is distinct)
     *     registeredDicts[baseLocale]
     * Return the first translation we find.
     * This way if you have a regionalization you are allowed to specify
     * only what's different from the base locale, everything else will
     * fall back on the base.
     */
    for(var i = 0; i < 2; i++) {
        var locales = gd._context.locales;
        for(var j = 0; j < 2; j++) {
            var dict = (locales[locale] || {}).dictionary;
            if(dict) {
                var out = dict[s];
                if(out) return out;
            }
            locales = Registry.localeRegistry;
        }

        var baseLocale = locale.split('-')[0];
        if(baseLocale === locale) break;
        locale = baseLocale;
    }

    return s;
};
