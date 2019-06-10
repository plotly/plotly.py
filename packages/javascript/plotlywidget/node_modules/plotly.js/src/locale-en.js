/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {
    moduleType: 'locale',
    name: 'en',
    dictionary: {
        'Click to enter Colorscale title': 'Click to enter Colourscale title'
    },
    format: {
        days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        shortDays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        months: [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ],
        shortMonths: [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ],
        periods: ['AM', 'PM'],
        dateTime: '%a %b %e %X %Y',
        date: '%d/%m/%Y',
        time: '%H:%M:%S',
        decimal: '.',
        thousands: ',',
        grouping: [3],
        currency: ['$', ''],
        year: '%Y',
        month: '%b %Y',
        dayMonth: '%b %-d',
        dayMonthYear: '%b %-d, %Y'
    }
};
