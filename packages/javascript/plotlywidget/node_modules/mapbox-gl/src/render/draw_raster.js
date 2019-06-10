// @flow

import { clamp } from '../util/util';

import ImageSource from '../source/image_source';
import browser from '../util/browser';
import StencilMode from '../gl/stencil_mode';
import DepthMode from '../gl/depth_mode';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type RasterStyleLayer from '../style/style_layer/raster_style_layer';
import type {OverscaledTileID} from '../source/tile_id';

export default drawRaster;

function drawRaster(painter: Painter, sourceCache: SourceCache, layer: RasterStyleLayer, coords: Array<OverscaledTileID>) {
    if (painter.renderPass !== 'translucent') return;
    if (layer.paint.get('raster-opacity') === 0) return;

    const context = painter.context;
    const gl = context.gl;
    const source = sourceCache.getSource();
    const program = painter.useProgram('raster');

    context.setStencilMode(StencilMode.disabled);
    context.setColorMode(painter.colorModeForRenderPass());

    // Constant parameters.
    gl.uniform1f(program.uniforms.u_brightness_low, layer.paint.get('raster-brightness-min'));
    gl.uniform1f(program.uniforms.u_brightness_high, layer.paint.get('raster-brightness-max'));
    gl.uniform1f(program.uniforms.u_saturation_factor, saturationFactor(layer.paint.get('raster-saturation')));
    gl.uniform1f(program.uniforms.u_contrast_factor, contrastFactor(layer.paint.get('raster-contrast')));
    gl.uniform3fv(program.uniforms.u_spin_weights, spinWeights(layer.paint.get('raster-hue-rotate')));
    gl.uniform1f(program.uniforms.u_buffer_scale, 1);
    gl.uniform1i(program.uniforms.u_image0, 0);
    gl.uniform1i(program.uniforms.u_image1, 1);

    const minTileZ = coords.length && coords[0].overscaledZ;

    for (const coord of coords) {
        // Set the lower zoom level to sublayer 0, and higher zoom levels to higher sublayers
        // Use gl.LESS to prevent double drawing in areas where tiles overlap.
        context.setDepthMode(painter.depthModeForSublayer(coord.overscaledZ - minTileZ,
            layer.paint.get('raster-opacity') === 1 ? DepthMode.ReadWrite : DepthMode.ReadOnly, gl.LESS));

        const tile = sourceCache.getTile(coord);
        const posMatrix = painter.transform.calculatePosMatrix(coord.toUnwrapped(), true);

        tile.registerFadeDuration(layer.paint.get('raster-fade-duration'));

        gl.uniformMatrix4fv(program.uniforms.u_matrix, false, posMatrix);

        const parentTile = sourceCache.findLoadedParent(coord, 0, {}),
            fade = getFadeValues(tile, parentTile, sourceCache, layer, painter.transform);

        let parentScaleBy, parentTL;

        context.activeTexture.set(gl.TEXTURE0);
        tile.texture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE, gl.LINEAR_MIPMAP_NEAREST);

        context.activeTexture.set(gl.TEXTURE1);

        if (parentTile) {
            parentTile.texture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE, gl.LINEAR_MIPMAP_NEAREST);
            parentScaleBy = Math.pow(2, parentTile.tileID.overscaledZ - tile.tileID.overscaledZ);
            parentTL = [tile.tileID.canonical.x * parentScaleBy % 1, tile.tileID.canonical.y * parentScaleBy % 1];

        } else {
            tile.texture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE, gl.LINEAR_MIPMAP_NEAREST);
        }

        // cross-fade parameters
        gl.uniform2fv(program.uniforms.u_tl_parent, parentTL || [0, 0]);
        gl.uniform1f(program.uniforms.u_scale_parent, parentScaleBy || 1);
        gl.uniform1f(program.uniforms.u_fade_t, fade.mix);
        gl.uniform1f(program.uniforms.u_opacity, fade.opacity * layer.paint.get('raster-opacity'));


        if (source instanceof ImageSource) {
            const buffer = source.boundsBuffer;
            const vao = source.boundsVAO;
            vao.bind(context, program, buffer, []);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, buffer.length);
        } else if (tile.maskedBoundsBuffer && tile.maskedIndexBuffer && tile.segments) {
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
}

function spinWeights(angle) {
    angle *= Math.PI / 180;
    const s = Math.sin(angle);
    const c = Math.cos(angle);
    return [
        (2 * c + 1) / 3,
        (-Math.sqrt(3) * s - c + 1) / 3,
        (Math.sqrt(3) * s - c + 1) / 3
    ];
}

function contrastFactor(contrast) {
    return contrast > 0 ?
        1 / (1 - contrast) :
        1 + contrast;
}

function saturationFactor(saturation) {
    return saturation > 0 ?
        1 - 1 / (1.001 - saturation) :
        -saturation;
}

function getFadeValues(tile, parentTile, sourceCache, layer, transform) {
    const fadeDuration = layer.paint.get('raster-fade-duration');

    if (fadeDuration > 0) {
        const now = browser.now();
        const sinceTile = (now - tile.timeAdded) / fadeDuration;
        const sinceParent = parentTile ? (now - parentTile.timeAdded) / fadeDuration : -1;

        const source = sourceCache.getSource();
        const idealZ = transform.coveringZoomLevel({
            tileSize: source.tileSize,
            roundZoom: source.roundZoom
        });

        // if no parent or parent is older, fade in; if parent is younger, fade out
        const fadeIn = !parentTile || Math.abs(parentTile.tileID.overscaledZ - idealZ) > Math.abs(tile.tileID.overscaledZ - idealZ);

        const childOpacity = (fadeIn && tile.refreshedUponExpiration) ? 1 : clamp(fadeIn ? sinceTile : 1 - sinceParent, 0, 1);

        // we don't crossfade tiles that were just refreshed upon expiring:
        // once they're old enough to pass the crossfading threshold
        // (fadeDuration), unset the `refreshedUponExpiration` flag so we don't
        // incorrectly fail to crossfade them when zooming
        if (tile.refreshedUponExpiration && sinceTile >= 1) tile.refreshedUponExpiration = false;

        if (parentTile) {
            return {
                opacity: 1,
                mix: 1 - childOpacity
            };
        } else {
            return {
                opacity: childOpacity,
                mix: 0
            };
        }
    } else {
        return {
            opacity: 1,
            mix: 0
        };
    }
}
