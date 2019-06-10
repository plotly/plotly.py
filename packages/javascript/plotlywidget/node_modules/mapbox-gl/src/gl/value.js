// @flow

import Color from '../style-spec/util/color';

import { clamp } from '../util/util';

import type Context from './context';
import type {
    BlendFuncType,
    ColorMaskType,
    DepthRangeType,
    DepthMaskType,
    StencilFuncType,
    StencilOpType,
    DepthFuncType,
    TextureUnitType,
    ViewportType,
} from './types';

export interface Value<T> {
    context: Context;
    current: T;
    get(): T;
    set(value: T): void;
}

export class ClearColor implements Value<Color> {
    context: Context;
    current: Color;

    constructor(context: Context) {
        this.context = context;
        this.current = Color.transparent;
    }

    get(): Color { return this.current; }

    set(v: Color): void {
        const c = this.current;
        if (v.r !== c.r || v.g !== c.g || v.b !== c.b || v.a !== c.a) {
            this.context.gl.clearColor(v.r, v.g, v.b, v.a);
            this.current = v;
        }
    }
}

export class ClearDepth implements Value<number> {
    context: Context;
    current: number;

    constructor(context: Context) {
        this.context = context;
        this.current = 1;
    }

    get(): number { return this.current; }

    set(v: number): void {
        if (this.current !== v) {
            this.context.gl.clearDepth(v);
            this.current = v;
        }
    }
}

export class ClearStencil implements Value<number> {
    context: Context;
    current: number;

    constructor(context: Context) {
        this.context = context;
        this.current = 0;
    }

    get(): number { return this.current; }

    set(v: number): void {
        if (this.current !== v) {
            this.context.gl.clearStencil(v);
            this.current = v;
        }
    }
}

export class ColorMask implements Value<ColorMaskType> {
    context: Context;
    current: ColorMaskType;

    constructor(context: Context) {
        this.context = context;
        this.current = [true, true, true, true];
    }

    get(): ColorMaskType { return this.current; }

    set(v: ColorMaskType): void {
        const c = this.current;
        if (v[0] !== c[0] || v[1] !== c[1] || v[2] !== c[2] || v[3] !== c[3]) {
            this.context.gl.colorMask(v[0], v[1], v[2], v[3]);
            this.current = v;
        }
    }
}

export class DepthMask implements Value<DepthMaskType> {
    context: Context;
    current: DepthMaskType;

    constructor(context: Context) {
        this.context = context;
        this.current = true;
    }

    get(): DepthMaskType { return this.current; }

    set(v: DepthMaskType): void {
        if (this.current !== v) {
            this.context.gl.depthMask(v);
            this.current = v;
        }
    }
}

export class StencilMask implements Value<number> {
    context: Context;
    current: number;

    constructor(context: Context) {
        this.context = context;
        this.current = 0xFF;
    }

    get(): number { return this.current; }

    set(v: number): void {
        if (this.current !== v) {
            this.context.gl.stencilMask(v);
            this.current = v;
        }
    }
}

export class StencilFunc implements Value<StencilFuncType> {
    context: Context;
    current: StencilFuncType;

    constructor(context: Context) {
        this.context = context;
        this.current = {
            func: context.gl.ALWAYS,
            ref: 0,
            mask: 0xFF
        };
    }

    get(): StencilFuncType { return this.current; }

    set(v: StencilFuncType): void {
        const c = this.current;
        if (v.func !== c.func || v.ref !== c.ref || v.mask !== c.mask) {
            this.context.gl.stencilFunc(v.func, v.ref, v.mask);
            this.current = v;
        }
    }
}

export class StencilOp implements Value<StencilOpType> {
    context: Context;
    current: StencilOpType;

    constructor(context: Context) {
        this.context = context;
        const gl = this.context.gl;
        this.current = [gl.KEEP, gl.KEEP, gl.KEEP];
    }

    get(): StencilOpType { return this.current; }

    set(v: StencilOpType): void {
        const c = this.current;
        if (v[0] !== c[0] || v[1] !== c[1] || v[2] !== c[2]) {
            this.context.gl.stencilOp(v[0], v[1], v[2]);
            this.current = v;
        }
    }
}

export class StencilTest implements Value<boolean> {
    context: Context;
    current: boolean;

    constructor(context: Context) {
        this.context = context;
        this.current = false;
    }

    get(): boolean { return this.current; }

