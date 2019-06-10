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
var signaling_1 = require("@phosphor/signaling");
var panel_1 = require("./panel");
var stackedlayout_1 = require("./stackedlayout");
/**
 * A panel where visible widgets are stacked atop one another.
 *
 * #### Notes
 * This class provides a convenience wrapper around a [[StackedLayout]].
 */
var StackedPanel = (function (_super) {
    __extends(StackedPanel, _super);
    /**
     * Construct a new stacked panel.
     *
     * @param options - The options for initializing the panel.
     */
    function StackedPanel(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, { layout: Private.createLayout(options) }) || this;
        _this._widgetRemoved = new signaling_1.Signal(_this);
        _this.addClass('p-StackedPanel');
        return _this;
    }
    Object.defineProperty(StackedPanel.prototype, "widgetRemoved", {
        /**
         * A signal emitted when a widget is removed from a stacked panel.
         */
        get: function () {
            return this._widgetRemoved;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * A message handler invoked on a `'child-added'` message.
     */
    StackedPanel.prototype.onChildAdded = function (msg) {
        msg.child.addClass('p-StackedPanel-child');
    };
    /**
     * A message handler invoked on a `'child-removed'` message.
     */
    StackedPanel.prototype.onChildRemoved = function (msg) {
        msg.child.removeClass('p-StackedPanel-child');
        this._widgetRemoved.emit(msg.child);
    };
    return StackedPanel;
}(panel_1.Panel));
exports.StackedPanel = StackedPanel;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * Create a stacked layout for the given panel options.
     */
    function createLayout(options) {
        return options.layout || new stackedlayout_1.StackedLayout();
    }
    Private.createLayout = createLayout;
})(Private || (Private = {}));
