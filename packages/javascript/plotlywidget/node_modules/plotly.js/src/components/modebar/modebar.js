/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');
var isNumeric = require('fast-isnumeric');

var Lib = require('../../lib');
var Icons = require('../../../build/ploticon');
var Parser = new DOMParser();

/**
 * UI controller for interactive plots
 * @Class
 * @Param {object} opts
 * @Param {object} opts.buttons    nested arrays of grouped buttons config objects
 * @Param {object} opts.container  container div to append modeBar
 * @Param {object} opts.graphInfo  primary plot object containing data and layout
 */
function ModeBar(opts) {
    this.container = opts.container;
    this.element = document.createElement('div');

    this.update(opts.graphInfo, opts.buttons);

    this.container.appendChild(this.element);
}

var proto = ModeBar.prototype;

/**
 * Update modeBar (buttons and logo)
 *
 * @param {object} graphInfo  primary plot object containing data and layout
 * @param {array of arrays} buttons nested arrays of grouped buttons to initialize
 *
 */
proto.update = function(graphInfo, buttons) {
    this.graphInfo = graphInfo;

    var context = this.graphInfo._context;
    var fullLayout = this.graphInfo._fullLayout;
    var modeBarId = 'modebar-' + fullLayout._uid;

    this.element.setAttribute('id', modeBarId);
    this._uid = modeBarId;

    this.element.className = 'modebar';
    if(context.displayModeBar === 'hover') this.element.className += ' modebar--hover ease-bg';

    if(fullLayout.modebar.orientation === 'v') {
        this.element.className += ' vertical';
        buttons = buttons.reverse();
    }

    var style = fullLayout.modebar;
    var bgSelector = context.displayModeBar === 'hover' ? '.js-plotly-plot .plotly:hover ' : '';

    Lib.deleteRelatedStyleRule(modeBarId);
    Lib.addRelatedStyleRule(modeBarId, bgSelector + '#' + modeBarId + ' .modebar-group', 'background-color: ' + style.bgcolor);
    Lib.addRelatedStyleRule(modeBarId, '#' + modeBarId + ' .modebar-btn .icon path', 'fill: ' + style.color);
    Lib.addRelatedStyleRule(modeBarId, '#' + modeBarId + ' .modebar-btn:hover .icon path', 'fill: ' + style.activecolor);
    Lib.addRelatedStyleRule(modeBarId, '#' + modeBarId + ' .modebar-btn.active .icon path', 'fill: ' + style.activecolor);

    // if buttons or logo have changed, redraw modebar interior
    var needsNewButtons = !this.hasButtons(buttons);
    var needsNewLogo = (this.hasLogo !== context.displaylogo);
    var needsNewLocale = (this.locale !== context.locale);

    this.locale = context.locale;

    if(needsNewButtons || needsNewLogo || needsNewLocale) {
        this.removeAllButtons();

        this.updateButtons(buttons);

        if(context.watermark || context.displaylogo) {
            var logoGroup = this.getLogo();
            if(context.watermark) {
                logoGroup.className = logoGroup.className + ' watermark';
            }

            if(fullLayout.modebar.orientation === 'v') {
                this.element.insertBefore(logoGroup, this.element.childNodes[0]);
            } else {
                this.element.appendChild(logoGroup);
            }

            this.hasLogo = true;
        }
    }

    this.updateActiveButton();
};

proto.updateButtons = function(buttons) {
    var _this = this;

    this.buttons = buttons;
    this.buttonElements = [];
    this.buttonsNames = [];

    this.buttons.forEach(function(buttonGroup) {
        var group = _this.createGroup();

        buttonGroup.forEach(function(buttonConfig) {
            var buttonName = buttonConfig.name;
            if(!buttonName) {
                throw new Error('must provide button \'name\' in button config');
            }
            if(_this.buttonsNames.indexOf(buttonName) !== -1) {
                throw new Error('button name \'' + buttonName + '\' is taken');
            }
            _this.buttonsNames.push(buttonName);

            var button = _this.createButton(buttonConfig);
            _this.buttonElements.push(button);
            group.appendChild(button);
        });

        _this.element.appendChild(group);
    });
};

/**
 * Empty div for containing a group of buttons
 * @Return {HTMLelement}
 */
proto.createGroup = function() {
    var group = document.createElement('div');
    group.className = 'modebar-group';
    return group;
};

/**
 * Create a new button div and set constant and configurable attributes
 * @Param {object} config (see ./buttons.js for more info)
 * @Return {HTMLelement}
 */
proto.createButton = function(config) {
    var _this = this;
    var button = document.createElement('a');

    button.setAttribute('rel', 'tooltip');
    button.className = 'modebar-btn';

    var title = config.title;
    if(title === undefined) title = config.name;
    // for localization: allow title to be a callable that takes gd as arg
    else if(typeof title === 'function') title = title(this.graphInfo);

    if(title || title === 0) button.setAttribute('data-title', title);

    if(config.attr !== undefined) button.setAttribute('data-attr', config.attr);

    var val = config.val;
    if(val !== undefined) {
        if(typeof val === 'function') val = val(this.graphInfo);
        button.setAttribute('data-val', val);
    }

    var click = config.click;
    if(typeof click !== 'function') {
        throw new Error('must provide button \'click\' function in button config');
    } else {
        button.addEventListener('click', function(ev) {
            config.click(_this.graphInfo, ev);

            // only needed for 'hoverClosestGeo' which does not call relayout
            _this.updateActiveButton(ev.currentTarget);
        });
    }

    button.setAttribute('data-toggle', config.toggle || false);
    if(config.toggle) d3.select(button).classed('active', true);

    var icon = config.icon;
    if(typeof icon === 'function') {
        button.appendChild(icon());
    } else {
        button.appendChild(this.createIcon(icon || Icons.question));
    }
    button.setAttribute('data-gravity', config.gravity || 'n');

    return button;
};

