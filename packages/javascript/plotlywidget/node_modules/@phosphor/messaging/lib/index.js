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
var collections_1 = require("@phosphor/collections");
/**
 * A message which can be delivered to a message handler.
 *
 * #### Notes
 * This class may be subclassed to create complex message types.
 */
var Message = (function () {
    /**
     * Construct a new message.
     *
     * @param type - The type of the message.
     */
    function Message(type) {
        this.type = type;
    }
    Object.defineProperty(Message.prototype, "isConflatable", {
        /**
         * Test whether the message is conflatable.
         *
         * #### Notes
         * Message conflation is an advanced topic. Most message types will
         * not make use of this feature.
         *
         * If a conflatable message is posted to a handler while another
         * conflatable message of the same `type` has already been posted
         * to the handler, the `conflate()` method of the existing message
         * will be invoked. If that method returns `true`, the new message
         * will not be enqueued. This allows messages to be compressed, so
         * that only a single instance of the message type is processed per
         * cycle, no matter how many times messages of that type are posted.
         *
         * Custom message types may reimplement this property.
         *
         * The default implementation is always `false`.
         */
        get: function () {
            return false;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Conflate this message with another message of the same `type`.
     *
     * @param other - A conflatable message of the same `type`.
     *
     * @returns `true` if the message was successfully conflated, or
     *   `false` otherwise.
     *
     * #### Notes
     * Message conflation is an advanced topic. Most message types will
     * not make use of this feature.
     *
     * This method is called automatically by the message loop when the
     * given message is posted to the handler paired with this message.
     * This message will already be enqueued and conflatable, and the
     * given message will have the same `type` and also be conflatable.
     *
     * This method should merge the state of the other message into this
     * message as needed so that when this message is finally delivered
     * to the handler, it receives the most up-to-date information.
     *
     * If this method returns `true`, it signals that the other message
     * was successfully conflated and that message will not be enqueued.
     *
     * If this method returns `false`, the other message will be enqueued
     * for normal delivery.
     *
     * Custom message types may reimplement this method.
     *
     * The default implementation always returns `false`.
     */
    Message.prototype.conflate = function (other) {
        return false;
    };
    return Message;
}());
exports.Message = Message;
/**
 * A convenience message class which conflates automatically.
 *
 * #### Notes
 * Message conflation is an advanced topic. Most user code will not
 * make use of this class.
 *
 * This message class is useful for creating message instances which
 * should be conflated, but which have no state other than `type`.
 *
 * If conflation of stateful messages is required, a custom `Message`
 * subclass should be created.
 */
var ConflatableMessage = (function (_super) {
    __extends(ConflatableMessage, _super);
    function ConflatableMessage() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(ConflatableMessage.prototype, "isConflatable", {
        /**
         * Test whether the message is conflatable.
         *
         * #### Notes
         * This property is always `true`.
         */
        get: function () {
            return true;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Conflate this message with another message of the same `type`.
     *
     * #### Notes
     * This method always returns `true`.
     */
    ConflatableMessage.prototype.conflate = function (other) {
        return true;
    };
    return ConflatableMessage;
}(Message));
exports.ConflatableMessage = ConflatableMessage;
/**
 * The namespace for the global singleton message loop.
 */
var MessageLoop;
(function (MessageLoop) {
    /**
     * Send a message to a message handler to process immediately.
     *
     * @param handler - The handler which should process the message.
     *
     * @param msg - The message to deliver to the handler.
     *
     * #### Notes
     * The message will first be sent through any installed message hooks
     * for the handler. If the message passes all hooks, it will then be
     * delivered to the `processMessage` method of the handler.
     *
     * The message will not be conflated with pending posted messages.
     *
     * Exceptions in hooks and handlers will be caught and logged.
     */
    function sendMessage(handler, msg) {
        // Lookup the message hooks for the handler.
        var hooks = messageHooks.get(handler);
        // Handle the common case of no installed hooks.
        if (!hooks || hooks.length === 0) {
            invokeHandler(handler, msg);
            return;
        }
        // Invoke the message hooks starting with the newest first.
        var passed = algorithm_1.every(algorithm_1.retro(hooks), function (hook) {
            return hook ? invokeHook(hook, handler, msg) : true;
        });
        // Invoke the handler if the message passes all hooks.
        if (passed) {
            invokeHandler(handler, msg);
        }
    }
    MessageLoop.sendMessage = sendMessage;
    /**
     * Post a message to a message handler to process in the future.
     *
     * @param handler - The handler which should process the message.
     *
     * @param msg - The message to post to the handler.
     *
     * #### Notes
     * The message will be conflated with the pending posted messages for
     * the handler, if possible. If the message is not conflated, it will
     * be queued for normal delivery on the next cycle of the event loop.
     *
     * Exceptions in hooks and handlers will be caught and logged.
     */
    function postMessage(handler, msg) {
        // Handle the common case of a non-conflatable message.
        if (!msg.isConflatable) {
            enqueueMessage(handler, msg);
            return;
        }
        // Conflate the message with an existing message if possible.
        var conflated = algorithm_1.some(messageQueue, function (posted) {
            if (posted.handler !== handler) {
                return false;
            }
            if (!posted.msg) {
                return false;
            }
            if (posted.msg.type !== msg.type) {
                return false;
            }
            if (!posted.msg.isConflatable) {
                return false;
            }
            return posted.msg.conflate(msg);
        });
        // Enqueue the message if it was not conflated.
        if (!conflated) {
            enqueueMessage(handler, msg);
        }
    }
    MessageLoop.postMessage = postMessage;
    /**
     * Install a message hook for a message handler.
     *
     * @param handler - The message handler of interest.
     *
     * @param hook - The message hook to install.
     *
     * #### Notes
     * A message hook is invoked before a message is delivered to the
     * handler. If the hook returns `false`, no other hooks will be
     * invoked and the message will not be delivered to the handler.
     *
     * The most recently installed message hook is executed first.
     *
     * If the hook is already installed, this is a no-op.
     */
    function installMessageHook(handler, hook) {
        // Lookup the hooks for the handler.
        var hooks = messageHooks.get(handler);
        // Bail early if the hook is already installed.
        if (hooks && hooks.indexOf(hook) !== -1) {
            return;
        }
        // Add the hook to the end, so it will be the first to execute.
        if (!hooks) {
            messageHooks.set(handler, [hook]);
        }
        else {
            hooks.push(hook);
        }
    }
    MessageLoop.installMessageHook = installMessageHook;
    /**
     * Remove an installed message hook for a message handler.
     *
     * @param handler - The message handler of interest.
     *
     * @param hook - The message hook to remove.
     *
     * #### Notes
     * It is safe to call this function while the hook is executing.
     *
     * If the hook is not installed, this is a no-op.
     */
    function removeMessageHook(handler, hook) {
        // Lookup the hooks for the handler.
        var hooks = messageHooks.get(handler);
        // Bail early if the hooks do not exist.
        if (!hooks) {
            return;
        }
        // Lookup the index of the hook and bail if not found.
        var i = hooks.indexOf(hook);
        if (i === -1) {
            return;
        }
        // Clear the hook and schedule a cleanup of the array.
        hooks[i] = null;
        scheduleCleanup(hooks);
    }
    MessageLoop.removeMessageHook = removeMessageHook;
    /**
     * Clear all message data associated with a message handler.
     *
     * @param handler - The message handler of interest.
     *
     * #### Notes
     * This will clear all posted messages and hooks for the handler.
     */
    function clearData(handler) {
        // Lookup the hooks for the handler.
        var hooks = messageHooks.get(handler);
        // Clear all messsage hooks for the handler.
        if (hooks && hooks.length > 0) {
            algorithm_1.ArrayExt.fill(hooks, null);
            scheduleCleanup(hooks);
        }
        // Clear all posted messages for the handler.
        algorithm_1.each(messageQueue, function (posted) {
            if (posted.handler === handler) {
                posted.handler = null;
                posted.msg = null;
            }
        });
    }
    MessageLoop.clearData = clearData;
    /**
     * Process the pending posted messages in the queue immediately.
     *
     * #### Notes
     * This function is useful when posted messages must be processed
     * immediately, instead of on the next animation frame.
     *
     * This function should normally not be needed, but it may be
     * required to work around certain browser idiosyncrasies.
     *
     * Recursing into this function is a no-op.
     */
    function flush() {
        // Bail if recursion is detected or if there is no pending task.
        if (flushGuard || loopTaskID === 0) {
            return;
        }
        // Unschedule the pending loop task.
        unschedule(loopTaskID);
        // Run the message loop within the recursion guard.
        flushGuard = true;
        runMessageLoop();
        flushGuard = false;
    }
    MessageLoop.flush = flush;
    /**
     * Get the message loop exception handler.
     *
     * @returns The current exception handler.
     *
     * #### Notes
     * The default exception handler is `console.error`.
     */
    function getExceptionHandler() {
        return exceptionHandler;
    }
    MessageLoop.getExceptionHandler = getExceptionHandler;
    /**
     * Set the message loop exception handler.
     *
     * @param handler - The function to use as the exception handler.
     *
     * @returns The old exception handler.
     *
     * #### Notes
     * The exception handler is invoked when a message handler or a
     * message hook throws an exception.
     */
    function setExceptionHandler(handler) {
        var old = exceptionHandler;
        exceptionHandler = handler;
        return old;
    }
    MessageLoop.setExceptionHandler = setExceptionHandler;
    /**
     * The queue of posted message pairs.
     */
    var messageQueue = new collections_1.LinkedList();
    /**
     * A mapping of handler to array of installed message hooks.
     */
    var messageHooks = new WeakMap();
    /**
     * A set of message hook arrays which are pending cleanup.
     */
    var dirtySet = new Set();
    /**
     * The message loop exception handler.
     */
    var exceptionHandler = function (err) {
        console.error(err);
    };
    /**
     * The id of the pending loop task animation frame.
     */
    var loopTaskID = 0;
    /**
     * A guard flag to prevent flush recursion.
     */
    var flushGuard = false;
    /**
     * A function to schedule an event loop callback.
     */
    var schedule = (function () {
        var ok = typeof requestAnimationFrame === 'function';
        return ok ? requestAnimationFrame : setImmediate;
    })();
    /**
     * A function to unschedule an event loop callback.
     */
    var unschedule = (function () {
        var ok = typeof cancelAnimationFrame === 'function';
        return ok ? cancelAnimationFrame : clearImmediate;
    })();
    /**
     * Invoke a message hook with the specified handler and message.
     *
     * Returns the result of the hook, or `true` if the hook throws.
     *
     * Exceptions in the hook will be caught and logged.
     */
    function invokeHook(hook, handler, msg) {
        var result = true;
        try {
            if (typeof hook === 'function') {
                result = hook(handler, msg);
            }
            else {
                result = hook.messageHook(handler, msg);
            }
        }
        catch (err) {
            exceptionHandler(err);
        }
        return result;
    }
    /**
     * Invoke a message handler with the specified message.
     *
     * Exceptions in the handler will be caught and logged.
     */
    function invokeHandler(handler, msg) {
        try {
            handler.processMessage(msg);
        }
        catch (err) {
            exceptionHandler(err);
        }
    }
    /**
     * Add a message to the end of the message queue.
     *
     * This will automatically schedule a run of the message loop.
     */
    function enqueueMessage(handler, msg) {
        // Add the posted message to the queue.
        messageQueue.addLast({ handler: handler, msg: msg });
        // Bail if a loop task is already pending.
        if (loopTaskID !== 0) {
            return;
        }
        // Schedule a run of the message loop.
        loopTaskID = schedule(runMessageLoop);
    }
    /**
     * Run an iteration of the message loop.
     *
     * This will process all pending messages in the queue. If a message
     * is added to the queue while the message loop is running, it will
     * be processed on the next cycle of the loop.
     */
    function runMessageLoop() {
        // Clear the task ID so the next loop can be scheduled.
        loopTaskID = 0;
        // If the message queue is empty, there is nothing else to do.
        if (messageQueue.isEmpty) {
            return;
        }
        // Add a sentinel value to the end of the queue. The queue will
        // only be processed up to the sentinel. Messages posted during
        // this cycle will execute on the next cycle.
        var sentinel = { handler: null, msg: null };
        messageQueue.addLast(sentinel);
        // Enter the message loop.
        while (true) {
            // Remove the first posted message in the queue.
            var posted = messageQueue.removeFirst();
            // If the value is the sentinel, exit the loop.
            if (posted === sentinel) {
                return;
            }
            // Dispatch the message if it has not been cleared.
            if (posted.handler && posted.msg) {
                sendMessage(posted.handler, posted.msg);
            }
        }
    }
    /**
     * Schedule a cleanup of a message hooks array.
     *
     * This will add the array to the dirty set and schedule a deferred
     * cleanup of the array contents. On cleanup, any `null` hook will
     * be removed from the array.
     */
    function scheduleCleanup(hooks) {
        if (dirtySet.size === 0) {
            schedule(cleanupDirtySet);
        }
        dirtySet.add(hooks);
    }
    /**
     * Cleanup the message hook arrays in the dirty set.
     *
     * This function should only be invoked asynchronously, when the
     * stack frame is guaranteed to not be on the path of user code.
     */
    function cleanupDirtySet() {
        dirtySet.forEach(cleanupHooks);
        dirtySet.clear();
    }
    /**
     * Cleanup the dirty hooks in a message hooks array.
     *
     * This will remove any `null` hook from the array.
     *
     * This function should only be invoked asynchronously, when the
     * stack frame is guaranteed to not be on the path of user code.
     */
    function cleanupHooks(hooks) {
        algorithm_1.ArrayExt.removeAllWhere(hooks, isNull);
    }
    /**
     * Test whether a value is `null`.
     */
    function isNull(value) {
        return value === null;
    }
})(MessageLoop = exports.MessageLoop || (exports.MessageLoop = {}));
