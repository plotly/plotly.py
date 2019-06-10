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
 * A virtual node which represents plain text content.
 *
 * #### Notes
 * User code will not typically create a `VirtualText` node directly.
 * Instead, the `h()` function will be used to create an element tree.
 */
var VirtualText = (function () {
    /**
     * Construct a new virtual text node.
     *
     * @param content - The text content for the node.
     */
    function VirtualText(content) {
        /**
         * The type of the node.
         *
         * This value can be used as a type guard for discriminating the
         * `VirtualNode` union type.
         */
        this.type = 'text';
        this.content = content;
    }
    return VirtualText;
}());
exports.VirtualText = VirtualText;
/**
 * A virtual node which represents an HTML element.
 *
 * #### Notes
 * User code will not typically create a `VirtualElement` node directly.
 * Instead, the `h()` function will be used to create an element tree.
 */
var VirtualElement = (function () {
    /**
     * Construct a new virtual element node.
     *
     * @param tag - The element tag name.
     *
     * @param attrs - The element attributes.
     *
     * @param children - The element children.
     */
    function VirtualElement(tag, attrs, children) {
        /**
         * The type of the node.
         *
         * This value can be used as a type guard for discriminating the
         * `VirtualNode` union type.
         */
        this.type = 'element';
        this.tag = tag;
        this.attrs = attrs;
        this.children = children;
    }
    return VirtualElement;
}());
exports.VirtualElement = VirtualElement;
function h(tag) {
    var attrs = {};
    var children = [];
    for (var i = 1, n = arguments.length; i < n; ++i) {
        var arg = arguments[i];
        if (typeof arg === 'string') {
            children.push(new VirtualText(arg));
        }
        else if (arg instanceof VirtualText) {
            children.push(arg);
        }
        else if (arg instanceof VirtualElement) {
            children.push(arg);
        }
        else if (arg instanceof Array) {
            extend(children, arg);
        }
        else if (i === 1 && arg && typeof arg === 'object') {
            attrs = arg;
        }
    }
    return new VirtualElement(tag, attrs, children);
    function extend(array, values) {
        for (var _i = 0, values_1 = values; _i < values_1.length; _i++) {
            var child = values_1[_i];
            if (typeof child === 'string') {
                array.push(new VirtualText(child));
            }
            else if (child instanceof VirtualText) {
                array.push(child);
            }
            else if (child instanceof VirtualElement) {
                array.push(child);
            }
        }
    }
}
exports.h = h;
/**
 * The namespace for the `h` function statics.
 */
