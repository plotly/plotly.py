// @flow

import Coordinate from '../geo/coordinate';

import { OverscaledTileID } from '../source/tile_id';

export default tileCover;

function tileCover(z: number, bounds: [Coordinate, Coordinate, Coordinate, Coordinate],
        actualZ: number, renderWorldCopies: boolean | void) {
    if (renderWorldCopies === undefined) {
        renderWorldCopies = true;
    }
    const tiles = 1 << z;
    const t = {};

    function scanLine(x0, x1, y) {
        let x, w, wx, coord;
        if (y >= 0 && y <= tiles) {
            for (x = x0; x < x1; x++) {
                w = Math.floor(x / tiles);
                wx = (x % tiles + tiles) % tiles;
                if (w === 0 || renderWorldCopies === true) {
                    coord = new OverscaledTileID(actualZ, w, z, wx, y);
                    t[coord.key] = coord;
                }
            }
        }
    }

    // Divide the screen up in two triangles and scan each of them:
    // +---/
    // | / |
    // /---+
    scanTriangle(bounds[0], bounds[1], bounds[2], 0, tiles, scanLine);
    scanTriangle(bounds[2], bounds[3], bounds[0], 0, tiles, scanLine);

    return Object.keys(t).map((id) => {
        return t[id];
    });
}


// Taken from polymaps src/Layer.js
// https://github.com/simplegeo/polymaps/blob/master/src/Layer.js#L333-L383

function edge(a: Coordinate, b: Coordinate) {
    if (a.row > b.row) { const t = a; a = b; b = t; }
    return {
        x0: a.column,
        y0: a.row,
        x1: b.column,
        y1: b.row,
        dx: b.column - a.column,
        dy: b.row - a.row
    };
}

function scanSpans(e0, e1, ymin, ymax, scanLine) {
    const y0 = Math.max(ymin, Math.floor(e1.y0));
    const y1 = Math.min(ymax, Math.ceil(e1.y1));

    // sort edges by x-coordinate
    if ((e0.x0 === e1.x0 && e0.y0 === e1.y0) ?
        (e0.x0 + e1.dy / e0.dy * e0.dx < e1.x1) :
        (e0.x1 - e1.dy / e0.dy * e0.dx < e1.x0)) {
        const t = e0; e0 = e1; e1 = t;
    }

    // scan lines!
    const m0 = e0.dx / e0.dy;
    const m1 = e1.dx / e1.dy;
    const d0 = e0.dx > 0; // use y + 1 to compute x0
    const d1 = e1.dx < 0; // use y + 1 to compute x1
    for (let y = y0; y < y1; y++) {
        const x0 = m0 * Math.max(0, Math.min(e0.dy, y + d0 - e0.y0)) + e0.x0;
        const x1 = m1 * Math.max(0, Math.min(e1.dy, y + d1 - e1.y0)) + e1.x0;
        scanLine(Math.floor(x1), Math.ceil(x0), y);
    }
}

function scanTriangle(a: Coordinate, b: Coordinate, c: Coordinate, ymin, ymax, scanLine) {
    let ab = edge(a, b),
        bc = edge(b, c),
        ca = edge(c, a);

    let t;

    // sort edges by y-length
    if (ab.dy > bc.dy) { t = ab; ab = bc; bc = t; }
    if (ab.dy > ca.dy) { t = ab; ab = ca; ca = t; }
    if (bc.dy > ca.dy) { t = bc; bc = ca; ca = t; }

    // scan span! scan span!
    if (ab.dy) scanSpans(ca, ab, ymin, ymax, scanLine);
    if (bc.dy) scanSpans(ca, bc, ymin, ymax, scanLine);
}

