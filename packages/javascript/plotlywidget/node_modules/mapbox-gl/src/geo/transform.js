// @flow

import LngLat from './lng_lat';

import Point from '@mapbox/point-geometry';
import Coordinate from './coordinate';
import { wrap, clamp } from '../util/util';
import {number as interpolate} from '../style-spec/util/interpolate';
import tileCover from '../util/tile_cover';
import { CanonicalTileID, UnwrappedTileID } from '../source/tile_id';
import EXTENT from '../data/extent';
import glmatrix from '@mapbox/gl-matrix';

const vec4 = glmatrix.vec4,
    mat4 = glmatrix.mat4,
    mat2 = glmatrix.mat2;

/**
 * A single transform, generally used for a single tile to be
 * scaled, rotated, and zoomed.
 * @private
 */
class Transform {
    tileSize: number;
    tileZoom: number;
    lngRange: ?[number, number];
    latRange: ?[number, number];
    scale: number;
    width: number;
    height: number;
    angle: number;
    rotationMatrix: Float64Array;
    zoomFraction: number;
    pixelsToGLUnits: Array<number>;
    cameraToCenterDistance: number;
    projMatrix: Float64Array;
    alignedProjMatrix: Float64Array;
    pixelMatrix: Float64Array;
    pixelMatrixInverse: Float64Array;
    _fov: number;
    _pitch: number;
    _zoom: number;
    _unmodified: boolean;
    _renderWorldCopies: boolean;
    _minZoom: number;
    _maxZoom: number;
    _center: LngLat;
    _constraining: boolean;
    _posMatrixCache: {[number]: Float32Array};
    _alignedPosMatrixCache: {[number]: Float32Array};

    constructor(minZoom: ?number, maxZoom: ?number, renderWorldCopies: boolean | void) {
        this.tileSize = 512; // constant

        this._renderWorldCopies = renderWorldCopies === undefined ? true : renderWorldCopies;
        this._minZoom = minZoom || 0;
        this._maxZoom = maxZoom || 22;

        this.latRange = [-85.05113, 85.05113];

        this.width = 0;
        this.height = 0;
        this._center = new LngLat(0, 0);
        this.zoom = 0;
        this.angle = 0;
        this._fov = 0.6435011087932844;
        this._pitch = 0;
        this._unmodified = true;
        this._posMatrixCache = {};
        this._alignedPosMatrixCache = {};
    }

    clone(): Transform {
        const clone = new Transform(this._minZoom, this._maxZoom, this._renderWorldCopies);
        clone.tileSize = this.tileSize;
        clone.latRange = this.latRange;
        clone.width = this.width;
        clone.height = this.height;
        clone._center = this._center;
        clone.zoom = this.zoom;
        clone.angle = this.angle;
        clone._fov = this._fov;
        clone._pitch = this._pitch;
        clone._unmodified = this._unmodified;
        clone._calcMatrices();
        return clone;
    }

    get minZoom(): number { return this._minZoom; }
    set minZoom(zoom: number) {
        if (this._minZoom === zoom) return;
        this._minZoom = zoom;
        this.zoom = Math.max(this.zoom, zoom);
    }

    get maxZoom(): number { return this._maxZoom; }
    set maxZoom(zoom: number) {
        if (this._maxZoom === zoom) return;
        this._maxZoom = zoom;
        this.zoom = Math.min(this.zoom, zoom);
    }

    get renderWorldCopies(): boolean { return this._renderWorldCopies; }
    set renderWorldCopies(renderWorldCopies?: ?boolean) {
        if (renderWorldCopies === undefined) {
            renderWorldCopies = true;
        } else if (renderWorldCopies === null) {
            renderWorldCopies = false;
        }

        this._renderWorldCopies = renderWorldCopies;
    }

    get worldSize(): number {
        return this.tileSize * this.scale;
    }

    get centerPoint(): Point {
        return this.size._div(2);
    }

    get size(): Point {
        return new Point(this.width, this.height);
    }

