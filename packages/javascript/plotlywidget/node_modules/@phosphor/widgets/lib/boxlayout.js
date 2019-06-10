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
 * A layout which arranges its widgets in a single row or column.
 */
var BoxLayout = (function (_super) {
    __extends(BoxLayout, _super);
    /**
     * Construct a new box layout.
     *
     * @param options - The options for initializing the layout.
     */
    function BoxLayout(options) {
        if (options === void 0) { options = {}; }
        var _this = _super.call(this) || this;
        _this._fixed = 0;
        _this._spacing = 4;
        _this._dirty = false;
        _this._sizers = [];
        _this._items = [];
        _this._box = null;
        _this._alignment = 'start';
        _this._direction = 'top-to-bottom';
        if (options.direction !== undefined) {
            _this._direction = options.direction;
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
    BoxLayout.prototype.dispose = function () {
        // Dispose of the layout items.
        algorithm_1.each(this._items, function (item) { item.dispose(); });
        // Clear the layout state.
        this._box = null;
        this._items.length = 0;
        this._sizers.length = 0;
        // Dispose of the rest of the layout.
        _super.prototype.dispose.call(this);
    };
    Object.defineProperty(BoxLayout.prototype, "direction", {
        /**
         * Get the layout direction for the box layout.
         */
        get: function () {
            return this._direction;
        },
        /**
         * Set the layout direction for the box layout.
         */
        set: function (value) {
            if (this._direction === value) {
                return;
            }
            this._direction = value;
            if (!this.parent) {
                return;
            }
            this.parent.dataset['direction'] = value;
            this.parent.fit();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(BoxLayout.prototype, "alignment", {
        /**
         * Get the content alignment for the box layout.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand to fill the
         * entire box layout.
         */
        get: function () {
            return this._alignment;
        },
        /**
         * Set the content alignment for the box layout.
         *
         * #### Notes
         * This is the alignment of the widgets in the layout direction.
         *
         * The alignment has no effect if the widgets can expand to fill the
         * entire box layout.
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
    Object.defineProperty(BoxLayout.prototype, "spacing", {
        /**
         * Get the inter-element spacing for the box layout.
         */
        get: function () {
            return this._spacing;
        },
        /**
         * Set the inter-element spacing for the box layout.
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
    /**
     * Perform layout initialization which requires the parent widget.
     */
    BoxLayout.prototype.init = function () {
        this.parent.dataset['direction'] = this.direction;
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
    BoxLayout.prototype.attachWidget = function (index, widget) {
        // Create and add a new layout item for the widget.
        algorithm_1.ArrayExt.insert(this._items, index, new layout_1.LayoutItem(widget));
        // Create and add a new sizer for the widget.
        algorithm_1.ArrayExt.insert(this._sizers, index, new boxengine_1.BoxSizer());
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
    BoxLayout.prototype.moveWidget = function (fromIndex, toIndex, widget) {
        // Move the layout item for the widget.
        algorithm_1.ArrayExt.move(this._items, fromIndex, toIndex);
        // Move the sizer for the widget.
        algorithm_1.ArrayExt.move(this._sizers, fromIndex, toIndex);
        // Post an update request for the parent widget.
        this.parent.update();
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
    BoxLayout.prototype.detachWidget = function (index, widget) {
        // Remove the layout item for the widget.
        var item = algorithm_1.ArrayExt.removeAt(this._items, index);
        // Remove the sizer for the widget.
        algorithm_1.ArrayExt.removeAt(this._sizers, index);
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
        // Dispose of the layout item.
        item.dispose();
        // Post a fit request for the parent widget.
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'before-show'` message.
     */
    BoxLayout.prototype.onBeforeShow = function (msg) {
        _super.prototype.onBeforeShow.call(this, msg);
        this.parent.update();
    };
    /**
     * A message handler invoked on a `'before-attach'` message.
     */
    BoxLayout.prototype.onBeforeAttach = function (msg) {
        _super.prototype.onBeforeAttach.call(this, msg);
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-shown'` message.
     */
    BoxLayout.prototype.onChildShown = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'child-hidden'` message.
     */
    BoxLayout.prototype.onChildHidden = function (msg) {
        this.parent.fit();
    };
    /**
     * A message handler invoked on a `'resize'` message.
     */
    BoxLayout.prototype.onResize = function (msg) {
        if (this.parent.isVisible) {
            this._update(msg.width, msg.height);
        }
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    BoxLayout.prototype.onUpdateRequest = function (msg) {
        if (this.parent.isVisible) {
            this._update(-1, -1);
        }
    };
    /**
     * A message handler invoked on a `'fit-request'` message.
     */
    BoxLayout.prototype.onFitRequest = function (msg) {
        if (this.parent.isAttached) {
            this._fit();
        }
    };
    /**
     * Fit the layout to the total size required by the widgets.
     */
    BoxLayout.prototype._fit = function () {
        // Compute the visible item count.
        var nVisible = 0;
        for (var i = 0, n = this._items.length; i < n; ++i) {
            nVisible += +!this._items[i].isHidden;
        }
        // Update the fixed space for the visible items.
        this._fixed = this._spacing * Math.max(0, nVisible - 1);
        // Setup the computed minimum size.
        var horz = Private.isHorizontal(this._direction);
        var minW = horz ? this._fixed : 0;
        var minH = horz ? 0 : this._fixed;
        // Update the sizers and computed minimum size.
        for (var i = 0, n = this._items.length; i < n; ++i) {
            // Fetch the item and corresponding box sizer.
            var item = this._items[i];
            var sizer = this._sizers[i];
            // If the item is hidden, it should consume zero size.
            if (item.isHidden) {
                sizer.minSize = 0;
                sizer.maxSize = 0;
                continue;
            }
            // Update the size limits for the item.
            item.fit();
            // Update the size basis and stretch factor.
            sizer.sizeHint = BoxLayout.getSizeBasis(item.widget);
            sizer.stretch = BoxLayout.getStretch(item.widget);
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
    BoxLayout.prototype._update = function (offsetWidth, offsetHeight) {
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
        // Compute the layout area adjusted for border and padding.
        var top = this._box.paddingTop;
        var left = this._box.paddingLeft;
        var width = offsetWidth - this._box.horizontalSum;
        var height = offsetHeight - this._box.verticalSum;
        // Distribute the layout space and adjust the start position.
        var delta;
        switch (this._direction) {
            case 'left-to-right':
                delta = boxengine_1.BoxEngine.calc(this._sizers, Math.max(0, width - this._fixed));
                break;
            case 'top-to-bottom':
                delta = boxengine_1.BoxEngine.calc(this._sizers, Math.max(0, height - this._fixed));
                break;
            case 'right-to-left':
                delta = boxengine_1.BoxEngine.calc(this._sizers, Math.max(0, width - this._fixed));
                left += width;
                break;
            case 'bottom-to-top':
                delta = boxengine_1.BoxEngine.calc(this._sizers, Math.max(0, height - this._fixed));
                top += height;
                break;
            default:
                throw 'unreachable';
        }
        // Setup the variables for justification and alignment offset.
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
            // Update the widget geometry and advance the relevant edge.
            switch (this._direction) {
                case 'left-to-right':
                    item.update(left + offset, top, size + extra, height);
                    left += size + extra + this._spacing;
                    break;
                case 'top-to-bottom':
                    item.update(left, top + offset, width, size + extra);
                    top += size + extra + this._spacing;
                    break;
                case 'right-to-left':
                    item.update(left - offset - size - extra, top, size + extra, height);
                    left -= size + extra + this._spacing;
                    break;
                case 'bottom-to-top':
                    item.update(left, top - offset - size - extra, width, size + extra);
                    top -= size + extra + this._spacing;
                    break;
                default:
                    throw 'unreachable';
            }
        }
    };
    return BoxLayout;
}(panellayout_1.PanelLayout));
exports.BoxLayout = BoxLayout;
/**
 * The namespace for the `BoxLayout` class statics.
 */
(function (BoxLayout) {
    /**
     * Get the box layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box layout stretch factor for the widget.
     */
    function getStretch(widget) {
        return Private.stretchProperty.get(widget);
    }
    BoxLayout.getStretch = getStretch;
    /**
     * Set the box layout stretch factor for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the stretch factor.
     */
    function setStretch(widget, value) {
        Private.stretchProperty.set(widget, value);
    }
    BoxLayout.setStretch = setStretch;
    /**
     * Get the box layout size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The box layout size basis for the widget.
     */
    function getSizeBasis(widget) {
        return Private.sizeBasisProperty.get(widget);
    }
    BoxLayout.getSizeBasis = getSizeBasis;
    /**
     * Set the box layout size basis for the given widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the size basis.
     */
    function setSizeBasis(widget, value) {
        Private.sizeBasisProperty.set(widget, value);
    }
    BoxLayout.setSizeBasis = setSizeBasis;
})(BoxLayout = exports.BoxLayout || (exports.BoxLayout = {}));
exports.BoxLayout = BoxLayout;
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
     * The property descriptor for a widget size basis.
     */
    Private.sizeBasisProperty = new properties_1.AttachedProperty({
        name: 'sizeBasis',
        create: function () { return 0; },
        coerce: function (owner, value) { return Math.max(0, Math.floor(value)); },
        changed: onChildSizingChanged
    });
    /**
     * Test whether a direction has horizontal orientation.
     */
    function isHorizontal(dir) {
        return dir === 'left-to-right' || dir === 'right-to-left';
    }
    Private.isHorizontal = isHorizontal;
    /**
     * Clamp a spacing value to an integer >= 0.
     */
    function clampSpacing(value) {
        return Math.max(0, Math.floor(value));
    }
    Private.clampSpacing = clampSpacing;
    /**
     * The change handler for the attached sizing properties.
     */
    function onChildSizingChanged(child) {
        if (child.parent && child.parent.layout instanceof BoxLayout) {
            child.parent.fit();
        }
    }
})(Private || (Private = {}));
