// @flow
import IndexBuffer from './index_buffer';

import VertexBuffer from './vertex_buffer';
import Framebuffer from './framebuffer';
import DepthMode from './depth_mode';
import StencilMode from './stencil_mode';
import ColorMode from './color_mode';
import { deepEqual } from '../util/util';
import { ClearColor, ClearDepth, ClearStencil, ColorMask, DepthMask, StencilMask, StencilFunc, StencilOp, StencilTest, DepthRange, DepthTest, DepthFunc, Blend, BlendFunc, BlendColor, Program, LineWidth, ActiveTextureUnit, Viewport, BindFramebuffer, BindRenderbuffer, BindTexture, BindVertexBuffer, BindElementBuffer, BindVertexArrayOES, PixelStoreUnpack, PixelStoreUnpackPremultiplyAlpha } from './value';


import type {TriangleIndexArray, LineIndexArray} from '../data/index_array_type';
import type {
    StructArray,
    StructArrayMember
} from '../util/struct_array';
import type Color from '../style-spec/util/color';

type ClearArgs = {
    color?: Color,
    depth?: number,
    stencil?: number
};


class Context {
    gl: WebGLRenderingContext;
    extVertexArrayObject: any;
    currentNumAttributes: ?number;
    lineWidthRange: [number, number];

    clearColor: ClearColor;
    clearDepth: ClearDepth;
    clearStencil: ClearStencil;
    colorMask: ColorMask;
    depthMask: DepthMask;
    stencilMask: StencilMask;
    stencilFunc: StencilFunc;
    stencilOp: StencilOp;
    stencilTest: StencilTest;
    depthRange: DepthRange;
    depthTest: DepthTest;
    depthFunc: DepthFunc;
    blend: Blend;
    blendFunc: BlendFunc;
    blendColor: BlendColor;
    program: Program;
    lineWidth: LineWidth;
    activeTexture: ActiveTextureUnit;
    viewport: Viewport;
    bindFramebuffer: BindFramebuffer;
    bindRenderbuffer: BindRenderbuffer;
    bindTexture: BindTexture;
    bindVertexBuffer: BindVertexBuffer;
    bindElementBuffer: BindElementBuffer;
    bindVertexArrayOES: BindVertexArrayOES;
    pixelStoreUnpack: PixelStoreUnpack;
    pixelStoreUnpackPremultiplyAlpha: PixelStoreUnpackPremultiplyAlpha;

    extTextureFilterAnisotropic: any;
    extTextureFilterAnisotropicMax: any;
    extTextureHalfFloat: any;

    constructor(gl: WebGLRenderingContext) {
        this.gl = gl;
        this.extVertexArrayObject = this.gl.getExtension('OES_vertex_array_object');
        this.lineWidthRange = gl.getParameter(gl.ALIASED_LINE_WIDTH_RANGE);

        this.clearColor = new ClearColor(this);
        this.clearDepth = new ClearDepth(this);
        this.clearStencil = new ClearStencil(this);
        this.colorMask = new ColorMask(this);
        this.depthMask = new DepthMask(this);
        this.stencilMask = new StencilMask(this);
        this.stencilFunc = new StencilFunc(this);
        this.stencilOp = new StencilOp(this);
        this.stencilTest = new StencilTest(this);
        this.depthRange = new DepthRange(this);
        this.depthTest = new DepthTest(this);
        this.depthFunc = new DepthFunc(this);
        this.blend = new Blend(this);
        this.blendFunc = new BlendFunc(this);
        this.blendColor = new BlendColor(this);
        this.program = new Program(this);
        this.lineWidth = new LineWidth(this);
        this.activeTexture = new ActiveTextureUnit(this);
        this.viewport = new Viewport(this);
        this.bindFramebuffer = new BindFramebuffer(this);
        this.bindRenderbuffer = new BindRenderbuffer(this);
        this.bindTexture = new BindTexture(this);
        this.bindVertexBuffer = new BindVertexBuffer(this);
        this.bindElementBuffer = new BindElementBuffer(this);
        this.bindVertexArrayOES = this.extVertexArrayObject && new BindVertexArrayOES(this);
        this.pixelStoreUnpack = new PixelStoreUnpack(this);
        this.pixelStoreUnpackPremultiplyAlpha = new PixelStoreUnpackPremultiplyAlpha(this);

        this.extTextureFilterAnisotropic = (
            gl.getExtension('EXT_texture_filter_anisotropic') ||
            gl.getExtension('MOZ_EXT_texture_filter_anisotropic') ||
            gl.getExtension('WEBKIT_EXT_texture_filter_anisotropic')
        );
        if (this.extTextureFilterAnisotropic) {
            this.extTextureFilterAnisotropicMax = gl.getParameter(this.extTextureFilterAnisotropic.MAX_TEXTURE_MAX_ANISOTROPY_EXT);
        }

        this.extTextureHalfFloat = gl.getExtension('OES_texture_half_float');
        if (this.extTextureHalfFloat) {
            gl.getExtension('OES_texture_half_float_linear');
        }

    }

