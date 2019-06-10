/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');

var Plots = require('../../plots/plots');
var Color = require('../color');
var Drawing = require('../drawing');
var Lib = require('../../lib');
var svgTextUtils = require('../../lib/svg_text_utils');
var arrayEditor = require('../../plot_api/plot_template').arrayEditor;

var LINE_SPACING = require('../../constants/alignment').LINE_SPACING;

var constants = require('./constants');
var ScrollBox = require('./scrollbox');

module.exports = function draw(gd) {
    var fullLayout = gd._fullLayout;
    var menuData = Lib.filterVisible(fullLayout[constants.name]);

    /* Update menu data is bound to the header-group.
     * The items in the header group are always present.
     *
     * Upon clicking on a header its corresponding button
     * data is bound to the button-group.
     *
     * We draw all headers in one group before all buttons
     * so that the buttons *always* appear above the headers.
     *
     * Note that only one set of buttons are visible at once.
     *
     * <g container />
     *
     *     <g header-group />
     *         <g item header />
     *         <text item header-arrow />
     *     <g header-group />
     *         <g item header />
     *         <text item header-arrow />
     *     ...
     *
     *     <g button-group />
     *         <g item button />
     *         <g item button />
     *         ...
     */

    function clearAutoMargin(menuOpts) {
        Plots.autoMargin(gd, autoMarginId(menuOpts));
    }

    // draw update menu container
    var menus = fullLayout._menulayer
        .selectAll('g.' + constants.containerClassName)
        .data(menuData.length > 0 ? [0] : []);

    menus.enter().append('g')
        .classed(constants.containerClassName, true)
        .style('cursor', 'pointer');

    menus.exit().each(function() {
        // Most components don't need to explicitly remove autoMargin, because
        // marginPushers does this - but updatemenu updates don't go through
        // a full replot so we need to explicitly remove it.
        // This is for removing *all* updatemenus, removing individuals is
        // handled below, in headerGroups.exit
        d3.select(this).selectAll('g.' + constants.headerGroupClassName)
            .each(clearAutoMargin);
    }).remove();

    // return early if no update menus are visible
    if(menuData.length === 0) return;

    // join header group
    var headerGroups = menus.selectAll('g.' + constants.headerGroupClassName)
        .data(menuData, keyFunction);

    headerGroups.enter().append('g')
        .classed(constants.headerGroupClassName, true);

    // draw dropdown button container
    var gButton = Lib.ensureSingle(menus, 'g', constants.dropdownButtonGroupClassName, function(s) {
        s.style('pointer-events', 'all');
    });

    // find dimensions before plotting anything (this mutates menuOpts)
    for(var i = 0; i < menuData.length; i++) {
        var menuOpts = menuData[i];
        findDimensions(gd, menuOpts);
    }

    // setup scrollbox
    var scrollBoxId = 'updatemenus' + fullLayout._uid;
    var scrollBox = new ScrollBox(gd, gButton, scrollBoxId);

    // remove exiting header, remove dropped buttons and reset margins
    if(headerGroups.enter().size()) {
        // make sure gButton is on top of all headers
        gButton.node().parentNode.appendChild(gButton.node());
        gButton.call(removeAllButtons);
    }

    headerGroups.exit().each(function(menuOpts) {
        gButton.call(removeAllButtons);
        clearAutoMargin(menuOpts);
    }).remove();

    // draw headers!
    headerGroups.each(function(menuOpts) {
        var gHeader = d3.select(this);

        var _gButton = menuOpts.type === 'dropdown' ? gButton : null;
        Plots.manageCommandObserver(gd, menuOpts, menuOpts.buttons, function(data) {
            setActive(gd, menuOpts, menuOpts.buttons[data.index], gHeader, _gButton, scrollBox, data.index, true);
        });

        if(menuOpts.type === 'dropdown') {
            drawHeader(gd, gHeader, gButton, scrollBox, menuOpts);

            // if this menu is active, update the dropdown container
            if(isActive(gButton, menuOpts)) {
                drawButtons(gd, gHeader, gButton, scrollBox, menuOpts);
            }
        } else {
            drawButtons(gd, gHeader, null, null, menuOpts);
        }
    });
};

