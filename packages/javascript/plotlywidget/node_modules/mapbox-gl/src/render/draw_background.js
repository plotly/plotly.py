// @flow

import {
    isPatternMissing,
    setPatternUniforms,
    prepare as preparePattern
} from './pattern';

import StencilMode from '../gl/stencil_mode';
import DepthMode from '../gl/depth_mode';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type BackgroundStyleLayer from '../style/style_layer/background_style_layer';

export default drawBackground;

function drawBackground(painter: Painter, sourceCache: SourceCache, layer: BackgroundStyleLayer) {
    const color = layer.paint.get('background-color');
    const opacity = layer.paint.get('background-opacity');

    if (opacity === 0) return;

    const context = painter.context;
    const gl = context.gl;
    const transform = painter.transform;
    const tileSize = transform.tileSize;
    const image = layer.paint.get('background-pattern');

    const pass = (!image && color.a === 1 && opacity === 1) ? 'opaque' : 'translucent';
    if (painter.renderPass !== pass) return;

    context.setStencilMode(StencilMode.disabled);
    context.setDepthMode(painter.depthModeForSublayer(0, pass === 'opaque' ? DepthMode.ReadWrite : DepthMode.ReadOnly));
    context.setColorMode(painter.colorModeForRenderPass());

    let program;
    if (image) {
        if (isPatternMissing(image, painter)) return;
        program = painter.useProgram('backgroundPattern');
        preparePattern(image, painter, program);
        painter.tileExtentPatternVAO.bind(context, program, painter.tileExtentBuffer, []);
    } else {
        program = painter.useProgram('background');
        gl.uniform4fv(program.uniforms.u_color, [color.r, color.g, color.b, color.a]);
        painter.tileExtentVAO.bind(context, program, painter.tileExtentBuffer, []);
    }

    gl.uniform1f(program.uniforms.u_opacity, opacity);
    const tileIDs = transform.coveringTiles({tileSize});

    for (const tileID of tileIDs) {
        if (image) {
            setPatternUniforms({tileID, tileSize}, painter, program);
        }
        gl.uniformMatrix4fv(program.uniforms.u_matrix, false, painter.transform.calculatePosMatrix(tileID.toUnwrapped()));
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, painter.tileExtentBuffer.length);
    }
}
