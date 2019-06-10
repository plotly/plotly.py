"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var boxlayout_1 = require("./boxlayout");
var panel_1 = require("./panel");
/**
 * A panel which arranges its widgets in a single row or column.
 *
 * #### Notes
 * This class provides a convenience wrapper around a [[BoxLayout]].
 */
var BoxPanel = (function (_super) {
    __extends(BoxPanel, _super);
    /**
     * Construct a new box panel.
     *
     * @param options - The options for initializing the box panel.
     */
    function BoxPanel(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, { layout: Private.createLayout(options) }) || this;
        _this.addClass('p-BoxPanel');
        return _this;
    }
    Object.defineProperty(BoxPanel.prototype, "direction", {
        /**
         * Get the layout direction for the box panel.
         */
        get: function () {
            return this.layout.direction;
        },
        /**
         * Set the layout direction for the box panel.
         */
        set: function (value) {
            this.layout.direction = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BoxPanel.prototype, "alignment", {
        /**
         * Get the content alignment for the box panel.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand to fill the
         * entire box layout.
         */
        get: function () {
            return this.layout.alignment;
        },
        /**
         * Set the content alignment for the box panel.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand to fill the
         * entire box layout.
         */
        set: function (value) {
            this.layout.alignment = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BoxPanel.prototype, "spacing", {
        /**
         * Get the inter-element spacing for the box panel.
         */
        get: function () {
            return this.layout.spacing;
        },
        /**
         * Set the inter-element spacing for the box panel.
         */
        set: function (value) {
            this.layout.spacing = value;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    BoxPanel.prototype.onChildAdded = function (msg) {
        msg.child.addClass('p-BoxPanel-child');
    };
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    BoxPanel.prototype.onChildRemoved = function (msg) {
        msg.child.removeClass('p-BoxPanel-child');
    };
    return BoxPanel;
}(panel_1.Panel));
exports.BoxPanel = BoxPanel;
/**
 * The namespace for the `BoxPanel` class statics.
 */
(function (BoxPanel) {
    /**
     * Get the box panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box panel stretch factor for the widget.
     */
    function getStretch(widget) {
        return boxlayout_1.BoxLayout.getStretch(widget);
    }
    BoxPanel.getStretch = getStretch;
    /**
     * Set the box panel stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget, value) {
        boxlayout_1.BoxLayout.setStretch(widget, value);
    }
    BoxPanel.setStretch = setStretch;
    /**
     * Get the box panel size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box panel size basis for the widget.
     */
    function getSizeBasis(widget) {
        return boxlayout_1.BoxLayout.getSizeBasis(widget);
    }
    BoxPanel.getSizeBasis = getSizeBasis;
    /**
     * Set the box panel size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the size basis.
     */
    function setSizeBasis(widget, value) {
        boxlayout_1.BoxLayout.setSizeBasis(widget, value);
    }
    BoxPanel.setSizeBasis = setSizeBasis;
})(BoxPanel = exports.BoxPanel || (exports.BoxPanel = {}));
exports.BoxPanel = BoxPanel;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create a box layout for the given panel options.
     */
    function createLayout(options) {
        return options.layout || new boxlayout_1.BoxLayout(options);
    }
    Private.createLayout = createLayout;
})(Private || (Private = {}));
