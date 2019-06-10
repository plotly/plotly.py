// @flow

import {
    isPatternMissing,
    setPatternUniforms,
    prepare as preparePattern
} from './pattern';

import Color from '../style-spec/util/color';
import DepthMode from '../gl/depth_mode';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type FillStyleLayer from '../style/style_layer/fill_style_layer';
import type FillBucket from '../data/bucket/fill_bucket';
import type {OverscaledTileID} from '../source/tile_id';
import type {CrossFaded} from '../style/cross_faded';

export default drawFill;

function drawFill(painter: Painter, sourceCache: SourceCache, layer: FillStyleLayer, coords: Array<OverscaledTileID>) {
    const color = layer.paint.get('fill-color');
    const opacity = layer.paint.get('fill-opacity');

    if (opacity.constantOr(1) === 0) {
        return;
    }

    const context = painter.context;
    context.setColorMode(painter.colorModeForRenderPass());

    const pass = (!layer.paint.get('fill-pattern') &&
        color.constantOr(Color.transparent).a === 1 &&
        opacity.constantOr(0) === 1) ? 'opaque' : 'translucent';

    // Draw fill
    if (painter.renderPass === pass) {
        // Once we switch to earcut drawing we can pull most of the WebGL setup
        // outside of this coords loop.
        context.setDepthMode(painter.depthModeForSublayer(1, painter.renderPass === 'opaque' ? DepthMode.ReadWrite : DepthMode.ReadOnly));
        drawFillTiles(painter, sourceCache, layer, coords, drawFillTile);
    }

    // Draw stroke
    if (painter.renderPass === 'translucent' && layer.paint.get('fill-antialias')) {
        context.lineWidth.set(2);

        // If we defined a different color for the fill outline, we are
        // going to ignore the bits in 0x07 and just care about the global
        // clipping mask.
        // Otherwise, we only want to drawFill the antialiased parts that are
        // *outside* the current shape. This is important in case the fill
        // or stroke color is translucent. If we wouldn't clip to outside
        // the current shape, some pixels from the outline stroke overlapped
        // the (non-antialiased) fill.
        context.setDepthMode(painter.depthModeForSublayer(
            layer.getPaintProperty('fill-outline-color') ? 2 : 0, DepthMode.ReadOnly));
        drawFillTiles(painter, sourceCache, layer, coords, drawStrokeTile);
    }
}

function drawFillTiles(painter, sourceCache, layer, coords, drawFn) {
    if (isPatternMissing(layer.paint.get('fill-pattern'), painter)) return;

    let firstTile = true;
    for (const coord of coords) {
        const tile = sourceCache.getTile(coord);
        const bucket: ?FillBucket = (tile.getBucket(layer): any);
        if (!bucket) continue;

        painter.context.setStencilMode(painter.stencilModeForClipping(coord));
        drawFn(painter, sourceCache, layer, tile, coord, bucket, firstTile);
        firstTile = false;
    }
}

function drawFillTile(painter, sourceCache, layer, tile, coord, bucket, firstTile) {
    const gl = painter.context.gl;
    const programConfiguration = bucket.programConfigurations.get(layer.id);

    const program = setFillProgram('fill', layer.paint.get('fill-pattern'), painter, programConfiguration, layer, tile, coord, firstTile);

    program.draw(
        painter.context,
        gl.TRIANGLES,
        layer.id,
        bucket.layoutVertexBuffer,
        bucket.indexBuffer,
        bucket.segments,
        programConfiguration);
}

function drawStrokeTile(painter, sourceCache, layer, tile, coord, bucket, firstTile) {
    const gl = painter.context.gl;
    const programConfiguration = bucket.programConfigurations.get(layer.id);
    const pattern = layer.getPaintProperty('fill-outline-color') ? null : layer.paint.get('fill-pattern');

    const program = setFillProgram('fillOutline', pattern, painter, programConfiguration, layer, tile, coord, firstTile);
    gl.uniform2f(program.uniforms.u_world, gl.drawingBufferWidth, gl.drawingBufferHeight);

    program.draw(
        painter.context,
        gl.LINES,
        layer.id,
        bucket.layoutVertexBuffer,
        bucket.indexBuffer2,
        bucket.segments2,
        programConfiguration);
}

function setFillProgram(programId, pat: ?CrossFaded<string>, painter, programConfiguration, layer, tile, coord, firstTile) {
    let program;
    const prevProgram = painter.context.program.get();
    if (!pat) {
        program = painter.useProgram(programId, programConfiguration);
        if (firstTile || program.program !== prevProgram) {
            programConfiguration.setUniforms(painter.context, program, layer.paint, {zoom: painter.transform.zoom});
        }
    } else {
        program = painter.useProgram(`${programId}Pattern`, programConfiguration);
        if (firstTile || program.program !== prevProgram) {
            programConfiguration.setUniforms(painter.context, program, layer.paint, {zoom: painter.transform.zoom});
            preparePattern(pat, painter, program);
        }
        setPatternUniforms(tile, painter, program);
    }
    painter.context.gl.uniformMatrix4fv(program.uniforms.u_matrix, false, painter.translatePosMatrix(
        coord.posMatrix, tile,
        layer.paint.get('fill-translate'),
        layer.paint.get('fill-translate-anchor')
    ));
    return program;
}
