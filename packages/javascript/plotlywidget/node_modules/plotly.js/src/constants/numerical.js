/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';


module.exports = {
    /**
     * Standardize all missing data in calcdata to use undefined
     * never null or NaN.
     * That way we can use !==undefined, or !== BADNUM,
     * to test for real data
     */
    BADNUM: undefined,

    /*
     * Limit certain operations to well below floating point max value
     * to avoid glitches: Make sure that even when you multiply it by the
     * number of pixels on a giant screen it still works
     */
    FP_SAFE: Number.MAX_VALUE / 10000,

    /*
     * conversion of date units to milliseconds
     * year and month constants are marked "AVG"
     * to remind us that not all years and months
     * have the same length
     */
    ONEAVGYEAR: 31557600000, // 365.25 days
    ONEAVGMONTH: 2629800000, // 1/12 of ONEAVGYEAR
    ONEDAY: 86400000,
    ONEHOUR: 3600000,
    ONEMIN: 60000,
    ONESEC: 1000,

    /*
     * For fast conversion btwn world calendars and epoch ms, the Julian Day Number
     * of the unix epoch. From calendars.instance().newDate(1970, 1, 1).toJD()
     */
    EPOCHJD: 2440587.5,

    /*
     * Are two values nearly equal? Compare to 1PPM
     */
    ALMOST_EQUAL: 1 - 1e-6,

    /*
     * If we're asked to clip a non-positive log value, how far off-screen
     * do we put it?
     */
    LOG_CLIP: 10,

    /*
     * not a number, but for displaying numbers: the "minus sign" symbol is
     * wider than the regular ascii dash "-"
     */
    MINUS_SIGN: '\u2212'
};
