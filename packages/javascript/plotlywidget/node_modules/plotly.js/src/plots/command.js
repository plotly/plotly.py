/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../registry');
var Lib = require('../lib');

/*
 * Create or update an observer. This function is designed to be
 * idempotent so that it can be called over and over as the component
 * updates, and will attach and detach listeners as needed.
 *
 * @param {optional object} container
 *      An object on which the observer is stored. This is the mechanism
 *      by which it is idempotent. If it already exists, another won't be
 *      added. Each time it's called, the value lookup table is updated.
 * @param {array} commandList
 *      An array of commands, following either `buttons` of `updatemenus`
 *      or `steps` of `sliders`.
 * @param {function} onchange
 *      A listener called when the value is changed. Receives data object
 *      with information about the new state.
 */
exports.manageCommandObserver = function(gd, container, commandList, onchange) {
    var ret = {};
    var enabled = true;

    if(container && container._commandObserver) {
        ret = container._commandObserver;
    }

    if(!ret.cache) {
        ret.cache = {};
    }

    // Either create or just recompute this:
    ret.lookupTable = {};

    var binding = exports.hasSimpleAPICommandBindings(gd, commandList, ret.lookupTable);

    if(container && container._commandObserver) {
        if(!binding) {
            // If container exists and there are no longer any bindings,
            // remove existing:
            if(container._commandObserver.remove) {
                container._commandObserver.remove();
                container._commandObserver = null;
                return ret;
            }
        } else {
            // If container exists and there *are* bindings, then the lookup
            // table should have been updated and check is already attached,
            // so there's nothing to be done:
            return ret;
        }
    }

    // Determine whether there's anything to do for this binding:

    if(binding) {
        // Build the cache:
        bindingValueHasChanged(gd, binding, ret.cache);

        ret.check = function check() {
            if(!enabled) return;

            var update = bindingValueHasChanged(gd, binding, ret.cache);

            if(update.changed && onchange) {
                // Disable checks for the duration of this command in order to avoid
                // infinite loops:
                if(ret.lookupTable[update.value] !== undefined) {
                    ret.disable();
                    Promise.resolve(onchange({
                        value: update.value,
                        type: binding.type,
                        prop: binding.prop,
                        traces: binding.traces,
                        index: ret.lookupTable[update.value]
                    })).then(ret.enable, ret.enable);
                }
            }

            return update.changed;
        };

        var checkEvents = [
            'plotly_relayout',
            'plotly_redraw',
            'plotly_restyle',
            'plotly_update',
            'plotly_animatingframe',
            'plotly_afterplot'
        ];

        for(var i = 0; i < checkEvents.length; i++) {
            gd._internalOn(checkEvents[i], ret.check);
        }

        ret.remove = function() {
            for(var i = 0; i < checkEvents.length; i++) {
                gd._removeInternalListener(checkEvents[i], ret.check);
            }
        };
    } else {
        // TODO: It'd be really neat to actually give a *reason* for this, but at least a warning
        // is a start
        Lib.log('Unable to automatically bind plot updates to API command');

        ret.lookupTable = {};
        ret.remove = function() {};
    }

    ret.disable = function disable() {
        enabled = false;
    };

    ret.enable = function enable() {
        enabled = true;
    };

    if(container) {
        container._commandObserver = ret;
    }

    return ret;
};

/*
 * This function checks to see if an array of objects containing
 * method and args properties is compatible with automatic two-way
 * binding. The criteria right now are that
 *
 *   1. multiple traces may be affected
 *   2. only one property may be affected
 *   3. the same property must be affected by all commands
 */
exports.hasSimpleAPICommandBindings = function(gd, commandList, bindingsByValue) {
    var i;
    var n = commandList.length;

    var refBinding;

    for(i = 0; i < n; i++) {
        var binding;
        var command = commandList[i];
        var method = command.method;
        var args = command.args;

        if(!Array.isArray(args)) args = [];

        // If any command has no method, refuse to bind:
        if(!method) {
            return false;
        }
        var bindings = exports.computeAPICommandBindings(gd, method, args);

        // Right now, handle one and *only* one property being set:
        if(bindings.length !== 1) {
            return false;
        }

        if(!refBinding) {
            refBinding = bindings[0];
            if(Array.isArray(refBinding.traces)) {
                refBinding.traces.sort();
            }
        } else {
            binding = bindings[0];
            if(binding.type !== refBinding.type) {
                return false;
            }
            if(binding.prop !== refBinding.prop) {
                return false;
            }
            if(Array.isArray(refBinding.traces)) {
                if(Array.isArray(binding.traces)) {
                    binding.traces.sort();
                    for(var j = 0; j < refBinding.traces.length; j++) {
                        if(refBinding.traces[j] !== binding.traces[j]) {
                            return false;
                        }
                    }
                } else {
                    return false;
                }
            } else {
                if(binding.prop !== refBinding.prop) {
                    return false;
                }
            }
        }

        binding = bindings[0];
        var value = binding.value;
        if(Array.isArray(value)) {
            if(value.length === 1) {
                value = value[0];
            } else {
                return false;
            }
        }
        if(bindingsByValue) {
            bindingsByValue[value] = i;
        }
    }

    return refBinding;
};

