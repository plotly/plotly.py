"use strict";
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
var signaling_1 = require("@phosphor/signaling");
var widget_1 = require("./widget");
/**
 * An abstract base class for creating Phosphor layouts.
 *
 * #### Notes
 * A layout is used to add widgets to a parent and to arrange those
 * widgets within the parent's DOM node.
 *
 * This class implements the base functionality which is required of
 * nearly all layouts. It must be subclassed in order to be useful.
 *
 * Notably, this class does not define a uniform interface for adding
 * widgets to the layout. A subclass should define that API in a way
 * which is meaningful for its intended use.
 */
var Layout = (function () {
    /**
     * Construct a new layout.
     *
     * @param options - The options for initializing the layout.
     */
    function Layout(options) {
        if (options === void 0) { options = {}; }
        this._disposed = false;
        this._parent = null;
        this._fitPolicy = options.fitPolicy || 'set-min-size';
    }
    /**
     * Dispose of the resources held by the layout.
     *
     * #### Notes
     * This should be reimplemented to clear and dispose of the widgets.
     *
     * All reimplementations should call the superclass method.
     *
     * This method is called automatically when the parent is disposed.
     */
    Layout.prototype.dispose = function () {
        this._parent = null;
        this._disposed = true;
        signaling_1.Signal.clearData(this);
        properties_1.AttachedProperty.clearData(this);
    };
    Object.defineProperty(Layout.prototype, "isDisposed", {
        /**
         * Test whether the layout is disposed.
         */
        get: function () {
            return this._disposed;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Layout.prototype, "parent", {
        /**
         * Get the parent widget of the layout.
         */
        get: function () {
            return this._parent;
        },
        /**
         * Set the parent widget of the layout.
         *
         * #### Notes
         * This is set automatically when installing the layout on the parent
         * widget. The parent widget should not be set directly by user code.
         */
        set: function (value) {
            if (this._parent === value) {
                return;
            }
            if (this._parent) {
                throw new Error('Cannot change parent widget.');
            }
            if (value.layout !== this) {
                throw new Error('Invalid parent widget.');
            }
            this._parent = value;
            this.init();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Layout.prototype, "fitPolicy", {
        /**
         * Get the fit policy for the layout.
         *
         * #### Notes
         * The fit policy controls the computed size constraints which are
         * applied to the parent widget by the layout.
         *
         * Some layout implementations may ignore the fit policy.
         */
        get: function () {
            return this._fitPolicy;
        },
        /**
         * Set the fit policy for the layout.
         *
         * #### Notes
         * The fit policy controls the computed size constraints which are
         * applied to the parent widget by the layout.
         *
         * Some layout implementations may ignore the fit policy.
         *
         * Changing the fit policy will clear the current size constraint
         * for the parent widget and then re-fit the parent.
         */
        set: function (value) {
            // Bail if the policy does not change
            if (this._fitPolicy === value) {
                return;
            }
            // Update the internal policy.
            this._fitPolicy = value;
            // Clear the size constraints and schedule a fit of the parent.
            if (this._parent) {
                var style = this._parent.node.style;
                style.minWidth = '';
                style.minHeight = '';
                style.maxWidth = '';
                style.maxHeight = '';
                this._parent.fit();
            }
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Process a message sent to the parent widget.
     *
     * @param msg - The message sent to the parent widget.
     *
     * #### Notes
     * This method is called by the parent widget to process a message.
     *
     * Subclasses may reimplement this method as needed.
     */
    Layout.prototype.processParentMessage = function (msg) {
        switch (msg.type) {
            case 'resize':
                this.onResize(msg);
                break;
            case 'update-request':
                this.onUpdateRequest(msg);
                break;
            case 'fit-request':
                this.onFitRequest(msg);
                break;
            case 'before-show':
                this.onBeforeShow(msg);
                break;
            case 'after-show':
                this.onAfterShow(msg);
                break;
            case 'before-hide':
                this.onBeforeHide(msg);
                break;
            case 'after-hide':
                this.onAfterHide(msg);
                break;
            case 'before-attach':
                this.onBeforeAttach(msg);
                break;
            case 'after-attach':
                this.onAfterAttach(msg);
                break;
            case 'before-detach':
                this.onBeforeDetach(msg);
                break;
            case 'after-detach':
                this.onAfterDetach(msg);
                break;
            case 'child-removed':
                this.onChildRemoved(msg);
                break;
            case 'child-shown':
                this.onChildShown(msg);
                break;
            case 'child-hidden':
                this.onChildHidden(msg);
                break;
        }
    };
    /**
     * Perform layout initialization which requires the parent widget.
     *
     * #### Notes
     * This method is invoked immediately after the layout is installed
     * on the parent widget.
     *
     * The default implementation reparents all of the widgets to the
     * layout parent widget.
     *
     * Subclasses should reimplement this method and attach the child
     * widget nodes to the parent widget's node.
     */
    Layout.prototype.init = function () {
        var _this = this;
        algorithm_1.each(this, function (widget) {
            widget.parent = _this.parent;
        });
    };
    /**
     * A message handler invoked on a `'resize'` message.
     *
     * #### Notes
     * The layout should ensure that its widgets are resized according
     * to the specified layout space, and that they are sent a `'resize'`
     * message if appropriate.
     *
     * The default implementation of this method sends an `UnknownSize`
     * resize message to all widgets.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onResize = function (msg) {
        algorithm_1.each(this, function (widget) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.ResizeMessage.UnknownSize);
        });
    };
    /**
     * A message handler invoked on an `'update-request'` message.
     *
     * #### Notes
     * The layout should ensure that its widgets are resized according
     * to the available layout space, and that they are sent a `'resize'`
     * message if appropriate.
     *
     * The default implementation of this method sends an `UnknownSize`
     * resize message to all widgets.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onUpdateRequest = function (msg) {
        algorithm_1.each(this, function (widget) {
            messaging_1.MessageLoop.sendMessage(widget, widget_1.Widget.ResizeMessage.UnknownSize);
        });
    };
    /**
     * A message handler invoked on a `'before-attach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onBeforeAttach = function (msg) {
        algorithm_1.each(this, function (widget) {
            messaging_1.MessageLoop.sendMessage(widget, msg);
        });
    };
    /**
     * A message handler invoked on an `'after-attach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onAfterAttach = function (msg) {
        algorithm_1.each(this, function (widget) {
            messaging_1.MessageLoop.sendMessage(widget, msg);
        });
    };
    /**
     * A message handler invoked on a `'before-detach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onBeforeDetach = function (msg) {
        algorithm_1.each(this, function (widget) {
            messaging_1.MessageLoop.sendMessage(widget, msg);
        });
    };
    /**
     * A message handler invoked on an `'after-detach'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message
     * to all widgets. It assumes all widget nodes are attached to the
     * parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onAfterDetach = function (msg) {
        algorithm_1.each(this, function (widget) {
            messaging_1.MessageLoop.sendMessage(widget, msg);
        });
    };
    /**
     * A message handler invoked on a `'before-show'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onBeforeShow = function (msg) {
        algorithm_1.each(this, function (widget) {
            if (!widget.isHidden) {
                messaging_1.MessageLoop.sendMessage(widget, msg);
            }
        });
    };
    /**
     * A message handler invoked on an `'after-show'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onAfterShow = function (msg) {
        algorithm_1.each(this, function (widget) {
            if (!widget.isHidden) {
                messaging_1.MessageLoop.sendMessage(widget, msg);
            }
        });
    };
    /**
     * A message handler invoked on a `'before-hide'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onBeforeHide = function (msg) {
        algorithm_1.each(this, function (widget) {
            if (!widget.isHidden) {
                messaging_1.MessageLoop.sendMessage(widget, msg);
            }
        });
    };
    /**
     * A message handler invoked on an `'after-hide'` message.
     *
     * #### Notes
     * The default implementation of this method forwards the message to
     * all non-hidden widgets. It assumes all widget nodes are attached
     * to the parent widget node.
     *
     * This may be reimplemented by subclasses as needed.
     */
    Layout.prototype.onAfterHide = function (msg) {
        algorithm_1.each(this, function (widget) {
            if (!widget.isHidden) {
                messaging_1.MessageLoop.sendMessage(widget, msg);
            }
        });
    };
    /**
     * A message handler invoked on a `'child-removed'` message.
     *
     * #### Notes
     * This will remove the child widget from the layout.
     *
     * Subclasses should **not** typically reimplement this method.
     */
    Layout.prototype.onChildRemoved = function (msg) {
        this.removeWidget(msg.child);
    };
    /**
     * A message handler invoked on a `'fit-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Layout.prototype.onFitRequest = function (msg) { };
    /**
     * A message handler invoked on a `'child-shown'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Layout.prototype.onChildShown = function (msg) { };
    /**
     * A message handler invoked on a `'child-hidden'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Layout.prototype.onChildHidden = function (msg) { };
    return Layout;
}());
exports.Layout = Layout;
/**
 * The namespace for the `Layout` class statics.
 */
(function (Layout) {
    /**
     * Get the horizontal alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The horizontal alignment for the widget.
     *
     * #### Notes
     * If the layout width allocated to a widget is larger than its max
     * width, the horizontal alignment controls how the widget is placed
     * within the extra horizontal space.
     *
     * If the allocated width is less than the widget's max width, the
     * horizontal alignment has no effect.
     *
     * Some layout implementations may ignore horizontal alignment.
     */
    function getHorizontalAlignment(widget) {
        return Private.horizontalAlignmentProperty.get(widget);
    }
    Layout.getHorizontalAlignment = getHorizontalAlignment;
    /**
     * Set the horizontal alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the horizontal alignment.
     *
     * #### Notes
     * If the layout width allocated to a widget is larger than its max
     * width, the horizontal alignment controls how the widget is placed
     * within the extra horizontal space.
     *
     * If the allocated width is less than the widget's max width, the
     * horizontal alignment has no effect.
     *
     * Some layout implementations may ignore horizontal alignment.
     *
     * Changing the horizontal alignment will post an `update-request`
     * message to widget's parent, provided the parent has a layout
     * installed.
     */
    function setHorizontalAlignment(widget, value) {
        Private.horizontalAlignmentProperty.set(widget, value);
    }
    Layout.setHorizontalAlignment = setHorizontalAlignment;
    /**
     * Get the vertical alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The vertical alignment for the widget.
     *
     * #### Notes
     * If the layout height allocated to a widget is larger than its max
     * height, the vertical alignment controls how the widget is placed
     * within the extra vertical space.
     *
     * If the allocated height is less than the widget's max height, the
     * vertical alignment has no effect.
     *
     * Some layout implementations may ignore vertical alignment.
     */
    function getVerticalAlignment(widget) {
        return Private.verticalAlignmentProperty.get(widget);
    }
    Layout.getVerticalAlignment = getVerticalAlignment;
    /**
     * Set the vertical alignment for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @param value - The value for the vertical alignment.
     *
     * #### Notes
     * If the layout height allocated to a widget is larger than its max
     * height, the vertical alignment controls how the widget is placed
     * within the extra vertical space.
     *
     * If the allocated height is less than the widget's max height, the
     * vertical alignment has no effect.
     *
     * Some layout implementations may ignore vertical alignment.
     *
     * Changing the horizontal alignment will post an `update-request`
     * message to widget's parent, provided the parent has a layout
     * installed.
     */
    function setVerticalAlignment(widget, value) {
        Private.verticalAlignmentProperty.set(widget, value);
    }
    Layout.setVerticalAlignment = setVerticalAlignment;
})(Layout = exports.Layout || (exports.Layout = {}));
exports.Layout = Layout;
/**
 * An object which assists in the absolute layout of widgets.
 *
 * #### Notes
 * This class is useful when implementing a layout which arranges its
 * widgets using absolute positioning.
 *
 * This class is used by nearly all of the built-in Phosphor layouts.
 */
var LayoutItem = (function () {
    /**
     * Construct a new layout item.
     *
     * @param widget - The widget to be managed by the item.
     *
     * #### Notes
     * The widget will be set to absolute positioning.
     */
    function LayoutItem(widget) {
        this._top = NaN;
        this._left = NaN;
        this._width = NaN;
        this._height = NaN;
        this._minWidth = 0;
        this._minHeight = 0;
        this._maxWidth = Infinity;
        this._maxHeight = Infinity;
        this._disposed = false;
        this.widget = widget;
        this.widget.node.style.position = 'absolute';
    }
    /**
     * Dispose of the the layout item.
     *
     * #### Notes
     * This will reset the positioning of the widget.
     */
    LayoutItem.prototype.dispose = function () {
        // Do nothing if the item is already disposed.
        if (this._disposed) {
            return;
        }
        // Mark the item as disposed.
        this._disposed = true;
        // Reset the widget style.
        var style = this.widget.node.style;
        style.position = '';
        style.top = '';
        style.left = '';
        style.width = '';
        style.height = '';
    };
    Object.defineProperty(LayoutItem.prototype, "minWidth", {
        /**
         * The computed minimum width of the widget.
         *
         * #### Notes
         * This value can be updated by calling the `fit` method.
         */
        get: function () {
            return this._minWidth;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "minHeight", {
        /**
         * The computed minimum height of the widget.
         *
         * #### Notes
         * This value can be updated by calling the `fit` method.
         */
        get: function () {
            return this._minHeight;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "maxWidth", {
        /**
         * The computed maximum width of the widget.
         *
         * #### Notes
         * This value can be updated by calling the `fit` method.
         */
        get: function () {
            return this._maxWidth;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "maxHeight", {
        /**
         * The computed maximum height of the widget.
         *
         * #### Notes
         * This value can be updated by calling the `fit` method.
         */
        get: function () {
            return this._maxHeight;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "isDisposed", {
        /**
         * Whether the layout item is disposed.
         */
        get: function () {
            return this._disposed;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "isHidden", {
        /**
         * Whether the managed widget is hidden.
         */
        get: function () {
            return this.widget.isHidden;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "isVisible", {
        /**
         * Whether the managed widget is visible.
         */
        get: function () {
            return this.widget.isVisible;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LayoutItem.prototype, "isAttached", {
        /**
         * Whether the managed widget is attached.
         */
        get: function () {
            return this.widget.isAttached;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Update the computed size limits of the managed widget.
     */
    LayoutItem.prototype.fit = function () {
        var limits = domutils_1.ElementExt.sizeLimits(this.widget.node);
        this._minWidth = limits.minWidth;
        this._minHeight = limits.minHeight;
        this._maxWidth = limits.maxWidth;
        this._maxHeight = limits.maxHeight;
    };
    /**
     * Update the position and size of the managed widget.
     *
     * @param left - The left edge position of the layout box.
     *
     * @param top - The top edge position of the layout box.
     *
     * @param width - The width of the layout box.
     *
     * @param height - The height of the layout box.
     */
    LayoutItem.prototype.update = function (left, top, width, height) {
        // Clamp the size to the computed size limits.
        var clampW = Math.max(this._minWidth, Math.min(width, this._maxWidth));
        var clampH = Math.max(this._minHeight, Math.min(height, this._maxHeight));
        // Ajdust the left edge for the horizontal alignment, if needed.
        if (clampW < width) {
            switch (Layout.getHorizontalAlignment(this.widget)) {
                case 'left':
                    break;
                case 'center':
                    left += (width - clampW) / 2;
                    break;
                case 'right':
                    left += width - clampW;
                    break;
                default:
                    throw 'unreachable';
            }
        }
        // Ajdust the top edge for the vertical alignment, if needed.
        if (clampH < height) {
            switch (Layout.getVerticalAlignment(this.widget)) {
                case 'top':
                    break;
                case 'center':
                    top += (height - clampH) / 2;
                    break;
                case 'bottom':
                    top += height - clampH;
                    break;
                default:
                    throw 'unreachable';
            }
        }
        // Set up the resize variables.
        var resized = false;
        var style = this.widget.node.style;
        // Update the top edge of the widget if needed.
        if (this._top !== top) {
            this._top = top;
            style.top = top + "px";
        }
        // Update the left edge of the widget if needed.
        if (this._left !== left) {
            this._left = left;
            style.left = left + "px";
        }
        // Update the width of the widget if needed.
        if (this._width !== clampW) {
            resized = true;
            this._width = clampW;
            style.width = clampW + "px";
        }
        // Update the height of the widget if needed.
        if (this._height !== clampH) {
            resized = true;
            this._height = clampH;
            style.height = clampH + "px";
        }
        // Send a resize message to the widget if needed.
        if (resized) {
            var msg = new widget_1.Widget.ResizeMessage(clampW, clampH);
            messaging_1.MessageLoop.sendMessage(this.widget, msg);
        }
    };
    return LayoutItem;
}());
exports.LayoutItem = LayoutItem;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The attached property for a widget horizontal alignment.
     */
    Private.horizontalAlignmentProperty = new properties_1.AttachedProperty({
        name: 'horizontalAlignment',
        create: function () { return 'center'; },
        changed: onAlignmentChanged
    });
    /**
     * The attached property for a widget vertical alignment.
     */
    Private.verticalAlignmentProperty = new properties_1.AttachedProperty({
        name: 'verticalAlignment',
        create: function () { return 'top'; },
        changed: onAlignmentChanged
    });
    /**
     * The change handler for the attached alignment properties.
     */
    function onAlignmentChanged(child) {
        if (child.parent && child.parent.layout) {
            child.parent.update();
        }
    }
})(Private || (Private = {}));
