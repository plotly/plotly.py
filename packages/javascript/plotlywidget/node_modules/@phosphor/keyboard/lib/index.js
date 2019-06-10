"use strict";
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Get the global application keyboard layout instance.
 *
 * @returns The keyboard layout for use by the application.
 *
 * #### Notes
 * The default keyboard layout is US-English.
 */
function getKeyboardLayout() {
    return Private.keyboardLayout;
}
exports.getKeyboardLayout = getKeyboardLayout;
/**
 * Set the global application keyboard layout instance.
 *
 * @param - The keyboard layout for use by the application.
 *
 * #### Notes
 * The keyboard layout should typically be set on application startup
 * to a layout which is appropriate for the user's system.
 */
function setKeyboardLayout(layout) {
    Private.keyboardLayout = layout;
}
exports.setKeyboardLayout = setKeyboardLayout;
/**
 * A concrete implementation of [[IKeyboardLayout]] based on keycodes.
 *
 * The `keyCode` property of a `'keydown'` event is a browser and OS
 * specific representation of the physical key (not character) which
 * was pressed on a keyboard. While not the most convenient API, it
 * is currently the only one which works reliably on all browsers.
 *
 * This class accepts a user-defined mapping of keycode to key, which
 * allows for reliable shortcuts tailored to the user's system.
 */
var KeycodeLayout = (function () {
    /**
     * Construct a new keycode layout.
     *
     * @param name - The human readable name for the layout.
     *
     * @param codes - A mapping of keycode to key value.
     */
    function KeycodeLayout(name, codes) {
        this.name = name;
        this._codes = codes;
        this._keys = KeycodeLayout.extractKeys(codes);
    }
    /**
     * Get an array of the key values supported by the layout.
     *
     * @returns A new array of the supported key values.
     */
    KeycodeLayout.prototype.keys = function () {
        return Object.keys(this._keys);
    };
    /**
     * Test whether the given key is a valid value for the layout.
     *
     * @param key - The user provided key to test for validity.
     *
     * @returns `true` if the key is valid, `false` otherwise.
     */
    KeycodeLayout.prototype.isValidKey = function (key) {
        return key in this._keys;
    };
    /**
     * Get the key for a `'keydown'` event.
     *
     * @param event - The event object for a `'keydown'` event.
     *
     * @returns The associated key value, or an empty string if
     *   the event does not represent a valid primary key.
     */
    KeycodeLayout.prototype.keyForKeydownEvent = function (event) {
        return this._codes[event.keyCode] || '';
    };
    return KeycodeLayout;
}());
exports.KeycodeLayout = KeycodeLayout;
/**
 * The namespace for the `KeycodeLayout` class statics.
 */
(function (KeycodeLayout) {
    /**
     * Extract the set of keys from a code map.
     *
     * @param code - The code map of interest.
     *
     * @returns A set of the keys in the code map.
     */
    function extractKeys(codes) {
        var keys = Object.create(null);
        for (var c in codes) {
            keys[codes[c]] = true;
        }
        return keys;
    }
    KeycodeLayout.extractKeys = extractKeys;
})(KeycodeLayout = exports.KeycodeLayout || (exports.KeycodeLayout = {}));
exports.KeycodeLayout = KeycodeLayout;
/**
 * A keycode-based keyboard layout for US English keyboards.
 *
 * This layout is valid for the following OS/Browser combinations.
 *
 * - Windows
 *   - Chrome
 *   - Firefox
 *   - IE
 *
 * - OSX
 *   - Chrome
 *   - Firefox
 *   - Safari
 *
 * - Linux
 *   - Chrome
 *   - Firefox
 *
 * Other combinations may also work, but are untested.
 */
exports.EN_US = new KeycodeLayout('en-us', {
    8: 'Backspace',
    9: 'Tab',
    13: 'Enter',
    19: 'Pause',
    27: 'Escape',
    32: 'Space',
    33: 'PageUp',
    34: 'PageDown',
    35: 'End',
    36: 'Home',
    37: 'ArrowLeft',
    38: 'ArrowUp',
    39: 'ArrowRight',
    40: 'ArrowDown',
    45: 'Insert',
    46: 'Delete',
    48: '0',
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',
    59: ';',
    61: '=',
    65: 'A',
    66: 'B',
    67: 'C',
    68: 'D',
    69: 'E',
    70: 'F',
    71: 'G',
    72: 'H',
    73: 'I',
    74: 'J',
    75: 'K',
    76: 'L',
    77: 'M',
    78: 'N',
    79: 'O',
    80: 'P',
    81: 'Q',
    82: 'R',
    83: 'S',
    84: 'T',
    85: 'U',
    86: 'V',
    87: 'W',
    88: 'X',
    89: 'Y',
    90: 'Z',
    93: 'ContextMenu',
    96: '0',
    97: '1',
    98: '2',
    99: '3',
    100: '4',
    101: '5',
    102: '6',
    103: '7',
    104: '8',
    105: '9',
    106: '*',
    107: '+',
    109: '-',
    110: '.',
    111: '/',
    112: 'F1',
    113: 'F2',
    114: 'F3',
    115: 'F4',
    116: 'F5',
    117: 'F6',
    118: 'F7',
    119: 'F8',
    120: 'F9',
    121: 'F10',
    122: 'F11',
    123: 'F12',
    173: '-',
    186: ';',
    187: '=',
    188: ',',
    189: '-',
    190: '.',
    191: '/',
    192: '`',
    219: '[',
    220: '\\',
    221: ']',
    222: '\''
});
/**
 * The namespace for the module implementation details.
 */
var Private;
(function (Private) {
    /**
     * The global keyboard layout instance.
     */
    Private.keyboardLayout = exports.EN_US;
})(Private || (Private = {}));