// Note that '_index' is set at the default step,
// it corresponds to the menu index in the user layout update menu container.
// Because a menu can be set invisible,
// this is a more 'consistent' field than the index in the menuData.
function keyFunction(menuOpts) {
    return menuOpts._index;
}

function isFolded(gButton) {
    return +gButton.attr(constants.menuIndexAttrName) === -1;
}

function isActive(gButton, menuOpts) {
    return +gButton.attr(constants.menuIndexAttrName) === menuOpts._index;
}

function setActive(gd, menuOpts, buttonOpts, gHeader, gButton, scrollBox, buttonIndex, isSilentUpdate) {
    // update 'active' attribute in menuOpts
    menuOpts.active = buttonIndex;

    // due to templating, it's possible this slider doesn't even exist yet
    arrayEditor(gd.layout, constants.name, menuOpts)
        .applyUpdate('active', buttonIndex);

    if(menuOpts.type === 'buttons') {
        drawButtons(gd, gHeader, null, null, menuOpts);
    } else if(menuOpts.type === 'dropdown') {
        // fold up buttons and redraw header
        gButton.attr(constants.menuIndexAttrName, '-1');

        drawHeader(gd, gHeader, gButton, scrollBox, menuOpts);

        if(!isSilentUpdate) {
            drawButtons(gd, gHeader, gButton, scrollBox, menuOpts);
        }
    }
}

function drawHeader(gd, gHeader, gButton, scrollBox, menuOpts) {
    var header = Lib.ensureSingle(gHeader, 'g', constants.headerClassName, function(s) {
        s.style('pointer-events', 'all');
    });

    var dims = menuOpts._dims;
    var active = menuOpts.active;
    var headerOpts = menuOpts.buttons[active] || constants.blankHeaderOpts;
    var posOpts = { y: menuOpts.pad.t, yPad: 0, x: menuOpts.pad.l, xPad: 0, index: 0 };
    var positionOverrides = {
        width: dims.headerWidth,
        height: dims.headerHeight
    };

    header
        .call(drawItem, menuOpts, headerOpts, gd)
        .call(setItemPosition, menuOpts, posOpts, positionOverrides);

    // draw drop arrow at the right edge
    var arrow = Lib.ensureSingle(gHeader, 'text', constants.headerArrowClassName, function(s) {
        s.classed('user-select-none', true)
            .attr('text-anchor', 'end')
            .call(Drawing.font, menuOpts.font)
            .text(constants.arrowSymbol[menuOpts.direction]);
    });

    arrow.attr({
        x: dims.headerWidth - constants.arrowOffsetX + menuOpts.pad.l,
        y: dims.headerHeight / 2 + constants.textOffsetY + menuOpts.pad.t
    });

    header.on('click', function() {
        gButton.call(removeAllButtons,
            String(isActive(gButton, menuOpts) ? -1 : menuOpts._index)
        );

        drawButtons(gd, gHeader, gButton, scrollBox, menuOpts);
    });

    header.on('mouseover', function() {
        header.call(styleOnMouseOver);
    });

    header.on('mouseout', function() {
        header.call(styleOnMouseOut, menuOpts);
    });

    // translate header group
    Drawing.setTranslate(gHeader, dims.lx, dims.ly);
}

