// @flow

import glMatrix from '@mapbox/gl-matrix';

import {
    isPatternMissing,
    setPatternUniforms,
    prepare as preparePattern
} from './pattern';
import Texture from './texture';
import Color from '../style-spec/util/color';
import DepthMode from '../gl/depth_mode';
const mat3 = glMatrix.mat3;
const mat4 = glMatrix.mat4;
const vec3 = glMatrix.vec3;
import StencilMode from '../gl/stencil_mode';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type FillExtrusionStyleLayer from '../style/style_layer/fill_extrusion_style_layer';
import type FillExtrusionBucket from '../data/bucket/fill_extrusion_bucket';
import type {OverscaledTileID} from '../source/tile_id';

export default draw;

function draw(painter: Painter, source: SourceCache, layer: FillExtrusionStyleLayer, coords: Array<OverscaledTileID>) {
    if (layer.paint.get('fill-extrusion-opacity') === 0) {
        return;
    }

    if (painter.renderPass === 'offscreen') {
        drawToExtrusionFramebuffer(painter, layer);

        let first = true;
        for (const coord of coords) {
            const tile = source.getTile(coord);
            const bucket: ?FillExtrusionBucket = (tile.getBucket(layer): any);
            if (!bucket) continue;

            drawExtrusion(painter, source, layer, tile, coord, bucket, first);
            first = false;
        }
    } else if (painter.renderPass === 'translucent') {
        drawExtrusionTexture(painter, layer);
    }
}

function drawToExtrusionFramebuffer(painter, layer) {
    const context = painter.context;
    const gl = context.gl;

    let renderTarget = layer.viewportFrame;

    if (painter.depthRboNeedsClear) {
        painter.setupOffscreenDepthRenderbuffer();
    }

    if (!renderTarget) {
        const texture = new Texture(context, {width: painter.width, height: painter.height, data: null}, gl.RGBA);
        texture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE);

        renderTarget = layer.viewportFrame = context.createFramebuffer(painter.width, painter.height);
        renderTarget.colorAttachment.set(texture.texture);
    }

    context.bindFramebuffer.set(renderTarget.framebuffer);
    renderTarget.depthAttachment.set(painter.depthRbo);

    if (painter.depthRboNeedsClear) {
        context.clear({ depth: 1 });
        painter.depthRboNeedsClear = false;
    }

    context.clear({ color: Color.transparent });

    context.setStencilMode(StencilMode.disabled);
    context.setDepthMode(new DepthMode(gl.LEQUAL, DepthMode.ReadWrite, [0, 1]));
    context.setColorMode(painter.colorModeForRenderPass());
}

function drawExtrusionTexture(painter, layer) {
    const renderedTexture = layer.viewportFrame;
    if (!renderedTexture) return;

    const context = painter.context;
    const gl = context.gl;
    const program = painter.useProgram('extrusionTexture');

    context.setStencilMode(StencilMode.disabled);
    context.setDepthMode(DepthMode.disabled);
    context.setColorMode(painter.colorModeForRenderPass());

    context.activeTexture.set(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, renderedTexture.colorAttachment.get());

    gl.uniform1f(program.uniforms.u_opacity, layer.paint.get('fill-extrusion-opacity'));
    gl.uniform1i(program.uniforms.u_image, 0);

    const matrix = mat4.create();
    mat4.ortho(matrix, 0, painter.width, painter.height, 0, 0, 1);
    gl.uniformMatrix4fv(program.uniforms.u_matrix, false, matrix);

    gl.uniform2f(program.uniforms.u_world, gl.drawingBufferWidth, gl.drawingBufferHeight);

    painter.viewportVAO.bind(context, program, painter.viewportBuffer, []);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
}

function drawExtrusion(painter, source, layer, tile, coord, bucket, first) {
    const context = painter.context;
    const gl = context.gl;

    const image = layer.paint.get('fill-extrusion-pattern');

    const prevProgram = painter.context.program.get();
    const programConfiguration = bucket.programConfigurations.get(layer.id);
    const program = painter.useProgram(image ? 'fillExtrusionPattern' : 'fillExtrusion', programConfiguration);
    if (first || program.program !== prevProgram) {
        programConfiguration.setUniforms(context, program, layer.paint, {zoom: painter.transform.zoom});
    }

    if (image) {
        if (isPatternMissing(image, painter)) return;
        preparePattern(image, painter, program);
        setPatternUniforms(tile, painter, program);
        gl.uniform1f(program.uniforms.u_height_factor, -Math.pow(2, coord.overscaledZ) / tile.tileSize / 8);
    }

    painter.context.gl.uniformMatrix4fv(program.uniforms.u_matrix, false, painter.translatePosMatrix(
        coord.posMatrix,
        tile,
        layer.paint.get('fill-extrusion-translate'),
        layer.paint.get('fill-extrusion-translate-anchor')
    ));

    setLight(program, painter);

    program.draw(
        context,
        gl.TRIANGLES,
        layer.id,
        bucket.layoutVertexBuffer,
        bucket.indexBuffer,
        bucket.segments,
        programConfiguration);
}

function setLight(program, painter) {
    const gl = painter.context.gl;
    const light = painter.style.light;

    const _lp = light.properties.get('position');
    const lightPos = [_lp.x, _lp.y, _lp.z];

    const lightMat = mat3.create();
    if (light.properties.get('anchor') === 'viewport') {
        mat3.fromRotation(lightMat, -painter.transform.angle);
    }
    vec3.transformMat3(lightPos, lightPos, lightMat);

    const color = light.properties.get('color');

    gl.uniform3fv(program.uniforms.u_lightpos, lightPos);
    gl.uniform1f(program.uniforms.u_lightintensity, light.properties.get('intensity'));
    gl.uniform3f(program.uniforms.u_lightcolor, color.r, color.g, color.b);
}
