// @flow

import browser from '../util/browser';

import { mat4 } from '@mapbox/gl-matrix';
import SourceCache from '../source/source_cache';
import EXTENT from '../data/extent';
import pixelsToTileUnits from '../source/pixels_to_tile_units';
import { filterObject } from '../util/util';
import VertexArrayObject from './vertex_array_object';
import { RasterBoundsArray, PosArray } from '../data/array_types';
import rasterBoundsAttributes from '../data/raster_bounds_attributes';
import posAttributes from '../data/pos_attributes';
import ProgramConfiguration from '../data/program_configuration';
import CrossTileSymbolIndex from '../symbol/cross_tile_symbol_index';
import shaders from '../shaders';
import Program from './program';
import Context from '../gl/context';
import DepthMode from '../gl/depth_mode';
import StencilMode from '../gl/stencil_mode';
import ColorMode from '../gl/color_mode';
import Texture from './texture';
import updateTileMasks from './tile_mask';
import Color from '../style-spec/util/color';
import symbol from './draw_symbol';
import circle from './draw_circle';
import heatmap from './draw_heatmap';
import line from './draw_line';
import fill from './draw_fill';
import fillExtrusion from './draw_fill_extrusion';
import hillshade from './draw_hillshade';
import raster from './draw_raster';
import background from './draw_background';
import debug from './draw_debug';

const draw = {
    symbol,
    circle,
    heatmap,
    line,
    fill,
    'fill-extrusion': fillExtrusion,
    hillshade,
    raster,
    background,
    debug
};

import type Transform from '../geo/transform';
import type Tile from '../source/tile';
import type {OverscaledTileID} from '../source/tile_id';
import type Style from '../style/style';
import type StyleLayer from '../style/style_layer';
import type LineAtlas from './line_atlas';
import type ImageManager from './image_manager';
import type GlyphManager from './glyph_manager';
import type VertexBuffer from '../gl/vertex_buffer';
import type {DepthMaskType, DepthFuncType} from '../gl/types';

export type RenderPass = 'offscreen' | 'opaque' | 'translucent';

type PainterOptions = {
    showOverdrawInspector: boolean,
    showTileBoundaries: boolean,
    rotating: boolean,
    zooming: boolean,
    fadeDuration: number
}

/**
 * Initialize a new painter object.
 *
 * @param {Canvas} gl an experimental-webgl drawing context
 * @private
 */
class Painter {
    context: Context;
    transform: Transform;
    _tileTextures: { [number]: Array<Texture> };
    numSublayers: number;
    depthEpsilon: number;
    emptyProgramConfiguration: ProgramConfiguration;
    width: number;
    height: number;
    depthRbo: WebGLRenderbuffer;
    depthRboNeedsClear: boolean;
    tileExtentBuffer: VertexBuffer;
    tileExtentVAO: VertexArrayObject;
    tileExtentPatternVAO: VertexArrayObject;
    debugBuffer: VertexBuffer;
    debugVAO: VertexArrayObject;
    rasterBoundsBuffer: VertexBuffer;
    rasterBoundsVAO: VertexArrayObject;
    viewportBuffer: VertexBuffer;
    viewportVAO: VertexArrayObject;
    _tileClippingMaskIDs: { [number]: number };
    style: Style;
    options: PainterOptions;
    lineAtlas: LineAtlas;
    imageManager: ImageManager;
    glyphManager: GlyphManager;
    depthRange: number;
    renderPass: RenderPass;
    currentLayer: number;
    id: string;
    _showOverdrawInspector: boolean;
    cache: { [string]: Program };
    crossTileSymbolIndex: CrossTileSymbolIndex;
    symbolFadeChange: number;

    constructor(gl: WebGLRenderingContext, transform: Transform) {
        this.context = new Context(gl);
        this.transform = transform;
        this._tileTextures = {};

        this.setup();

        // Within each layer there are multiple distinct z-planes that can be drawn to.
        // This is implemented using the WebGL depth buffer.
        this.numSublayers = SourceCache.maxUnderzooming + SourceCache.maxOverzooming + 1;
        this.depthEpsilon = 1 / Math.pow(2, 16);

        this.depthRboNeedsClear = true;

        this.emptyProgramConfiguration = new ProgramConfiguration();

        this.crossTileSymbolIndex = new CrossTileSymbolIndex();
    }

