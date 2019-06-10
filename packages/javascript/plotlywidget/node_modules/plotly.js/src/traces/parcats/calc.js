/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

// Requirements
// ============
var wrap = require('../../lib/gup').wrap;
var hasColorscale = require('../../components/colorscale/helpers').hasColorscale;
var colorscaleCalc = require('../../components/colorscale/calc');
var filterUnique = require('../../lib/filter_unique.js');
var Drawing = require('../../components/drawing');
var Lib = require('../../lib');

/**
 * Create a wrapped ParcatsModel object from trace
 *
 * Note: trace defaults have already been applied
 * @param {Object} gd
 * @param {Object} trace
 * @return {Array.<ParcatsModel>}
 */
module.exports = function calc(gd, trace) {
    var visibleDims = Lib.filterVisible(trace.dimensions);

    if(visibleDims.length === 0) return [];

    var uniqueInfoDims = visibleDims.map(function(dim) {
        var categoryValues;
        if(dim.categoryorder === 'trace') {
            // Use order of first occurrence in trace
            categoryValues = null;
        } else if(dim.categoryorder === 'array') {
            // Use categories specified in `categoryarray` first,
            // then add extra to the end in trace order
            categoryValues = dim.categoryarray;
        } else {
            // Get all categories up front so we can order them
            // Should we check for numbers as sort numerically?
            categoryValues = filterUnique(dim.values).sort();
            if(dim.categoryorder === 'category descending') {
                categoryValues = categoryValues.reverse();
            }
        }
        return getUniqueInfo(dim.values, categoryValues);
    });

    var counts,
        count,
        totalCount;
    if(Lib.isArrayOrTypedArray(trace.counts)) {
        counts = trace.counts;
    } else {
        counts = [trace.counts];
    }

    validateDimensionDisplayInds(visibleDims);

    visibleDims.forEach(function(dim, dimInd) {
        validateCategoryProperties(dim, uniqueInfoDims[dimInd]);
    });

    // Handle path colors
    // ------------------
    var line = trace.line;
    var markerColorscale;

    // Process colorscale
    if(line) {
        if(hasColorscale(trace, 'line')) {
            colorscaleCalc(gd, trace, {
                vals: trace.line.color,
                containerStr: 'line',
                cLetter: 'c'
            });
        }
        markerColorscale = Drawing.tryColorscale(line);
    } else {
        markerColorscale = Lib.identity;
    }

    // Build color generation function
    function getMarkerColorInfo(index) {
        var value;
        if(Lib.isArrayOrTypedArray(line.color)) {
            value = line.color[index % line.color.length];
        } else {
            value = line.color;
        }

        return {color: markerColorscale(value), rawColor: value};
    }

    // Number of values and counts
    // ---------------------------
    var numValues = visibleDims[0].values.length;

    // Build path info
    // ---------------
    // Mapping from category inds to PathModel objects
    var pathModels = {};

    // Category inds array for each dimension
    var categoryIndsDims = uniqueInfoDims.map(function(di) {return di.inds;});

    // Initialize total count
    totalCount = 0;
    var valueInd;
    var d;

    for(valueInd = 0; valueInd < numValues; valueInd++) {
        // Category inds for this input value across dimensions
        var categoryIndsPath = [];
        for(d = 0; d < categoryIndsDims.length; d++) {
            categoryIndsPath.push(categoryIndsDims[d][valueInd]);
        }

        // Count
        count = counts[valueInd % counts.length];

        // Update total count
        totalCount += count;

        // Path color
        var pathColorInfo = getMarkerColorInfo(valueInd);

        // path key
        var pathKey = categoryIndsPath + '-' + pathColorInfo.rawColor;

        // Create / Update PathModel
        if(pathModels[pathKey] === undefined) {
            pathModels[pathKey] = createPathModel(categoryIndsPath,
                pathColorInfo.color,
                pathColorInfo.rawColor);
        }
        updatePathModel(pathModels[pathKey], valueInd, count);
    }

    var dimensionModels = visibleDims.map(function(di, i) {
        return createDimensionModel(i, di._index, di._displayindex, di.label, totalCount);
    });


    for(valueInd = 0; valueInd < numValues; valueInd++) {
        count = counts[valueInd % counts.length];

        for(d = 0; d < dimensionModels.length; d++) {
            var containerInd = dimensionModels[d].containerInd;
            var catInd = uniqueInfoDims[d].inds[valueInd];
            var cats = dimensionModels[d].categories;

            if(cats[catInd] === undefined) {
                var catValue = trace.dimensions[containerInd]._categoryarray[catInd];
                var catLabel = trace.dimensions[containerInd]._ticktext[catInd];
                cats[catInd] = createCategoryModel(d, catInd, catValue, catLabel);
            }

            updateCategoryModel(cats[catInd], valueInd, count);
        }
    }

    // Compute unique
    return wrap(createParcatsModel(dimensionModels, pathModels, totalCount));
};

// Models
// ======