    get bearing(): number {
        return -this.angle / Math.PI * 180;
    }
    set bearing(bearing: number) {
        const b = -wrap(bearing, -180, 180) * Math.PI / 180;
        if (this.angle === b) return;
        this._unmodified = false;
        this.angle = b;
        this._calcMatrices();

        // 2x2 matrix for rotating points
        this.rotationMatrix = mat2.create();
        mat2.rotate(this.rotationMatrix, this.rotationMatrix, this.angle);
    }

    get pitch(): number {
        return this._pitch / Math.PI * 180;
    }
    set pitch(pitch: number) {
        const p = clamp(pitch, 0, 60) / 180 * Math.PI;
        if (this._pitch === p) return;
        this._unmodified = false;
        this._pitch = p;
        this._calcMatrices();
    }

    get fov(): number {
        return this._fov / Math.PI * 180;
    }
    set fov(fov: number) {
        fov = Math.max(0.01, Math.min(60, fov));
        if (this._fov === fov) return;
        this._unmodified = false;
        this._fov = fov / 180 * Math.PI;
        this._calcMatrices();
    }

    get zoom(): number { return this._zoom; }
    set zoom(zoom: number) {
        const z = Math.min(Math.max(zoom, this.minZoom), this.maxZoom);
        if (this._zoom === z) return;
        this._unmodified = false;
        this._zoom = z;
        this.scale = this.zoomScale(z);
        this.tileZoom = Math.floor(z);
        this.zoomFraction = z - this.tileZoom;
        this._constrain();
        this._calcMatrices();
    }

    get center(): LngLat { return this._center; }
    set center(center: LngLat) {
        if (center.lat === this._center.lat && center.lng === this._center.lng) return;
        this._unmodified = false;
        this._center = center;
        this._constrain();
        this._calcMatrices();
    }

    /**
     * Return a zoom level that will cover all tiles the transform
     * @param {Object} options
     * @param {number} options.tileSize
     * @param {boolean} options.roundZoom
     * @returns {number} zoom level
     */
    coveringZoomLevel(options: {roundZoom?: boolean, tileSize: number}) {
        return (options.roundZoom ? Math.round : Math.floor)(
            this.zoom + this.scaleZoom(this.tileSize / options.tileSize)
        );
    }

    /**
     * Return any "wrapped" copies of a given tile coordinate that are visible
     * in the current view.
     *
     * @private
     */
    getVisibleUnwrappedCoordinates(tileID: CanonicalTileID) {
        const ul = this.pointCoordinate(new Point(0, 0), 0);
        const ur = this.pointCoordinate(new Point(this.width, 0), 0);
        const w0 = Math.floor(ul.column);
        const w1 = Math.floor(ur.column);
        const result = [new UnwrappedTileID(0, tileID)];
        if (this._renderWorldCopies) {
            for (let w = w0; w <= w1; w++) {
                if (w === 0) continue;
                result.push(new UnwrappedTileID(w, tileID));
            }
        }
        return result;
    }

    /**
     * Return all coordinates that could cover this transform for a covering
     * zoom level.
     * @param {Object} options
     * @param {number} options.tileSize
     * @param {number} options.minzoom
     * @param {number} options.maxzoom
     * @param {boolean} options.roundZoom
     * @param {boolean} options.reparseOverscaled
     * @param {boolean} options.renderWorldCopies
     * @returns {Array<Tile>} tiles
     */
    coveringTiles(
        options: {
            tileSize: number,
            minzoom?: number,
            maxzoom?: number,
            roundZoom?: boolean,
            reparseOverscaled?: boolean,
            renderWorldCopies?: boolean
        }
    ) {
        let z = this.coveringZoomLevel(options);
        const actualZ = z;

        if (options.minzoom !== undefined && z < options.minzoom) return [];
        if (options.maxzoom !== undefined && z > options.maxzoom) z = options.maxzoom;

        const centerCoord = this.pointCoordinate(this.centerPoint, z);
        const centerPoint = new Point(centerCoord.column - 0.5, centerCoord.row - 0.5);
        const cornerCoords = [
            this.pointCoordinate(new Point(0, 0), z),
            this.pointCoordinate(new Point(this.width, 0), z),
            this.pointCoordinate(new Point(this.width, this.height), z),
            this.pointCoordinate(new Point(0, this.height), z)
        ];
        return tileCover(z, cornerCoords, options.reparseOverscaled ? actualZ : z, this._renderWorldCopies)
            .sort((a, b) => centerPoint.dist(a.canonical) - centerPoint.dist(b.canonical));
    }