    createIndexBuffer(array: TriangleIndexArray | LineIndexArray, dynamicDraw?: boolean) {
        return new IndexBuffer(this, array, dynamicDraw);
    }

    createVertexBuffer(array: StructArray, attributes: $ReadOnlyArray<StructArrayMember>, dynamicDraw?: boolean) {
        return new VertexBuffer(this, array, attributes, dynamicDraw);
    }

    createRenderbuffer(storageFormat: number, width: number, height: number) {
        const gl = this.gl;

        const rbo = gl.createRenderbuffer();
        this.bindRenderbuffer.set(rbo);
        gl.renderbufferStorage(gl.RENDERBUFFER, storageFormat, width, height);
        this.bindRenderbuffer.set(null);

        return rbo;
    }

    createFramebuffer(width: number, height: number) {
        return new Framebuffer(this, width, height);
    }

    clear({color, depth}: ClearArgs) {
        const gl = this.gl;
        let mask = 0;

        if (color) {
            mask |= gl.COLOR_BUFFER_BIT;
            this.clearColor.set(color);
            this.colorMask.set([true, true, true, true]);
        }

        if (typeof depth !== 'undefined') {
            mask |= gl.DEPTH_BUFFER_BIT;
            this.clearDepth.set(depth);
            this.depthMask.set(true);
        }

        // See note in Painter#clearStencil: implement this the easy way once GPU bug/workaround is fixed upstream
        // if (typeof stencil !== 'undefined') {
        //     mask |= gl.STENCIL_BUFFER_BIT;
        //     this.clearStencil.set(stencil);
        //     this.stencilMask.set(0xFF);
        // }

        gl.clear(mask);
    }

    setDepthMode(depthMode: $ReadOnly<DepthMode>) {
        if (depthMode.func === this.gl.ALWAYS && !depthMode.mask) {
            this.depthTest.set(false);
        } else {
            this.depthTest.set(true);
            this.depthFunc.set(depthMode.func);
            this.depthMask.set(depthMode.mask);
            this.depthRange.set(depthMode.range);
        }
    }

    setStencilMode(stencilMode: $ReadOnly<StencilMode>) {
        if (stencilMode.test.func === this.gl.ALWAYS && !stencilMode.mask) {
            this.stencilTest.set(false);
        } else {
            this.stencilTest.set(true);
            this.stencilMask.set(stencilMode.mask);
            this.stencilOp.set([stencilMode.fail, stencilMode.depthFail, stencilMode.pass]);
            this.stencilFunc.set({
                func: stencilMode.test.func,
                ref: stencilMode.ref,
                mask: stencilMode.test.mask
            });
        }
    }

    setColorMode(colorMode: $ReadOnly<ColorMode>) {
        if (deepEqual(colorMode.blendFunction, ColorMode.Replace)) {
            this.blend.set(false);
        } else {
            this.blend.set(true);
            this.blendFunc.set(colorMode.blendFunction);
            this.blendColor.set(colorMode.blendColor);
        }

        this.colorMask.set(colorMode.mask);
    }
}

export default Context;
