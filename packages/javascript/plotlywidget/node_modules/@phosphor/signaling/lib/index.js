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
/**
 * A concrete implementation of `ISignal`.
 *
 * #### Example
 * ```typescript
 * import { ISignal, Signal } from '@phosphor/signaling';
 *
 * class SomeClass {
 *
 *   constructor(name: string) {
 *     this.name = name;
 *   }
 *
 *   readonly name: string;
 *
 *   get valueChanged: ISignal<this, number> {
 *     return this._valueChanged;
 *   }
 *
 *   get value(): number {
 *     return this._value;
 *   }
 *
 *   set value(value: number) {
 *     if (value === this._value) {
 *       return;
 *     }
 *     this._value = value;
 *     this._valueChanged.emit(value);
 *   }
 *
 *   private _value = 0;
 *   private _valueChanged = new Signal<this, number>(this);
 * }
 *
 * function logger(sender: SomeClass, value: number): void {
 *   console.log(sender.name, value);
 * }
 *
 * let m1 = new SomeClass('foo');
 * let m2 = new SomeClass('bar');
 *
 * m1.valueChanged.connect(logger);
 * m2.valueChanged.connect(logger);
 *
 * m1.value = 42;  // logs: foo 42
 * m2.value = 17;  // logs: bar 17
 * ```
 */
var Signal = (function () {
    /**
     * Construct a new signal.
     *
     * @param sender - The sender which owns the signal.
     */
    function Signal(sender) {
        this.sender = sender;
    }
    /**
     * Connect a slot to the signal.
     *
     * @param slot - The slot to invoke when the signal is emitted.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection succeeds, `false` otherwise.
     */
    Signal.prototype.connect = function (slot, thisArg) {
        return Private.connect(this, slot, thisArg);
    };
    /**
     * Disconnect a slot from the signal.
     *
     * @param slot - The slot to disconnect from the signal.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection is removed, `false` otherwise.
     */
    Signal.prototype.disconnect = function (slot, thisArg) {
        return Private.disconnect(this, slot, thisArg);
    };
    /**
     * Emit the signal and invoke the connected slots.
     *
     * @param args - The args to pass to the connected slots.
     *
     * #### Notes
     * Slots are invoked synchronously in connection order.
     *
     * Exceptions thrown by connected slots will be caught and logged.
     */
    Signal.prototype.emit = function (args) {
        Private.emit(this, args);
    };
    return Signal;
}());
exports.Signal = Signal;
/**
 * The namespace for the `Signal` class statics.
 */
