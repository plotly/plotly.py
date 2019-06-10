/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

module.exports = {

    // attribute container name
    name: 'rangeslider',

    // class names

    containerClassName: 'rangeslider-container',
    bgClassName: 'rangeslider-bg',
    rangePlotClassName: 'rangeslider-rangeplot',

    maskMinClassName: 'rangeslider-mask-min',
    maskMaxClassName: 'rangeslider-mask-max',
    slideBoxClassName: 'rangeslider-slidebox',

    grabberMinClassName: 'rangeslider-grabber-min',
    grabAreaMinClassName: 'rangeslider-grabarea-min',
    handleMinClassName: 'rangeslider-handle-min',

    grabberMaxClassName: 'rangeslider-grabber-max',
    grabAreaMaxClassName: 'rangeslider-grabarea-max',
    handleMaxClassName: 'rangeslider-handle-max',

    maskMinOppAxisClassName: 'rangeslider-mask-min-opp-axis',
    maskMaxOppAxisClassName: 'rangeslider-mask-max-opp-axis',

    // style constants

    maskColor: 'rgba(0,0,0,0.4)',
    maskOppAxisColor: 'rgba(0,0,0,0.2)',

    slideBoxFill: 'transparent',
    slideBoxCursor: 'ew-resize',

    grabAreaFill: 'transparent',
    grabAreaCursor: 'col-resize',
    grabAreaWidth: 10,

    handleWidth: 4,
    handleRadius: 1,
    handleStrokeWidth: 1,

    extraPad: 15
};
