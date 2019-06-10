/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var countryRegex = require('country-regex');
var Lib = require('../lib');

// make list of all country iso3 ids from at runtime
var countryIds = Object.keys(countryRegex);

var locationmodeToIdFinder = {
    'ISO-3': Lib.identity,
    'USA-states': Lib.identity,
    'country names': countryNameToISO3
};

function countryNameToISO3(countryName) {
    for(var i = 0; i < countryIds.length; i++) {
        var iso3 = countryIds[i];
        var regex = new RegExp(countryRegex[iso3]);

        if(regex.test(countryName.trim().toLowerCase())) return iso3;
    }

    Lib.log('Unrecognized country name: ' + countryName + '.');

    return false;
}

function locationToFeature(locationmode, location, features) {
    if(!location || typeof location !== 'string') return false;

    var locationId = locationmodeToIdFinder[locationmode](location);
    var filteredFeatures;
    var f, i;

    if(locationId) {
        if(locationmode === 'USA-states') {
            // Filter out features out in USA
            //
            // This is important as the Natural Earth files
            // include state/provinces from USA, Canada, Australia and Brazil
            // which have some overlay in their two-letter ids. For example,
            // 'WA' is used for both Washington state and Western Australia.
            filteredFeatures = [];
            for(i = 0; i < features.length; i++) {
                f = features[i];
                if(f.properties && f.properties.gu && f.properties.gu === 'USA') {
                    filteredFeatures.push(f);
                }
            }
        } else {
            filteredFeatures = features;
        }

        for(i = 0; i < filteredFeatures.length; i++) {
            f = filteredFeatures[i];
            if(f.id === locationId) return f;
        }

        Lib.log([
            'Location with id', locationId,
            'does not have a matching topojson feature at this resolution.'
        ].join(' '));
    }

    return false;
}

module.exports = {
    locationToFeature: locationToFeature
};
