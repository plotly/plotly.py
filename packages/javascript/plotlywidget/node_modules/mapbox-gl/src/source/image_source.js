// @flow

import { getCoordinatesCenter } from '../util/util';

import { CanonicalTileID } from './tile_id';
import LngLat from '../geo/lng_lat';
import Point from '@mapbox/point-geometry';
import { Event, ErrorEvent, Evented } from '../util/evented';
import { getImage, ResourceType } from '../util/ajax';
import browser from '../util/browser';
import EXTENT from '../data/extent';
import { RasterBoundsArray } from '../data/array_types';
import rasterBoundsAttributes from '../data/raster_bounds_attributes';
import VertexArrayObject from '../render/vertex_array_object';
import Texture from '../render/texture';

import type {Source} from './source';
import type {CanvasSourceSpecification} from './canvas_source';
import type Map from '../ui/map';
import type Dispatcher from '../util/dispatcher';
import type Tile from './tile';
import type Coordinate from '../geo/coordinate';
import type {Callback} from '../types/callback';
import type VertexBuffer from '../gl/vertex_buffer';

/**
 * A data source containing an image.
 * (See the [Style Specification](https://www.mapbox.com/mapbox-gl-style-spec/#sources-image) for detailed documentation of options.)
 *
 * @example
 * // add to map
 * map.addSource('some id', {
 *    type: 'image',
 *    url: 'https://www.mapbox.com/images/foo.png',
 *    coordinates: [
 *        [-76.54, 39.18],
 *        [-76.52, 39.18],
 *        [-76.52, 39.17],
 *        [-76.54, 39.17]
 *    ]
 * });
 *
 * // update
 * var mySource = map.getSource('some id');
 * mySource.setCoordinates([
 *     [-76.54335737228394, 39.18579907229748],
 *     [-76.52803659439087, 39.1838364847587],
 *     [-76.5295386314392, 39.17683392507606],
 *     [-76.54520273208618, 39.17876344106642]
 * ]);
 *
 * map.removeSource('some id');  // remove
 * @see [Add an image](https://www.mapbox.com/mapbox-gl-js/example/image-on-a-map/)
 */
class ImageSource extends Evented implements Source {
    type: string;
    id: string;
    minzoom: number;
    maxzoom: number;
    tileSize: number;
    url: string;

    coordinates: [[number, number], [number, number], [number, number], [number, number]];
    tiles: {[string]: Tile};
    options: any;
    dispatcher: Dispatcher;
    map: Map;
    texture: Texture;
    image: ImageData;
    centerCoord: Coordinate;
    tileID: CanonicalTileID;
    _boundsArray: RasterBoundsArray;
    boundsBuffer: VertexBuffer;
    boundsVAO: VertexArrayObject;

    /**
     * @private
     */
    constructor(id: string, options: ImageSourceSpecification | VideoSourceSpecification | CanvasSourceSpecification, dispatcher: Dispatcher, eventedParent: Evented) {
        super();
        this.id = id;
        this.dispatcher = dispatcher;
        this.coordinates = options.coordinates;

        this.type = 'image';
        this.minzoom = 0;
        this.maxzoom = 22;
        this.tileSize = 512;
        this.tiles = {};

        this.setEventedParent(eventedParent);

        this.options = options;
    }

    load() {
        this.fire(new Event('dataloading', {dataType: 'source'}));

        this.url = this.options.url;

        getImage(this.map._transformRequest(this.url, ResourceType.Image), (err, image) => {
            if (err) {
                this.fire(new ErrorEvent(err));
            } else if (image) {
                this.image = browser.getImageData(image);
                this._finishLoading();
            }
        });
    }

    _finishLoading() {
        if (this.map) {
            this.setCoordinates(this.coordinates);
            this.fire(new Event('data', {dataType: 'source', sourceDataType: 'metadata'}));
        }
    }

    onAdd(map: Map) {
        this.map = map;
        this.load();
    }

