/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var id2name = require('./axis_ids').id2name;
var scaleZoom = require('./scale_zoom');
var makePadFn = require('./autorange').makePadFn;
var concatExtremes = require('./autorange').concatExtremes;

var ALMOST_EQUAL = require('../../constants/numerical').ALMOST_EQUAL;
var FROM_BL = require('../../constants/alignment').FROM_BL;

exports.handleConstraintDefaults = function(containerIn, containerOut, coerce, allAxisIds, layoutOut) {
    var constraintGroups = layoutOut._axisConstraintGroups;
    var matchGroups = layoutOut._axisMatchGroups;
    var axId = containerOut._id;
    var axLetter = axId.charAt(0);
    var splomStash = ((layoutOut._splomAxes || {})[axLetter] || {})[axId] || {};
    var thisID = containerOut._id;
    var letter = thisID.charAt(0);

    // coerce the constraint mechanics even if this axis has no scaleanchor
    // because it may be the anchor of another axis.
    var constrain = coerce('constrain');
    Lib.coerce(containerIn, containerOut, {
        constraintoward: {
            valType: 'enumerated',
            values: letter === 'x' ? ['left', 'center', 'right'] : ['bottom', 'middle', 'top'],
            dflt: letter === 'x' ? 'center' : 'middle'
        }
    }, 'constraintoward');

    var matches, matchOpts;

    if((containerIn.matches || splomStash.matches) && !containerOut.fixedrange) {
        matchOpts = getConstraintOpts(matchGroups, thisID, allAxisIds, layoutOut);
        matches = Lib.coerce(containerIn, containerOut, {
            matches: {
                valType: 'enumerated',
                values: matchOpts.linkableAxes || [],
                dflt: splomStash.matches
            }
        }, 'matches');
    }

    // 'matches' wins over 'scaleanchor' (for now)
    var scaleanchor, scaleOpts;

    if(!matches && containerIn.scaleanchor && !(containerOut.fixedrange && constrain !== 'domain')) {
        scaleOpts = getConstraintOpts(constraintGroups, thisID, allAxisIds, layoutOut, constrain);
        scaleanchor = Lib.coerce(containerIn, containerOut, {
            scaleanchor: {
                valType: 'enumerated',
                values: scaleOpts.linkableAxes || []
            }
        }, 'scaleanchor');
    }

    if(matches) {
        delete containerOut.constrain;
        updateConstraintGroups(matchGroups, matchOpts.thisGroup, thisID, matches, 1);
    } else if(allAxisIds.indexOf(containerIn.matches) !== -1) {
        Lib.warn('ignored ' + containerOut._name + '.matches: "' +
            containerIn.matches + '" to avoid either an infinite loop ' +
            'or because the target axis has fixed range.');
    }

    if(scaleanchor) {
        var scaleratio = coerce('scaleratio');

        // TODO: I suppose I could do attribute.min: Number.MIN_VALUE to avoid zero,
        // but that seems hacky. Better way to say "must be a positive number"?
        // Of course if you use several super-tiny values you could eventually
        // force a product of these to zero and all hell would break loose...
        // Likewise with super-huge values.
        if(!scaleratio) scaleratio = containerOut.scaleratio = 1;

        updateConstraintGroups(constraintGroups, scaleOpts.thisGroup, thisID, scaleanchor, scaleratio);
    } else if(allAxisIds.indexOf(containerIn.scaleanchor) !== -1) {
        Lib.warn('ignored ' + containerOut._name + '.scaleanchor: "' +
            containerIn.scaleanchor + '" to avoid either an infinite loop ' +
            'and possibly inconsistent scaleratios, or because the target ' +
            'axis has fixed range or this axis declares a *matches* constraint.');
    }
};

// If this axis is already part of a constraint group, we can't
// scaleanchor any other axis in that group, or we'd make a loop.
// Filter allAxisIds to enforce this, also matching axis types.
function getConstraintOpts(groups, thisID, allAxisIds, layoutOut, constrain) {
    var doesNotConstrainRange = constrain !== 'range';
    var thisType = layoutOut[id2name(thisID)].type;
    var i, j, idj, axj;

    var linkableAxes = [];
    for(j = 0; j < allAxisIds.length; j++) {
        idj = allAxisIds[j];
        if(idj === thisID) continue;

        axj = layoutOut[id2name(idj)];
        if(axj.type === thisType) {
            if(!axj.fixedrange) {
                linkableAxes.push(idj);
            } else if(doesNotConstrainRange && axj.anchor) {
                // allow domain constraints on subplots where
                // BOTH axes have fixedrange:true and constrain:domain
                var counterAxj = layoutOut[id2name(axj.anchor)];
                if(counterAxj.fixedrange) {
                    linkableAxes.push(idj);
                }
            }
        }
    }

    for(i = 0; i < groups.length; i++) {
        if(groups[i][thisID]) {
            var thisGroup = groups[i];

            var linkableAxesNoLoops = [];
            for(j = 0; j < linkableAxes.length; j++) {
                idj = linkableAxes[j];
                if(!thisGroup[idj]) linkableAxesNoLoops.push(idj);
            }
            return {linkableAxes: linkableAxesNoLoops, thisGroup: thisGroup};
        }
    }

    return {linkableAxes: linkableAxes, thisGroup: null};
}