    set(v: boolean): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            if (v) {
                gl.enable(gl.STENCIL_TEST);
            } else {
                gl.disable(gl.STENCIL_TEST);
            }
            this.current = v;
        }
    }
}

export class DepthRange implements Value<DepthRangeType> {
    context: Context;
    current: DepthRangeType;

    constructor(context: Context) {
        this.context = context;
        this.current = [0, 1];
    }

    get(): DepthRangeType { return this.current; }

    set(v: DepthRangeType): void {
        const c = this.current;
        if (v[0] !== c[0] || v[1] !== c[1]) {
            this.context.gl.depthRange(v[0], v[1]);
            this.current = v;
        }
    }
}

export class DepthTest implements Value<boolean> {
    context: Context;
    current: boolean;

    constructor(context: Context) {
        this.context = context;
        this.current = false;
    }

    get(): boolean { return this.current; }

    set(v: boolean): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            if (v) {
                gl.enable(gl.DEPTH_TEST);
            } else {
                gl.disable(gl.DEPTH_TEST);
            }
            this.current = v;
        }
    }
}

export class DepthFunc implements Value<DepthFuncType> {
    context: Context;
    current: DepthFuncType;

    constructor(context: Context) {
        this.context = context;
        this.current = context.gl.LESS;
    }

    get(): DepthFuncType { return this.current; }

    set(v: DepthFuncType): void {
        if (this.current !== v) {
            this.context.gl.depthFunc(v);
            this.current = v;
        }
    }
}

export class Blend implements Value<boolean> {
    context: Context;
    current: boolean;

    constructor(context: Context) {
        this.context = context;
        this.current = false;
    }

    get(): boolean { return this.current; }

    set(v: boolean): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            if (v) {
                gl.enable(gl.BLEND);
            } else {
                gl.disable(gl.BLEND);
            }
            this.current = v;
        }
    }
}

export class BlendFunc implements Value<BlendFuncType> {
    context: Context;
    current: BlendFuncType;

    constructor(context: Context) {
        this.context = context;
        const gl = this.context.gl;
        this.current = [gl.ONE, gl.ZERO];
    }

    get(): BlendFuncType { return this.current; }

    set(v: BlendFuncType): void {
        const c = this.current;
        if (v[0] !== c[0] || v[1] !== c[1]) {
            this.context.gl.blendFunc(v[0], v[1]);
            this.current = v;
        }
    }
}

export class BlendColor implements Value<Color> {
    context: Context;
    current: Color;

    constructor(context: Context) {
        this.context = context;
        this.current = Color.transparent;
    }

    get(): Color { return this.current; }

    set(v: Color): void {
        const c = this.current;
        if (v.r !== c.r || v.g !== c.g || v.b !== c.b || v.a !== c.a) {
            this.context.gl.blendColor(v.r, v.g, v.b, v.a);
            this.current = v;
        }
    }
}

export class Program implements Value<?WebGLProgram> {
    context: Context;
    current: ?WebGLProgram;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): ?WebGLProgram { return this.current; }

    set(v: ?WebGLProgram): void {
        if (this.current !== v) {
            this.context.gl.useProgram(v);
            this.current = v;
        }
    }
}

export class LineWidth implements Value<number> {
    context: Context;
    current: number;

    constructor(context: Context) {
        this.context = context;
        this.current = 1;
    }

    get(): number { return this.current; }

    set(v: number): void {
        const range = this.context.lineWidthRange;
        const clamped = clamp(v, range[0], range[1]);
        if (this.current !== clamped) {
            this.context.gl.lineWidth(clamped);
            this.current = v;
        }
    }
}

export class ActiveTextureUnit implements Value<TextureUnitType> {
    context: Context;
    current: TextureUnitType;

    constructor(context: Context) {
        this.context = context;
        this.current = context.gl.TEXTURE0;
    }

    get(): TextureUnitType { return this.current; }

    set(v: TextureUnitType): void {
        if (this.current !== v) {
            this.context.gl.activeTexture(v);
            this.current = v;
        }
    }
}

export class Viewport implements Value<ViewportType> {
    context: Context;
    current: ViewportType;

    constructor(context: Context) {
        this.context = context;
        const gl = this.context.gl;
        this.current = [0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight];
    }

    get(): ViewportType { return this.current; }

    set(v: ViewportType): void {
        const c = this.current;
        if (v[0] !== c[0] || v[1] !== c[1] || v[2] !== c[2] || v[3] !== c[3]) {
            this.context.gl.viewport(v[0], v[1], v[2], v[3]);
            this.current = v;
        }
    }
}