(function (h) {
    h.a = h.bind(undefined, 'a');
    h.abbr = h.bind(undefined, 'abbr');
    h.address = h.bind(undefined, 'address');
    h.area = h.bind(undefined, 'area');
    h.article = h.bind(undefined, 'article');
    h.aside = h.bind(undefined, 'aside');
    h.audio = h.bind(undefined, 'audio');
    h.b = h.bind(undefined, 'b');
    h.bdi = h.bind(undefined, 'bdi');
    h.bdo = h.bind(undefined, 'bdo');
    h.blockquote = h.bind(undefined, 'blockquote');
    h.br = h.bind(undefined, 'br');
    h.button = h.bind(undefined, 'button');
    h.canvas = h.bind(undefined, 'canvas');
    h.caption = h.bind(undefined, 'caption');
    h.cite = h.bind(undefined, 'cite');
    h.code = h.bind(undefined, 'code');
    h.col = h.bind(undefined, 'col');
    h.colgroup = h.bind(undefined, 'colgroup');
    h.data = h.bind(undefined, 'data');
    h.datalist = h.bind(undefined, 'datalist');
    h.dd = h.bind(undefined, 'dd');
    h.del = h.bind(undefined, 'del');
    h.dfn = h.bind(undefined, 'dfn');
    h.div = h.bind(undefined, 'div');
    h.dl = h.bind(undefined, 'dl');
    h.dt = h.bind(undefined, 'dt');
    h.em = h.bind(undefined, 'em');
    h.embed = h.bind(undefined, 'embed');
    h.fieldset = h.bind(undefined, 'fieldset');
    h.figcaption = h.bind(undefined, 'figcaption');
    h.figure = h.bind(undefined, 'figure');
    h.footer = h.bind(undefined, 'footer');
    h.form = h.bind(undefined, 'form');
    h.h1 = h.bind(undefined, 'h1');
    h.h2 = h.bind(undefined, 'h2');
    h.h3 = h.bind(undefined, 'h3');
    h.h4 = h.bind(undefined, 'h4');
    h.h5 = h.bind(undefined, 'h5');
    h.h6 = h.bind(undefined, 'h6');
    h.header = h.bind(undefined, 'header');
    h.hr = h.bind(undefined, 'hr');
    h.i = h.bind(undefined, 'i');
    h.iframe = h.bind(undefined, 'iframe');
    h.img = h.bind(undefined, 'img');
    h.input = h.bind(undefined, 'input');
    h.ins = h.bind(undefined, 'ins');
    h.kbd = h.bind(undefined, 'kbd');
    h.label = h.bind(undefined, 'label');
    h.legend = h.bind(undefined, 'legend');
    h.li = h.bind(undefined, 'li');
    h.main = h.bind(undefined, 'main');
    h.map = h.bind(undefined, 'map');
    h.mark = h.bind(undefined, 'mark');
    h.meter = h.bind(undefined, 'meter');
    h.nav = h.bind(undefined, 'nav');
    h.noscript = h.bind(undefined, 'noscript');
    h.object = h.bind(undefined, 'object');
    h.ol = h.bind(undefined, 'ol');
    h.optgroup = h.bind(undefined, 'optgroup');
    h.option = h.bind(undefined, 'option');
    h.output = h.bind(undefined, 'output');
    h.p = h.bind(undefined, 'p');
    h.param = h.bind(undefined, 'param');
    h.pre = h.bind(undefined, 'pre');
    h.progress = h.bind(undefined, 'progress');
    h.q = h.bind(undefined, 'q');
    h.rp = h.bind(undefined, 'rp');
    h.rt = h.bind(undefined, 'rt');
    h.ruby = h.bind(undefined, 'ruby');
    h.s = h.bind(undefined, 's');
    h.samp = h.bind(undefined, 'samp');
    h.section = h.bind(undefined, 'section');
    h.select = h.bind(undefined, 'select');
    h.small = h.bind(undefined, 'small');
    h.source = h.bind(undefined, 'source');
    h.span = h.bind(undefined, 'span');
    h.strong = h.bind(undefined, 'strong');
    h.sub = h.bind(undefined, 'sub');
    h.summary = h.bind(undefined, 'summary');
    h.sup = h.bind(undefined, 'sup');
    h.table = h.bind(undefined, 'table');
    h.tbody = h.bind(undefined, 'tbody');
    h.td = h.bind(undefined, 'td');
    h.textarea = h.bind(undefined, 'textarea');
    h.tfoot = h.bind(undefined, 'tfoot');
    h.th = h.bind(undefined, 'th');
    h.thead = h.bind(undefined, 'thead');
    h.time = h.bind(undefined, 'time');
    h.title = h.bind(undefined, 'title');
    h.tr = h.bind(undefined, 'tr');
    h.track = h.bind(undefined, 'track');
    h.u = h.bind(undefined, 'u');
    h.ul = h.bind(undefined, 'ul');
    h.var_ = h.bind(undefined, 'var');
    h.video = h.bind(undefined, 'video');
    h.wbr = h.bind(undefined, 'wbr');
})(h = exports.h || (exports.h = {}));
/**
 * The namespace for the virtual DOM rendering functions.
 */