/*
 * Add this axis to the axis constraint groups, which is the collection
 * of axes that are all constrained together on scale.
 *
 * constraintGroups: a list of objects. each object is
 * {axis_id: scale_within_group}, where scale_within_group is
 * only important relative to the rest of the group, and defines
 * the relative scales between all axes in the group
 *
 * thisGroup: the group the current axis is already in
 * thisID: the id if the current axis
 * scaleanchor: the id of the axis to scale it with
 * scaleratio: the ratio of this axis to the scaleanchor axis
 */
function updateConstraintGroups(constraintGroups, thisGroup, thisID, scaleanchor, scaleratio) {
    var i, j, groupi, keyj, thisGroupIndex;

    if(thisGroup === null) {
        thisGroup = {};
        thisGroup[thisID] = 1;
        thisGroupIndex = constraintGroups.length;
        constraintGroups.push(thisGroup);
    } else {
        thisGroupIndex = constraintGroups.indexOf(thisGroup);
    }

    var thisGroupKeys = Object.keys(thisGroup);

    // we know that this axis isn't in any other groups, but we don't know
    // about the scaleanchor axis. If it is, we need to merge the groups.
    for(i = 0; i < constraintGroups.length; i++) {
        groupi = constraintGroups[i];
        if(i !== thisGroupIndex && groupi[scaleanchor]) {
            var baseScale = groupi[scaleanchor];
            for(j = 0; j < thisGroupKeys.length; j++) {
                keyj = thisGroupKeys[j];
                groupi[keyj] = baseScale * scaleratio * thisGroup[keyj];
            }
            constraintGroups.splice(thisGroupIndex, 1);
            return;
        }
    }

    // otherwise, we insert the new scaleanchor axis as the base scale (1)
    // in its group, and scale the rest of the group to it
    if(scaleratio !== 1) {
        for(j = 0; j < thisGroupKeys.length; j++) {
            thisGroup[thisGroupKeys[j]] *= scaleratio;
        }
    }
    thisGroup[scaleanchor] = 1;
}