export class BindFramebuffer implements Value<?WebGLFramebuffer> {
    context: Context;
    current: ?WebGLFramebuffer;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): ?WebGLFramebuffer { return this.current; }

    set(v: ?WebGLFramebuffer): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            gl.bindFramebuffer(gl.FRAMEBUFFER, v);
            this.current = v;
        }
    }
}

export class BindRenderbuffer implements Value<?WebGLRenderbuffer> {
    context: Context;
    current: ?WebGLRenderbuffer;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): ?WebGLRenderbuffer { return this.current; }

    set(v: ?WebGLRenderbuffer): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            gl.bindRenderbuffer(gl.RENDERBUFFER, v);
            this.current = v;
        }
    }
}

export class BindTexture implements Value<?WebGLTexture> {
    context: Context;
    current: ?WebGLTexture;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): ?WebGLTexture { return this.current; }

    set(v: ?WebGLTexture): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            gl.bindTexture(gl.TEXTURE_2D, v);
            this.current = v;
        }
    }
}

export class BindVertexBuffer implements Value<?WebGLBuffer> {
    context: Context;
    current: ?WebGLBuffer;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): ?WebGLBuffer { return this.current; }

    set(v: ?WebGLBuffer): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            gl.bindBuffer(gl.ARRAY_BUFFER, v);
            this.current = v;
        }
    }
}

export class BindElementBuffer implements Value<?WebGLBuffer> {
    context: Context;
    current: ?WebGLBuffer;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): ?WebGLBuffer { return this.current; }

    set(v: ?WebGLBuffer): void {
        // Always rebind
        const gl = this.context.gl;
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, v);
        this.current = v;
    }
}

export class BindVertexArrayOES implements Value<any> {
    context: Context;
    current: any;

    constructor(context: Context) {
        this.context = context;
        this.current = null;
    }

    get(): any { return this.current; }

    set(v: any): void {
        if (this.current !== v && this.context.extVertexArrayObject) {
            this.context.extVertexArrayObject.bindVertexArrayOES(v);
            this.current = v;
        }
    }
}

export class PixelStoreUnpack implements Value<number> {
    context: Context;
    current: number;

    constructor(context: Context) {
        this.context = context;
        this.current = 4;
    }

    get(): number { return this.current; }

    set(v: number): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            gl.pixelStorei(gl.UNPACK_ALIGNMENT, v);
            this.current = v;
        }
    }
}

export class PixelStoreUnpackPremultiplyAlpha implements Value<boolean> {
    context: Context;
    current: boolean;

    constructor(context: Context) {
        this.context = context;
        this.current = false;
    }

    get(): boolean { return this.current; }

    set(v: boolean): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, (v: any));
            this.current = v;
        }
    }
}

/**
 * Framebuffer values
 * @private
 */
export class FramebufferValue<T> {
    context: Context;
    parent: WebGLFramebuffer;
    current: ?T;

    constructor(context: Context, parent: WebGLFramebuffer) {
        this.context = context;
        this.current = null;
        this.parent = parent;
    }

    get(): ?T { return this.current; }
}

export class ColorAttachment extends FramebufferValue<?WebGLTexture> implements Value<?WebGLTexture> {
    dirty: boolean;

    constructor(context: Context, parent: WebGLFramebuffer) {
        super(context, parent);
        this.dirty = false;
    }

    set(v: ?WebGLTexture): void {
        if (this.dirty || this.current !== v) {
            const gl = this.context.gl;
            this.context.bindFramebuffer.set(this.parent);
            // note: it's possible to attach a renderbuffer to the color
            // attachment point, but thus far MBGL only uses textures for color
            gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, v, 0);
            this.current = v;
            this.dirty = false;
        }
    }

    setDirty() {
        this.dirty = true;
    }
}

export class DepthAttachment extends FramebufferValue<?WebGLRenderbuffer> implements Value<?WebGLRenderbuffer> {
    set(v: ?WebGLRenderbuffer): void {
        if (this.current !== v) {
            const gl = this.context.gl;
            this.context.bindFramebuffer.set(this.parent);
            // note: it's possible to attach a texture to the depth attachment
            // point, but thus far MBGL only uses renderbuffers for depth
            gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.RENDERBUFFER, v);
            this.current = v;
        }
    }
}