/**
 * Add an icon to a button
 * @Param {object} thisIcon
 * @Param {number} thisIcon.width
 * @Param {string} thisIcon.path
 * @Param {string} thisIcon.color
 * @Return {HTMLelement}
 */
proto.createIcon = function(thisIcon) {
    var iconHeight = isNumeric(thisIcon.height) ?
        Number(thisIcon.height) :
        thisIcon.ascent - thisIcon.descent;
    var svgNS = 'http://www.w3.org/2000/svg';
    var icon;

    if(thisIcon.path) {
        icon = document.createElementNS(svgNS, 'svg');
        icon.setAttribute('viewBox', [0, 0, thisIcon.width, iconHeight].join(' '));
        icon.setAttribute('class', 'icon');

        var path = document.createElementNS(svgNS, 'path');
        path.setAttribute('d', thisIcon.path);

        if(thisIcon.transform) {
            path.setAttribute('transform', thisIcon.transform);
        } else if(thisIcon.ascent !== undefined) {
            // Legacy icon transform calculation
            path.setAttribute('transform', 'matrix(1 0 0 -1 0 ' + thisIcon.ascent + ')');
        }

        icon.appendChild(path);
    }

    if(thisIcon.svg) {
        var svgDoc = Parser.parseFromString(thisIcon.svg, 'application/xml');
        icon = svgDoc.childNodes[0];
    }

    icon.setAttribute('height', '1em');
    icon.setAttribute('width', '1em');

    return icon;
};

/**
 * Updates active button with attribute specified in layout
 * @Param {object} graphInfo plot object containing data and layout
 * @Return {HTMLelement}
 */
proto.updateActiveButton = function(buttonClicked) {
    var fullLayout = this.graphInfo._fullLayout;
    var dataAttrClicked = (buttonClicked !== undefined) ?
        buttonClicked.getAttribute('data-attr') :
        null;

    this.buttonElements.forEach(function(button) {
        var thisval = button.getAttribute('data-val') || true;
        var dataAttr = button.getAttribute('data-attr');
        var isToggleButton = (button.getAttribute('data-toggle') === 'true');
        var button3 = d3.select(button);

        // Use 'data-toggle' and 'buttonClicked' to toggle buttons
        // that have no one-to-one equivalent in fullLayout
        if(isToggleButton) {
            if(dataAttr === dataAttrClicked) {
                button3.classed('active', !button3.classed('active'));
            }
        } else {
            var val = (dataAttr === null) ?
                dataAttr :
                Lib.nestedProperty(fullLayout, dataAttr).get();

            button3.classed('active', val === thisval);
        }
    });
};

/**
 * Check if modeBar is configured as button configuration argument
 *
 * @Param {object} buttons 2d array of grouped button config objects
 * @Return {boolean}
 */
proto.hasButtons = function(buttons) {
    var currentButtons = this.buttons;

    if(!currentButtons) return false;

    if(buttons.length !== currentButtons.length) return false;

    for(var i = 0; i < buttons.length; ++i) {
        if(buttons[i].length !== currentButtons[i].length) return false;
        for(var j = 0; j < buttons[i].length; j++) {
            if(buttons[i][j].name !== currentButtons[i][j].name) return false;
        }
    }

    return true;
};

/**
 * @return {HTMLDivElement} The logo image wrapped in a group
 */
proto.getLogo = function() {
    var group = this.createGroup();
    var a = document.createElement('a');

    a.href = 'https://plot.ly/';
    a.target = '_blank';
    a.setAttribute('data-title', Lib._(this.graphInfo, 'Produced with Plotly'));
    a.className = 'modebar-btn plotlyjsicon modebar-btn--logo';

    a.appendChild(this.createIcon(Icons.newplotlylogo));

    group.appendChild(a);
    return group;
};

proto.removeAllButtons = function() {
    while(this.element.firstChild) {
        this.element.removeChild(this.element.firstChild);
    }

    this.hasLogo = false;
};

proto.destroy = function() {
    Lib.removeElement(this.container.querySelector('.modebar'));
    Lib.deleteRelatedStyleRule(this._uid);
};

function createModeBar(gd, buttons) {
    var fullLayout = gd._fullLayout;

    var modeBar = new ModeBar({
        graphInfo: gd,
        container: fullLayout._modebardiv.node(),
        buttons: buttons
    });

    if(fullLayout._privateplot) {
        d3.select(modeBar.element).append('span')
            .classed('badge-private float--left', true)
            .text('PRIVATE');
    }

    return modeBar;
}

module.exports = createModeBar;
