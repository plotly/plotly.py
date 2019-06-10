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
 * A generic doubly-linked list.
 */
var LinkedList = (function () {
    /**
     * Construct a new linked list.
     */
    function LinkedList() {
        this._first = null;
        this._last = null;
        this._length = 0;
    }
    Object.defineProperty(LinkedList.prototype, "isEmpty", {
        /**
         * Whether the list is empty.
         *
         * #### Complexity
         * Constant.
         */
        get: function () {
            return this._length === 0;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LinkedList.prototype, "length", {
        /**
         * The length of the list.
         *
         * #### Complexity
         * Constant.
         */
        get: function () {
            return this._length;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LinkedList.prototype, "first", {
        /**
         * The first value in the list.
         *
         * This is `undefined` if the list is empty.
         *
         * #### Complexity
         * Constant.
         */
        get: function () {
            return this._first ? this._first.value : undefined;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LinkedList.prototype, "last", {
        /**
         * The last value in the list.
         *
         * This is `undefined` if the list is empty.
         *
         * #### Complexity
         * Constant.
         */
        get: function () {
            return this._last ? this._last.value : undefined;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LinkedList.prototype, "firstNode", {
        /**
         * The first node in the list.
         *
         * This is `null` if the list is empty.
         *
         * #### Complexity
         * Constant.
         */
        get: function () {
            return this._first;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(LinkedList.prototype, "lastNode", {
        /**
         * The last node in the list.
         *
         * This is `null` if the list is empty.
         *
         * #### Complexity
         * Constant.
         */
        get: function () {
            return this._last;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * Create an iterator over the values in the list.
     *
     * @returns A new iterator starting with the first value.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.iter = function () {
        return new LinkedList.ForwardValueIterator(this._first);
    };
    /**
     * Create a reverse iterator over the values in the list.
     *
     * @returns A new iterator starting with the last value.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.retro = function () {
        return new LinkedList.RetroValueIterator(this._last);
    };
    /**
     * Create an iterator over the nodes in the list.
     *
     * @returns A new iterator starting with the first node.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.nodes = function () {
        return new LinkedList.ForwardNodeIterator(this._first);
    };
    /**
     * Create a reverse iterator over the nodes in the list.
     *
     * @returns A new iterator starting with the last node.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.retroNodes = function () {
        return new LinkedList.RetroNodeIterator(this._last);
    };
    /**
     * Add a value to the beginning of the list.
     *
     * @param value - The value to add to the beginning of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.addFirst = function (value) {
        var node = new Private.LinkedListNode(this, value);
        if (!this._first) {
            this._first = node;
            this._last = node;
        }
        else {
            node.next = this._first;
            this._first.prev = node;
            this._first = node;
        }
        this._length++;
        return node;
    };
    /**
     * Add a value to the end of the list.
     *
     * @param value - The value to add to the end of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.addLast = function (value) {
        var node = new Private.LinkedListNode(this, value);
        if (!this._last) {
            this._first = node;
            this._last = node;
        }
        else {
            node.prev = this._last;
            this._last.next = node;
            this._last = node;
        }
        this._length++;
        return node;
    };
    /**
     * Insert a value before a specific node in the list.
     *
     * @param value - The value to insert before the reference node.
     *
     * @param ref - The reference node of interest. If this is `null`,
     *   the value will be added to the beginning of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Notes
     * The reference node must be owned by the list.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.insertBefore = function (value, ref) {
        if (!ref || ref === this._first) {
            return this.addFirst(value);
        }
        if (!(ref instanceof Private.LinkedListNode) || ref.list !== this) {
            throw new Error('Reference node is not owned by the list.');
        }
        var node = new Private.LinkedListNode(this, value);
        var _ref = ref;
        var prev = _ref.prev;
        node.next = _ref;
        node.prev = prev;
        _ref.prev = node;
        prev.next = node;
        this._length++;
        return node;
    };
    /**
     * Insert a value after a specific node in the list.
     *
     * @param value - The value to insert after the reference node.
     *
     * @param ref - The reference node of interest. If this is `null`,
     *   the value will be added to the end of the list.
     *
     * @returns The list node which holds the value.
     *
     * #### Notes
     * The reference node must be owned by the list.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.insertAfter = function (value, ref) {
        if (!ref || ref === this._last) {
            return this.addLast(value);
        }
        if (!(ref instanceof Private.LinkedListNode) || ref.list !== this) {
            throw new Error('Reference node is not owned by the list.');
        }
        var node = new Private.LinkedListNode(this, value);
        var _ref = ref;
        var next = _ref.next;
        node.next = next;
        node.prev = _ref;
        _ref.next = node;
        next.prev = node;
        this._length++;
        return node;
    };
    /**
     * Remove and return the value at the beginning of the list.
     *
     * @returns The removed value, or `undefined` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.removeFirst = function () {
        var node = this._first;
        if (!node) {
            return undefined;
        }
        if (node === this._last) {
            this._first = null;
            this._last = null;
        }
        else {
            this._first = node.next;
            this._first.prev = null;
        }
        node.list = null;
        node.next = null;
        node.prev = null;
        this._length--;
        return node.value;
    };
    /**
     * Remove and return the value at the end of the list.
     *
     * @returns The removed value, or `undefined` if the list is empty.
     *
     * #### Complexity
     * Constant.
     */
    LinkedList.prototype.removeLast = function () {
        var node = this._last;
        if (!node) {
            return undefined;
        }
        if (node === this._first) {
            this._first = null;
            this._last = null;
        }
        else {
            this._last = node.prev;
            this._last.next = null;
        }
        node.list = null;
        node.next = null;
        node.prev = null;
        this._length--;
        return node.value;
    };
    /**
     * Remove a specific node from the list.
     *
     * @param node - The node to remove from the list.
     *
     * #### Complexity
     * Constant.
     *
     * #### Notes
     * The node must be owned by the list.
     */
    LinkedList.prototype.removeNode = function (node) {
        if (!(node instanceof Private.LinkedListNode) || node.list !== this) {
            throw new Error('Node is not owned by the list.');
        }
        var _node = node;
        if (_node === this._first && _node === this._last) {
            this._first = null;
            this._last = null;
        }
        else if (_node === this._first) {
            this._first = _node.next;
            this._first.prev = null;
        }
        else if (_node === this._last) {
            this._last = _node.prev;
            this._last.next = null;
        }
        else {
            _node.next.prev = _node.prev;
            _node.prev.next = _node.next;
        }
        _node.list = null;
        _node.next = null;
        _node.prev = null;
        this._length--;
    };
    /**
     * Remove all values from the list.
     *
     * #### Complexity
     * Linear.
     */
    LinkedList.prototype.clear = function () {
        var node = this._first;
        while (node) {
            var next = node.next;
            node.list = null;
            node.prev = null;
            node.next = null;
            node = next;
        }
        this._first = null;
        this._last = null;
        this._length = 0;
    };
    return LinkedList;
}());
exports.LinkedList = LinkedList;
/**
 * The namespace for the `LinkedList` class statics.
 */
(function (LinkedList) {
    /**
     * Create a linked list from an iterable of values.
     *
     * @param values - The iterable or array-like object of interest.
     *
     * @returns A new linked list initialized with the given values.
     */
    function from(values) {
        var list = new LinkedList();
        algorithm_1.each(values, function (value) { list.addLast(value); });
        return list;
    }
    LinkedList.from = from;
    /**
     * A forward iterator for values in a linked list.
     */
    var ForwardValueIterator = (function () {
        /**
         * Construct a forward value iterator.
         *
         * @param node - The first node in the list.
         */
        function ForwardValueIterator(node) {
            this._node = node;
        }
        /**
         * Get an iterator over the object's values.
         *
         * @returns An iterator which yields the object's values.
         */
        ForwardValueIterator.prototype.iter = function () {
            return this;
        };
        /**
         * Create an independent clone of the iterator.
         *
         * @returns A new independent clone of the iterator.
         */
        ForwardValueIterator.prototype.clone = function () {
            return new ForwardValueIterator(this._node);
        };
        /**
         * Get the next value from the iterator.
         *
         * @returns The next value from the iterator, or `undefined`.
         */
        ForwardValueIterator.prototype.next = function () {
            if (!this._node) {
                return undefined;
            }
            var node = this._node;
            this._node = node.next;
            return node.value;
        };
        return ForwardValueIterator;
    }());
    LinkedList.ForwardValueIterator = ForwardValueIterator;
    /**
     * A reverse iterator for values in a linked list.
     */
    var RetroValueIterator = (function () {
        /**
         * Construct a retro value iterator.
         *
         * @param node - The last node in the list.
         */
        function RetroValueIterator(node) {
            this._node = node;
        }
        /**
         * Get an iterator over the object's values.
         *
         * @returns An iterator which yields the object's values.
         */
        RetroValueIterator.prototype.iter = function () {
            return this;
        };
        /**
         * Create an independent clone of the iterator.
         *
         * @returns A new independent clone of the iterator.
         */
        RetroValueIterator.prototype.clone = function () {
            return new RetroValueIterator(this._node);
        };
        /**
         * Get the next value from the iterator.
         *
         * @returns The next value from the iterator, or `undefined`.
         */
        RetroValueIterator.prototype.next = function () {
            if (!this._node) {
                return undefined;
            }
            var node = this._node;
            this._node = node.prev;
            return node.value;
        };
        return RetroValueIterator;
    }());
    LinkedList.RetroValueIterator = RetroValueIterator;
    /**
     * A forward iterator for nodes in a linked list.
     */
    var ForwardNodeIterator = (function () {
        /**
         * Construct a forward node iterator.
         *
         * @param node - The first node in the list.
         */
        function ForwardNodeIterator(node) {
            this._node = node;
        }
        /**
         * Get an iterator over the object's values.
         *
         * @returns An iterator which yields the object's values.
         */
        ForwardNodeIterator.prototype.iter = function () {
            return this;
        };
        /**
         * Create an independent clone of the iterator.
         *
         * @returns A new independent clone of the iterator.
         */
        ForwardNodeIterator.prototype.clone = function () {
            return new ForwardNodeIterator(this._node);
        };
        /**
         * Get the next value from the iterator.
         *
         * @returns The next value from the iterator, or `undefined`.
         */
        ForwardNodeIterator.prototype.next = function () {
            if (!this._node) {
                return undefined;
            }
            var node = this._node;
            this._node = node.next;
            return node;
        };
        return ForwardNodeIterator;
    }());
    LinkedList.ForwardNodeIterator = ForwardNodeIterator;
    /**
     * A reverse iterator for nodes in a linked list.
     */
    var RetroNodeIterator = (function () {
        /**
         * Construct a retro node iterator.
         *
         * @param node - The last node in the list.
         */
        function RetroNodeIterator(node) {
            this._node = node;
        }
        /**
         * Get an iterator over the object's values.
         *
         * @returns An iterator which yields the object's values.
         */
        RetroNodeIterator.prototype.iter = function () {
            return this;
        };
        /**
         * Create an independent clone of the iterator.
         *
         * @returns A new independent clone of the iterator.
         */
        RetroNodeIterator.prototype.clone = function () {
            return new RetroNodeIterator(this._node);
        };
        /**
         * Get the next value from the iterator.
         *
         * @returns The next value from the iterator, or `undefined`.
         */
        RetroNodeIterator.prototype.next = function () {
            if (!this._node) {
                return undefined;
            }
            var node = this._node;
            this._node = node.prev;
            return node;
        };
        return RetroNodeIterator;
    }());
    LinkedList.RetroNodeIterator = RetroNodeIterator;
})(LinkedList = exports.LinkedList || (exports.LinkedList = {}));
exports.LinkedList = LinkedList;
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The internal linked list node implementation.
     */
    var LinkedListNode = (function () {
        /**
         * Construct a new linked list node.
         *
         * @param list - The list which owns the node.
         *
         * @param value - The value for the link.
         */
        function LinkedListNode(list, value) {
            /**
             * The linked list which created and owns the node.
             */
            this.list = null;
            /**
             * The next node in the list.
             */
            this.next = null;
            /**
             * The previous node in the list.
             */
            this.prev = null;
            this.list = list;
            this.value = value;
        }
        return LinkedListNode;
    }());
    Private.LinkedListNode = LinkedListNode;
})(Private || (Private = {}));
