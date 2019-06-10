// @flow

import jsdom from 'jsdom';

import gl from 'gl';
import sinon from 'sinon';
import { extend } from './util';

const { window: _window } = new jsdom.JSDOM('', {
    virtualConsole: new jsdom.VirtualConsole().sendTo(console)
});

restore();

export default _window;

function restore(): Window {
    // Remove previous window from exported object
    const previousWindow = _window;
    if (previousWindow.close) previousWindow.close();
    for (const key in previousWindow) {
        if (previousWindow.hasOwnProperty(key)) {
            delete (previousWindow: any)[key];
        }
    }

    // Create new window and inject into exported object
    const { window } = new jsdom.JSDOM('', {
        // Send jsdom console output to the node console object.
        virtualConsole: new jsdom.VirtualConsole().sendTo(console)
    });

    window.devicePixelRatio = 1;

    window.requestAnimationFrame = function(callback) {
        return setImmediate(callback, 0);
    };
    window.cancelAnimationFrame = clearImmediate;

    // Add webgl context with the supplied GL
    const originalGetContext = window.HTMLCanvasElement.prototype.getContext;
    window.HTMLCanvasElement.prototype.getContext = function (type, attributes) {
        if (type === 'webgl') {
            if (!this._webGLContext) {
                this._webGLContext = gl(this.width, this.height, attributes);
            }
            return this._webGLContext;
        }
        // Fallback to existing HTMLCanvasElement getContext behaviour
        return originalGetContext.call(this, type, attributes);
    };

    window.useFakeHTMLCanvasGetContext = function() {
        this.HTMLCanvasElement.prototype.getContext = function() { return '2d'; };
    };

    window.useFakeXMLHttpRequest = function() {
        sinon.xhr.supportsCORS = true;
        this.server = sinon.fakeServer.create();
        this.XMLHttpRequest = this.server.xhr;
    };

    window.URL.revokeObjectURL = function () {};

    window.restore = restore;

    window.ImageData = window.ImageData || function() { return false; };
    window.ImageBitmap = window.ImageBitmap || function() { return false; };
    window.WebGLFramebuffer = window.WebGLFramebuffer || Object;
    extend(_window, window);

    return window;
}
