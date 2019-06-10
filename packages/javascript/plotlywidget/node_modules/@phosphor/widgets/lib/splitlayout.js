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
var panellayout_1 = require("./panellayout");
var widget_1 = require("./widget");
/**
 * A layout which arranges its widgets into resizable sections.
 */
var SplitLayout = (function (_super) {
    __extends(SplitLayout, _super);
    /**
     * Construct a new split layout.
     *
     * @param options - The options for initializing the layout.
     */
    function SplitLayout(options) {
        var _this = _super.call(this) || this;
        _this._fixed = 0;
        _this._spacing = 4;
        _this._dirty = false;
        _this._hasNormedSizes = false;
        _this._sizers = [];
        _this._items = [];
        _this._handles = [];
        _this._box = null;
        _this._alignment = 'start';
        _this._orientation = 'horizontal';
        _this.renderer = options.renderer;
        if (options.orientation !== undefined) {
            _this._orientation = options.orientation;
        }
        if (options.alignment !== undefined) {
            _this._alignment = options.alignment;
        }
        if (options.spacing !== undefined) {
            _this._spacing = Private.clampSpacing(options.spacing);
        }
        return _this;
    }
    /**
     * Dispose of the resources held by the layout.
     */
    SplitLayout.prototype.dispose = function () {
        // Dispose of the layout items.
        algorithm_1.each(this._items, function (item) { item.dispose(); });
        // Clear the layout state.
        this._box = null;
        this._items.length = 0;
        this._sizers.length = 0;
        this._handles.length = 0;
        // Dispose of the rest of the layout.
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(SplitLayout.prototype, "orientation", {
        /**
         * Get the layout orientation for the split layout.
         */
        get: function () {
            return this._orientation;
        },
        /**
         * Set the layout orientation for the split layout.
         */
        set: function (value) {
            if (this._orientation === value) {
                return;
            }
            this._orientation = value;
            if (!this.parent) {
                return;
            }
            this.parent.dataset['orientation'] = value;
            this.parent.fit();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitLayout.prototype, "alignment", {
        /**
         * Get the content alignment for the split layout.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand  to fill the
         * entire split layout.
         */
        get: function () {
            return this._alignment;
        },
        /**
         * Set the content alignment for the split layout.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand  to fill the
         * entire split layout.
         */
        set: function (value) {
            if (this._alignment === value) {
                return;
            }
            this._alignment = value;
            if (!this.parent) {
                return;
            }
            this.parent.dataset['alignment'] = value;
            this.parent.update();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitLayout.prototype, "spacing", {
        /**
         * Get the inter-element spacing for the split layout.
         */
        get: function () {
            return this._spacing;
        },
        /**
         * Set the inter-element spacing for the split layout.
         */
        set: function (value) {
            value = Private.clampSpacing(value);
            if (this._spacing === value) {
                return;
            }
            this._spacing = value;
            if (!this.parent) {
                return;
            }
            this.parent.fit();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(SplitLayout.prototype, "handles", {
        /**
         * A read-only array of the split handles in the layout.
         */
        get: function () {
            return this._handles;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Get the relative sizes of the widgets in the layout.
     *
     * @returns A new array of the relative sizes of the widgets.
     *
     * #### Notes
     * The returned sizes reflect the sizes of the widgets normalized
     * relative to their siblings.
     *
     * This method **does not** measure the DOM nodes.
     */
    SplitLayout.prototype.relativeSizes = function () {
        return Private.normalize(this._sizers.map(function (sizer) { return sizer.size; }));
    };
    /**
     * Set the relative sizes for the widgets in the layout.
     *
     * @param sizes - The relative sizes for the widgets in the panel.
     *
     * #### Notes
     * Extra values are ignored, too few will yield an undefined layout.
     *
     * The actual geometry of the DOM nodes is updated asynchronously.
     */
    SplitLayout.prototype.setRelativeSizes = function (sizes) {
        // Copy the sizes and pad with zeros as needed.
        var n = this._sizers.length;
        var temp = sizes.slice(0, n);
        while (temp.length < n) {
            temp.push(0);
        }
        // Normalize the padded sizes.
        var normed = Private.normalize(temp);
        // Apply the normalized sizes to the sizers.
        for (var i = 0; i < n; ++i) {
            var sizer = this._sizers[i];
            sizer.sizeHint = normed[i];
            sizer.size = normed[i];
        }
        // Set the flag indicating the sizes are normalized.
        this._hasNormedSizes = true;
        // Trigger an update of the parent widget.
        if (this.parent) {
            this.parent.update();
        }
    };
    /**
     * Move the offset position of a split handle.
     *
     * @param index - The index of the handle of the interest.
     *
     * @param position - The desired offset position of the handle.
     *
     * #### Notes
     * The position is relative to the offset parent.
     *
     * This will move the handle as close as possible to the desired
     * position. The sibling widgets will be adjusted as necessary.
     */
    SplitLayout.prototype.moveHandle = function (index, position) {
        // Bail if the index is invalid or the handle is hidden.
        var handle = this._handles[index];
        if (!handle || handle.classList.contains('p-mod-hidden')) {
            return;
        }
        // Compute the desired delta movement for the handle.
        var delta;
        if (this._orientation === 'horizontal') {
            delta = position - handle.offsetLeft;
        }
        else {
            delta = position - handle.offsetTop;
        }
        // Bail if there is no handle movement.
        if (delta === 0) {
            return;
        }
        // Prevent widget resizing unless needed.
        for (var _i = 0, _a = this._sizers; _i < _a.length; _i++) {
            var sizer = _a[_i];
            if (sizer.size > 0) {
                sizer.sizeHint = sizer.size;
            }
        }
        // Adjust the sizers to reflect the handle movement.
        boxengine_1.BoxEngine.adjust(this._sizers, index, delta);
        // Update the layout of the widgets.
        if (this.parent) {
            this.parent.update();
        }
    };
    /**
     * Perform layout initialization which requires the parent widget.
     */
    SplitLayout.prototype.init = function () {
        this.parent.dataset['orientation'] = this.orientation;
        this.parent.dataset['alignment'] = this.alignment;
        _super.prototype.init.call(this);
    };
    /**
     * Attach a widget to the parent's DOM node.
     *
     * @param index - The current index of the widget in the layout.
     *
     * @param widget - The widget to attach to the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    SplitLayout.prototype.attachWidget = function (index, widget) {
        // Create the item, handle, and sizer for the new widget.
        var item = new layout_1.LayoutItem(widget);
        var handle = Private.createHandle(this.renderer);
        var average = Private.averageSize(this._sizers);
        var sizer = Private.createSizer(average);
        // Insert the item, handle, and sizer into the internal arrays.
        algorithm_1.ArrayExt.insert(this._items, index, item);
        algorithm_1.ArrayExt.insert(this._sizers, index, sizer);
        algorithm_1.ArrayExt.insert(this._handles, index, handle);
        // Send a `'before-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeAttach);
        }
        // Add the widget and handle nodes to the parent.
        this.parent.node.appendChild(widget.node);
        this.parent.node.appendChild(handle);
        // Send an `'after-attach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterAttach);
        }
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * Move a widget in the parent's DOM node.
     *
     * @param fromIndex - The previous index of the widget in the layout.
     *
     * @param toIndex - The current index of the widget in the layout.
     *
     * @param widget - The widget to move in the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    SplitLayout.prototype.moveWidget = function (fromIndex, toIndex, widget) {
        // Move the item, sizer, and handle for the widget.
        algorithm_1.ArrayExt.move(this._items, fromIndex, toIndex);
        algorithm_1.ArrayExt.move(this._sizers, fromIndex, toIndex);
        algorithm_1.ArrayExt.move(this._handles, fromIndex, toIndex);
        // Post a fit request to the parent to show/hide last handle.
        this.parent.fit();
    };
    /**
     * Detach a widget from the parent's DOM node.
     *
     * @param index - The previous index of the widget in the layout.
     *
     * @param widget - The widget to detach from the parent.
     *
     * #### Notes
     * This is a reimplementation of the superclass method.
     */
    SplitLayout.prototype.detachWidget = function (index, widget) {
        // Remove the item, handle, and sizer for the widget.
        var item = algorithm_1.ArrayExt.removeAt(this._items, index);
        var handle = algorithm_1.ArrayExt.removeAt(this._handles, index);
        algorithm_1.ArrayExt.removeAt(this._sizers, index);
        // Send a `'before-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.BeforeDetach);
        }
        // Remove the widget and handle nodes from the parent.
        this.parent.node.removeChild(widget.node);
        this.parent.node.removeChild(handle);
        // Send an `'after-detach'` message if the parent is attached.
        if (this.parent.isAttached) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.Msg.AfterDetach);
        }
        // Dispose of the layout item.
        item.dispose();
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'before-show'` message.
     */
    SplitLayout.prototype.onBeforeShow = function (msg) {
        _super.prototype.onBeforeShow.call(this, msg);
        this.parent.update();
    };
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    SplitLayout.prototype.onBeforeAttach = function (msg) {
        _super.prototype.onBeforeAttach.call(this, msg);
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-shown'` message.
     */
    SplitLayout.prototype.onChildShown = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-hidden'` message.
     */
    SplitLayout.prototype.onChildHidden = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'resize'` message.
     */
    SplitLayout.prototype.onResize = function (msg) {
        if (this.parent.isVisible) {
            this._update(msg.width, msg.height);
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    SplitLayout.prototype.onUpdateRequest = function (msg) {
        if (this.parent.isVisible) {
            this._update(-1, -1);
        }
    };
    /**
     * A message handler invoked on a `'fit-request'` message.
     */
    SplitLayout.prototype.onFitRequest = function (msg) {
        if (this.parent.isAttached) {
            this._fit();
        }
    };
    /**
     * Fit the layout to the total size required by the widgets.
     */
    SplitLayout.prototype._fit = function () {
        // Update the handles and track the visible widget count.
        var nVisible = 0;
        var lastHandleIndex = -1;
        for (var i = 0, n = this._items.length; i < n; ++i) {
            if (this._items[i].isHidden) {
                this._handles[i].classList.add('p-mod-hidden');
            }
            else {
                this._handles[i].classList.remove('p-mod-hidden');
                lastHandleIndex = i;
                nVisible++;
            }
        }
        // Hide the handle for the last visible widget.
        if (lastHandleIndex !== -1) {
            this._handles[lastHandleIndex].classList.add('p-mod-hidden');
        }
        // Update the fixed space for the visible items.
        this._fixed = this._spacing * Math.max(0, nVisible - 1);
        // Setup the computed minimum size.
        var horz = this._orientation === 'horizontal';
        var minW = horz ? this._fixed : 0;
        var minH = horz ? 0 : this._fixed;
        // Update the sizers and computed size limits.
        for (var i = 0, n = this._items.length; i < n; ++i) {
            // Fetch the item and corresponding box sizer.
            var item = this._items[i];
            var sizer = this._sizers[i];
            // Prevent resizing unless necessary.
            if (sizer.size > 0) {
                sizer.sizeHint = sizer.size;
            }
            // If the item is hidden, it should consume zero size.
            if (item.isHidden) {
                sizer.minSize = 0;
                sizer.maxSize = 0;
                continue;
            }
            // Update the size limits for the item.
            item.fit();
            // Update the stretch factor.
            sizer.stretch = SplitLayout.getStretch(item.widget);
            // Update the sizer limits and computed min size.
            if (horz) {
                sizer.minSize = item.minWidth;
                sizer.maxSize = item.maxWidth;
                minW += item.minWidth;
                minH = Math.max(minH, item.minHeight);
            }
            else {
                sizer.minSize = item.minHeight;
                sizer.maxSize = item.maxHeight;
                minH += item.minHeight;
                minW = Math.max(minW, item.minWidth);
            }
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
    SplitLayout.prototype._update = function (offsetWidth, offsetHeight) {
        // Clear the dirty flag to indicate the update occurred.
        this._dirty = false;
        // Compute the visible item count.
        var nVisible = 0;
        for (var i = 0, n = this._items.length; i < n; ++i) {
            nVisible += +!this._items[i].isHidden;
        }
        // Bail early if there are no visible items to layout.
        if (nVisible === 0) {
            return;
        }
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
        // Compute the actual layout bounds adjusted for border and padding.
        var top = this._box.paddingTop;
        var left = this._box.paddingLeft;
        var width = offsetWidth - this._box.horizontalSum;
        var height = offsetHeight - this._box.verticalSum;
        // Compute the adjusted layout space.
        var space;
        var horz = this._orientation === 'horizontal';
        if (horz) {
            space = Math.max(0, width - this._fixed);
        }
        else {
            space = Math.max(0, height - this._fixed);
        }
        // Scale the size hints if they are normalized.
        if (this._hasNormedSizes) {
            for (var _i = 0, _a = this._sizers; _i < _a.length; _i++) {
                var sizer = _a[_i];
                sizer.sizeHint *= space;
            }
            this._hasNormedSizes = false;
        }
        // Distribute the layout space to the box sizers.
        var delta = boxengine_1.BoxEngine.calc(this._sizers, space);
        // Set up the variables for justification and alignment offset.
        var extra = 0;
        var offset = 0;
        // Account for alignment if there is extra layout space.
        if (delta > 0) {
            switch (this._alignment) {
                case 'start':
                    break;
                case 'center':
                    extra = 0;
                    offset = delta / 2;
                    break;
                case 'end':
                    extra = 0;
                    offset = delta;
                    break;
                case 'justify':
                    extra = delta / nVisible;
                    offset = 0;
                    break;
                default:
                    throw 'unreachable';
            }
        }
        // Layout the items using the computed box sizes.
        for (var i = 0, n = this._items.length; i < n; ++i) {
            // Fetch the item.
            var item = this._items[i];
            // Ignore hidden items.
            if (item.isHidden) {
                continue;
            }
            // Fetch the computed size for the widget.
            var size = this._sizers[i].size;
            // Fetch the style for the handle.
            var handleStyle = this._handles[i].style;
            // Update the widget and handle, and advance the relevant edge.
            if (horz) {
                item.update(left + offset, top, size + extra, height);
                left += size + extra;
                handleStyle.top = top + "px";
                handleStyle.left = left + offset + "px";
                handleStyle.width = this._spacing + "px";
                handleStyle.height = height + "px";
                left += this._spacing;
            }
            else {
                item.update(left, top + offset, width, size + extra);
                top += size + extra;
                handleStyle.top = top + offset + "px";
                handleStyle.left = left + "px";
                handleStyle.width = width + "px";
                handleStyle.height = this._spacing + "px";
                top += this._spacing;
            }
        }
    };
    return SplitLayout;
}(panellayout_1.PanelLayout));
exports.SplitLayout = SplitLayout;
/**
 * The namespace for the `SplitLayout` class statics.
 */
(function (SplitLayout) {
    /**
     * Get the split layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The split layout stretch factor for the widget.
     */
    function getStretch(widget) {
        return Private.stretchProperty.get(widget);
    }
    SplitLayout.getStretch = getStretch;
    /**
     * Set the split layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget, value) {
        Private.stretchProperty.set(widget, value);
    }
    SplitLayout.setStretch = setStretch;
})(SplitLayout = exports.SplitLayout || (exports.SplitLayout = {}));
exports.SplitLayout = SplitLayout;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The property descriptor for a widget stretch factor.
     */
    Private.stretchProperty = new properties_1.AttachedProperty({
        name: 'stretch',
        create: function () { return 0; },
        coerce: function (owner, value) { return Math.max(0, Math.floor(value)); },
        changed: onChildSizingChanged
    });
    /**
     * Create a new box sizer with the given size hint.
     */
    function createSizer(size) {
        var sizer = new boxengine_1.BoxSizer();
        sizer.sizeHint = Math.floor(size);
        return sizer;
    }
    Private.createSizer = createSizer;
    /**
     * Create a new split handle node using the given renderer.
     */
    function createHandle(renderer) {
        var handle = renderer.createHandle();
        handle.style.position = 'absolute';
        return handle;
    }
    Private.createHandle = createHandle;
    /**
     * Clamp a spacing value to an integer >= 0.
     */
    function clampSpacing(value) {
        return Math.max(0, Math.floor(value));
    }
    Private.clampSpacing = clampSpacing;
    /**
     * Compute the average size of an array of box sizers.
     */
    function averageSize(sizers) {
        return sizers.reduce(function (v, s) { return v + s.size; }, 0) / sizers.length || 0;
    }
    Private.averageSize = averageSize;
    /**
     * Normalize an array of values.
     */
    function normalize(values) {
        var n = values.length;
        if (n === 0) {
            return [];
        }
        var sum = values.reduce(function (a, b) { return a + Math.abs(b); }, 0);
        return sum === 0 ? values.map(function (v) { return 1 / n; }) : values.map(function (v) { return v / sum; });
    }
    Private.normalize = normalize;
    /**
     * The change handler for the attached sizing properties.
     */
    function onChildSizingChanged(child) {
        if (child.parent && child.parent.layout instanceof SplitLayout) {
            child.parent.fit();
        }
    }
})(Private || (Private = {}));
