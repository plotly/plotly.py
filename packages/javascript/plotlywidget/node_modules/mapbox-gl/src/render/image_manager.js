// @flow

import ShelfPack from '@mapbox/shelf-pack';

import { RGBAImage } from '../util/image';
import { ImagePosition } from './image_atlas';
import Texture from './texture';
import assert from 'assert';

import type {StyleImage} from '../style/style_image';
import type Context from '../gl/context';
import type {Bin} from '@mapbox/shelf-pack';
import type {Callback} from '../types/callback';

type Pattern = {
    bin: Bin,
    position: ImagePosition
};

// When copied into the atlas texture, image data is padded by one pixel on each side. Icon
// images are padded with fully transparent pixels, while pattern images are padded with a
// copy of the image data wrapped from the opposite side. In both cases, this ensures the
// correct behavior of GL_LINEAR texture sampling mode.
const padding = 1;

/*
    ImageManager does two things:

        1. Tracks requests for icon images from tile workers and sends responses when the requests are fulfilled.
        2. Builds a texture atlas for pattern images.

    These are disparate responsibilities and should eventually be handled by different classes. When we implement
    data-driven support for `*-pattern`, we'll likely use per-bucket pattern atlases, and that would be a good time
    to refactor this.
*/
class ImageManager {
    images: {[string]: StyleImage};
    loaded: boolean;
    requestors: Array<{ids: Array<string>, callback: Callback<{[string]: StyleImage}>}>;

    shelfPack: ShelfPack;
    patterns: {[string]: Pattern};
    atlasImage: RGBAImage;
    atlasTexture: ?Texture;
    dirty: boolean;

    constructor() {
        this.images = {};
        this.loaded = false;
        this.requestors = [];

        this.shelfPack = new ShelfPack(64, 64, {autoResize: true});
        this.patterns = {};
        this.atlasImage = new RGBAImage({width: 64, height: 64});
        this.dirty = true;
    }

    isLoaded() {
        return this.loaded;
    }

    setLoaded(loaded: boolean) {
        if (this.loaded === loaded) {
            return;
        }

        this.loaded = loaded;

        if (loaded) {
            for (const {ids, callback} of this.requestors) {
                this._notify(ids, callback);
            }
            this.requestors = [];
        }
    }

    getImage(id: string): ?StyleImage {
        return this.images[id];
    }

    addImage(id: string, image: StyleImage) {
        assert(!this.images[id]);
        this.images[id] = image;
    }

    removeImage(id: string) {
        assert(this.images[id]);
        delete this.images[id];

        const pattern = this.patterns[id];
        if (pattern) {
            this.shelfPack.unref(pattern.bin);
            delete this.patterns[id];
        }
    }

    getImages(ids: Array<string>, callback: Callback<{[string]: StyleImage}>) {
        // If the sprite has been loaded, or if all the icon dependencies are already present
        // (i.e. if they've been addeded via runtime styling), then notify the requestor immediately.
        // Otherwise, delay notification until the sprite is loaded. At that point, if any of the
        // dependencies are still unavailable, we'll just assume they are permanently missing.
        let hasAllDependencies = true;
        if (!this.isLoaded()) {
            for (const id of ids) {
                if (!this.images[id]) {
                    hasAllDependencies = false;
                }
            }
        }
        if (this.isLoaded() || hasAllDependencies) {
            this._notify(ids, callback);
        } else {
            this.requestors.push({ids, callback});
        }
    }

    _notify(ids: Array<string>, callback: Callback<{[string]: StyleImage}>) {
        const response = {};

        for (const id of ids) {
            const image = this.images[id];
            if (image) {
                // Clone the image so that our own copy of its ArrayBuffer doesn't get transferred.
                response[id] = {
                    data: image.data.clone(),
                    pixelRatio: image.pixelRatio,
                    sdf: image.sdf
                };
            }
        }

        callback(null, response);
    }

    // Pattern stuff

    getPixelSize() {
        return {
            width: this.shelfPack.w,
            height: this.shelfPack.h
        };
    }

    getPattern(id: string): ?ImagePosition {
        const pattern = this.patterns[id];
        if (pattern) {
            return pattern.position;
        }

        const image = this.getImage(id);
        if (!image) {
            return null;
        }

        const width = image.data.width + padding * 2;
        const height = image.data.height + padding * 2;

        const bin = this.shelfPack.packOne(width, height);
        if (!bin) {
            return null;
        }

        this.atlasImage.resize(this.getPixelSize());

        const src = image.data;
        const dst = this.atlasImage;

        const x = bin.x + padding;
        const y = bin.y + padding;
        const w = src.width;
        const h = src.height;

        RGBAImage.copy(src, dst, { x: 0, y: 0 }, { x, y }, { width: w, height: h });

        // Add 1 pixel wrapped padding on each side of the image.
        RGBAImage.copy(src, dst, { x: 0, y: h - 1 }, { x: x, y: y - 1 }, { width: w, height: 1 }); // T
        RGBAImage.copy(src, dst, { x: 0, y:     0 }, { x: x, y: y + h }, { width: w, height: 1 }); // B
        RGBAImage.copy(src, dst, { x: w - 1, y: 0 }, { x: x - 1, y: y }, { width: 1, height: h }); // L
        RGBAImage.copy(src, dst, { x: 0,     y: 0 }, { x: x + w, y: y }, { width: 1, height: h }); // R

        this.dirty = true;

        const position = new ImagePosition(bin, image);
        this.patterns[id] = { bin, position };
        return position;
    }

    bind(context: Context) {
        const gl = context.gl;
        if (!this.atlasTexture) {
            this.atlasTexture = new Texture(context, this.atlasImage, gl.RGBA);
        } else if (this.dirty) {
            this.atlasTexture.update(this.atlasImage);
            this.dirty = false;
        }

        this.atlasTexture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE);
    }
}

export default ImageManager;