(function (Signal) {
    /**
     * Remove all connections between a sender and receiver.
     *
     * @param sender - The sender object of interest.
     *
     * @param receiver - The receiver object of interest.
     *
     * #### Notes
     * If a `thisArg` is provided when connecting a signal, that object
     * is considered the receiver. Otherwise, the `slot` is considered
     * the receiver.
     */
    function disconnectBetween(sender, receiver) {
        Private.disconnectBetween(sender, receiver);
    }
    Signal.disconnectBetween = disconnectBetween;
    /**
     * Remove all connections where the given object is the sender.
     *
     * @param sender - The sender object of interest.
     */
    function disconnectSender(sender) {
        Private.disconnectSender(sender);
    }
    Signal.disconnectSender = disconnectSender;
    /**
     * Remove all connections where the given object is the receiver.
     *
     * @param receiver - The receiver object of interest.
     *
     * #### Notes
     * If a `thisArg` is provided when connecting a signal, that object
     * is considered the receiver. Otherwise, the `slot` is considered
     * the receiver.
     */
    function disconnectReceiver(receiver) {
        Private.disconnectReceiver(receiver);
    }
    Signal.disconnectReceiver = disconnectReceiver;
    /**
     * Remove all connections where an object is the sender or receiver.
     *
     * @param object - The object of interest.
     *
     * #### Notes
     * If a `thisArg` is provided when connecting a signal, that object
     * is considered the receiver. Otherwise, the `slot` is considered
     * the receiver.
     */
    function disconnectAll(object) {
        Private.disconnectAll(object);
    }
    Signal.disconnectAll = disconnectAll;
    /**
     * Clear all signal data associated with the given object.
     *
     * @param object - The object for which the data should be cleared.
     *
     * #### Notes
     * This removes all signal connections and any other signal data
     * associated with the object.
     */
    function clearData(object) {
        Private.disconnectAll(object);
    }
    Signal.clearData = clearData;
    /**
     * Get the signal exception handler.
     *
     * @returns The current exception handler.
     *
     * #### Notes
     * The default exception handler is `console.error`.
     */
    function getExceptionHandler() {
        return Private.exceptionHandler;
    }
    Signal.getExceptionHandler = getExceptionHandler;
    /**
     * Set the signal exception handler.
     *
     * @param handler - The function to use as the exception handler.
     *
     * @returns The old exception handler.
     *
     * #### Notes
     * The exception handler is invoked when a slot throws an exception.
     */
    function setExceptionHandler(handler) {
        var old = Private.exceptionHandler;
        Private.exceptionHandler = handler;
        return old;
    }
    Signal.setExceptionHandler = setExceptionHandler;
})(Signal = exports.Signal || (exports.Signal = {}));
exports.Signal = Signal;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The signal exception handler function.
     */
    Private.exceptionHandler = function (err) {
        console.error(err);
    };
    /**
     * Connect a slot to a signal.
     *
     * @param signal - The signal of interest.
     *
     * @param slot - The slot to invoke when the signal is emitted.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection succeeds, `false` otherwise.
     */
    function connect(signal, slot, thisArg) {
        // Coerce a `null` `thisArg` to `undefined`.
        thisArg = thisArg || undefined;
        // Ensure the sender's array of receivers is created.
        var receivers = receiversForSender.get(signal.sender);
        if (!receivers) {
            receivers = [];
            receiversForSender.set(signal.sender, receivers);
        }
        // Bail if a matching connection already exists.
        if (findConnection(receivers, signal, slot, thisArg)) {
            return false;
        }
        // Choose the best object for the receiver.
        var receiver = thisArg || slot;
        // Ensure the receiver's array of senders is created.
        var senders = sendersForReceiver.get(receiver);
        if (!senders) {
            senders = [];
            sendersForReceiver.set(receiver, senders);
        }
        // Create a new connection and add it to the end of each array.
        var connection = { signal: signal, slot: slot, thisArg: thisArg };
        receivers.push(connection);
        senders.push(connection);
        // Indicate a successful connection.
        return true;
    }
    Private.connect = connect;
    /**
     * Disconnect a slot from a signal.
     *
     * @param signal - The signal of interest.
     *
     * @param slot - The slot to disconnect from the signal.
     *
     * @param thisArg - The `this` context for the slot. If provided,
     *   this must be a non-primitive object.
     *
     * @returns `true` if the connection is removed, `false` otherwise.
     */
    function disconnect(signal, slot, thisArg) {
        // Coerce a `null` `thisArg` to `undefined`.
        thisArg = thisArg || undefined;
        // Lookup the list of receivers, and bail if none exist.
        var receivers = receiversForSender.get(signal.sender);
        if (!receivers || receivers.length === 0) {
            return false;
        }
        // Bail if no matching connection exits.
        var connection = findConnection(receivers, signal, slot, thisArg);
        if (!connection) {
            return false;
        }
        // Choose the best object for the receiver.
        var receiver = thisArg || slot;
        // Lookup the array of senders, which is now known to exist.
        var senders = sendersForReceiver.get(receiver);
        // Clear the connection and schedule cleanup of the arrays.
        connection.signal = null;
        scheduleCleanup(receivers);
        scheduleCleanup(senders);
        // Indicate a successful disconnection.
        return true;
    }
    Private.disconnect = disconnect;
    /**
     * Remove all connections between a sender and receiver.
     *
     * @param sender - The sender object of interest.
     *
     * @param receiver - The receiver object of interest.
     */
    function disconnectBetween(sender, receiver) {
        // If there are no receivers, there is nothing to do.
        var receivers = receiversForSender.get(sender);
        if (!receivers || receivers.length === 0) {
            return;
        }
        // If there are no senders, there is nothing to do.
        var senders = sendersForReceiver.get(receiver);
        if (!senders || senders.length === 0) {
            return;
        }
        // Clear each connection between the sender and receiver.
        algorithm_1.each(senders, function (connection) {
            // Skip connections which have already been cleared.
            if (!connection.signal) {
                return;
            }
            // Clear the connection if it matches the sender.
            if (connection.signal.sender === sender) {
                connection.signal = null;
            }
        });
        // Schedule a cleanup of the senders and receivers.
        scheduleCleanup(receivers);
        scheduleCleanup(senders);
    }
    Private.disconnectBetween = disconnectBetween;
    /**
     * Remove all connections where the given object is the sender.
     *
     * @param sender - The sender object of interest.
     */
    function disconnectSender(sender) {
        // If there are no receivers, there is nothing to do.
        var receivers = receiversForSender.get(sender);
        if (!receivers || receivers.length === 0) {
            return;
        }
        // Clear each receiver connection.
        algorithm_1.each(receivers, function (connection) {
            // Skip connections which have already been cleared.
            if (!connection.signal) {
                return;
            }
            // Choose the best object for the receiver.
            var receiver = connection.thisArg || connection.slot;
            // Clear the connection.
            connection.signal = null;
            // Cleanup the array of senders, which is now known to exist.
            scheduleCleanup(sendersForReceiver.get(receiver));
        });
        // Schedule a cleanup of the receivers.
        scheduleCleanup(receivers);
    }
    Private.disconnectSender = disconnectSender;
    /**
     * Remove all connections where the given object is the receiver.
     *
     * @param receiver - The receiver object of interest.
     */
    function disconnectReceiver(receiver) {
        // If there are no senders, there is nothing to do.
        var senders = sendersForReceiver.get(receiver);
        if (!senders || senders.length === 0) {
            return;
        }
        // Clear each sender connection.
        algorithm_1.each(senders, function (connection) {
            // Skip connections which have already been cleared.
            if (!connection.signal) {
                return;
            }
            // Lookup the sender for the connection.
            var sender = connection.signal.sender;
            // Clear the connection.
            connection.signal = null;
            // Cleanup the array of receivers, which is now known to exist.
            scheduleCleanup(receiversForSender.get(sender));
        });
        // Schedule a cleanup of the list of senders.
        scheduleCleanup(senders);
    }
    Private.disconnectReceiver = disconnectReceiver;
    /**
     * Remove all connections where an object is the sender or receiver.
     *
     * @param object - The object of interest.
     */
    function disconnectAll(object) {
        // Clear and cleanup any receiver connections.
        var receivers = receiversForSender.get(object);
        if (receivers && receivers.length > 0) {
            algorithm_1.each(receivers, function (connection) { connection.signal = null; });
            scheduleCleanup(receivers);
        }
        // Clear and cleanup any sender connections.
        var senders = sendersForReceiver.get(object);
        if (senders && senders.length > 0) {
            algorithm_1.each(senders, function (connection) { connection.signal = null; });
            scheduleCleanup(senders);
        }
    }
    Private.disconnectAll = disconnectAll;
    /**
     * Emit a signal and invoke its connected slots.
     *
     * @param signal - The signal of interest.
     *
     * @param args - The args to pass to the connected slots.
     *
     * #### Notes
     * Slots are invoked synchronously in connection order.
     *
     * Exceptions thrown by connected slots will be caught and logged.
     */
    function emit(signal, args) {
        // If there are no receivers, there is nothing to do.
        var receivers = receiversForSender.get(signal.sender);
        if (!receivers || receivers.length === 0) {
            return;
        }
        // Invoke the slots for connections with a matching signal.
        // Any connections added during emission are not invoked.
        for (var i = 0, n = receivers.length; i < n; ++i) {
            var connection = receivers[i];
            if (connection.signal === signal) {
                invokeSlot(connection, args);
            }
        }
    }
    Private.emit = emit;
    /**
     * A weak mapping of sender to array of receiver connections.
     */
    var receiversForSender = new WeakMap();
    /**
     * A weak mapping of receiver to array of sender connections.
     */
    var sendersForReceiver = new WeakMap();
    /**
     * A set of connection arrays which are pending cleanup.
     */
    var dirtySet = new Set();
    /**
     * A function to schedule an event loop callback.
     */
    var schedule = (function () {
        var ok = typeof requestAnimationFrame === 'function';
        return ok ? requestAnimationFrame : setImmediate;
    })();
    /**
     * Find a connection which matches the given parameters.
     */
    function findConnection(connections, signal, slot, thisArg) {
        return algorithm_1.find(connections, function (connection) { return (connection.signal === signal &&
            connection.slot === slot &&
            connection.thisArg === thisArg); });
    }
    /**
     * Invoke a slot with the given parameters.
     *
     * The connection is assumed to be valid.
     *
     * Exceptions in the slot will be caught and logged.
     */
    function invokeSlot(connection, args) {
        var signal = connection.signal, slot = connection.slot, thisArg = connection.thisArg;
        try {
            slot.call(thisArg, signal.sender, args);
        }
        catch (err) {
            Private.exceptionHandler(err);
        }
    }
    /**
     * Schedule a cleanup of a connection array.
     *
     * This will add the array to the dirty set and schedule a deferred
     * cleanup of the array contents. On cleanup, any connection with a
     * `null` signal will be removed from the array.
     */
    function scheduleCleanup(array) {
        if (dirtySet.size === 0) {
            schedule(cleanupDirtySet);
        }
        dirtySet.add(array);
    }
    /**
     * Cleanup the connection lists in the dirty set.
     *
     * This function should only be invoked asynchronously, when the
     * stack frame is guaranteed to not be on the path of user code.
     */
    function cleanupDirtySet() {
        dirtySet.forEach(cleanupConnections);
        dirtySet.clear();
    }
    /**
     * Cleanup the dirty connections in a connections array.
     *
     * This will remove any connection with a `null` signal.
     *
     * This function should only be invoked asynchronously, when the
     * stack frame is guaranteed to not be on the path of user code.
     */
    function cleanupConnections(connections) {
        algorithm_1.ArrayExt.removeAllWhere(connections, isDeadConnection);
    }
    /**
     * Test whether a connection is dead.
     *
     * A dead connection has a `null` signal.
     */
    function isDeadConnection(connection) {
        return connection.signal === null;
    }
})(Private || (Private = {}));
