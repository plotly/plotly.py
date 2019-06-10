/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = function makeBinAttrs(axLetter, match) {
    return {
        start: {
            valType: 'any', // for date axes
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the starting value for the', axLetter,
                'axis bins. Defaults to the minimum data value,',
                'shifted down if necessary to make nice round values',
                'and to remove ambiguous bin edges. For example, if most of the',
                'data is integers we shift the bin edges 0.5 down, so a `size`',
                'of 5 would have a default `start` of -0.5, so it is clear',
                'that 0-4 are in the first bin, 5-9 in the second, but',
                'continuous data gets a start of 0 and bins [0,5), [5,10) etc.',
                'Dates behave similarly, and `start` should be a date string.',
                'For category data, `start` is based on the category serial',
                'numbers, and defaults to -0.5.',
                (match ? (
                    'If multiple non-overlaying histograms share a subplot, ' +
                    'the first explicit `start` is used exactly and all others ' +
                    'are shifted down (if necessary) to differ from that one ' +
                    'by an integer number of bins.'
                ) : '')
            ].join(' ')
        },
        end: {
            valType: 'any', // for date axes
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the end value for the', axLetter,
                'axis bins. The last bin may not end exactly at this value,',
                'we increment the bin edge by `size` from `start` until we',
                'reach or exceed `end`. Defaults to the maximum data value.',
                'Like `start`, for dates use a date string, and for category',
                'data `end` is based on the category serial numbers.'
            ].join(' ')
        },
        size: {
            valType: 'any', // for date axes
            role: 'style',
            editType: 'calc',
            description: [
                'Sets the size of each', axLetter, 'axis bin.',
                'Default behavior: If `nbins' + axLetter + '` is 0 or omitted,',
                'we choose a nice round bin size such that the number of bins',
                'is about the same as the typical number of samples in each bin.',
                'If `nbins' + axLetter + '` is provided, we choose a nice round',
                'bin size giving no more than that many bins.',
                'For date data, use milliseconds or *M<n>* for months, as in',
                '`axis.dtick`. For category data, the number of categories to',
                'bin together (always defaults to 1).',
                (match ? (
                    'If multiple non-overlaying histograms share a subplot, ' +
                    'the first explicit `size` is used and all others discarded. ' +
                    'If no `size` is provided,the sample data from all traces ' +
                    'is combined to determine `size` as described above.'
                ) : '')
            ].join(' ')
        },
        editType: 'calc'
    };
};
