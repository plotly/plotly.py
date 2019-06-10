// @flow
import { RGBAImage } from '../util/image';

import { warnOnce, clamp } from '../util/util';
import { register } from '../util/web_worker_transfer';

export class Level {
    dim: number;
    border: number;
    stride: number;
    data: Int32Array;

    constructor(dim: number, border: number, data: ?Int32Array) {
        if (dim <= 0) throw new RangeError('Level must have positive dimension');
        this.dim = dim;
        this.border = border;
        this.stride = this.dim + 2 * this.border;
        this.data = data || new Int32Array((this.dim + 2 * this.border) * (this.dim + 2 * this.border));
    }

    set(x: number, y: number, value: number) {
        this.data[this._idx(x, y)] = value + 65536;
    }

    get(x: number, y: number) {
        return this.data[this._idx(x, y)] - 65536;
    }

    _idx(x: number, y: number) {
        if (x < -this.border || x >= this.dim + this.border ||  y < -this.border || y >= this.dim + this.border) throw new RangeError('out of range source coordinates for DEM data');
        return (y + this.border) * this.stride + (x + this.border);
    }
}

register('Level', Level);

// DEMData is a data structure for decoding, backfilling, and storing elevation data for processing in the hillshade shaders
// data can be populated either from a pngraw image tile or from serliazed data sent back from a worker. When data is initially
// loaded from a image tile, we decode the pixel values using the mapbox terrain-rgb tileset decoding formula, but we store the
// elevation data in a Level as an Int32 value. we add 65536 (2^16) to eliminate negative values and enable the use of
// integer overflow when creating the texture used in the hillshadePrepare step.

// DEMData also handles the backfilling of data from a tile's neighboring tiles. This is necessary because we use a pixel's 8
// surrounding pixel values to compute the slope at that pixel, and we cannot accurately calculate the slope at pixels on a
// tile's edge without backfilling from neighboring tiles.

export default class DEMData {
    uid: string;
    scale: number;
    level: Level;
    loaded: boolean;

    constructor(uid: string, scale: ?number, data: ?Level) {
        this.uid = uid;
        this.scale = scale || 1;
        // if no data is provided, use a temporary empty level to satisfy flow
        this.level = data || new Level(256, 512);
        this.loaded = !!data;
    }

    loadFromImage(data: RGBAImage, encoding: "mapbox" | "terrarium") {
        if (data.height !== data.width) throw new RangeError('DEM tiles must be square');
        if (encoding && encoding !== "mapbox" && encoding !== "terrarium") return warnOnce(
            `"${encoding}" is not a valid encoding type. Valid types include "mapbox" and "terrarium".`
        );
        // Build level 0
        const level = this.level = new Level(data.width, data.width / 2);
        const pixels = data.data;

        this._unpackData(level, pixels, encoding || "mapbox");

        // in order to avoid flashing seams between tiles, here we are initially populating a 1px border of pixels around the image
        // with the data of the nearest pixel from the image. this data is eventually replaced when the tile's neighboring
        // tiles are loaded and the accurate data can be backfilled using DEMData#backfillBorder
        for (let x = 0; x < level.dim; x++) {
            // left vertical border
            level.set(-1, x, level.get(0, x));
            // right vertical border
            level.set(level.dim, x, level.get(level.dim - 1, x));
            // left horizontal border
            level.set(x, -1, level.get(x, 0));
            // right horizontal border
            level.set(x, level.dim, level.get(x, level.dim - 1));
        }
        // corners
        level.set(-1, -1, level.get(0, 0));
        level.set(level.dim, -1, level.get(level.dim - 1, 0));
        level.set(-1, level.dim, level.get(0, level.dim - 1));
        level.set(level.dim, level.dim, level.get(level.dim - 1, level.dim - 1));
        this.loaded = true;
    }

    _unpackMapbox(r: number, g: number, b: number) {
        // unpacking formula for mapbox.terrain-rgb:
        // https://www.mapbox.com/help/access-elevation-data/#mapbox-terrain-rgb
        return ((r * 256 * 256 + g * 256.0 + b) / 10.0 - 10000.0);
    }

    _unpackTerrarium(r: number, g: number, b: number) {
        // unpacking formula for mapzen terrarium:
        // https://aws.amazon.com/public-datasets/terrain/
        return ((r * 256 + g + b / 256) - 32768.0);
    }

    _unpackData(level: Level, pixels: Uint8Array | Uint8ClampedArray, encoding: string) {
        const unpackFunctions = {"mapbox": this._unpackMapbox, "terrarium": this._unpackTerrarium};
        const unpack = unpackFunctions[encoding];
        for (let y = 0; y < level.dim; y++) {
            for (let x = 0; x < level.dim; x++) {
                const i = y * level.dim + x;
                const j = i * 4;
                level.set(x, y, this.scale * unpack(pixels[j], pixels[j + 1], pixels[j + 2]));
            }
        }
    }

    getPixels() {
        return new RGBAImage({width: this.level.dim + 2 * this.level.border, height: this.level.dim + 2 * this.level.border}, new Uint8Array(this.level.data.buffer));
    }

    backfillBorder(borderTile: DEMData, dx: number, dy: number) {
        const t = this.level;
        const o = borderTile.level;

        if (t.dim !== o.dim) throw new Error('level mismatch (dem dimension)');

        let _xMin = dx * t.dim,
            _xMax = dx * t.dim + t.dim,
            _yMin = dy * t.dim,
            _yMax = dy * t.dim + t.dim;

        switch (dx) {
        case -1:
            _xMin = _xMax - 1;
            break;
        case 1:
            _xMax = _xMin + 1;
            break;
        }

        switch (dy) {
        case -1:
            _yMin = _yMax - 1;
            break;
        case 1:
            _yMax = _yMin + 1;
            break;
        }

        const xMin = clamp(_xMin, -t.border, t.dim + t.border);
        const xMax = clamp(_xMax, -t.border, t.dim + t.border);
        const yMin = clamp(_yMin, -t.border, t.dim + t.border);
        const yMax = clamp(_yMax, -t.border, t.dim + t.border);

        const ox = -dx * t.dim;
        const oy = -dy * t.dim;
        for (let y = yMin; y < yMax; y++) {
            for (let x = xMin; x < xMax; x++) {
                t.set(x, y, o.get(x + ox, y + oy));
            }
        }
    }
}

register('DEMData', DEMData);
