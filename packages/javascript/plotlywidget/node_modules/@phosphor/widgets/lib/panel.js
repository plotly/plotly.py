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
var panellayout_1 = require("./panellayout");
var widget_1 = require("./widget");
/**
 * A simple and convenient panel widget class.
 *
 * #### Notes
 * This class is suitable as a base class for implementing a variety of
 * convenience panel widgets, but can also be used directly with CSS to
 * arrange a collection of widgets.
 *
 * This class provides a convenience wrapper around a [[PanelLayout]].
 */
var Panel = (function (_super) {
    __extends(Panel, _super);
    /**
     * Construct a new panel.
     *
     * @param options - The options for initializing the panel.
     */
    function Panel(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this) || this;
        _this.addClass('p-Panel');
        _this.layout = Private.createLayout(options);
        return _this;
    }
    Object.defineProperty(Panel.prototype, "widgets", {
        /**
         * A read-only array of the widgets in the panel.
         */
        get: function () {
            return this.layout.widgets;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Add a widget to the end of the panel.
     *
     * @param widget - The widget to add to the panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     */
    Panel.prototype.addWidget = function (widget) {
        this.layout.addWidget(widget);
    };
    /**
     * Insert a widget at the specified index.
     *
     * @param index - The index at which to insert the widget.
     *
     * @param widget - The widget to insert into to the panel.
     *
     * #### Notes
     * If the widget is already contained in the panel, it will be moved.
     */
    Panel.prototype.insertWidget = function (index, widget) {
        this.layout.insertWidget(index, widget);
    };
    return Panel;
}(widget_1.Widget));
exports.Panel = Panel;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create a panel layout for the given panel options.
     */
    function createLayout(options) {
        return options.layout || new panellayout_1.PanelLayout();
    }
    Private.createLayout = createLayout;
})(Private || (Private = {}));
