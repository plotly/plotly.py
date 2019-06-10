// @flow

import window from './window';

const now = window.performance && window.performance.now ?
    window.performance.now.bind(window.performance) :
    Date.now.bind(Date);

const raf = window.requestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.msRequestAnimationFrame;

const cancel = window.cancelAnimationFrame ||
    window.mozCancelAnimationFrame ||
    window.webkitCancelAnimationFrame ||
    window.msCancelAnimationFrame;

/**
 * @private
 */
const exported = {
    /**
     * Provides a function that outputs milliseconds: either performance.now()
     * or a fallback to Date.now()
     */
    now,

    frame(fn: Function) {
        return raf(fn);
    },

    cancelFrame(id: number) {
        return cancel(id);
    },

    getImageData(img: CanvasImageSource): ImageData {
        const canvas = window.document.createElement('canvas');
        const context = canvas.getContext('2d');
        if (!context) {
            throw new Error('failed to create canvas 2d context');
        }
        canvas.width = img.width;
        canvas.height = img.height;
        context.drawImage(img, 0, 0, img.width, img.height);
        return context.getImageData(0, 0, img.width, img.height);
    },

    hardwareConcurrency: window.navigator.hardwareConcurrency || 4,
    get devicePixelRatio() { return window.devicePixelRatio; },
    supportsWebp: false
};

export default exported;

if (window.document) {
    const webpImgTest = window.document.createElement('img');
    webpImgTest.onload = function() {
        exported.supportsWebp = true;
    };
    webpImgTest.src = 'data:image/webp;base64,UklGRh4AAABXRUJQVlA4TBEAAAAvAQAAAAfQ//73v/+BiOh/AAA=';
}
