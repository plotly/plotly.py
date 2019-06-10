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
var algorithm_1 = require("@phosphor/algorithm");
var domutils_1 = require("@phosphor/domutils");
var messaging_1 = require("@phosphor/messaging");
var properties_1 = require("@phosphor/properties");
var boxengine_1 = require("./boxengine");
var layout_1 = require("./layout");
var widget_1 = require("./widget");
/**
 * A layout which arranges its widgets in a grid.
 */
var GridLayout = (function (_super) {
    __extends(GridLayout, _super);
    /**
     * Construct a new grid layout.
     *
     * @param options - The options for initializing the layout.
     */
    function GridLayout(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this, options) || this;
        _this._dirty = false;
        _this._rowSpacing = 4;
        _this._columnSpacing = 4;
        _this._items = [];
        _this._rowStarts = [];
        _this._columnStarts = [];
        _this._rowSizers = [new boxengine_1.BoxSizer()];
        _this._columnSizers = [new boxengine_1.BoxSizer()];
        _this._box = null;
        if (options.rowCount !== undefined) {
            Private.reallocSizers(_this._rowSizers, options.rowCount);
        }
        if (options.columnCount !== undefined) {
            Private.reallocSizers(_this._columnSizers, options.columnCount);
        }
        if (options.rowSpacing !== undefined) {
            _this._rowSpacing = Private.clampValue(options.rowSpacing);
        }
        if (options.columnSpacing !== undefined) {
            _this._columnSpacing = Private.clampValue(options.columnSpacing);
        }
        return _this;
    }
    /**
     * Dispose of the resources held by the layout.
     */
    GridLayout.prototype.dispose = function () {
        // Dispose of the widgets and layout items.
        algorithm_1.each(this._items, function (item) {
            var widget = item.widget;
            item.dispose();
            widget.dispose();
        });
        // Clear the layout state.
        this._box = null;
        this._items.length = 0;
        this._rowStarts.length = 0;
        this._rowSizers.length = 0;
        this._columnStarts.length = 0;
        this._columnSizers.length = 0;
        // Dispose of the rest of the layout.
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(GridLayout.prototype, "rowCount", {
        /**
         * Get the number of rows in the layout.
         */
        get: function () {
            return this._rowSizers.length;
        },
        /**
         * Set the number of rows in the layout.
         *
         * #### Notes
         * The minimum row count is `1`.
         */
        set: function (value) {
            // Do nothing if the row count does not change.
            if (value === this.rowCount) {
                return;
            }
            // Reallocate the row sizers.
            Private.reallocSizers(this._rowSizers, value);
            // Schedule a fit of the parent.
            if (this.parent) {
                this.parent.fit();
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridLayout.prototype, "columnCount", {
        /**
         * Get the number of columns in the layout.
         */
        get: function () {
            return this._columnSizers.length;
        },
        /**
         * Set the number of columns in the layout.
         *
         * #### Notes
         * The minimum column count is `1`.
         */
        set: function (value) {
            // Do nothing if the column count does not change.
            if (value === this.columnCount) {
                return;
            }
            // Reallocate the column sizers.
            Private.reallocSizers(this._columnSizers, value);
            // Schedule a fit of the parent.
            if (this.parent) {
                this.parent.fit();
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridLayout.prototype, "rowSpacing", {
        /**
         * Get the row spacing for the layout.
         */
        get: function () {
            return this._rowSpacing;
        },
        /**
         * Set the row spacing for the layout.
         */
        set: function (value) {
            // Clamp the spacing to the allowed range.
            value = Private.clampValue(value);
            // Bail if the spacing does not change
            if (this._rowSpacing === value) {
                return;
            }
            // Update the internal spacing.
            this._rowSpacing = value;
            // Schedule a fit of the parent.
            if (this.parent) {
                this.parent.fit();
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridLayout.prototype, "columnSpacing", {
        /**
         * Get the column spacing for the layout.
         */
        get: function () {
            return this._columnSpacing;
        },
        /**
         * Set the col spacing for the layout.
         */
        set: function (value) {
            // Clamp the spacing to the allowed range.
            value = Private.clampValue(value);
            // Bail if the spacing does not change
            if (this._columnSpacing === value) {
                return;
            }
            // Update the internal spacing.
            this._columnSpacing = value;
            // Schedule a fit of the parent.
            if (this.parent) {
                this.parent.fit();
            }
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Get the stretch factor for a specific row.
     *
     * @param index - The row index of interest.
     *
     * @returns The stretch factor for the row.
     *
     * #### Notes
     * This returns `-1` if the index is out of range.
     */
    GridLayout.prototype.rowStretch = function (index) {
        var sizer = this._rowSizers[index];
        return sizer ? sizer.stretch : -1;
    };
    /**
     * Set the stretch factor for a specific row.
     *
     * @param index - The row index of interest.
     *
     * @param value - The stretch factor for the row.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    GridLayout.prototype.setRowStretch = function (index, value) {
        // Look up the row sizer.
        var sizer = this._rowSizers[index];
        // Bail if the index is out of range.
        if (!sizer) {
            return;
        }
        // Clamp the value to the allowed range.
        value = Private.clampValue(value);
        // Bail if the stretch does not change.
        if (sizer.stretch === value) {
            return;
        }
        // Update the sizer stretch.
        sizer.stretch = value;
        // Schedule an update of the parent.
        if (this.parent) {
            this.parent.update();
        }
    };
    /**
     * Get the stretch factor for a specific column.
     *
     * @param index - The column index of interest.
     *
     * @returns The stretch factor for the column.
     *
     * #### Notes
     * This returns `-1` if the index is out of range.
     */
    GridLayout.prototype.columnStretch = function (index) {
        var sizer = this._columnSizers[index];
        return sizer ? sizer.stretch : -1;
    };
    /**
     * Set the stretch factor for a specific column.
     *
     * @param index - The column index of interest.
     *
     * @param value - The stretch factor for the column.
     *
     * #### Notes
     * This is a no-op if the index is out of range.
     */
    GridLayout.prototype.setColumnStretch = function (index, value) {
        // Look up the column sizer.
        var sizer = this._columnSizers[index];
        // Bail if the index is out of range.
        if (!sizer) {
            return;
        }
        // Clamp the value to the allowed range.
        value = Private.clampValue(value);
        // Bail if the stretch does not change.
        if (sizer.stretch === value) {
            return;
        }
        // Update the sizer stretch.
        sizer.stretch = value;
        // Schedule an update of the parent.
        if (this.parent) {
            this.parent.update();
        }
    };
    /**
     * Create an iterator over the widgets in the layout.
     *
     * @returns A new iterator over the widgets in the layout.
     */
    GridLayout.prototype.iter = function () {
        return algorithm_1.map(this._items, function (item) { return item.widget; });
    };
    /**
     * Add a widget to the grid layout.
     *
     * @param widget - The widget to add to the layout.
     *
     * #### Notes
     * If the widget is already contained in the layout, this is no-op.
     */
    GridLayout.prototype.addWidget = function (widget) {
        // Look up the index for the widget.
        var i = algorithm_1.ArrayExt.findFirstIndex(this._items, function (it) { return it.widget === widget; });
        // Bail if the widget is already in the layout.
        if (i !== -1) {
            return;
        }
        // Add the widget to the layout.
        this._items.push(new layout_1.LayoutItem(widget));
        // Attach the widget to the parent.
        if (this.parent) {
            this.attachWidget(widget);
        }
    };
    /**
     * Remove a widget from the grid layout.
     *
     * @param widget - The widget to remove from the layout.
     *
     * #### Notes
     * A widget is automatically removed from the layout when its `parent`
     * is set to `null`. This method should only be invoked directly when
     * removing a widget from a layout which has yet to be installed on a
     * parent widget.
     *
     * This method does *not* modify the widget's `parent`.
     */
    GridLayout.prototype.removeWidget = function (widget) {
        // Look up the index for the widget.
        var i = algorithm_1.ArrayExt.findFirstIndex(this._items, function (it) { return it.widget === widget; });
        // Bail if the widget is not in the layout.
        if (i !== -1) {
            return;
        }
        // Remove the widget from the layout.
        var item = algorithm_1.ArrayExt.removeAt(this._items, i);
        // Detach the widget from the parent.
        if (this.parent) {
            this.detachWidget(widget);
        }
        // Dispose the layout item.
        item.dispose();
    };
    /**
     * Perform layout initialization which requires the parent widget.
     */
    GridLayout.prototype.init = function () {
        var _this = this;
        _super.prototype.init.call(this);
        algorithm_1.each(this, function (widget) { _this.attachWidget(widget); });
    };
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param widget - The widget to attach to the parent.
     */
    GridLayout.prototype.attachWidget = function (widget) {
        // Send a `'before-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeAttach);
        }
        // Add the widget's node to the parent.
        this.parent.node.appendChild(widget.node);
        // Send an `'after-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterAttach);
        }
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param widget - The widget to detach from the parent.
     */
    GridLayout.prototype.detachWidget = function (widget) {
        // Send a `'before-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeDetach);
        }
        // Remove the widget's node from the parent.
        this.parent.node.removeChild(widget.node);
        // Send an `'after-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterDetach);
        }
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'before-show'` message.
     */
    GridLayout.prototype.onBeforeShow = function (msg) {
        _super.prototype.onBeforeShow.call(this, msg);
        this.parent.update();
    };
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    GridLayout.prototype.onBeforeAttach = function (msg) {
        _super.prototype.onBeforeAttach.call(this, msg);
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-shown'` message.
     */
    GridLayout.prototype.onChildShown = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-hidden'` message.
     */
    GridLayout.prototype.onChildHidden = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'resize'` message.
     */
    GridLayout.prototype.onResize = function (msg) {
        if (this.parent.isVisible) {
            this._update(msg.width, msg.height);
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    GridLayout.prototype.onUpdateRequest = function (msg) {
        if (this.parent.isVisible) {
            this._update(-1, -1);
        }
    };
    /**
     * A message handler invoked on a `'fit-request'` message.
     */
    GridLayout.prototype.onFitRequest = function (msg) {
        if (this.parent.isAttached) {
            this._fit();
        }
    };
    /**
     * Fit the layout to the total size required by the widgets.
     */
    GridLayout.prototype._fit = function () {
        // Reset the min sizes of the sizers.
        for (var i = 0, n = this.rowCount; i < n; ++i) {
            this._rowSizers[i].minSize = 0;
        }
        for (var i = 0, n = this.columnCount; i < n; ++i) {
            this._columnSizers[i].minSize = 0;
        }
        // Filter for the visible layout items.
        var items = this._items.filter(function (it) { return !it.isHidden; });
        // Fit the layout items.
        for (var i = 0, n = items.length; i < n; ++i) {
            items[i].fit();
        }
        // Get the max row and column index.
        var maxRow = this.rowCount - 1;
        var maxCol = this.columnCount - 1;
        // Sort the items by row span.
        items.sort(Private.rowSpanCmp);
        // Update the min sizes of the row sizers.
        for (var i = 0, n = items.length; i < n; ++i) {
            // Fetch the item.
            var item = items[i];
            // Get the row bounds for the item.
            var config = GridLayout.getCellConfig(item.widget);
            var r1 = Math.min(config.row, maxRow);
            var r2 = Math.min(config.row + config.rowSpan - 1, maxRow);
            // Distribute the minimum height to the sizers as needed.
            Private.distributeMin(this._rowSizers, r1, r2, item.minHeight);
        }
        // Sort the items by column span.
        items.sort(Private.columnSpanCmp);
        // Update the min sizes of the column sizers.
        for (var i = 0, n = items.length; i < n; ++i) {
            // Fetch the item.
            var item = items[i];
            // Get the column bounds for the item.
            var config = GridLayout.getCellConfig(item.widget);
            var c1 = Math.min(config.column, maxCol);
            var c2 = Math.min(config.column + config.columnSpan - 1, maxCol);
            // Distribute the minimum width to the sizers as needed.
            Private.distributeMin(this._columnSizers, c1, c2, item.minWidth);
        }
        // If no size constraint is needed, just update the parent.
        if (this.fitPolicy === 'set-no-constraint') {
            messaging_1.MessageLoop.sendMessage(this.parent, widget_1.Widget.Msg.UpdateRequest);
            return;
        }
        // Set up the computed min size.
        var minH = maxRow * this._rowSpacing;
        var minW = maxCol * this._columnSpacing;
        // Add the sizer minimums to the computed min size.
        for (var i = 0, n = this.rowCount; i < n; ++i) {
            minH += this._rowSizers[i].minSize;
        }
        for (var i = 0, n = this.columnCount; i < n; ++i) {
            minW += this._columnSizers[i].minSize;
        }
        // Update the box sizing and add it to the computed min size.
        var box = this._box = domutils_1.ElementExt.boxSizing(this.parent.node);
        minW += box.horizontalSum;
        minH += box.verticalSum;
        // Update the parent's min size constraints.
        var style = this.parent.node.style;
        style.minWidth = minW + "px";
        style.minHeight = minH + "px";
        // Set the dirty flag to ensure only a single update occurs.
        this._dirty = true;
        // Notify the ancestor that it should fit immediately. This may
        // cause a resize of the parent, fulfilling the required update.
        if (this.parent.parent) {
            messaging_1.MessageLoop.sendMessage(this.parent.parent, widget_1.Widget.Msg.FitRequest);
        }
        // If the dirty flag is still set, the parent was not resized.
        // Trigger the required update on the parent widget immediately.
        if (this._dirty) {
            messaging_1.MessageLoop.sendMessage(this.parent, widget_1.Widget.Msg.UpdateRequest);
        }
    };
    /**
     * Update the layout position and size of the widgets.
     *
     * The parent offset dimensions should be `-1` if unknown.
     */
    GridLayout.prototype._update = function (offsetWidth, offsetHeight) {
        // Clear the dirty flag to indicate the update occurred.
        this._dirty = false;
        // Measure the parent if the offset dimensions are unknown.
        if (offsetWidth < 0) {
            offsetWidth = this.parent.node.offsetWidth;
        }
        if (offsetHeight < 0) {
            offsetHeight = this.parent.node.offsetHeight;
        }
        // Ensure the parent box sizing data is computed.
        if (!this._box) {
            this._box = domutils_1.ElementExt.boxSizing(this.parent.node);
        }
        // Compute the layout area adjusted for border and padding.
        var top = this._box.paddingTop;
        var left = this._box.paddingLeft;
        var width = offsetWidth - this._box.horizontalSum;
        var height = offsetHeight - this._box.verticalSum;
        // Get the max row and column index.
        var maxRow = this.rowCount - 1;
        var maxCol = this.columnCount - 1;
        // Compute the total fixed row and column space.
        var fixedRowSpace = maxRow * this._rowSpacing;
        var fixedColSpace = maxCol * this._columnSpacing;
        // Distribute the available space to the box sizers.
        boxengine_1.BoxEngine.calc(this._rowSizers, Math.max(0, height - fixedRowSpace));
        boxengine_1.BoxEngine.calc(this._columnSizers, Math.max(0, width - fixedColSpace));
        // Update the row start positions.
        for (var i = 0, pos = top, n = this.rowCount; i < n; ++i) {
            this._rowStarts[i] = pos;
            pos += this._rowSizers[i].size + this._rowSpacing;
        }
        // Update the column start positions.
        for (var i = 0, pos = left, n = this.columnCount; i < n; ++i) {
            this._columnStarts[i] = pos;
            pos += this._columnSizers[i].size + this._columnSpacing;
        }
        // Update the geometry of the layout items.
        for (var i = 0, n = this._items.length; i < n; ++i) {
            // Fetch the item.
            var item = this._items[i];
            // Ignore hidden items.
            if (item.isHidden) {
                continue;
            }
            // Fetch the cell bounds for the widget.
            var config = GridLayout.getCellConfig(item.widget);
            var r1 = Math.min(config.row, maxRow);
            var c1 = Math.min(config.column, maxCol);
            var r2 = Math.min(config.row + config.rowSpan - 1, maxRow);
            var c2 = Math.min(config.column + config.columnSpan - 1, maxCol);
            // Compute the cell geometry.
            var x = this._columnStarts[c1];
            var y = this._rowStarts[r1];
            var w = this._columnStarts[c2] + this._columnSizers[c2].size - x;
            var h = this._rowStarts[r2] + this._rowSizers[r2].size - y;
            // Update the geometry of the layout item.
            item.update(x, y, w, h);
        }
    };
    return GridLayout;
}(layout_1.Layout));
exports.GridLayout = GridLayout;
/**
 * The namespace for the `GridLayout` class statics.
 */
(function (GridLayout) {
    /**
     * Get the cell config for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The cell config for the widget.
     */
    function getCellConfig(widget) {
        return Private.cellConfigProperty.get(widget);
    }
    GridLayout.getCellConfig = getCellConfig;
    /**
     * Set the cell config for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the cell config.
     */
    function setCellConfig(widget, value) {
        Private.cellConfigProperty.set(widget, Private.normalizeConfig(value));
    }
    GridLayout.setCellConfig = setCellConfig;
})(GridLayout = exports.GridLayout || (exports.GridLayout = {}));
exports.GridLayout = GridLayout;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The property descriptor for the widget cell config.
     */
    Private.cellConfigProperty = new properties_1.AttachedProperty({
        name: 'cellConfig',
        create: function () { return ({ row: 0, column: 0, rowSpan: 1, columnSpan: 1 }); },
        changed: onChildCellConfigChanged
    });
    /**
     * Normalize a partial cell config object.
     */
    function normalizeConfig(config) {
        var row = Math.max(0, Math.floor(config.row || 0));
        var column = Math.max(0, Math.floor(config.column || 0));
        var rowSpan = Math.max(1, Math.floor(config.rowSpan || 0));
        var columnSpan = Math.max(1, Math.floor(config.columnSpan || 0));
        return { row: row, column: column, rowSpan: rowSpan, columnSpan: columnSpan };
    }
    Private.normalizeConfig = normalizeConfig;
    /**
     * Clamp a value to an integer >= 0.
     */
    function clampValue(value) {
        return Math.max(0, Math.floor(value));
    }
    Private.clampValue = clampValue;
    /**
     * A sort comparison function for row spans.
     */
    function rowSpanCmp(a, b) {
        var c1 = Private.cellConfigProperty.get(a.widget);
        var c2 = Private.cellConfigProperty.get(b.widget);
        return c1.rowSpan - c2.rowSpan;
    }
    Private.rowSpanCmp = rowSpanCmp;
    /**
     * A sort comparison function for column spans.
     */
    function columnSpanCmp(a, b) {
        var c1 = Private.cellConfigProperty.get(a.widget);
        var c2 = Private.cellConfigProperty.get(b.widget);
        return c1.columnSpan - c2.columnSpan;
    }
    Private.columnSpanCmp = columnSpanCmp;
    /**
     * Reallocate the box sizers for the given grid dimensions.
     */
    function reallocSizers(sizers, count) {
        // Coerce the count to the valid range.
        count = Math.max(1, Math.floor(count));
        // Add the missing sizers.
        while (sizers.length < count) {
            sizers.push(new boxengine_1.BoxSizer());
        }
        // Remove the extra sizers.
        if (sizers.length < count) {
            sizers.length = count;
        }
    }
    Private.reallocSizers = reallocSizers;
    /**
     * Distribute a min size constraint across a range of sizers.
     */
    function distributeMin(sizers, i1, i2, minSize) {
        // Sanity check the indices.
        if (i2 < i1) {
            return;
        }
        // Handle the simple case of no cell span.
        if (i1 === i2) {
            var sizer = sizers[i1];
            sizer.minSize = Math.max(sizer.minSize, minSize);
            return;
        }
        // Compute the total current min size of the span.
        var totalMin = 0;
        for (var i = i1; i <= i2; ++i) {
            totalMin += sizers[i].minSize;
        }
        // Do nothing if the total is greater than the required.
        if (totalMin >= minSize) {
            return;
        }
        // Compute the portion of the space to allocate to each sizer.
        var portion = (minSize - totalMin) / (i2 - i1 + 1);
        // Add the portion to each sizer.
        for (var i = i1; i <= i2; ++i) {
            sizers[i].minSize += portion;
        }
    }
    Private.distributeMin = distributeMin;
    /**
     * The change handler for the child cell config property.
     */
    function onChildCellConfigChanged(child) {
        if (child.parent && child.parent.layout instanceof GridLayout) {
            child.parent.fit();
        }
    }
})(Private || (Private = {}));