    /*
     * Update the GL viewport, projection matrix, and transforms to compensate
     * for a new width and height value.
     */
    resize(width: number, height: number) {
        const gl = this.context.gl;

        this.width = width * browser.devicePixelRatio;
        this.height = height * browser.devicePixelRatio;
        this.context.viewport.set([0, 0, this.width, this.height]);

        if (this.style) {
            for (const layerId of this.style._order) {
                this.style._layers[layerId].resize();
            }
        }

        if (this.depthRbo) {
            gl.deleteRenderbuffer(this.depthRbo);
            this.depthRbo = null;
        }
    }

    setup() {
        const context = this.context;

        const tileExtentArray = new PosArray();
        tileExtentArray.emplaceBack(0, 0);
        tileExtentArray.emplaceBack(EXTENT, 0);
        tileExtentArray.emplaceBack(0, EXTENT);
        tileExtentArray.emplaceBack(EXTENT, EXTENT);
        this.tileExtentBuffer = context.createVertexBuffer(tileExtentArray, posAttributes.members);
        this.tileExtentVAO = new VertexArrayObject();
        this.tileExtentPatternVAO = new VertexArrayObject();

        const debugArray = new PosArray();
        debugArray.emplaceBack(0, 0);
        debugArray.emplaceBack(EXTENT, 0);
        debugArray.emplaceBack(EXTENT, EXTENT);
        debugArray.emplaceBack(0, EXTENT);
        debugArray.emplaceBack(0, 0);
        this.debugBuffer = context.createVertexBuffer(debugArray, posAttributes.members);
        this.debugVAO = new VertexArrayObject();

        const rasterBoundsArray = new RasterBoundsArray();
        rasterBoundsArray.emplaceBack(0, 0, 0, 0);
        rasterBoundsArray.emplaceBack(EXTENT, 0, EXTENT, 0);
        rasterBoundsArray.emplaceBack(0, EXTENT, 0, EXTENT);
        rasterBoundsArray.emplaceBack(EXTENT, EXTENT, EXTENT, EXTENT);
        this.rasterBoundsBuffer = context.createVertexBuffer(rasterBoundsArray, rasterBoundsAttributes.members);
        this.rasterBoundsVAO = new VertexArrayObject();

        const viewportArray = new PosArray();
        viewportArray.emplaceBack(0, 0);
        viewportArray.emplaceBack(1, 0);
        viewportArray.emplaceBack(0, 1);
        viewportArray.emplaceBack(1, 1);
        this.viewportBuffer = context.createVertexBuffer(viewportArray, posAttributes.members);
        this.viewportVAO = new VertexArrayObject();
    }

    /*
     * Reset the drawing canvas by clearing the stencil buffer so that we can draw
     * new tiles at the same location, while retaining previously drawn pixels.
     */
    clearStencil() {
        const context = this.context;
        const gl = context.gl;

        // As a temporary workaround for https://github.com/mapbox/mapbox-gl-js/issues/5490,
        // pending an upstream fix, we draw a fullscreen stencil=0 clipping mask here,
        // effectively clearing the stencil buffer: once an upstream patch lands, remove
        // this function in favor of context.clear({ stencil: 0x0 })

        context.setColorMode(ColorMode.disabled);
        context.setDepthMode(DepthMode.disabled);
        context.setStencilMode(new StencilMode({ func: gl.ALWAYS, mask: 0 }, 0x0, 0xFF, gl.ZERO, gl.ZERO, gl.ZERO));

        const matrix = mat4.create();
        mat4.ortho(matrix, 0, this.width, this.height, 0, 0, 1);
        mat4.scale(matrix, matrix, [gl.drawingBufferWidth, gl.drawingBufferHeight, 0]);

        const program = this.useProgram('clippingMask');
        gl.uniformMatrix4fv(program.uniforms.u_matrix, false, matrix);

        this.viewportVAO.bind(context, program, this.viewportBuffer, []);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    }