function bindingValueHasChanged(gd, binding, cache) {
    var container, value, obj;
    var changed = false;

    if(binding.type === 'data') {
        // If it's data, we need to get a trace. Based on the limited scope
        // of what we cover, we can just take the first trace from the list,
        // or otherwise just the first trace:
        container = gd._fullData[binding.traces !== null ? binding.traces[0] : 0];
    } else if(binding.type === 'layout') {
        container = gd._fullLayout;
    } else {
        return false;
    }

    value = Lib.nestedProperty(container, binding.prop).get();

    obj = cache[binding.type] = cache[binding.type] || {};

    if(obj.hasOwnProperty(binding.prop)) {
        if(obj[binding.prop] !== value) {
            changed = true;
        }
    }

    obj[binding.prop] = value;

    return {
        changed: changed,
        value: value
    };
}

/*
 * Execute an API command. There's really not much to this; it just provides
 * a common hook so that implementations don't need to be synchronized across
 * multiple components with the ability to invoke API commands.
 *
 * @param {string} method
 *      The name of the plotly command to execute. Must be one of 'animate',
 *      'restyle', 'relayout', 'update'.
 * @param {array} args
 *      A list of arguments passed to the API command
 */
exports.executeAPICommand = function(gd, method, args) {
    if(method === 'skip') return Promise.resolve();

    var _method = Registry.apiMethodRegistry[method];
    var allArgs = [gd];
    if(!Array.isArray(args)) args = [];

    for(var i = 0; i < args.length; i++) {
        allArgs.push(args[i]);
    }

    return _method.apply(null, allArgs).catch(function(err) {
        Lib.warn('API call to Plotly.' + method + ' rejected.', err);
        return Promise.reject(err);
    });
};

exports.computeAPICommandBindings = function(gd, method, args) {
    var bindings;

    if(!Array.isArray(args)) args = [];

    switch(method) {
        case 'restyle':
            bindings = computeDataBindings(gd, args);
            break;
        case 'relayout':
            bindings = computeLayoutBindings(gd, args);
            break;
        case 'update':
            bindings = computeDataBindings(gd, [args[0], args[2]])
                .concat(computeLayoutBindings(gd, [args[1]]));
            break;
        case 'animate':
            bindings = computeAnimateBindings(gd, args);
            break;
        default:
            // This is the case where intelligent logic about what affects
            // this command is not implemented. It causes no ill effects.
            // For example, addFrames simply won't bind to a control component.
            bindings = [];
    }
    return bindings;
};

function computeAnimateBindings(gd, args) {
    // We'll assume that the only relevant modification an animation
    // makes that's meaningfully tracked is the frame:
    if(Array.isArray(args[0]) && args[0].length === 1 && ['string', 'number'].indexOf(typeof args[0][0]) !== -1) {
        return [{type: 'layout', prop: '_currentFrame', value: args[0][0].toString()}];
    } else {
        return [];
    }
}

function computeLayoutBindings(gd, args) {
    var bindings = [];

    var astr = args[0];
    var aobj = {};
    if(typeof astr === 'string') {
        aobj[astr] = args[1];
    } else if(Lib.isPlainObject(astr)) {
        aobj = astr;
    } else {
        return bindings;
    }

    crawl(aobj, function(path, attrName, attr) {
        bindings.push({type: 'layout', prop: path, value: attr});
    }, '', 0);

    return bindings;
}

function computeDataBindings(gd, args) {
    var traces, astr, val, aobj;
    var bindings = [];

    // Logic copied from Plotly.restyle:
    astr = args[0];
    val = args[1];
    traces = args[2];
    aobj = {};
    if(typeof astr === 'string') {
        aobj[astr] = val;
    } else if(Lib.isPlainObject(astr)) {
        // the 3-arg form
        aobj = astr;

        if(traces === undefined) {
            traces = val;
        }
    } else {
        return bindings;
    }

    if(traces === undefined) {
        // Explicitly assign this to null instead of undefined:
        traces = null;
    }

    crawl(aobj, function(path, attrName, attr) {
        var thisTraces;
        if(Array.isArray(attr)) {
            var nAttr = Math.min(attr.length, gd.data.length);
            if(traces) {
                nAttr = Math.min(nAttr, traces.length);
            }
            thisTraces = [];
            for(var j = 0; j < nAttr; j++) {
                thisTraces[j] = traces ? traces[j] : j;
            }
        } else {
            thisTraces = traces ? traces.slice(0) : null;
        }

        // Convert [7] to just 7 when traces is null:
        if(thisTraces === null) {
            if(Array.isArray(attr)) {
                attr = attr[0];
            }
        } else if(Array.isArray(thisTraces)) {
            if(!Array.isArray(attr)) {
                var tmp = attr;
                attr = [];
                for(var i = 0; i < thisTraces.length; i++) {
                    attr[i] = tmp;
                }
            }
            attr.length = Math.min(thisTraces.length, attr.length);
        }

        bindings.push({
            type: 'data',
            prop: path,
            traces: thisTraces,
            value: attr
        });
    }, '', 0);

    return bindings;
}

function crawl(attrs, callback, path, depth) {
    Object.keys(attrs).forEach(function(attrName) {
        var attr = attrs[attrName];

        if(attrName[0] === '_') return;

        var thisPath = path + (depth > 0 ? '.' : '') + attrName;

        if(Lib.isPlainObject(attr)) {
            crawl(attr, callback, thisPath, depth + 1);
        } else {
            // Only execute the callback on leaf nodes:
            callback(thisPath, attrName, attr);
        }
    });
}