function drawButtons(gd, gHeader, gButton, scrollBox, menuOpts) {
    // If this is a set of buttons, set pointer events = all since we play
    // some minor games with which container is which in order to simplify
    // the drawing of *either* buttons or menus
    if(!gButton) {
        gButton = gHeader;
        gButton.attr('pointer-events', 'all');
    }

    var buttonData = (!isFolded(gButton) || menuOpts.type === 'buttons') ?
        menuOpts.buttons :
        [];

    var klass = menuOpts.type === 'dropdown' ? constants.dropdownButtonClassName : constants.buttonClassName;

    var buttons = gButton.selectAll('g.' + klass)
        .data(Lib.filterVisible(buttonData));

    var enter = buttons.enter().append('g')
        .classed(klass, true);

    var exit = buttons.exit();

    if(menuOpts.type === 'dropdown') {
        enter.attr('opacity', '0')
            .transition()
            .attr('opacity', '1');

        exit.transition()
            .attr('opacity', '0')
            .remove();
    } else {
        exit.remove();
    }

    var x0 = 0;
    var y0 = 0;
    var dims = menuOpts._dims;

    var isVertical = ['up', 'down'].indexOf(menuOpts.direction) !== -1;

    if(menuOpts.type === 'dropdown') {
        if(isVertical) {
            y0 = dims.headerHeight + constants.gapButtonHeader;
        } else {
            x0 = dims.headerWidth + constants.gapButtonHeader;
        }
    }

    if(menuOpts.type === 'dropdown' && menuOpts.direction === 'up') {
        y0 = -constants.gapButtonHeader + constants.gapButton - dims.openHeight;
    }

    if(menuOpts.type === 'dropdown' && menuOpts.direction === 'left') {
        x0 = -constants.gapButtonHeader + constants.gapButton - dims.openWidth;
    }

    var posOpts = {
        x: dims.lx + x0 + menuOpts.pad.l,
        y: dims.ly + y0 + menuOpts.pad.t,
        yPad: constants.gapButton,
        xPad: constants.gapButton,
        index: 0,
    };

    var scrollBoxPosition = {
        l: posOpts.x + menuOpts.borderwidth,
        t: posOpts.y + menuOpts.borderwidth
    };

    buttons.each(function(buttonOpts, buttonIndex) {
        var button = d3.select(this);

        button
            .call(drawItem, menuOpts, buttonOpts, gd)
            .call(setItemPosition, menuOpts, posOpts);

        button.on('click', function() {
            // skip `dragend` events
            if(d3.event.defaultPrevented) return;

            setActive(gd, menuOpts, buttonOpts, gHeader, gButton, scrollBox, buttonIndex);

            if(buttonOpts.execute) {
                Plots.executeAPICommand(gd, buttonOpts.method, buttonOpts.args);
            }

            gd.emit('plotly_buttonclicked', {menu: menuOpts, button: buttonOpts, active: menuOpts.active});
        });

        button.on('mouseover', function() {
            button.call(styleOnMouseOver);
        });

        button.on('mouseout', function() {
            button.call(styleOnMouseOut, menuOpts);
            buttons.call(styleButtons, menuOpts);
        });
    });

    buttons.call(styleButtons, menuOpts);

    if(isVertical) {
        scrollBoxPosition.w = Math.max(dims.openWidth, dims.headerWidth);
        scrollBoxPosition.h = posOpts.y - scrollBoxPosition.t;
    } else {
        scrollBoxPosition.w = posOpts.x - scrollBoxPosition.l;
        scrollBoxPosition.h = Math.max(dims.openHeight, dims.headerHeight);
    }

    scrollBoxPosition.direction = menuOpts.direction;

    if(scrollBox) {
        if(buttons.size()) {
            drawScrollBox(gd, gHeader, gButton, scrollBox, menuOpts, scrollBoxPosition);
        } else {
            hideScrollBox(scrollBox);
        }
    }
}

function drawScrollBox(gd, gHeader, gButton, scrollBox, menuOpts, position) {
    // enable the scrollbox
    var direction = menuOpts.direction;
    var isVertical = (direction === 'up' || direction === 'down');
    var dims = menuOpts._dims;

    var active = menuOpts.active;
    var translateX, translateY;
    var i;
    if(isVertical) {
        translateY = 0;
        for(i = 0; i < active; i++) {
            translateY += dims.heights[i] + constants.gapButton;
        }
    } else {
        translateX = 0;
        for(i = 0; i < active; i++) {
            translateX += dims.widths[i] + constants.gapButton;
        }
    }

    scrollBox.enable(position, translateX, translateY);

    if(scrollBox.hbar) {
        scrollBox.hbar
            .attr('opacity', '0')
            .transition()
            .attr('opacity', '1');
    }

    if(scrollBox.vbar) {
        scrollBox.vbar
            .attr('opacity', '0')
            .transition()
            .attr('opacity', '1');
    }
}

function hideScrollBox(scrollBox) {
    var hasHBar = !!scrollBox.hbar;
    var hasVBar = !!scrollBox.vbar;

    if(hasHBar) {
        scrollBox.hbar
            .transition()
            .attr('opacity', '0')
            .each('end', function() {
                hasHBar = false;
                if(!hasVBar) scrollBox.disable();
            });
    }

    if(hasVBar) {
        scrollBox.vbar
            .transition()
            .attr('opacity', '0')
            .each('end', function() {
                hasVBar = false;
                if(!hasHBar) scrollBox.disable();
            });
    }
}