// Parcats Model
// -------------
/**
 * @typedef {Object} ParcatsModel
 *  Object containing calculated information about a parcats trace
 *
 * @property {Array.<DimensionModel>} dimensions
 *  Array of dimension models
 * @property {Object.<string,PathModel>} paths
 *  Dictionary from category inds string (e.g. "1,2,1,1") to path model
 * @property {Number} maxCats
 *  The maximum number of categories of any dimension in the diagram
 * @property {Number} count
 *  Total number of input values
 * @property {Object} trace
 */

/**
 * Create and new ParcatsModel object
 * @param {Array.<DimensionModel>} dimensions
 * @param {Object.<string,PathModel>} paths
 * @param {Number} count
 * @return {ParcatsModel}
 */
function createParcatsModel(dimensions, paths, count) {
    var maxCats = dimensions
        .map(function(d) {return d.categories.length;})
        .reduce(function(v1, v2) {return Math.max(v1, v2);});
    return {dimensions: dimensions, paths: paths, trace: undefined, maxCats: maxCats, count: count};
}

// Dimension Model
// ---------------
/**
 * @typedef {Object} DimensionModel
 *  Object containing calculated information about a single dimension
 *
 * @property {Number} dimensionInd
 *  The index of this dimension among the *visible* dimensions
 * @property {Number} containerInd
 *  The index of this dimension in the original dimensions container,
 *  irrespective of dimension visibility
 * @property {Number} displayInd
 *  The display index of this dimension (where 0 is the left most dimension)
 * @property {String} dimensionLabel
 *  The label of this dimension
 * @property {Number} count
 *  Total number of input values
 * @property {Array.<CategoryModel>} categories
 * @property {Number|null} dragX
 *  The x position of dimension that is currently being dragged. null if not being dragged
 */

/**
 * Create and new DimensionModel object with an empty categories array
 * @param {Number} dimensionInd
 * @param {Number} containerInd
 * @param {Number} displayInd
 * @param {String} dimensionLabel
 * @param {Number} count
 *  Total number of input values
 * @return {DimensionModel}
 */
function createDimensionModel(dimensionInd, containerInd, displayInd, dimensionLabel, count) {
    return {
        dimensionInd: dimensionInd,
        containerInd: containerInd,
        displayInd: displayInd,
        dimensionLabel: dimensionLabel,
        count: count,
        categories: [],
        dragX: null
    };
}

// Category Model
// --------------
/**
 * @typedef {Object} CategoryModel
 *  Object containing calculated information about a single category.
 *
 * @property {Number} dimensionInd
 *  The index of this categories dimension
 * @property {Number} categoryInd
 *  The index of this category
 * @property {Number} displayInd
 *  The display index of this category (where 0 is the topmost category)
 * @property {String} categoryLabel
 *  The name of this category
 * @property categoryValue: Raw value of the category
 * @property {Array} valueInds
 *  Array of indices (into the original value array) of all samples in this category
 * @property {Number} count
 *  The number of elements from the original array in this path
 * @property {Number|null} dragY
 *  The y position of category that is currently being dragged. null if not being dragged
 */

/**
 * Create and return a new CategoryModel object
 * @param {Number} dimensionInd
 * @param {Number} categoryInd
 *  The display index of this category (where 0 is the topmost category)
 * @param {String} categoryValue
 * @param {String} categoryLabel
 * @return {CategoryModel}
 */
function createCategoryModel(dimensionInd, categoryInd, categoryValue, categoryLabel) {
    return {
        dimensionInd: dimensionInd,
        categoryInd: categoryInd,
        categoryValue: categoryValue,
        displayInd: categoryInd,
        categoryLabel: categoryLabel,
        valueInds: [],
        count: 0,
        dragY: null
    };
}

/**
 * Update a CategoryModel object with a new value index
 * Note: The calling parameter is modified in place.
 *
 * @param {CategoryModel} categoryModel
 * @param {Number} valueInd
 * @param {Number} count
 */
function updateCategoryModel(categoryModel, valueInd, count) {
    categoryModel.valueInds.push(valueInd);
    categoryModel.count += count;
}


// Path Model
// ----------
/**
 * @typedef {Object} PathModel
 *  Object containing calculated information about the samples in a path.
 *
 * @property {Array} categoryInds
 *  Array of category indices for each dimension (length `numDimensions`)
 * @param {String} pathColor
 *  Color of this path. (Note: Any colorscaling has already taken place)
 * @property {Array} valueInds
 *  Array of indices (into the original value array) of all samples in this path
 * @property {Number} count
 *  The number of elements from the original array in this path
 * @property {String} color
 *  The path's color (ass CSS color string)
 * @property rawColor
 *  The raw color value specified by the user. May be a CSS color string or a Number
 */

/**
 * Create and return a new PathModel object
 * @param {Array} categoryInds
 * @param color
 * @param rawColor
 * @return {PathModel}
 */
function createPathModel(categoryInds, color, rawColor) {
    return {
        categoryInds: categoryInds,
        color: color,
        rawColor: rawColor,
        valueInds: [],
        count: 0
    };
}

