// @flow

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type StyleLayer from '../style/style_layer';
import type {OverscaledTileID} from '../source/tile_id';
import type SymbolBucket from '../data/bucket/symbol_bucket';
import pixelsToTileUnits from '../source/pixels_to_tile_units';
import DepthMode from '../gl/depth_mode';
import StencilMode from '../gl/stencil_mode';

export default drawCollisionDebug;

function drawCollisionDebugGeometry(painter: Painter, sourceCache: SourceCache, layer: StyleLayer, coords: Array<OverscaledTileID>, drawCircles: boolean) {
    const context = painter.context;
    const gl = context.gl;
    const program = drawCircles ? painter.useProgram('collisionCircle') : painter.useProgram('collisionBox');

    context.setDepthMode(DepthMode.disabled);
    context.setStencilMode(StencilMode.disabled);
    context.setColorMode(painter.colorModeForRenderPass());

    for (let i = 0; i < coords.length; i++) {
        const coord = coords[i];
        const tile = sourceCache.getTile(coord);
        const bucket: ?SymbolBucket = (tile.getBucket(layer): any);
        if (!bucket) continue;
        const buffers = drawCircles ? bucket.collisionCircle : bucket.collisionBox;
        if (!buffers) continue;


        gl.uniformMatrix4fv(program.uniforms.u_matrix, false, coord.posMatrix);

        if (!drawCircles) {
            context.lineWidth.set(1);
        }

        gl.uniform1f(program.uniforms.u_camera_to_center_distance, painter.transform.cameraToCenterDistance);
        const pixelRatio = pixelsToTileUnits(tile, 1, painter.transform.zoom);
        const scale = Math.pow(2, painter.transform.zoom - tile.tileID.overscaledZ);
        gl.uniform1f(program.uniforms.u_pixels_to_tile_units, pixelRatio);
        gl.uniform2f(program.uniforms.u_extrude_scale,
            painter.transform.pixelsToGLUnits[0] / (pixelRatio * scale),
            painter.transform.pixelsToGLUnits[1] / (pixelRatio * scale));
        gl.uniform1f(program.uniforms.u_overscale_factor, tile.tileID.overscaleFactor());

        program.draw(
            context,
            drawCircles ? gl.TRIANGLES : gl.LINES,
            layer.id,
            buffers.layoutVertexBuffer,
            buffers.indexBuffer,
            buffers.segments,
            null,
            buffers.collisionVertexBuffer,
            null);
    }
}

function drawCollisionDebug(painter: Painter, sourceCache: SourceCache, layer: StyleLayer, coords: Array<OverscaledTileID>) {
    drawCollisionDebugGeometry(painter, sourceCache, layer, coords, false);
    drawCollisionDebugGeometry(painter, sourceCache, layer, coords, true);
}