function drawItem(item, menuOpts, itemOpts, gd) {
    item.call(drawItemRect, menuOpts)
        .call(drawItemText, menuOpts, itemOpts, gd);
}

function drawItemRect(item, menuOpts) {
    var rect = Lib.ensureSingle(item, 'rect', constants.itemRectClassName, function(s) {
        s.attr({
            rx: constants.rx,
            ry: constants.ry,
            'shape-rendering': 'crispEdges'
        });
    });

    rect.call(Color.stroke, menuOpts.bordercolor)
        .call(Color.fill, menuOpts.bgcolor)
        .style('stroke-width', menuOpts.borderwidth + 'px');
}

function drawItemText(item, menuOpts, itemOpts, gd) {
    var text = Lib.ensureSingle(item, 'text', constants.itemTextClassName, function(s) {
        s.classed('user-select-none', true)
            .attr({
                'text-anchor': 'start',
                'data-notex': 1
            });
    });

    var tx = itemOpts.label;
    var _meta = gd._fullLayout._meta;
    if(_meta) tx = Lib.templateString(tx, _meta);

    text.call(Drawing.font, menuOpts.font)
        .text(tx)
        .call(svgTextUtils.convertToTspans, gd);
}

function styleButtons(buttons, menuOpts) {
    var active = menuOpts.active;

    buttons.each(function(buttonOpts, i) {
        var button = d3.select(this);

        if(i === active && menuOpts.showactive) {
            button.select('rect.' + constants.itemRectClassName)
                .call(Color.fill, constants.activeColor);
        }
    });
}

function styleOnMouseOver(item) {
    item.select('rect.' + constants.itemRectClassName)
        .call(Color.fill, constants.hoverColor);
}

function styleOnMouseOut(item, menuOpts) {
    item.select('rect.' + constants.itemRectClassName)
        .call(Color.fill, menuOpts.bgcolor);
}