var VirtualDOM;
(function (VirtualDOM) {
    /**
     * Create a real DOM element from a virtual element node.
     *
     * @param node - The virtual element node to realize.
     *
     * @returns A new DOM element for the given virtual element node.
     *
     * #### Notes
     * This creates a brand new *real* DOM element with a structure which
     * matches the given virtual DOM node.
     *
     * If virtual diffing is desired, use the `render` function instead.
     */
    function realize(node) {
        return Private.createDOMNode(node);
    }
    VirtualDOM.realize = realize;
    /**
     * Render virtual DOM content into a host element.
     *
     * @param content - The virtual DOM content to render.
     *
     * @param host - The host element for the rendered content.
     *
     * #### Notes
     * This renders the delta from the previous rendering. It assumes that
     * the content of the host element is not manipulated by external code.
     *
     * Providing `null` content will clear the rendering.
     *
     * Externally modifying the provided content or the host element will
     * result in undefined rendering behavior.
     */
    function render(content, host) {
        var oldContent = Private.hostMap.get(host) || [];
        var newContent = Private.asContentArray(content);
        Private.hostMap.set(host, newContent);
        Private.updateContent(host, oldContent, newContent);
    }
    VirtualDOM.render = render;
})(VirtualDOM = exports.VirtualDOM || (exports.VirtualDOM = {}));
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * A weak mapping of host element to virtual DOM content.
     */
    Private.hostMap = new WeakMap();
    /**
     * Cast a content value to a content array.
     */
    function asContentArray(value) {
        if (!value) {
            return [];
        }
        if (value instanceof Array) {
            return value;
        }
        return [value];
    }
    Private.asContentArray = asContentArray;
    function createDOMNode(node) {
        // Create a text node for a virtual text node.
        if (node.type === 'text') {
            return document.createTextNode(node.content);
        }
        // Create the HTML element with the specified tag.
        var element = document.createElement(node.tag);
        // Add the attributes for the new element.
        addAttrs(element, node.attrs);
        // Recursively populate the element with child content.
        for (var i = 0, n = node.children.length; i < n; ++i) {
            element.appendChild(createDOMNode(node.children[i]));
        }
        // Return the populated element.
        return element;
    }
    Private.createDOMNode = createDOMNode;
    /**
     * Update a host element with the delta of the virtual content.
     *
     * This is the core "diff" algorithm. There is no explicit "patch"
     * phase. The host is patched at each step as the diff progresses.
     */
    function updateContent(host, oldContent, newContent) {
        // Bail early if the content is identical.
        if (oldContent === newContent) {
            return;
        }
        // Collect the old keyed elems into a mapping.
        var oldKeyed = collectKeys(host, oldContent);
        // Create a copy of the old content which can be modified in-place.
        var oldCopy = oldContent.slice();
        // Update the host with the new content. The diff always proceeds
        // forward and never modifies a previously visited index. The old
        // copy array is modified in-place to reflect the changes made to
        // the host children. This causes the stale nodes to be pushed to
        // the end of the host node and removed at the end of the loop.
        var currElem = host.firstChild;
        var newCount = newContent.length;
        for (var i = 0; i < newCount; ++i) {
            // If the old content is exhausted, create a new node.
            if (i >= oldCopy.length) {
                host.appendChild(createDOMNode(newContent[i]));
                continue;
            }
            // Lookup the old and new virtual nodes.
            var oldVNode = oldCopy[i];
            var newVNode = newContent[i];
            // If both elements are identical, there is nothing to do.
            if (oldVNode === newVNode) {
                currElem = currElem.nextSibling;
                continue;
            }
            // Handle the simplest case of in-place text update first.
            if (oldVNode.type === 'text' && newVNode.type === 'text') {
                currElem.textContent = newVNode.content;
                currElem = currElem.nextSibling;
                continue;
            }
            // If the old or new node is a text node, the other node is now
            // known to be an element node, so create and insert a new node.
            if (oldVNode.type === 'text' || newVNode.type === 'text') {
                algorithm_1.ArrayExt.insert(oldCopy, i, newVNode);
                host.insertBefore(createDOMNode(newVNode), currElem);
                continue;
            }
            // At this point, both nodes are known to be element nodes.
            // If the new elem is keyed, move an old keyed elem to the proper
            // location before proceeding with the diff. The search can start
            // at the current index, since the unmatched old keyed elems are
            // pushed forward in the old copy array.
            var newKey = newVNode.attrs.key;
            if (newKey && newKey in oldKeyed) {
                var pair = oldKeyed[newKey];
                if (pair.vNode !== oldVNode) {
                    algorithm_1.ArrayExt.move(oldCopy, oldCopy.indexOf(pair.vNode, i + 1), i);
                    host.insertBefore(pair.element, currElem);
                    oldVNode = pair.vNode;
                    currElem = pair.element;
                }
            }
            // If both elements are identical, there is nothing to do.
            if (oldVNode === newVNode) {
                currElem = currElem.nextSibling;
                continue;
            }
            // If the old elem is keyed and does not match the new elem key,
            // create a new node. This is necessary since the old keyed elem
            // may be matched at a later point in the diff.
            var oldKey = oldVNode.attrs.key;
            if (oldKey && oldKey !== newKey) {
                algorithm_1.ArrayExt.insert(oldCopy, i, newVNode);
                host.insertBefore(createDOMNode(newVNode), currElem);
                continue;
            }
            // If the tags are different, create a new node.
            if (oldVNode.tag !== newVNode.tag) {
                algorithm_1.ArrayExt.insert(oldCopy, i, newVNode);
                host.insertBefore(createDOMNode(newVNode), currElem);
                continue;
            }
            // At this point, the element can be updated in-place.
            // Update the element attributes.
            updateAttrs(currElem, oldVNode.attrs, newVNode.attrs);
            // Update the element content.
            updateContent(currElem, oldVNode.children, newVNode.children);
            // Step to the next sibling element.
            currElem = currElem.nextSibling;
        }
        // Dispose of the old nodes pushed to the end of the host.
        for (var i = oldCopy.length - newCount; i > 0; --i) {
            host.removeChild(host.lastChild);
        }
    }
    Private.updateContent = updateContent;
    /**
     * A set of special-cased attribute names.
     */
    var specialAttrs = {
        'key': true,
        'className': true,
        'htmlFor': true,
        'dataset': true,
        'style': true,
    };
    /**
     * Add element attributes to a newly created HTML element.
     */
    function addAttrs(element, attrs) {
        // Add the inline event listeners and node attributes.
        for (var name_1 in attrs) {
            if (name_1 in specialAttrs) {
                continue;
            }
            if (name_1.substr(0, 2) === 'on') {
                element[name_1] = attrs[name_1];
            }
            else {
                element.setAttribute(name_1, attrs[name_1]);
            }
        }
        // Add the element `class` attribute.
        if (attrs.className !== undefined) {
            element.setAttribute('class', attrs.className);
        }
        // Add the element `for` attribute.
        if (attrs.htmlFor !== undefined) {
            element.setAttribute('for', attrs.htmlFor);
        }
        // Add the dataset values.
        if (attrs.dataset) {
            addDataset(element, attrs.dataset);
        }
        // Add the inline styles.
        if (attrs.style) {
            addStyle(element, attrs.style);
        }
    }
    /**
     * Update the element attributes of an HTML element.
     */
    function updateAttrs(element, oldAttrs, newAttrs) {
        // Do nothing if the attrs are the same object.
        if (oldAttrs === newAttrs) {
            return;
        }
        // Setup the strongly typed loop variable.
        var name;
        // Remove attributes and listeners which no longer exist.
        for (name in oldAttrs) {
            if (name in specialAttrs || name in newAttrs) {
                continue;
            }
            if (name.substr(0, 2) === 'on') {
                element[name] = null;
            }
            else {
                element.removeAttribute(name);
            }
        }
        // Add and update new and existing attributes and listeners.
        for (name in newAttrs) {
            if (name in specialAttrs || oldAttrs[name] === newAttrs[name]) {
                continue;
            }
            if (name.substr(0, 2) === 'on') {
                element[name] = newAttrs[name];
            }
            else {
                element.setAttribute(name, newAttrs[name]);
            }
        }
        // Update the element `class` attribute.
        if (oldAttrs.className !== newAttrs.className) {
            if (newAttrs.className !== undefined) {
                element.setAttribute('class', newAttrs.className);
            }
            else {
                element.removeAttribute('class');
            }
        }
        // Add the element `for` attribute.
        if (oldAttrs.htmlFor !== newAttrs.htmlFor) {
            if (newAttrs.htmlFor !== undefined) {
                element.setAttribute('for', newAttrs.htmlFor);
            }
            else {
                element.removeAttribute('for');
            }
        }
        // Update the dataset values.
        if (oldAttrs.dataset !== newAttrs.dataset) {
            updateDataset(element, oldAttrs.dataset || {}, newAttrs.dataset || {});
        }
        // Update the inline styles.
        if (oldAttrs.style !== newAttrs.style) {
            updateStyle(element, oldAttrs.style || {}, newAttrs.style || {});
        }
    }
    /**
     * Add dataset values to a newly created HTML element.
     */
    function addDataset(element, dataset) {
        for (var name_2 in dataset) {
            element.setAttribute("data-" + name_2, dataset[name_2]);
        }
    }
    /**
     * Update the dataset values of an HTML element.
     */
    function updateDataset(element, oldDataset, newDataset) {
        for (var name_3 in oldDataset) {
            if (!(name_3 in newDataset)) {
                element.removeAttribute("data-" + name_3);
            }
        }
        for (var name_4 in newDataset) {
            if (oldDataset[name_4] !== newDataset[name_4]) {
                element.setAttribute("data-" + name_4, newDataset[name_4]);
            }
        }
    }
    /**
     * Add inline style values to a newly created HTML element.
     */
    function addStyle(element, style) {
        var elemStyle = element.style;
        var name;
        for (name in style) {
            elemStyle[name] = style[name];
        }
    }
    /**
     * Update the inline style values of an HTML element.
     */
    function updateStyle(element, oldStyle, newStyle) {
        var elemStyle = element.style;
        var name;
        for (name in oldStyle) {
            if (!(name in newStyle)) {
                elemStyle[name] = '';
            }
        }
        for (name in newStyle) {
            if (oldStyle[name] !== newStyle[name]) {
                elemStyle[name] = newStyle[name];
            }
        }
    }
    /**
     * Collect a mapping of keyed elements for the host content.
     */
    function collectKeys(host, content) {
        var node = host.firstChild;
        var keyMap = Object.create(null);
        for (var _i = 0, content_1 = content; _i < content_1.length; _i++) {
            var vNode = content_1[_i];
            if (vNode.type === 'element' && vNode.attrs.key) {
                keyMap[vNode.attrs.key] = { vNode: vNode, element: node };
            }
            node = node.nextSibling;
        }
        return keyMap;
    }
})(Private || (Private = {}));