exports.enforce = function enforce(gd) {
    var fullLayout = gd._fullLayout;
    var constraintGroups = fullLayout._axisConstraintGroups || [];

    var i, j, axisID, ax, normScale, mode, factor;

    for(i = 0; i < constraintGroups.length; i++) {
        var group = constraintGroups[i];
        var axisIDs = Object.keys(group);

        var minScale = Infinity;
        var maxScale = 0;
        // mostly matchScale will be the same as minScale
        // ie we expand axis ranges to encompass *everything*
        // that's currently in any of their ranges, but during
        // autorange of a subset of axes we will ignore other
        // axes for this purpose.
        var matchScale = Infinity;
        var normScales = {};
        var axes = {};
        var hasAnyDomainConstraint = false;

        // find the (normalized) scale of each axis in the group
        for(j = 0; j < axisIDs.length; j++) {
            axisID = axisIDs[j];
            axes[axisID] = ax = fullLayout[id2name(axisID)];

            if(ax._inputDomain) ax.domain = ax._inputDomain.slice();
            else ax._inputDomain = ax.domain.slice();

            if(!ax._inputRange) ax._inputRange = ax.range.slice();

            // set axis scale here so we can use _m rather than
            // having to calculate it from length and range
            ax.setScale();

            // abs: inverted scales still satisfy the constraint
            normScales[axisID] = normScale = Math.abs(ax._m) / group[axisID];
            minScale = Math.min(minScale, normScale);
            if(ax.constrain === 'domain' || !ax._constraintShrinkable) {
                matchScale = Math.min(matchScale, normScale);
            }

            // this has served its purpose, so remove it
            delete ax._constraintShrinkable;
            maxScale = Math.max(maxScale, normScale);

            if(ax.constrain === 'domain') hasAnyDomainConstraint = true;
        }

        // Do we have a constraint mismatch? Give a small buffer for rounding errors
        if(minScale > ALMOST_EQUAL * maxScale && !hasAnyDomainConstraint) continue;

        // now increase any ranges we need to until all normalized scales are equal
        for(j = 0; j < axisIDs.length; j++) {
            axisID = axisIDs[j];
            normScale = normScales[axisID];
            ax = axes[axisID];
            mode = ax.constrain;

            // even if the scale didn't change, if we're shrinking domain
            // we need to recalculate in case `constraintoward` changed
            if(normScale !== matchScale || mode === 'domain') {
                factor = normScale / matchScale;

                if(mode === 'range') {
                    scaleZoom(ax, factor);
                } else {
                    // mode === 'domain'

                    var inputDomain = ax._inputDomain;
                    var domainShrunk = (ax.domain[1] - ax.domain[0]) /
                        (inputDomain[1] - inputDomain[0]);
                    var rangeShrunk = (ax.r2l(ax.range[1]) - ax.r2l(ax.range[0])) /
                        (ax.r2l(ax._inputRange[1]) - ax.r2l(ax._inputRange[0]));

                    factor /= domainShrunk;

                    if(factor * rangeShrunk < 1) {
                        // we've asked to magnify the axis more than we can just by
                        // enlarging the domain - so we need to constrict range
                        ax.domain = ax._input.domain = inputDomain.slice();
                        scaleZoom(ax, factor);
                        continue;
                    }

                    if(rangeShrunk < 1) {
                        // the range has previously been constricted by ^^, but we've
                        // switched to the domain-constricted regime, so reset range
                        ax.range = ax._input.range = ax._inputRange.slice();
                        factor *= rangeShrunk;
                    }

                    if(ax.autorange) {
                        /*
                         * range & factor may need to change because range was
                         * calculated for the larger scaling, so some pixel
                         * paddings may get cut off when we reduce the domain.
                         *
                         * This is easier than the regular autorange calculation
                         * because we already know the scaling `m`, but we still
                         * need to cut out impossible constraints (like
                         * annotations with super-long arrows). That's what
                         * outerMin/Max are for - if the expansion was going to
                         * go beyond the original domain, it must be impossible
                         */
                        var rl0 = ax.r2l(ax.range[0]);
                        var rl1 = ax.r2l(ax.range[1]);
                        var rangeCenter = (rl0 + rl1) / 2;
                        var rangeMin = rangeCenter;
                        var rangeMax = rangeCenter;
                        var halfRange = Math.abs(rl1 - rangeCenter);
                        // extra tiny bit for rounding errors, in case we actually
                        // *are* expanding to the full domain
                        var outerMin = rangeCenter - halfRange * factor * 1.0001;
                        var outerMax = rangeCenter + halfRange * factor * 1.0001;
                        var getPad = makePadFn(ax);

                        updateDomain(ax, factor);
                        var m = Math.abs(ax._m);
                        var extremes = concatExtremes(gd, ax);
                        var minArray = extremes.min;
                        var maxArray = extremes.max;
                        var newVal;
                        var k;

                        for(k = 0; k < minArray.length; k++) {
                            newVal = minArray[k].val - getPad(minArray[k]) / m;
                            if(newVal > outerMin && newVal < rangeMin) {
                                rangeMin = newVal;
                            }
                        }

                        for(k = 0; k < maxArray.length; k++) {
                            newVal = maxArray[k].val + getPad(maxArray[k]) / m;
                            if(newVal < outerMax && newVal > rangeMax) {
                                rangeMax = newVal;
                            }
                        }

                        var domainExpand = (rangeMax - rangeMin) / (2 * halfRange);
                        factor /= domainExpand;

                        rangeMin = ax.l2r(rangeMin);
                        rangeMax = ax.l2r(rangeMax);
                        ax.range = ax._input.range = (rl0 < rl1) ?
                            [rangeMin, rangeMax] : [rangeMax, rangeMin];
                    }

                    updateDomain(ax, factor);
                }
            }
        }
    }
};

// For use before autoranging, check if this axis was previously constrained
// by domain but no longer is
exports.clean = function clean(gd, ax) {
    if(ax._inputDomain) {
        var isConstrained = false;
        var axId = ax._id;
        var constraintGroups = gd._fullLayout._axisConstraintGroups;
        for(var j = 0; j < constraintGroups.length; j++) {
            if(constraintGroups[j][axId]) {
                isConstrained = true;
                break;
            }
        }
        if(!isConstrained || ax.constrain !== 'domain') {
            ax._input.domain = ax.domain = ax._inputDomain;
            delete ax._inputDomain;
        }
    }
};

function updateDomain(ax, factor) {
    var inputDomain = ax._inputDomain;
    var centerFraction = FROM_BL[ax.constraintoward];
    var center = inputDomain[0] + (inputDomain[1] - inputDomain[0]) * centerFraction;

    ax.domain = ax._input.domain = [
        center + (inputDomain[0] - center) / factor,
        center + (inputDomain[1] - center) / factor
    ];
    ax.setScale();
}