/**
 * Update a PathModel object with a new value index
 * Note: The calling parameter is modified in place.
 *
 * @param {PathModel} pathModel
 * @param {Number} valueInd
 * @param {Number} count
 */
function updatePathModel(pathModel, valueInd, count) {
    pathModel.valueInds.push(valueInd);
    pathModel.count += count;
}

// Unique calculations
// ===================
/**
 * @typedef {Object} UniqueInfo
 *  Object containing information about the unique values of an input array
 *
 * @property {Array} uniqueValues
 *  The unique values in the input array
 * @property {Array} uniqueCounts
 *  The number of times each entry in uniqueValues occurs in input array.
 *  This has the same length as `uniqueValues`
 * @property {Array} inds
 *  Indices into uniqueValues that would reproduce original input array
 */

/**
 * Compute unique value information for an array
 *
 * IMPORTANT: Note that values are considered unique
 * if their string representations are unique.
 *
 * @param {Array} values
 * @param {Array|undefined} uniqueValues
 *  Array of expected unique values. The uniqueValues property of the resulting UniqueInfo object will begin with
 *  these entries. Entries are included even if there are zero occurrences in the values array. Entries found in
 *  the values array that are not present in uniqueValues will be included at the end of the array in the
 *  UniqueInfo object.
 * @return {UniqueInfo}
 */
function getUniqueInfo(values, uniqueValues) {
    // Initialize uniqueValues if not specified
    if(uniqueValues === undefined || uniqueValues === null) {
        uniqueValues = [];
    } else {
        // Shallow copy so append below doesn't alter input array
        uniqueValues = uniqueValues.map(function(e) {return e;});
    }

    // Initialize Variables
    var uniqueValueCounts = {};
    var uniqueValueInds = {};
    var inds = [];

    // Initialize uniqueValueCounts and
    uniqueValues.forEach(function(uniqueVal, valInd) {
        uniqueValueCounts[uniqueVal] = 0;
        uniqueValueInds[uniqueVal] = valInd;
    });

    // Compute the necessary unique info in a single pass
    for(var i = 0; i < values.length; i++) {
        var item = values[i];
        var itemInd;

        if(uniqueValueCounts[item] === undefined) {
            // This item has a previously unseen value
            uniqueValueCounts[item] = 1;
            itemInd = uniqueValues.push(item) - 1;
            uniqueValueInds[item] = itemInd;
        } else {
            // Increment count for this item
            uniqueValueCounts[item]++;
            itemInd = uniqueValueInds[item];
        }
        inds.push(itemInd);
    }

    // Build UniqueInfo
    var uniqueCounts = uniqueValues.map(function(v) { return uniqueValueCounts[v]; });

    return {
        uniqueValues: uniqueValues,
        uniqueCounts: uniqueCounts,
        inds: inds
    };
}


/**
 * Validate the requested display order for the dimensions.
 * If the display order is a permutation of 0 through dimensions.length - 1, link to _displayindex
 * Otherwise, replace the display order with the dimension order
 * @param {Object} trace
 */
function validateDimensionDisplayInds(visibleDims) {
    var displayInds = visibleDims.map(function(d) { return d.displayindex; });
    var i;

    if(isRangePermutation(displayInds)) {
        for(i = 0; i < visibleDims.length; i++) {
            visibleDims[i]._displayindex = visibleDims[i].displayindex;
        }
    } else {
        for(i = 0; i < visibleDims.length; i++) {
            visibleDims[i]._displayindex = i;
        }
    }
}


/**
 * Update category properties based on the unique values found for this dimension
 * @param {Object} dim
 * @param {UniqueInfo} uniqueInfoDim
 */
function validateCategoryProperties(dim, uniqueInfoDim) {
    // Update categoryarray
    dim._categoryarray = uniqueInfoDim.uniqueValues;

    // Handle ticktext
    if(dim.ticktext === null || dim.ticktext === undefined) {
        dim._ticktext = [];
    } else {
        // Shallow copy to avoid modifying input array
        dim._ticktext = dim.ticktext.slice();
    }

    // Extend ticktext with elements from uniqueInfoDim.uniqueValues
    for(var i = dim._ticktext.length; i < uniqueInfoDim.uniqueValues.length; i++) {
        dim._ticktext.push(uniqueInfoDim.uniqueValues[i]);
    }
}

/**
 * Determine whether an array contains a permutation of the integers from 0 to the array's length - 1
 * @param {Array} inds
 * @return {boolean}
 */
function isRangePermutation(inds) {
    var indsSpecified = new Array(inds.length);

    for(var i = 0; i < inds.length; i++) {
        // Check for out of bounds
        if(inds[i] < 0 || inds[i] >= inds.length) {
            return false;
        }

        // Check for collisions with already specified index
        if(indsSpecified[inds[i]] !== undefined) {
            return false;
        }

        indsSpecified[inds[i]] = true;
    }

    // Nothing out of bounds and no collisions. We have a permutation
    return true;
}