    _renderTileClippingMasks(tileIDs: Array<OverscaledTileID>) {
        const context = this.context;
        const gl = context.gl;

        context.setColorMode(ColorMode.disabled);
        context.setDepthMode(DepthMode.disabled);

        let idNext = 1;
        this._tileClippingMaskIDs = {};

        for (const tileID of tileIDs) {
            const id = this._tileClippingMaskIDs[tileID.key] = idNext++;

            // Tests will always pass, and ref value will be written to stencil buffer.
            context.setStencilMode(new StencilMode({ func: gl.ALWAYS, mask: 0 }, id, 0xFF, gl.KEEP, gl.KEEP, gl.REPLACE));

            const program = this.useProgram('clippingMask');
            gl.uniformMatrix4fv(program.uniforms.u_matrix, false, tileID.posMatrix);

            // Draw the clipping mask
            this.tileExtentVAO.bind(this.context, program, this.tileExtentBuffer, []);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, this.tileExtentBuffer.length);
        }
    }

    stencilModeForClipping(tileID: OverscaledTileID): StencilMode {
        const gl = this.context.gl;
        return new StencilMode({ func: gl.EQUAL, mask: 0xFF }, this._tileClippingMaskIDs[tileID.key], 0x00, gl.KEEP, gl.KEEP, gl.REPLACE);
    }

    colorModeForRenderPass(): $ReadOnly<ColorMode> {
        const gl = this.context.gl;
        if (this._showOverdrawInspector) {
            const numOverdrawSteps = 8;
            const a = 1 / numOverdrawSteps;

            return new ColorMode([gl.CONSTANT_COLOR, gl.ONE], new Color(a, a, a, 0), [true, true, true, true]);
        } else if (this.renderPass === 'opaque') {
            return ColorMode.unblended;
        } else {
            return ColorMode.alphaBlended;
        }
    }

    depthModeForSublayer(n: number, mask: DepthMaskType, func: ?DepthFuncType): DepthMode {
        const farDepth = 1 - ((1 + this.currentLayer) * this.numSublayers + n) * this.depthEpsilon;
        const nearDepth = farDepth - 1 + this.depthRange;
        return new DepthMode(func || this.context.gl.LEQUAL, mask, [nearDepth, farDepth]);
    }

    render(style: Style, options: PainterOptions) {
        this.style = style;
        this.options = options;

        this.lineAtlas = style.lineAtlas;
        this.imageManager = style.imageManager;
        this.glyphManager = style.glyphManager;

        this.symbolFadeChange = style.placement.symbolFadeChange(browser.now());

        for (const id in style.sourceCaches) {
            const sourceCache = this.style.sourceCaches[id];
            if (sourceCache.used) {
                sourceCache.prepare(this.context);
            }
        }

        const layerIds = this.style._order;

        const rasterSources = filterObject(
            this.style.sourceCaches,
            (sc) => { return sc.getSource().type === 'raster' || sc.getSource().type === 'raster-dem'; }
        );
        for (const key in rasterSources) {
            const sourceCache = rasterSources[key];
            const coords = sourceCache.getVisibleCoordinates();
            const visibleTiles = coords.map((c)=>{ return sourceCache.getTile(c); });
            updateTileMasks(visibleTiles, this.context);
        }

        // Offscreen pass
        // We first do all rendering that requires rendering to a separate
        // framebuffer, and then save those for rendering back to the map
        // later: in doing this we avoid doing expensive framebuffer restores.
        this.renderPass = 'offscreen';
        {
            let sourceCache;
            let coords = [];
            this.depthRboNeedsClear = true;

            for (let i = 0; i < layerIds.length; i++) {
                const layer = this.style._layers[layerIds[i]];

                if (!layer.hasOffscreenPass() || layer.isHidden(this.transform.zoom)) continue;

                if (layer.source !== (sourceCache && sourceCache.id)) {
                    sourceCache = this.style.sourceCaches[layer.source];
                    coords = [];

                    if (sourceCache) {
                        coords = sourceCache.getVisibleCoordinates();
                        coords.reverse();
                    }
                }

                if (!coords.length) continue;

                this.renderLayer(this, (sourceCache: any), layer, coords);
            }

            // Rebind the main framebuffer now that all offscreen layers
            // have been rendered:
            this.context.bindFramebuffer.set(null);
        }

        // Clear buffers in preparation for drawing to the main framebuffer
        this.context.clear({ color: options.showOverdrawInspector ? Color.black : Color.transparent, depth: 1 });

        this._showOverdrawInspector = options.showOverdrawInspector;

        this.depthRange = (style._order.length + 2) * this.numSublayers * this.depthEpsilon;

        // Opaque pass
        // Draw opaque layers top-to-bottom first.
        this.renderPass = 'opaque';
        {
            let sourceCache;
            let coords = [];

            this.currentLayer = layerIds.length - 1;

            for (this.currentLayer; this.currentLayer >= 0; this.currentLayer--) {
                const layer = this.style._layers[layerIds[this.currentLayer]];

                if (layer.source !== (sourceCache && sourceCache.id)) {
                    sourceCache = this.style.sourceCaches[layer.source];
                    coords = [];

                    if (sourceCache) {
                        this.clearStencil();
                        coords = sourceCache.getVisibleCoordinates();
                        if (sourceCache.getSource().isTileClipped) {
                            this._renderTileClippingMasks(coords);
                        }
                    }
                }

                this.renderLayer(this, (sourceCache: any), layer, coords);
            }
        }

        // Translucent pass
        // Draw all other layers bottom-to-top.
        this.renderPass = 'translucent';
        {
            let sourceCache;
            let coords = [];

            this.currentLayer = 0;

            for (this.currentLayer; this.currentLayer < layerIds.length; this.currentLayer++) {
                const layer = this.style._layers[layerIds[this.currentLayer]];

                if (layer.source !== (sourceCache && sourceCache.id)) {
                    sourceCache = this.style.sourceCaches[layer.source];
                    coords = [];

                    if (sourceCache) {
                        this.clearStencil();
                        coords = sourceCache.getVisibleCoordinates();
                        if (sourceCache.getSource().isTileClipped) {
                            this._renderTileClippingMasks(coords);
                        }
                    }

                    coords.reverse();
                }

                this.renderLayer(this, (sourceCache: any), layer, coords);
            }
        }

        if (this.options.showTileBoundaries) {
            const sourceCache = this.style.sourceCaches[Object.keys(this.style.sourceCaches)[0]];
            if (sourceCache) {
                draw.debug(this, sourceCache, sourceCache.getVisibleCoordinates());
            }
        }
    }

    setupOffscreenDepthRenderbuffer(): void {
        const context = this.context;
        // All of the 3D textures will use the same depth renderbuffer.
        if (!this.depthRbo) {
            this.depthRbo = context.createRenderbuffer(context.gl.DEPTH_COMPONENT16, this.width, this.height);
        }
    }

    renderLayer(painter: Painter, sourceCache: SourceCache, layer: StyleLayer, coords: Array<OverscaledTileID>) {
        if (layer.isHidden(this.transform.zoom)) return;
        if (layer.type !== 'background' && !coords.length) return;
        this.id = layer.id;

        draw[layer.type](painter, sourceCache, layer, coords);
    }

    /**
     * Transform a matrix to incorporate the *-translate and *-translate-anchor properties into it.
     * @param inViewportPixelUnitsUnits True when the units accepted by the matrix are in viewport pixels instead of tile units.
     * @returns {Float32Array} matrix
     */
    translatePosMatrix(matrix: Float32Array, tile: Tile, translate: [number, number], translateAnchor: 'map' | 'viewport', inViewportPixelUnitsUnits?: boolean) {
        if (!translate[0] && !translate[1]) return matrix;

        const angle = inViewportPixelUnitsUnits ?
            (translateAnchor === 'map' ? this.transform.angle : 0) :
            (translateAnchor === 'viewport' ? -this.transform.angle : 0);

        if (angle) {
            const sinA = Math.sin(angle);
            const cosA = Math.cos(angle);
            translate = [
                translate[0] * cosA - translate[1] * sinA,
                translate[0] * sinA + translate[1] * cosA
            ];
        }

        const translation = [
            inViewportPixelUnitsUnits ? translate[0] : pixelsToTileUnits(tile, translate[0], this.transform.zoom),
            inViewportPixelUnitsUnits ? translate[1] : pixelsToTileUnits(tile, translate[1], this.transform.zoom),
            0
        ];

        const translatedMatrix = new Float32Array(16);
        mat4.translate(translatedMatrix, matrix, translation);
        return translatedMatrix;
    }

    saveTileTexture(texture: Texture) {
        const textures = this._tileTextures[texture.size[0]];
        if (!textures) {
            this._tileTextures[texture.size[0]] = [texture];
        } else {
            textures.push(texture);
        }
    }

    getTileTexture(size: number) {
        const textures = this._tileTextures[size];
        return textures && textures.length > 0 ? textures.pop() : null;
    }

    _createProgramCached(name: string, programConfiguration: ProgramConfiguration): Program {
        this.cache = this.cache || {};
        const key = `${name}${programConfiguration.cacheKey || ''}${this._showOverdrawInspector ? '/overdraw' : ''}`;
        if (!this.cache[key]) {
            this.cache[key] = new Program(this.context, shaders[name], programConfiguration, this._showOverdrawInspector);
        }
        return this.cache[key];
    }

    useProgram(name: string, programConfiguration?: ProgramConfiguration): Program {
        const nextProgram = this._createProgramCached(name, programConfiguration || this.emptyProgramConfiguration);

        this.context.program.set(nextProgram.program);

        return nextProgram;
    }
}

export default Painter;
