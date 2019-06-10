/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var handleSubplotDefaults = require('../subplot_defaults');
var constants = require('./constants');
var layoutAttributes = require('./layout_attributes');

var axesNames = constants.axesNames;

module.exports = function supplyLayoutDefaults(layoutIn, layoutOut, fullData) {
    handleSubplotDefaults(layoutIn, layoutOut, fullData, {
        type: 'geo',
        attributes: layoutAttributes,
        handleDefaults: handleGeoDefaults,
        partition: 'y'
    });
};

function handleGeoDefaults(geoLayoutIn, geoLayoutOut, coerce) {
    var show;

    var resolution = coerce('resolution');
    var scope = coerce('scope');
    var scopeParams = constants.scopeDefaults[scope];

    var projType = coerce('projection.type', scopeParams.projType);
    var isAlbersUsa = geoLayoutOut._isAlbersUsa = projType === 'albers usa';

    // no other scopes are allowed for 'albers usa' projection
    if(isAlbersUsa) scope = geoLayoutOut.scope = 'usa';

    var isScoped = geoLayoutOut._isScoped = (scope !== 'world');
    var isConic = geoLayoutOut._isConic = projType.indexOf('conic') !== -1;
    geoLayoutOut._isClipped = !!constants.lonaxisSpan[projType];

    for(var i = 0; i < axesNames.length; i++) {
        var axisName = axesNames[i];
        var dtickDflt = [30, 10][i];
        var rangeDflt;

        if(isScoped) {
            rangeDflt = scopeParams[axisName + 'Range'];
        } else {
            var dfltSpans = constants[axisName + 'Span'];
            var hSpan = (dfltSpans[projType] || dfltSpans['*']) / 2;
            var rot = coerce(
                'projection.rotation.' + axisName.substr(0, 3),
                scopeParams.projRotate[i]
            );
            rangeDflt = [rot - hSpan, rot + hSpan];
        }

        coerce(axisName + '.range', rangeDflt);
        coerce(axisName + '.tick0');
        coerce(axisName + '.dtick', dtickDflt);

        show = coerce(axisName + '.showgrid');
        if(show) {
            coerce(axisName + '.gridcolor');
            coerce(axisName + '.gridwidth');
        }
    }

    var lonRange = geoLayoutOut.lonaxis.range;
    var latRange = geoLayoutOut.lataxis.range;

    // to cross antimeridian w/o ambiguity
    var lon0 = lonRange[0];
    var lon1 = lonRange[1];
    if(lon0 > 0 && lon1 < 0) lon1 += 360;

    var centerLon = (lon0 + lon1) / 2;
    var projLon;

    if(!isAlbersUsa) {
        var dfltProjRotate = isScoped ? scopeParams.projRotate : [centerLon, 0, 0];

        projLon = coerce('projection.rotation.lon', dfltProjRotate[0]);
        coerce('projection.rotation.lat', dfltProjRotate[1]);
        coerce('projection.rotation.roll', dfltProjRotate[2]);

        show = coerce('showcoastlines', !isScoped);
        if(show) {
            coerce('coastlinecolor');
            coerce('coastlinewidth');
        }

        show = coerce('showocean');
        if(show) coerce('oceancolor');
    }

    var centerLonDflt;
    var centerLatDflt;

    if(isAlbersUsa) {
        // 'albers usa' does not have a 'center',
        // these values were found using via:
        //   projection.invert([geoLayout.center.lon, geoLayoutIn.center.lat])
        centerLonDflt = -96.6;
        centerLatDflt = 38.7;
    } else {
        centerLonDflt = isScoped ? centerLon : projLon;
        centerLatDflt = (latRange[0] + latRange[1]) / 2;
    }

    coerce('center.lon', centerLonDflt);
    coerce('center.lat', centerLatDflt);

    if(isConic) {
        var dfltProjParallels = scopeParams.projParallels || [0, 60];
        coerce('projection.parallels', dfltProjParallels);
    }

    coerce('projection.scale');

    show = coerce('showland');
    if(show) coerce('landcolor');

    show = coerce('showlakes');
    if(show) coerce('lakecolor');

    show = coerce('showrivers');
    if(show) {
        coerce('rivercolor');
        coerce('riverwidth');
    }

    show = coerce('showcountries', isScoped && scope !== 'usa');
    if(show) {
        coerce('countrycolor');
        coerce('countrywidth');
    }

    if(scope === 'usa' || (scope === 'north america' && resolution === 50)) {
        // Only works for:
        //   USA states at 110m
        //   USA states + Canada provinces at 50m
        coerce('showsubunits', true);
        coerce('subunitcolor');
        coerce('subunitwidth');
    }

    if(!isScoped) {
        // Does not work in non-world scopes
        show = coerce('showframe', true);
        if(show) {
            coerce('framecolor');
            coerce('framewidth');
        }
    }

    coerce('bgcolor');
}