// find item dimensions (this mutates menuOpts)
function findDimensions(gd, menuOpts) {
    var dims = menuOpts._dims = {
        width1: 0,
        height1: 0,
        heights: [],
        widths: [],
        totalWidth: 0,
        totalHeight: 0,
        openWidth: 0,
        openHeight: 0,
        lx: 0,
        ly: 0
    };

    var fakeButtons = Drawing.tester.selectAll('g.' + constants.dropdownButtonClassName)
        .data(Lib.filterVisible(menuOpts.buttons));

    fakeButtons.enter().append('g')
        .classed(constants.dropdownButtonClassName, true);

    var isVertical = ['up', 'down'].indexOf(menuOpts.direction) !== -1;

    // loop over fake buttons to find width / height
    fakeButtons.each(function(buttonOpts, i) {
        var button = d3.select(this);

        button.call(drawItem, menuOpts, buttonOpts, gd);

        var text = button.select('.' + constants.itemTextClassName);

        // width is given by max width of all buttons
        var tWidth = text.node() && Drawing.bBox(text.node()).width;
        var wEff = Math.max(tWidth + constants.textPadX, constants.minWidth);

        // height is determined by item text
        var tHeight = menuOpts.font.size * LINE_SPACING;
        var tLines = svgTextUtils.lineCount(text);
        var hEff = Math.max(tHeight * tLines, constants.minHeight) + constants.textOffsetY;

        hEff = Math.ceil(hEff);
        wEff = Math.ceil(wEff);

        // Store per-item sizes since a row of horizontal buttons, for example,
        // don't all need to be the same width:
        dims.widths[i] = wEff;
        dims.heights[i] = hEff;

        // Height and width of individual element:
        dims.height1 = Math.max(dims.height1, hEff);
        dims.width1 = Math.max(dims.width1, wEff);

        if(isVertical) {
            dims.totalWidth = Math.max(dims.totalWidth, wEff);
            dims.openWidth = dims.totalWidth;
            dims.totalHeight += hEff + constants.gapButton;
            dims.openHeight += hEff + constants.gapButton;
        } else {
            dims.totalWidth += wEff + constants.gapButton;
            dims.openWidth += wEff + constants.gapButton;
            dims.totalHeight = Math.max(dims.totalHeight, hEff);
            dims.openHeight = dims.totalHeight;
        }
    });

    if(isVertical) {
        dims.totalHeight -= constants.gapButton;
    } else {
        dims.totalWidth -= constants.gapButton;
    }


    dims.headerWidth = dims.width1 + constants.arrowPadX;
    dims.headerHeight = dims.height1;

    if(menuOpts.type === 'dropdown') {
        if(isVertical) {
            dims.width1 += constants.arrowPadX;
            dims.totalHeight = dims.height1;
        } else {
            dims.totalWidth = dims.width1;
        }
        dims.totalWidth += constants.arrowPadX;
    }

    fakeButtons.remove();

    var paddedWidth = dims.totalWidth + menuOpts.pad.l + menuOpts.pad.r;
    var paddedHeight = dims.totalHeight + menuOpts.pad.t + menuOpts.pad.b;

    var graphSize = gd._fullLayout._size;
    dims.lx = graphSize.l + graphSize.w * menuOpts.x;
    dims.ly = graphSize.t + graphSize.h * (1 - menuOpts.y);

    var xanchor = 'left';
    if(Lib.isRightAnchor(menuOpts)) {
        dims.lx -= paddedWidth;
        xanchor = 'right';
    }
    if(Lib.isCenterAnchor(menuOpts)) {
        dims.lx -= paddedWidth / 2;
        xanchor = 'center';
    }

    var yanchor = 'top';
    if(Lib.isBottomAnchor(menuOpts)) {
        dims.ly -= paddedHeight;
        yanchor = 'bottom';
    }
    if(Lib.isMiddleAnchor(menuOpts)) {
        dims.ly -= paddedHeight / 2;
        yanchor = 'middle';
    }

    dims.totalWidth = Math.ceil(dims.totalWidth);
    dims.totalHeight = Math.ceil(dims.totalHeight);
    dims.lx = Math.round(dims.lx);
    dims.ly = Math.round(dims.ly);

    Plots.autoMargin(gd, autoMarginId(menuOpts), {
        x: menuOpts.x,
        y: menuOpts.y,
        l: paddedWidth * ({right: 1, center: 0.5}[xanchor] || 0),
        r: paddedWidth * ({left: 1, center: 0.5}[xanchor] || 0),
        b: paddedHeight * ({top: 1, middle: 0.5}[yanchor] || 0),
        t: paddedHeight * ({bottom: 1, middle: 0.5}[yanchor] || 0)
    });
}

function autoMarginId(menuOpts) {
    return constants.autoMarginIdRoot + menuOpts._index;
}

// set item positions (mutates posOpts)
function setItemPosition(item, menuOpts, posOpts, overrideOpts) {
    overrideOpts = overrideOpts || {};
    var rect = item.select('.' + constants.itemRectClassName);
    var text = item.select('.' + constants.itemTextClassName);
    var borderWidth = menuOpts.borderwidth;
    var index = posOpts.index;
    var dims = menuOpts._dims;

    Drawing.setTranslate(item, borderWidth + posOpts.x, borderWidth + posOpts.y);

    var isVertical = ['up', 'down'].indexOf(menuOpts.direction) !== -1;
    var finalHeight = overrideOpts.height || (isVertical ? dims.heights[index] : dims.height1);

    rect.attr({
        x: 0,
        y: 0,
        width: overrideOpts.width || (isVertical ? dims.width1 : dims.widths[index]),
        height: finalHeight
    });

    var tHeight = menuOpts.font.size * LINE_SPACING;
    var tLines = svgTextUtils.lineCount(text);
    var spanOffset = ((tLines - 1) * tHeight / 2);

    svgTextUtils.positionText(text, constants.textOffsetX,
        finalHeight / 2 - spanOffset + constants.textOffsetY);

    if(isVertical) {
        posOpts.y += dims.heights[index] + posOpts.yPad;
    } else {
        posOpts.x += dims.widths[index] + posOpts.xPad;
    }

    posOpts.index++;
}

function removeAllButtons(gButton, newMenuIndexAttr) {
    gButton
        .attr(constants.menuIndexAttrName, newMenuIndexAttr || '-1')
        .selectAll('g.' + constants.dropdownButtonClassName).remove();
}