    resize(width: number, height: number) {
        this.width = width;
        this.height = height;

        this.pixelsToGLUnits = [2 / width, -2 / height];
        this._constrain();
        this._calcMatrices();
    }

    get unmodified(): boolean { return this._unmodified; }

    zoomScale(zoom: number) { return Math.pow(2, zoom); }
    scaleZoom(scale: number) { return Math.log(scale) / Math.LN2; }

    project(lnglat: LngLat) {
        return new Point(
            this.lngX(lnglat.lng),
            this.latY(lnglat.lat));
    }

    unproject(point: Point): LngLat {
        return new LngLat(
            this.xLng(point.x),
            this.yLat(point.y));
    }

    get x(): number { return this.lngX(this.center.lng); }
    get y(): number { return this.latY(this.center.lat); }

    get point(): Point { return new Point(this.x, this.y); }

    /**
     * latitude to absolute x coord
     * @returns {number} pixel coordinate
     */
    lngX(lng: number) {
        return (180 + lng) * this.worldSize / 360;
    }
    /**
     * latitude to absolute y coord
     * @returns {number} pixel coordinate
     */
    latY(lat: number) {
        const y = 180 / Math.PI * Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360));
        return (180 - y) * this.worldSize / 360;
    }

    xLng(x: number) {
        return x * 360 / this.worldSize - 180;
    }
    yLat(y: number) {
        const y2 = 180 - y * 360 / this.worldSize;
        return 360 / Math.PI * Math.atan(Math.exp(y2 * Math.PI / 180)) - 90;
    }

    setLocationAtPoint(lnglat: LngLat, point: Point) {
        const translate = this.pointCoordinate(point)._sub(this.pointCoordinate(this.centerPoint));
        this.center = this.coordinateLocation(this.locationCoordinate(lnglat)._sub(translate));
        if (this._renderWorldCopies) {
            this.center = this.center.wrap();
        }
    }

    /**
     * Given a location, return the screen point that corresponds to it
     * @param {LngLat} lnglat location
     * @returns {Point} screen point
     */
    locationPoint(lnglat: LngLat) {
        return this.coordinatePoint(this.locationCoordinate(lnglat));
    }

    /**
     * Given a point on screen, return its lnglat
     * @param {Point} p screen point
     * @returns {LngLat} lnglat location
     */
    pointLocation(p: Point) {
        return this.coordinateLocation(this.pointCoordinate(p));
    }

    /**
     * Given a geographical lnglat, return an unrounded
     * coordinate that represents it at this transform's zoom level.
     * @param {LngLat} lnglat
     * @returns {Coordinate}
     */
    locationCoordinate(lnglat: LngLat) {
        return new Coordinate(
            this.lngX(lnglat.lng) / this.tileSize,
            this.latY(lnglat.lat) / this.tileSize,
            this.zoom).zoomTo(this.tileZoom);
    }

    /**
     * Given a Coordinate, return its geographical position.
     * @param {Coordinate} coord
     * @returns {LngLat} lnglat
     */
    coordinateLocation(coord: Coordinate) {
        const zoomedCoord = coord.zoomTo(this.zoom);
        return new LngLat(
            this.xLng(zoomedCoord.column * this.tileSize),
            this.yLat(zoomedCoord.row * this.tileSize));
    }

    pointCoordinate(p: Point, zoom?: number) {
        if (zoom === undefined) zoom = this.tileZoom;

        const targetZ = 0;
        // since we don't know the correct projected z value for the point,
        // unproject two points to get a line and then find the point on that
        // line with z=0

        const coord0 = [p.x, p.y, 0, 1];
        const coord1 = [p.x, p.y, 1, 1];

        vec4.transformMat4(coord0, coord0, this.pixelMatrixInverse);
        vec4.transformMat4(coord1, coord1, this.pixelMatrixInverse);

        const w0 = coord0[3];
        const w1 = coord1[3];
        const x0 = coord0[0] / w0;
        const x1 = coord1[0] / w1;
        const y0 = coord0[1] / w0;
        const y1 = coord1[1] / w1;
        const z0 = coord0[2] / w0;
        const z1 = coord1[2] / w1;

        const t = z0 === z1 ? 0 : (targetZ - z0) / (z1 - z0);

        return new Coordinate(
            interpolate(x0, x1, t) / this.tileSize,
            interpolate(y0, y1, t) / this.tileSize,
            this.zoom)._zoomTo(zoom);
    }

    /**
     * Given a coordinate, return the screen point that corresponds to it
     * @param {Coordinate} coord
     * @returns {Point} screen point
     */
    coordinatePoint(coord: Coordinate) {
        const zoomedCoord = coord.zoomTo(this.zoom);
        const p = [zoomedCoord.column * this.tileSize, zoomedCoord.row * this.tileSize, 0, 1];
        vec4.transformMat4(p, p, this.pixelMatrix);
        return new Point(p[0] / p[3], p[1] / p[3]);
    }

    /**
     * Calculate the posMatrix that, given a tile coordinate, would be used to display the tile on a map.
     * @param {UnwrappedTileID} unwrappedTileID;
     */
    calculatePosMatrix(unwrappedTileID: UnwrappedTileID, aligned: boolean = false): Float32Array {
        const posMatrixKey = unwrappedTileID.key;
        const cache = aligned ? this._alignedPosMatrixCache : this._posMatrixCache;
        if (cache[posMatrixKey]) {
            return cache[posMatrixKey];
        }

        const canonical = unwrappedTileID.canonical;
        const scale = this.worldSize / this.zoomScale(canonical.z);
        const unwrappedX = canonical.x + Math.pow(2, canonical.z) * unwrappedTileID.wrap;

        const posMatrix = mat4.identity(new Float64Array(16));
        mat4.translate(posMatrix, posMatrix, [unwrappedX * scale, canonical.y * scale, 0]);
        mat4.scale(posMatrix, posMatrix, [scale / EXTENT, scale / EXTENT, 1]);
        mat4.multiply(posMatrix, aligned ? this.alignedProjMatrix : this.projMatrix, posMatrix);

        cache[posMatrixKey] = new Float32Array(posMatrix);
        return cache[posMatrixKey];
    }

    _constrain() {
        if (!this.center || !this.width || !this.height || this._constraining) return;

        this._constraining = true;

        let minY = -90;
        let maxY = 90;
        let minX = -180;
        let maxX = 180;
        let sy, sx, x2, y2;
        const size = this.size,
            unmodified = this._unmodified;

        if (this.latRange) {
            const latRange = this.latRange;
            minY = this.latY(latRange[1]);
            maxY = this.latY(latRange[0]);
            sy = maxY - minY < size.y ? size.y / (maxY - minY) : 0;
        }

        if (this.lngRange) {
            const lngRange = this.lngRange;
            minX = this.lngX(lngRange[0]);
            maxX = this.lngX(lngRange[1]);
            sx = maxX - minX < size.x ? size.x / (maxX - minX) : 0;
        }

        // how much the map should scale to fit the screen into given latitude/longitude ranges
        const s = Math.max(sx || 0, sy || 0);

        if (s) {
            this.center = this.unproject(new Point(
                sx ? (maxX + minX) / 2 : this.x,
                sy ? (maxY + minY) / 2 : this.y));
            this.zoom += this.scaleZoom(s);
            this._unmodified = unmodified;
            this._constraining = false;
            return;
        }

        if (this.latRange) {
            const y = this.y,
                h2 = size.y / 2;

            if (y - h2 < minY) y2 = minY + h2;
            if (y + h2 > maxY) y2 = maxY - h2;
        }

        if (this.lngRange) {
            const x = this.x,
                w2 = size.x / 2;

            if (x - w2 < minX) x2 = minX + w2;
            if (x + w2 > maxX) x2 = maxX - w2;
        }

        // pan the map if the screen goes off the range
        if (x2 !== undefined || y2 !== undefined) {
            this.center = this.unproject(new Point(
                x2 !== undefined ? x2 : this.x,
                y2 !== undefined ? y2 : this.y));
        }

        this._unmodified = unmodified;
        this._constraining = false;
    }

    _calcMatrices() {
        if (!this.height) return;

        this.cameraToCenterDistance = 0.5 / Math.tan(this._fov / 2) * this.height;

        // Find the distance from the center point [width/2, height/2] to the
        // center top point [width/2, 0] in Z units, using the law of sines.
        // 1 Z unit is equivalent to 1 horizontal px at the center of the map
        // (the distance between[width/2, height/2] and [width/2 + 1, height/2])
        const halfFov = this._fov / 2;
        const groundAngle = Math.PI / 2 + this._pitch;
        const topHalfSurfaceDistance = Math.sin(halfFov) * this.cameraToCenterDistance / Math.sin(Math.PI - groundAngle - halfFov);
        const x = this.x, y = this.y;

        // Calculate z distance of the farthest fragment that should be rendered.
        const furthestDistance = Math.cos(Math.PI / 2 - this._pitch) * topHalfSurfaceDistance + this.cameraToCenterDistance;
        // Add a bit extra to avoid precision problems when a fragment's distance is exactly `furthestDistance`
        const farZ = furthestDistance * 1.01;

        // matrix for conversion from location to GL coordinates (-1 .. 1)
        let m = new Float64Array(16);
        mat4.perspective(m, this._fov, this.width / this.height, 1, farZ);

        mat4.scale(m, m, [1, -1, 1]);
        mat4.translate(m, m, [0, 0, -this.cameraToCenterDistance]);
        mat4.rotateX(m, m, this._pitch);
        mat4.rotateZ(m, m, this.angle);
        mat4.translate(m, m, [-x, -y, 0]);

        // scale vertically to meters per pixel (inverse of ground resolution):
        // worldSize / (circumferenceOfEarth * cos(lat * π / 180))
        const verticalScale = this.worldSize / (2 * Math.PI * 6378137 * Math.abs(Math.cos(this.center.lat * (Math.PI / 180))));
        mat4.scale(m, m, [1, 1, verticalScale, 1]);

        this.projMatrix = m;

        // Make a second projection matrix that is aligned to a pixel grid for rendering raster tiles.
        // We're rounding the (floating point) x/y values to achieve to avoid rendering raster images to fractional
        // coordinates. Additionally, we adjust by half a pixel in either direction in case that viewport dimension
        // is an odd integer to preserve rendering to the pixel grid. We're rotating this shift based on the angle
        // of the transformation so that 0°, 90°, 180°, and 270° rasters are crisp, and adjust the shift so that
        // it is always <= 0.5 pixels.
        const xShift = (this.width % 2) / 2, yShift = (this.height % 2) / 2,
            angleCos = Math.cos(this.angle), angleSin = Math.sin(this.angle),
            dx = x - Math.round(x) + angleCos * xShift + angleSin * yShift,
            dy = y - Math.round(y) + angleCos * yShift + angleSin * xShift;
        const alignedM = new Float64Array(m);
        mat4.translate(alignedM, alignedM, [ dx > 0.5 ? dx - 1 : dx, dy > 0.5 ? dy - 1 : dy, 0 ]);
        this.alignedProjMatrix = alignedM;

        // matrix for conversion from location to screen coordinates
        m = mat4.create();
        mat4.scale(m, m, [this.width / 2, -this.height / 2, 1]);
        mat4.translate(m, m, [1, -1, 0]);
        this.pixelMatrix = mat4.multiply(new Float64Array(16), m, this.projMatrix);

        // inverse matrix for conversion from screen coordinaes to location
        m = mat4.invert(new Float64Array(16), this.pixelMatrix);
        if (!m) throw new Error("failed to invert matrix");
        this.pixelMatrixInverse = m;

        this._posMatrixCache = {};
        this._alignedPosMatrixCache = {};
    }

    maxPitchScaleFactor() {
        // calcMatrices hasn't run yet
        if (!this.pixelMatrixInverse) return 1;

        const coord = this.pointCoordinate(new Point(0, 0)).zoomTo(this.zoom);
        const p = [coord.column * this.tileSize, coord.row * this.tileSize, 0, 1];
        const topPoint = vec4.transformMat4(p, p, this.pixelMatrix);
        return topPoint[3] / this.cameraToCenterDistance;
    }
}

export default Transform;
