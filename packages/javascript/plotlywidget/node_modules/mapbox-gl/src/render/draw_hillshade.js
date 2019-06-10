// @flow
import Coordinate from '../geo/coordinate';

import Texture from './texture';
import EXTENT from '../data/extent';
import { mat4 } from '@mapbox/gl-matrix';
import StencilMode from '../gl/stencil_mode';
import DepthMode from '../gl/depth_mode';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type HillshadeStyleLayer from '../style/style_layer/hillshade_style_layer';
import type {OverscaledTileID} from '../source/tile_id';

export default drawHillshade;

function drawHillshade(painter: Painter, sourceCache: SourceCache, layer: HillshadeStyleLayer, tileIDs: Array<OverscaledTileID>) {
    if (painter.renderPass !== 'offscreen' && painter.renderPass !== 'translucent') return;

    const context = painter.context;
    const sourceMaxZoom = sourceCache.getSource().maxzoom;

    context.setDepthMode(painter.depthModeForSublayer(0, DepthMode.ReadOnly));
    context.setStencilMode(StencilMode.disabled);
    context.setColorMode(painter.colorModeForRenderPass());

    for (const tileID of tileIDs) {
        const tile = sourceCache.getTile(tileID);
        if (tile.needsHillshadePrepare && painter.renderPass === 'offscreen') {
            prepareHillshade(painter, tile, sourceMaxZoom);
            continue;
        } else if (painter.renderPass === 'translucent') {
            renderHillshade(painter, tile, layer);
        }
    }

    context.viewport.set([0, 0, painter.width, painter.height]);
}

function setLight(program, painter, layer) {
    let azimuthal = layer.paint.get('hillshade-illumination-direction') * (Math.PI / 180);
    // modify azimuthal angle by map rotation if light is anchored at the viewport
    if (layer.paint.get('hillshade-illumination-anchor') === 'viewport')  azimuthal -= painter.transform.angle;
    painter.context.gl.uniform2f(program.uniforms.u_light, layer.paint.get('hillshade-exaggeration'), azimuthal);

}

function getTileLatRange(painter, tileID: OverscaledTileID) {
    const coordinate0 = tileID.toCoordinate();
    const coordinate1 = new Coordinate(coordinate0.column, coordinate0.row + 1, coordinate0.zoom);
    return [painter.transform.coordinateLocation(coordinate0).lat, painter.transform.coordinateLocation(coordinate1).lat];
}

function renderHillshade(painter, tile, layer) {
    const context = painter.context;
    const gl = context.gl;
    const fbo = tile.fbo;
    if (!fbo) return;

    const program = painter.useProgram('hillshade');
    const posMatrix = painter.transform.calculatePosMatrix(tile.tileID.toUnwrapped(), true);
    setLight(program, painter, layer);
    // for scaling the magnitude of a points slope by its latitude
    const latRange = getTileLatRange(painter, tile.tileID);
    context.activeTexture.set(gl.TEXTURE0);

    gl.bindTexture(gl.TEXTURE_2D, fbo.colorAttachment.get());

    gl.uniformMatrix4fv(program.uniforms.u_matrix, false, posMatrix);
    gl.uniform2fv(program.uniforms.u_latrange, latRange);
    gl.uniform1i(program.uniforms.u_image, 0);

    const shadowColor = layer.paint.get("hillshade-shadow-color");
    gl.uniform4f(program.uniforms.u_shadow, shadowColor.r, shadowColor.g, shadowColor.b, shadowColor.a);
    const highlightColor = layer.paint.get("hillshade-highlight-color");
    gl.uniform4f(program.uniforms.u_highlight, highlightColor.r, highlightColor.g, highlightColor.b, highlightColor.a);
    const accentColor = layer.paint.get("hillshade-accent-color");
    gl.uniform4f(program.uniforms.u_accent, accentColor.r, accentColor.g, accentColor.b, accentColor.a);

    if (tile.maskedBoundsBuffer && tile.maskedIndexBuffer && tile.segments) {
        program.draw(
            context,
            gl.TRIANGLES,
            layer.id,
            tile.maskedBoundsBuffer,
            tile.maskedIndexBuffer,
            tile.segments
        );
    } else {
        const buffer = painter.rasterBoundsBuffer;
        const vao = painter.rasterBoundsVAO;
        vao.bind(context, program, buffer, []);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, buffer.length);
    }
}


// hillshade rendering is done in two steps. the prepare step first calculates the slope of the terrain in the x and y
// directions for each pixel, and saves those values to a framebuffer texture in the r and g channels.
function prepareHillshade(painter, tile, sourceMaxZoom) {
    const context = painter.context;
    const gl = context.gl;
    // decode rgba levels by using integer overflow to convert each Uint32Array element -> 4 Uint8Array elements.
    // ex.
    // Uint32:
    // base 10 - 67308
    // base 2 - 0000 0000 0000 0001 0000 0110 1110 1100
    //
    // Uint8:
    // base 10 - 0, 1, 6, 236 (this order is reversed in the resulting array via the overflow.
    // first 8 bits represent 236, so the r component of the texture pixel will be 236 etc.)
    // base 2 - 0000 0000, 0000 0001, 0000 0110, 1110 1100
    if (tile.dem && tile.dem.level) {
        const tileSize = tile.dem.level.dim;

        const pixelData = tile.dem.getPixels();
        context.activeTexture.set(gl.TEXTURE1);

        // if UNPACK_PREMULTIPLY_ALPHA_WEBGL is set to true prior to drawHillshade being called
        // tiles will appear blank, because as you can see above the alpha value for these textures
        // is always 0
        context.pixelStoreUnpackPremultiplyAlpha.set(false);
        tile.demTexture = tile.demTexture || painter.getTileTexture(tile.tileSize);
        if (tile.demTexture) {
            const demTexture = tile.demTexture;
            demTexture.update(pixelData, { premultiply: false });
            demTexture.bind(gl.NEAREST, gl.CLAMP_TO_EDGE);
        } else {
            tile.demTexture = new Texture(context, pixelData, gl.RGBA, { premultiply: false });
            tile.demTexture.bind(gl.NEAREST, gl.CLAMP_TO_EDGE);
        }

        context.activeTexture.set(gl.TEXTURE0);

        let fbo = tile.fbo;

        if (!fbo) {
            const renderTexture = new Texture(context, {width: tileSize, height: tileSize, data: null}, gl.RGBA);
            renderTexture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE);

            fbo = tile.fbo = context.createFramebuffer(tileSize, tileSize);
            fbo.colorAttachment.set(renderTexture.texture);
        }

        context.bindFramebuffer.set(fbo.framebuffer);
        context.viewport.set([0, 0, tileSize, tileSize]);

        const matrix = mat4.create();
        // Flip rendering at y axis.
        mat4.ortho(matrix, 0, EXTENT, -EXTENT, 0, 0, 1);
        mat4.translate(matrix, matrix, [0, -EXTENT, 0]);

        const program = painter.useProgram('hillshadePrepare');

        gl.uniformMatrix4fv(program.uniforms.u_matrix, false, matrix);
        gl.uniform1f(program.uniforms.u_zoom, tile.tileID.overscaledZ);
        gl.uniform2fv(program.uniforms.u_dimension, [tileSize * 2, tileSize * 2]);
        gl.uniform1i(program.uniforms.u_image, 1);
        gl.uniform1f(program.uniforms.u_maxzoom, sourceMaxZoom);

        const buffer = painter.rasterBoundsBuffer;
        const vao = painter.rasterBoundsVAO;

        vao.bind(context, program, buffer, []);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, buffer.length);

        tile.needsHillshadePrepare = false;
    }
}