    /**
     * Sets the image's coordinates and re-renders the map.
     *
     * @param {Array<Array<number>>} coordinates Four geographical coordinates,
     *   represented as arrays of longitude and latitude numbers, which define the corners of the image.
     *   The coordinates start at the top left corner of the image and proceed in clockwise order.
     *   They do not have to represent a rectangle.
     * @returns {ImageSource} this
     */
    setCoordinates(coordinates: [[number, number], [number, number], [number, number], [number, number]]) {
        this.coordinates = coordinates;

        // Calculate which mercator tile is suitable for rendering the video in
        // and create a buffer with the corner coordinates. These coordinates
        // may be outside the tile, because raster tiles aren't clipped when rendering.

        const map = this.map;

        // transform the geo coordinates into (zoom 0) tile space coordinates
        const cornerZ0Coords = coordinates.map((coord) => {
            return map.transform.locationCoordinate(LngLat.convert(coord)).zoomTo(0);
        });

        // Compute the coordinates of the tile we'll use to hold this image's
        // render data
        const centerCoord = this.centerCoord = getCoordinatesCenter(cornerZ0Coords);
        // `column` and `row` may be fractional; round them down so that they
        // represent integer tile coordinates
        centerCoord.column = Math.floor(centerCoord.column);
        centerCoord.row = Math.floor(centerCoord.row);
        this.tileID = new CanonicalTileID(centerCoord.zoom, centerCoord.column, centerCoord.row);

        // Constrain min/max zoom to our tile's zoom level in order to force
        // SourceCache to request this tile (no matter what the map's zoom
        // level)
        this.minzoom = this.maxzoom = centerCoord.zoom;

        // Transform the corner coordinates into the coordinate space of our
        // tile.
        const tileCoords = cornerZ0Coords.map((coord) => {
            const zoomedCoord = coord.zoomTo(centerCoord.zoom);
            return new Point(
                Math.round((zoomedCoord.column - centerCoord.column) * EXTENT),
                Math.round((zoomedCoord.row - centerCoord.row) * EXTENT));
        });

        this._boundsArray = new RasterBoundsArray();
        this._boundsArray.emplaceBack(tileCoords[0].x, tileCoords[0].y, 0, 0);
        this._boundsArray.emplaceBack(tileCoords[1].x, tileCoords[1].y, EXTENT, 0);
        this._boundsArray.emplaceBack(tileCoords[3].x, tileCoords[3].y, 0, EXTENT);
        this._boundsArray.emplaceBack(tileCoords[2].x, tileCoords[2].y, EXTENT, EXTENT);

        if (this.boundsBuffer) {
            this.boundsBuffer.destroy();
            delete this.boundsBuffer;
        }

        this.fire(new Event('data', {dataType:'source', sourceDataType: 'content'}));
        return this;
    }

    prepare() {
        if (Object.keys(this.tiles).length === 0 || !this.image) {
            return;
        }

        const context = this.map.painter.context;
        const gl = context.gl;

        if (!this.boundsBuffer) {
            this.boundsBuffer = context.createVertexBuffer(this._boundsArray, rasterBoundsAttributes.members);
        }

        if (!this.boundsVAO) {
            this.boundsVAO = new VertexArrayObject();
        }

        if (!this.texture) {
            this.texture = new Texture(context, this.image, gl.RGBA);
            this.texture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE);
        }

        for (const w in this.tiles) {
            const tile = this.tiles[w];
            if (tile.state !== 'loaded') {
                tile.state = 'loaded';
                tile.texture = this.texture;
            }
        }
    }

    loadTile(tile: Tile, callback: Callback<void>) {
        // We have a single tile -- whoose coordinates are this.tileID -- that
        // covers the image we want to render.  If that's the one being
        // requested, set it up with the image; otherwise, mark the tile as
        // `errored` to indicate that we have no data for it.
        // If the world wraps, we may have multiple "wrapped" copies of the
        // single tile.
        if (this.tileID && this.tileID.equals(tile.tileID.canonical)) {
            this.tiles[String(tile.tileID.wrap)] = tile;
            tile.buckets = {};
            callback(null);
        } else {
            tile.state = 'errored';
            callback(null);
        }
    }

    serialize(): Object {
        return {
            type: 'image',
            url: this.options.url,
            coordinates: this.coordinates
        };
    }

    hasTransition() {
        return false;
    }
}

export default ImageSource;
