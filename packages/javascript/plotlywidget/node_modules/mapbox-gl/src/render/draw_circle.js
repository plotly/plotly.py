// @flow

import pixelsToTileUnits from '../source/pixels_to_tile_units';

import StencilMode from '../gl/stencil_mode';
import DepthMode from '../gl/depth_mode';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type CircleStyleLayer from '../style/style_layer/circle_style_layer';
import type CircleBucket from '../data/bucket/circle_bucket';
import type {OverscaledTileID} from '../source/tile_id';

export default drawCircles;

function drawCircles(painter: Painter, sourceCache: SourceCache, layer: CircleStyleLayer, coords: Array<OverscaledTileID>) {
    if (painter.renderPass !== 'translucent') return;

    const opacity = layer.paint.get('circle-opacity');
    const strokeWidth = layer.paint.get('circle-stroke-width');
    const strokeOpacity = layer.paint.get('circle-stroke-opacity');

    if (opacity.constantOr(1) === 0 && (strokeWidth.constantOr(1) === 0 || strokeOpacity.constantOr(1) === 0)) {
        return;
    }

    const context = painter.context;
    const gl = context.gl;

    context.setDepthMode(painter.depthModeForSublayer(0, DepthMode.ReadOnly));
    // Allow circles to be drawn across boundaries, so that
    // large circles are not clipped to tiles
    context.setStencilMode(StencilMode.disabled);
    context.setColorMode(painter.colorModeForRenderPass());

    let first = true;
    for (let i = 0; i < coords.length; i++) {
        const coord = coords[i];

        const tile = sourceCache.getTile(coord);
        const bucket: ?CircleBucket<*> = (tile.getBucket(layer): any);
        if (!bucket) continue;

        const prevProgram = painter.context.program.get();
        const programConfiguration = bucket.programConfigurations.get(layer.id);
        const program = painter.useProgram('circle', programConfiguration);
        if (first || program.program !== prevProgram) {
            programConfiguration.setUniforms(context, program, layer.paint, {zoom: painter.transform.zoom});
            first = false;
        }

        gl.uniform1f(program.uniforms.u_camera_to_center_distance, painter.transform.cameraToCenterDistance);
        gl.uniform1i(program.uniforms.u_scale_with_map, layer.paint.get('circle-pitch-scale') === 'map' ? 1 : 0);
        if (layer.paint.get('circle-pitch-alignment') === 'map') {
            gl.uniform1i(program.uniforms.u_pitch_with_map, 1);
            const pixelRatio = pixelsToTileUnits(tile, 1, painter.transform.zoom);
            gl.uniform2f(program.uniforms.u_extrude_scale, pixelRatio, pixelRatio);
        } else {
            gl.uniform1i(program.uniforms.u_pitch_with_map, 0);
            gl.uniform2fv(program.uniforms.u_extrude_scale, painter.transform.pixelsToGLUnits);
        }

        gl.uniformMatrix4fv(program.uniforms.u_matrix, false, painter.translatePosMatrix(
            coord.posMatrix,
            tile,
            layer.paint.get('circle-translate'),
            layer.paint.get('circle-translate-anchor')
        ));

        program.draw(
            context,
            gl.TRIANGLES,
            layer.id,
            bucket.layoutVertexBuffer,
            bucket.indexBuffer,
            bucket.segments,
            programConfiguration);
    }
}
