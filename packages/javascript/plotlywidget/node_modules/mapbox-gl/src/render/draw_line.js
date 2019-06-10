// @flow

import browser from '../util/browser';

import pixelsToTileUnits from '../source/pixels_to_tile_units';
import DepthMode from '../gl/depth_mode';
import Texture from './texture';

import type Painter from './painter';
import type SourceCache from '../source/source_cache';
import type LineStyleLayer from '../style/style_layer/line_style_layer';
import type LineBucket from '../data/bucket/line_bucket';
import type {OverscaledTileID} from '../source/tile_id';

export default function drawLine(painter: Painter, sourceCache: SourceCache, layer: LineStyleLayer, coords: Array<OverscaledTileID>) {
    if (painter.renderPass !== 'translucent') return;

    const opacity = layer.paint.get('line-opacity');
    if (opacity.constantOr(1) === 0) return;

    const context = painter.context;

    context.setDepthMode(painter.depthModeForSublayer(0, DepthMode.ReadOnly));
    context.setColorMode(painter.colorModeForRenderPass());

    const programId =
        layer.paint.get('line-dasharray') ? 'lineSDF' :
        layer.paint.get('line-pattern') ? 'linePattern' :
        layer.paint.get('line-gradient') ? 'lineGradient' : 'line';

    let prevTileZoom;
    let firstTile = true;

    for (const coord of coords) {
        const tile = sourceCache.getTile(coord);
        const bucket: ?LineBucket = (tile.getBucket(layer): any);
        if (!bucket) continue;

        const programConfiguration = bucket.programConfigurations.get(layer.id);
        const prevProgram = painter.context.program.get();
        const program = painter.useProgram(programId, programConfiguration);
        const programChanged = firstTile || program.program !== prevProgram;
        const tileRatioChanged = prevTileZoom !== tile.tileID.overscaledZ;

        if (programChanged) {
            programConfiguration.setUniforms(painter.context, program, layer.paint, {zoom: painter.transform.zoom});
        }
        drawLineTile(program, painter, tile, bucket, layer, coord, programConfiguration, programChanged, tileRatioChanged);
        prevTileZoom = tile.tileID.overscaledZ;
        firstTile = false;
    }
}

function drawLineTile(program, painter, tile, bucket, layer, coord, programConfiguration, programChanged, tileRatioChanged) {
    const context = painter.context;
    const gl = context.gl;
    const dasharray = layer.paint.get('line-dasharray');
    const image = layer.paint.get('line-pattern');

    let posA, posB, imagePosA, imagePosB;

    if (programChanged || tileRatioChanged) {
        const tileRatio = 1 / pixelsToTileUnits(tile, 1, painter.transform.tileZoom);

        if (dasharray) {
            posA = painter.lineAtlas.getDash(dasharray.from, layer.layout.get('line-cap') === 'round');
            posB = painter.lineAtlas.getDash(dasharray.to, layer.layout.get('line-cap') === 'round');

            const widthA = posA.width * dasharray.fromScale;
            const widthB = posB.width * dasharray.toScale;

            gl.uniform2f(program.uniforms.u_patternscale_a, tileRatio / widthA, -posA.height / 2);
            gl.uniform2f(program.uniforms.u_patternscale_b, tileRatio / widthB, -posB.height / 2);
            gl.uniform1f(program.uniforms.u_sdfgamma, painter.lineAtlas.width / (Math.min(widthA, widthB) * 256 * browser.devicePixelRatio) / 2);

        } else if (image) {
            imagePosA = painter.imageManager.getPattern(image.from);
            imagePosB = painter.imageManager.getPattern(image.to);
            if (!imagePosA || !imagePosB) return;

            gl.uniform2f(program.uniforms.u_pattern_size_a, imagePosA.displaySize[0] * image.fromScale / tileRatio, imagePosA.displaySize[1]);
            gl.uniform2f(program.uniforms.u_pattern_size_b, imagePosB.displaySize[0] * image.toScale / tileRatio, imagePosB.displaySize[1]);

            const {width, height} = painter.imageManager.getPixelSize();
            gl.uniform2fv(program.uniforms.u_texsize, [width, height]);
        }

        gl.uniform2f(program.uniforms.u_gl_units_to_pixels, 1 / painter.transform.pixelsToGLUnits[0], 1 / painter.transform.pixelsToGLUnits[1]);
    }

    if (programChanged) {

        if (dasharray) {
            gl.uniform1i(program.uniforms.u_image, 0);
            context.activeTexture.set(gl.TEXTURE0);
            painter.lineAtlas.bind(context);

            gl.uniform1f(program.uniforms.u_tex_y_a, (posA: any).y);
            gl.uniform1f(program.uniforms.u_tex_y_b, (posB: any).y);
            gl.uniform1f(program.uniforms.u_mix, dasharray.t);

        } else if (image) {
            gl.uniform1i(program.uniforms.u_image, 0);
            context.activeTexture.set(gl.TEXTURE0);
            painter.imageManager.bind(context);

            gl.uniform2fv(program.uniforms.u_pattern_tl_a, (imagePosA: any).tl);
            gl.uniform2fv(program.uniforms.u_pattern_br_a, (imagePosA: any).br);
            gl.uniform2fv(program.uniforms.u_pattern_tl_b, (imagePosB: any).tl);
            gl.uniform2fv(program.uniforms.u_pattern_br_b, (imagePosB: any).br);
            gl.uniform1f(program.uniforms.u_fade, image.t);
        }
    }

    context.setStencilMode(painter.stencilModeForClipping(coord));

    const posMatrix = painter.translatePosMatrix(coord.posMatrix, tile, layer.paint.get('line-translate'), layer.paint.get('line-translate-anchor'));
    gl.uniformMatrix4fv(program.uniforms.u_matrix, false, posMatrix);

    gl.uniform1f(program.uniforms.u_ratio, 1 / pixelsToTileUnits(tile, 1, painter.transform.zoom));

    if (layer.paint.get('line-gradient')) {
        context.activeTexture.set(gl.TEXTURE0);

        let gradientTexture = layer.gradientTexture;
        if (!layer.gradient) return;
        if (!gradientTexture) gradientTexture = layer.gradientTexture = new Texture(context, layer.gradient, gl.RGBA);
        gradientTexture.bind(gl.LINEAR, gl.CLAMP_TO_EDGE);

        gl.uniform1i(program.uniforms.u_image, 0);
    }

    program.draw(
        context,
        gl.TRIANGLES,
        layer.id,
        bucket.layoutVertexBuffer,
        bucket.indexBuffer,
        bucket.segments,
        programConfiguration);
}
