/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../lib');
var Template = require('../plot_api/plot_template');

/** Convenience wrapper for making array container logic DRY and consistent
 *
 * @param {object} parentObjIn
 *  user input object where the container in question is linked
 *  (i.e. either a user trace object or the user layout object)
 *
 * @param {object} parentObjOut
 *  full object where the coerced container will be linked
 *  (i.e. either a full trace object or the full layout object)
 *
 * @param {object} opts
 *  options object:
 *   - name {string}
 *      name of the key linking the container in question
 *   - inclusionAttr {string}
 *      name of the item attribute for inclusion/exclusion. Default is 'visible'.
 *      Since inclusion is true, use eg 'enabled' instead of 'disabled'.
 *   - handleItemDefaults {function}
 *      defaults method to be called on each item in the array container in question
 *
 *      Its arguments are:
 *          - itemIn {object} item in user layout
 *          - itemOut {object} item in full layout
 *          - parentObj {object} (as in closure)
 *          - opts {object} (as in closure)
 * N.B.
 *
 *  - opts is passed to handleItemDefaults so it can also store
 *    links to supplementary data (e.g. fullData for layout components)
 *
 */
module.exports = function handleArrayContainerDefaults(parentObjIn, parentObjOut, opts) {
    var name = opts.name;
    var inclusionAttr = opts.inclusionAttr || 'visible';

    var previousContOut = parentObjOut[name];

    var contIn = Lib.isArrayOrTypedArray(parentObjIn[name]) ? parentObjIn[name] : [];
    var contOut = parentObjOut[name] = [];
    var templater = Template.arrayTemplater(parentObjOut, name, inclusionAttr);
    var i, itemOut;

    for(i = 0; i < contIn.length; i++) {
        var itemIn = contIn[i];

        if(!Lib.isPlainObject(itemIn)) {
            itemOut = templater.newItem({});
            itemOut[inclusionAttr] = false;
        } else {
            itemOut = templater.newItem(itemIn);
        }

        itemOut._index = i;

        if(itemOut[inclusionAttr] !== false) {
            opts.handleItemDefaults(itemIn, itemOut, parentObjOut, opts);
        }

        contOut.push(itemOut);
    }

    var defaultItems = templater.defaultItems();
    for(i = 0; i < defaultItems.length; i++) {
        itemOut = defaultItems[i];
        itemOut._index = contOut.length;
        opts.handleItemDefaults({}, itemOut, parentObjOut, opts, {});
        contOut.push(itemOut);
    }

    // in case this array gets its defaults rebuilt independent of the whole layout,
    // relink the private keys just for this array.
    if(Lib.isArrayOrTypedArray(previousContOut)) {
        var len = Math.min(previousContOut.length, contOut.length);
        for(i = 0; i < len; i++) {
            Lib.relinkPrivateKeys(contOut[i], previousContOut[i]);
        }
    }

    return contOut;
};
