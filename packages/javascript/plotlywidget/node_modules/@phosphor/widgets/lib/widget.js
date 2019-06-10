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
var messaging_1 = require("@phosphor/messaging");
var properties_1 = require("@phosphor/properties");
var signaling_1 = require("@phosphor/signaling");
var title_1 = require("./title");
/**
 * The base class of the Phosphor widget hierarchy.
 *
 * #### Notes
 * This class will typically be subclassed in order to create a useful
 * widget. However, it can be used directly to host externally created
 * content.
 */
var Widget = (function () {
    /**
     * Construct a new widget.
     *
     * @param options - The options for initializing the widget.
     */
    function Widget(options) {
        if (options === void 0) { options = {}; }
        this._flags = 0;
        this._layout = null;
        this._parent = null;
        this._disposed = new signaling_1.Signal(this);
        this.node = Private.createNode(options);
        this.addClass('p-Widget');
    }
    /**
     * Dispose of the widget and its descendant widgets.
     *
     * #### Notes
     * It is unsafe to use the widget after it has been disposed.
     *
     * All calls made to this method after the first are a no-op.
     */
    Widget.prototype.dispose = function () {
        // Do nothing if the widget is already disposed.
        if (this.isDisposed) {
            return;
        }
        // Set the disposed flag and emit the disposed signal.
        this.setFlag(Widget.Flag.IsDisposed);
        this._disposed.emit(undefined);
        // Remove or detach the widget if necessary.
        if (this.parent) {
            this.parent = null;
        }
        else if (this.isAttached) {
            Widget.detach(this);
        }
        // Dispose of the widget layout.
        if (this._layout) {
            this._layout.dispose();
            this._layout = null;
        }
        // Clear the extra data associated with the widget.
        signaling_1.Signal.clearData(this);
        messaging_1.MessageLoop.clearData(this);
        properties_1.AttachedProperty.clearData(this);
    };
    Object.defineProperty(Widget.prototype, "disposed", {
        /**
         * A signal emitted when the widget is disposed.
         */
        get: function () {
            return this._disposed;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "isDisposed", {
        /**
         * Test whether the widget has been disposed.
         */
        get: function () {
            return this.testFlag(Widget.Flag.IsDisposed);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "isAttached", {
        /**
         * Test whether the widget's node is attached to the DOM.
         */
        get: function () {
            return this.testFlag(Widget.Flag.IsAttached);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "isHidden", {
        /**
         * Test whether the widget is explicitly hidden.
         */
        get: function () {
            return this.testFlag(Widget.Flag.IsHidden);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "isVisible", {
        /**
         * Test whether the widget is visible.
         *
         * #### Notes
         * A widget is visible when it is attached to the DOM, is not
         * explicitly hidden, and has no explicitly hidden ancestors.
         */
        get: function () {
            return this.testFlag(Widget.Flag.IsVisible);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "title", {
        /**
         * The title object for the widget.
         *
         * #### Notes
         * The title object is used by some container widgets when displaying
         * the widget alongside some title, such as a tab panel or side bar.
         *
         * Since not all widgets will use the title, it is created on demand.
         *
         * The `owner` property of the title is set to this widget.
         */
        get: function () {
            return Private.titleProperty.get(this);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "id", {
        /**
         * Get the id of the widget's DOM node.
         */
        get: function () {
            return this.node.id;
        },
        /**
         * Set the id of the widget's DOM node.
         */
        set: function (value) {
            this.node.id = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "dataset", {
        /**
         * The dataset for the widget's DOM node.
         */
        get: function () {
            return this.node.dataset;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "parent", {
        /**
         * Get the parent of the widget.
         */
        get: function () {
            return this._parent;
        },
        /**
         * Set the parent of the widget.
         *
         * #### Notes
         * Children are typically added to a widget by using a layout, which
         * means user code will not normally set the parent widget directly.
         *
         * The widget will be automatically removed from its old parent.
         *
         * This is a no-op if there is no effective parent change.
         */
        set: function (value) {
            if (this._parent === value) {
                return;
            }
            if (value && this.contains(value)) {
                throw new Error('Invalid parent widget.');
            }
            if (this._parent && !this._parent.isDisposed) {
                var msg = new Widget.ChildMessage('child-removed', this);
                messaging_1.MessageLoop.sendMessage(this._parent, msg);
            }
            this._parent = value;
            if (this._parent && !this._parent.isDisposed) {
                var msg = new Widget.ChildMessage('child-added', this);
                messaging_1.MessageLoop.sendMessage(this._parent, msg);
            }
            if (!this.isDisposed) {
                messaging_1.MessageLoop.sendMessage(this, Widget.Msg.ParentChanged);
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Widget.prototype, "layout", {
        /**
         * Get the layout for the widget.
         */
        get: function () {
            return this._layout;
        },
        /**
         * Set the layout for the widget.
         *
         * #### Notes
         * The layout is single-use only. It cannot be changed after the
         * first assignment.
         *
         * The layout is disposed automatically when the widget is disposed.
         */
        set: function (value) {
            if (this._layout === value) {
                return;
            }
            if (this.testFlag(Widget.Flag.DisallowLayout)) {
                throw new Error('Cannot set widget layout.');
            }
            if (this._layout) {
                throw new Error('Cannot change widget layout.');
            }
            if (value.parent) {
                throw new Error('Cannot change layout parent.');
            }
            this._layout = value;
            value.parent = this;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Create an iterator over the widget's children.
     *
     * @returns A new iterator over the children of the widget.
     *
     * #### Notes
     * The widget must have a populated layout in order to have children.
     *
     * If a layout is not installed, the returned iterator will be empty.
     */
    Widget.prototype.children = function () {
        return this._layout ? this._layout.iter() : algorithm_1.empty();
    };
    /**
     * Test whether a widget is a descendant of this widget.
     *
     * @param widget - The descendant widget of interest.
     *
     * @returns `true` if the widget is a descendant, `false` otherwise.
     */
    Widget.prototype.contains = function (widget) {
        for (var value = widget; value; value = value._parent) {
            if (value === this) {
                return true;
            }
        }
        return false;
    };
    /**
     * Test whether the widget's DOM node has the given class name.
     *
     * @param name - The class name of interest.
     *
     * @returns `true` if the node has the class, `false` otherwise.
     */
    Widget.prototype.hasClass = function (name) {
        return this.node.classList.contains(name);
    };
    /**
     * Add a class name to the widget's DOM node.
     *
     * @param name - The class name to add to the node.
     *
     * #### Notes
     * If the class name is already added to the node, this is a no-op.
     *
     * The class name must not contain whitespace.
     */
    Widget.prototype.addClass = function (name) {
        this.node.classList.add(name);
    };
    /**
     * Remove a class name from the widget's DOM node.
     *
     * @param name - The class name to remove from the node.
     *
     * #### Notes
     * If the class name is not yet added to the node, this is a no-op.
     *
     * The class name must not contain whitespace.
     */
    Widget.prototype.removeClass = function (name) {
        this.node.classList.remove(name);
    };
    /**
     * Toggle a class name on the widget's DOM node.
     *
     * @param name - The class name to toggle on the node.
     *
     * @param force - Whether to force add the class (`true`) or force
     *   remove the class (`false`). If not provided, the presence of
     *   the class will be toggled from its current state.
     *
     * @returns `true` if the class is now present, `false` otherwise.
     *
     * #### Notes
     * The class name must not contain whitespace.
     */
    Widget.prototype.toggleClass = function (name, force) {
        if (force === true) {
            this.node.classList.add(name);
            return true;
        }
        if (force === false) {
            this.node.classList.remove(name);
            return false;
        }
        return this.node.classList.toggle(name);
    };
    /**
     * Post an `'update-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for posting the message.
     */
    Widget.prototype.update = function () {
        messaging_1.MessageLoop.postMessage(this, Widget.Msg.UpdateRequest);
    };
    /**
     * Post a `'fit-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for posting the message.
     */
    Widget.prototype.fit = function () {
        messaging_1.MessageLoop.postMessage(this, Widget.Msg.FitRequest);
    };
    /**
     * Post an `'activate-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for posting the message.
     */
    Widget.prototype.activate = function () {
        messaging_1.MessageLoop.postMessage(this, Widget.Msg.ActivateRequest);
    };
    /**
     * Send a `'close-request'` message to the widget.
     *
     * #### Notes
     * This is a simple convenience method for sending the message.
     */
    Widget.prototype.close = function () {
        messaging_1.MessageLoop.sendMessage(this, Widget.Msg.CloseRequest);
    };
    /**
     * Show the widget and make it visible to its parent widget.
     *
     * #### Notes
     * This causes the [[isHidden]] property to be `false`.
     *
     * If the widget is not explicitly hidden, this is a no-op.
     */
    Widget.prototype.show = function () {
        if (!this.testFlag(Widget.Flag.IsHidden)) {
            return;
        }
        if (this.isAttached && (!this.parent || this.parent.isVisible)) {
            messaging_1.MessageLoop.sendMessage(this, Widget.Msg.BeforeShow);
        }
        this.clearFlag(Widget.Flag.IsHidden);
        this.removeClass('p-mod-hidden');
        if (this.isAttached && (!this.parent || this.parent.isVisible)) {
            messaging_1.MessageLoop.sendMessage(this, Widget.Msg.AfterShow);
        }
        if (this.parent) {
            var msg = new Widget.ChildMessage('child-shown', this);
            messaging_1.MessageLoop.sendMessage(this.parent, msg);
        }
    };
    /**
     * Hide the widget and make it hidden to its parent widget.
     *
     * #### Notes
     * This causes the [[isHidden]] property to be `true`.
     *
     * If the widget is explicitly hidden, this is a no-op.
     */
    Widget.prototype.hide = function () {
        if (this.testFlag(Widget.Flag.IsHidden)) {
            return;
        }
        if (this.isAttached && (!this.parent || this.parent.isVisible)) {
            messaging_1.MessageLoop.sendMessage(this, Widget.Msg.BeforeHide);
        }
        this.setFlag(Widget.Flag.IsHidden);
        this.addClass('p-mod-hidden');
        if (this.isAttached && (!this.parent || this.parent.isVisible)) {
            messaging_1.MessageLoop.sendMessage(this, Widget.Msg.AfterHide);
        }
        if (this.parent) {
            var msg = new Widget.ChildMessage('child-hidden', this);
            messaging_1.MessageLoop.sendMessage(this.parent, msg);
        }
    };
    /**
     * Show or hide the widget according to a boolean value.
     *
     * @param hidden - `true` to hide the widget, or `false` to show it.
     *
     * #### Notes
     * This is a convenience method for `hide()` and `show()`.
     */
    Widget.prototype.setHidden = function (hidden) {
        if (hidden) {
            this.hide();
        }
        else {
            this.show();
        }
    };
    /**
     * Test whether the given widget flag is set.
     *
     * #### Notes
     * This will not typically be called directly by user code.
     */
    Widget.prototype.testFlag = function (flag) {
        return (this._flags & flag) !== 0;
    };
    /**
     * Set the given widget flag.
     *
     * #### Notes
     * This will not typically be called directly by user code.
     */
    Widget.prototype.setFlag = function (flag) {
        this._flags |= flag;
    };
    /**
     * Clear the given widget flag.
     *
     * #### Notes
     * This will not typically be called directly by user code.
     */
    Widget.prototype.clearFlag = function (flag) {
        this._flags &= ~flag;
    };
    /**
     * Process a message sent to the widget.
     *
     * @param msg - The message sent to the widget.
     *
     * #### Notes
     * Subclasses may reimplement this method as needed.
     */
    Widget.prototype.processMessage = function (msg) {
        switch (msg.type) {
            case 'resize':
                this.notifyLayout(msg);
                this.onResize(msg);
                break;
            case 'update-request':
                this.notifyLayout(msg);
                this.onUpdateRequest(msg);
                break;
            case 'fit-request':
                this.notifyLayout(msg);
                this.onFitRequest(msg);
                break;
            case 'before-show':
                this.notifyLayout(msg);
                this.onBeforeShow(msg);
                break;
            case 'after-show':
                this.setFlag(Widget.Flag.IsVisible);
                this.notifyLayout(msg);
                this.onAfterShow(msg);
                break;
            case 'before-hide':
                this.notifyLayout(msg);
                this.onBeforeHide(msg);
                break;
            case 'after-hide':
                this.clearFlag(Widget.Flag.IsVisible);
                this.notifyLayout(msg);
                this.onAfterHide(msg);
                break;
            case 'before-attach':
                this.notifyLayout(msg);
                this.onBeforeAttach(msg);
                break;
            case 'after-attach':
                if (!this.isHidden && (!this.parent || this.parent.isVisible)) {
                    this.setFlag(Widget.Flag.IsVisible);
                }
                this.setFlag(Widget.Flag.IsAttached);
                this.notifyLayout(msg);
                this.onAfterAttach(msg);
                break;
            case 'before-detach':
                this.notifyLayout(msg);
                this.onBeforeDetach(msg);
                break;
            case 'after-detach':
                this.clearFlag(Widget.Flag.IsVisible);
                this.clearFlag(Widget.Flag.IsAttached);
                this.notifyLayout(msg);
                this.onAfterDetach(msg);
                break;
            case 'activate-request':
                this.notifyLayout(msg);
                this.onActivateRequest(msg);
                break;
            case 'close-request':
                this.notifyLayout(msg);
                this.onCloseRequest(msg);
                break;
            case 'child-added':
                this.notifyLayout(msg);
                this.onChildAdded(msg);
                break;
            case 'child-removed':
                this.notifyLayout(msg);
                this.onChildRemoved(msg);
                break;
            default:
                this.notifyLayout(msg);
                break;
        }
    };
    /**
     * Invoke the message processing routine of the widget's layout.
     *
     * @param msg - The message to dispatch to the layout.
     *
     * #### Notes
     * This is a no-op if the widget does not have a layout.
     *
     * This will not typically be called directly by user code.
     */
    Widget.prototype.notifyLayout = function (msg) {
        if (this._layout) {
            this._layout.processParentMessage(msg);
        }
    };
    /**
     * A message handler invoked on a `'close-request'` message.
     *
     * #### Notes
     * The default implementation unparents or detaches the widget.
     */
    Widget.prototype.onCloseRequest = function (msg) {
        if (this.parent) {
            this.parent = null;
        }
        else if (this.isAttached) {
            Widget.detach(this);
        }
    };
    /**
     * A message handler invoked on a `'resize'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onResize = function (msg) { };
    /**
     * A message handler invoked on an `'update-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onUpdateRequest = function (msg) { };
    /**
     * A message handler invoked on a `'fit-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onFitRequest = function (msg) { };
    /**
     * A message handler invoked on an `'activate-request'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onActivateRequest = function (msg) { };
    /**
     * A message handler invoked on a `'before-show'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onBeforeShow = function (msg) { };
    /**
     * A message handler invoked on an `'after-show'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onAfterShow = function (msg) { };
    /**
     * A message handler invoked on a `'before-hide'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onBeforeHide = function (msg) { };
    /**
     * A message handler invoked on an `'after-hide'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onAfterHide = function (msg) { };
    /**
     * A message handler invoked on a `'before-attach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onBeforeAttach = function (msg) { };
    /**
     * A message handler invoked on an `'after-attach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onAfterAttach = function (msg) { };
    /**
     * A message handler invoked on a `'before-detach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onBeforeDetach = function (msg) { };
    /**
     * A message handler invoked on an `'after-detach'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onAfterDetach = function (msg) { };
    /**
     * A message handler invoked on a `'child-added'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onChildAdded = function (msg) { };
    /**
     * A message handler invoked on a `'child-removed'` message.
     *
     * #### Notes
     * The default implementation of this handler is a no-op.
     */
    Widget.prototype.onChildRemoved = function (msg) { };
    return Widget;
}());
exports.Widget = Widget;
/**
 * The namespace for the `Widget` class statics.
 */
(function (Widget) {
    /**
     * An enum of widget bit flags.
     */
    var Flag;
    (function (Flag) {
        /**
         * The widget has been disposed.
         */
        Flag[Flag["IsDisposed"] = 1] = "IsDisposed";
        /**
         * The widget is attached to the DOM.
         */
        Flag[Flag["IsAttached"] = 2] = "IsAttached";
        /**
         * The widget is hidden.
         */
        Flag[Flag["IsHidden"] = 4] = "IsHidden";
        /**
         * The widget is visible.
         */
        Flag[Flag["IsVisible"] = 8] = "IsVisible";
        /**
         * A layout cannot be set on the widget.
         */
        Flag[Flag["DisallowLayout"] = 16] = "DisallowLayout";
    })(Flag = Widget.Flag || (Widget.Flag = {}));
    /**
     * A collection of stateless messages related to widgets.
     */
    var Msg;
    (function (Msg) {
        /**
         * A singleton `'before-show'` message.
         *
         * #### Notes
         * This message is sent to a widget before it becomes visible.
         *
         * This message is **not** sent when the widget is being attached.
         */
        Msg.BeforeShow = new messaging_1.Message('before-show');
        /**
         * A singleton `'after-show'` message.
         *
         * #### Notes
         * This message is sent to a widget after it becomes visible.
         *
         * This message is **not** sent when the widget is being attached.
         */
        Msg.AfterShow = new messaging_1.Message('after-show');
        /**
         * A singleton `'before-hide'` message.
         *
         * #### Notes
         * This message is sent to a widget before it becomes not-visible.
         *
         * This message is **not** sent when the widget is being detached.
         */
        Msg.BeforeHide = new messaging_1.Message('before-hide');
        /**
         * A singleton `'after-hide'` message.
         *
         * #### Notes
         * This message is sent to a widget after it becomes not-visible.
         *
         * This message is **not** sent when the widget is being detached.
         */
        Msg.AfterHide = new messaging_1.Message('after-hide');
        /**
         * A singleton `'before-attach'` message.
         *
         * #### Notes
         * This message is sent to a widget before it is attached.
         */
        Msg.BeforeAttach = new messaging_1.Message('before-attach');
        /**
         * A singleton `'after-attach'` message.
         *
         * #### Notes
         * This message is sent to a widget after it is attached.
         */
        Msg.AfterAttach = new messaging_1.Message('after-attach');
        /**
         * A singleton `'before-detach'` message.
         *
         * #### Notes
         * This message is sent to a widget before it is detached.
         */
        Msg.BeforeDetach = new messaging_1.Message('before-detach');
        /**
         * A singleton `'after-detach'` message.
         *
         * #### Notes
         * This message is sent to a widget after it is detached.
         */
        Msg.AfterDetach = new messaging_1.Message('after-detach');
        /**
         * A singleton `'parent-changed'` message.
         *
         * #### Notes
         * This message is sent to a widget when its parent has changed.
         */
        Msg.ParentChanged = new messaging_1.Message('parent-changed');
        /**
         * A singleton conflatable `'update-request'` message.
         *
         * #### Notes
         * This message can be dispatched to supporting widgets in order to
         * update their content based on the current widget state. Not all
         * widgets will respond to messages of this type.
         *
         * For widgets with a layout, this message will inform the layout to
         * update the position and size of its child widgets.
         */
        Msg.UpdateRequest = new messaging_1.ConflatableMessage('update-request');
        /**
         * A singleton conflatable `'fit-request'` message.
         *
         * #### Notes
         * For widgets with a layout, this message will inform the layout to
         * recalculate its size constraints to fit the space requirements of
         * its child widgets, and to update their position and size. Not all
         * layouts will respond to messages of this type.
         */
        Msg.FitRequest = new messaging_1.ConflatableMessage('fit-request');
        /**
         * A singleton conflatable `'activate-request'` message.
         *
         * #### Notes
         * This message should be dispatched to a widget when it should
         * perform the actions necessary to activate the widget, which
         * may include focusing its node or descendant node.
         */
        Msg.ActivateRequest = new messaging_1.ConflatableMessage('activate-request');
        /**
         * A singleton conflatable `'close-request'` message.
         *
         * #### Notes
         * This message should be dispatched to a widget when it should close
         * and remove itself from the widget hierarchy.
         */
        Msg.CloseRequest = new messaging_1.ConflatableMessage('close-request');
    })(Msg = Widget.Msg || (Widget.Msg = {}));
    /**
     * A message class for child related messages.
     */
    var ChildMessage = (function (_super) {
        __extends(ChildMessage, _super);
        /**
         * Construct a new child message.
         *
         * @param type - The message type.
         *
         * @param child - The child widget for the message.
         */
        function ChildMessage(type, child) {
            var _this = _super.call(this, type) || this;
            _this.child = child;
            return _this;
        }
        return ChildMessage;
    }(messaging_1.Message));
    Widget.ChildMessage = ChildMessage;
    /**
     * A message class for `'resize'` messages.
     */
    var ResizeMessage = (function (_super) {
        __extends(ResizeMessage, _super);
        /**
         * Construct a new resize message.
         *
         * @param width - The **offset width** of the widget, or `-1` if
         *   the width is not known.
         *
         * @param height - The **offset height** of the widget, or `-1` if
         *   the height is not known.
         */
        function ResizeMessage(width, height) {
            var _this = _super.call(this, 'resize') || this;
            _this.width = width;
            _this.height = height;
            return _this;
        }
        return ResizeMessage;
    }(messaging_1.Message));
    Widget.ResizeMessage = ResizeMessage;
    /**
     * The namespace for the `ResizeMessage` class statics.
     */
    (function (ResizeMessage) {
        /**
         * A singleton `'resize'` message with an unknown size.
         */
        ResizeMessage.UnknownSize = new ResizeMessage(-1, -1);
    })(ResizeMessage = Widget.ResizeMessage || (Widget.ResizeMessage = {}));
    /**
     * Attach a widget to a host DOM node.
     *
     * @param widget - The widget of interest.
     *
     * @param host - The DOM node to use as the widget's host.
     *
     * @param ref - The child of `host` to use as the reference element.
     *   If this is provided, the widget will be inserted before this
     *   node in the host. The default is `null`, which will cause the
     *   widget to be added as the last child of the host.
     *
     * #### Notes
     * This will throw an error if the widget is not a root widget, if
     * the widget is already attached, or if the host is not attached
     * to the DOM.
     */
    function attach(widget, host, ref) {
        if (ref === void 0) { ref = null; }
        if (widget.parent) {
            throw new Error('Cannot attach a child widget.');
        }
        if (widget.isAttached || document.body.contains(widget.node)) {
            throw new Error('Widget is already attached.');
        }
        if (!document.body.contains(host)) {
            throw new Error('Host is not attached.');
        }
        messaging_1.MessageLoop.sendMessage(widget, Widget.Msg.BeforeAttach);
        host.insertBefore(widget.node, ref);
        messaging_1.MessageLoop.sendMessage(widget, Widget.Msg.AfterAttach);
    }
    Widget.attach = attach;
    /**
     * Detach the widget from its host DOM node.
     *
     * @param widget - The widget of interest.
     *
     * #### Notes
     * This will throw an error if the widget is not a root widget,
     * or if the widget is not attached to the DOM.
     */
    function detach(widget) {
        if (widget.parent) {
            throw new Error('Cannot detach a child widget.');
        }
        if (!widget.isAttached || !document.body.contains(widget.node)) {
            throw new Error('Widget is not attached.');
        }
        messaging_1.MessageLoop.sendMessage(widget, Widget.Msg.BeforeDetach);
        widget.node.parentNode.removeChild(widget.node);
        messaging_1.MessageLoop.sendMessage(widget, Widget.Msg.AfterDetach);
    }
    Widget.detach = detach;
})(Widget = exports.Widget || (exports.Widget = {}));
exports.Widget = Widget;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * An attached property for the widget title object.
     */
    Private.titleProperty = new properties_1.AttachedProperty({
        name: 'title',
        create: function (owner) { return new title_1.Title({ owner: owner }); },
    });
    /**
     * Create a DOM node for the given widget options.
     */
    function createNode(options) {
        return options.node || document.createElement('div');
    }
    Private.createNode = createNode;
})(Private || (Private = {}));
