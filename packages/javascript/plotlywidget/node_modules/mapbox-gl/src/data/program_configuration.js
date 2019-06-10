// @flow

import { packUint8ToFloat } from '../shaders/encode_attribute';
import Color from '../style-spec/util/color';
import { register } from '../util/web_worker_transfer';
import { PossiblyEvaluatedPropertyValue } from '../style/properties';
import { StructArrayLayout1f4, StructArrayLayout2f8, StructArrayLayout4f16 } from './array_types';
import EvaluationParameters from '../style/evaluation_parameters';

import type Context from '../gl/context';
import type {TypedStyleLayer} from '../style/style_layer/typed_style_layer';
import type {StructArray, StructArrayMember} from '../util/struct_array';
import type VertexBuffer from '../gl/vertex_buffer';
import type Program from '../render/program';
import type {
    Feature,
    GlobalProperties,
    SourceExpression,
    CompositeExpression
} from '../style-spec/expression';
import type {PossiblyEvaluated} from '../style/properties';

function packColor(color: Color): [number, number] {
    return [
        packUint8ToFloat(255 * color.r, 255 * color.g),
        packUint8ToFloat(255 * color.b, 255 * color.a)
    ];
}

/**
 *  `Binder` is the interface definition for the strategies for constructing,
 *  uploading, and binding paint property data as GLSL attributes.
 *
 *  It has three implementations, one for each of the three strategies we use:
 *
 *  * For _constant_ properties -- those whose value is a constant, or the constant
 *    result of evaluating a camera expression at a particular camera position -- we
 *    don't need a vertex buffer, and instead use a uniform.
 *  * For data expressions, we use a vertex buffer with a single attribute value,
 *    the evaluated result of the source function for the given feature.
 *  * For composite expressions, we use a vertex buffer with two attributes: min and
 *    max values covering the range of zooms at which we expect the tile to be
 *    displayed. These values are calculated by evaluating the composite expression for
 *    the given feature at strategically chosen zoom levels. In addition to this
 *    attribute data, we also use a uniform value which the shader uses to interpolate
 *    between the min and max value at the final displayed zoom level. The use of a
 *    uniform allows us to cheaply update the value on every frame.
 *
 *  Note that the shader source varies depending on whether we're using a uniform or
 *  attribute. We dynamically compile shaders at runtime to accomodate this.
 *
 * @private
 */
interface Binder<T> {
    statistics: { max: number };

    populatePaintArray(length: number, feature: Feature): void;
    upload(Context): void;
    destroy(): void;

    defines(): Array<string>;

    setUniforms(context: Context,
                program: Program,
                globals: GlobalProperties,
                currentValue: PossiblyEvaluatedPropertyValue<T>): void;
}

class ConstantBinder<T> implements Binder<T> {
    value: T;
    name: string;
    type: string;
    statistics: { max: number };

    constructor(value: T, name: string, type: string) {
        this.value = value;
        this.name = name;
        this.type = type;
        this.statistics = { max: -Infinity };
    }

    defines() {
        return [`#define HAS_UNIFORM_u_${this.name}`];
    }

    populatePaintArray() {}
    upload() {}
    destroy() {}

    setUniforms(context: Context,
                program: Program,
                globals: GlobalProperties,
                currentValue: PossiblyEvaluatedPropertyValue<T>) {
        const value: any = currentValue.constantOr(this.value);
        const gl = context.gl;
        if (this.type === 'color') {
            gl.uniform4f(program.uniforms[`u_${this.name}`], value.r, value.g, value.b, value.a);
        } else {
            gl.uniform1f(program.uniforms[`u_${this.name}`], value);
        }
    }
}

class SourceExpressionBinder<T> implements Binder<T> {
    expression: SourceExpression;
    name: string;
    type: string;
    statistics: { max: number };

    paintVertexArray: StructArray;
    paintVertexAttributes: Array<StructArrayMember>;
    paintVertexBuffer: ?VertexBuffer;

    constructor(expression: SourceExpression, name: string, type: string) {
        this.expression = expression;
        this.name = name;
        this.type = type;
        this.statistics = { max: -Infinity };
        const PaintVertexArray = type === 'color' ? StructArrayLayout2f8 : StructArrayLayout1f4;
        this.paintVertexAttributes = [{
            name: `a_${name}`,
            type: 'Float32',
            components: type === 'color' ? 2 : 1,
            offset: 0
        }];
        this.paintVertexArray = new PaintVertexArray();
    }

    defines() {
        return [];
    }

    populatePaintArray(length: number, feature: Feature) {
        const paintArray = this.paintVertexArray;

        const start = paintArray.length;
        paintArray.reserve(length);

        const value = this.expression.evaluate(new EvaluationParameters(0), feature);

        if (this.type === 'color') {
            const color = packColor(value);
            for (let i = start; i < length; i++) {
                paintArray.emplaceBack(color[0], color[1]);
            }
        } else {
            for (let i = start; i < length; i++) {
                paintArray.emplaceBack(value);
            }

            this.statistics.max = Math.max(this.statistics.max, value);
        }
    }

    upload(context: Context) {
        if (this.paintVertexArray) {
            this.paintVertexBuffer = context.createVertexBuffer(this.paintVertexArray, this.paintVertexAttributes);
        }
    }

    destroy() {
        if (this.paintVertexBuffer) {
            this.paintVertexBuffer.destroy();
        }
    }

    setUniforms(context: Context, program: Program) {
        context.gl.uniform1f(program.uniforms[`a_${this.name}_t`], 0);
    }
}

class CompositeExpressionBinder<T> implements Binder<T> {
    expression: CompositeExpression;
    name: string;
    type: string;
    useIntegerZoom: boolean;
    zoom: number;
    statistics: { max: number };

    paintVertexArray: StructArray;
    paintVertexAttributes: Array<StructArrayMember>;
    paintVertexBuffer: ?VertexBuffer;

    constructor(expression: CompositeExpression, name: string, type: string, useIntegerZoom: boolean, zoom: number) {
        this.expression = expression;
        this.name = name;
        this.type = type;
        this.useIntegerZoom = useIntegerZoom;
        this.zoom = zoom;
        this.statistics = { max: -Infinity };
        const PaintVertexArray = type === 'color' ? StructArrayLayout4f16 : StructArrayLayout2f8;
        this.paintVertexAttributes = [{
            name: `a_${name}`,
            type: 'Float32',
            components: type === 'color' ? 4 : 2,
            offset: 0
        }];
        this.paintVertexArray = new PaintVertexArray();
    }

    defines() {
        return [];
    }

    populatePaintArray(length: number, feature: Feature) {
        const paintArray = this.paintVertexArray;

        const start = paintArray.length;
        paintArray.reserve(length);

        const min = this.expression.evaluate(new EvaluationParameters(this.zoom), feature);
        const max = this.expression.evaluate(new EvaluationParameters(this.zoom + 1), feature);

        if (this.type === 'color') {
            const minColor = packColor(min);
            const maxColor = packColor(max);
            for (let i = start; i < length; i++) {
                paintArray.emplaceBack(minColor[0], minColor[1], maxColor[0], maxColor[1]);
            }
        } else {
            for (let i = start; i < length; i++) {
                paintArray.emplaceBack(min, max);
            }

            this.statistics.max = Math.max(this.statistics.max, min, max);
        }
    }

    upload(context: Context) {
        if (this.paintVertexArray) {
            this.paintVertexBuffer = context.createVertexBuffer(this.paintVertexArray, this.paintVertexAttributes);
        }
    }

    destroy() {
        if (this.paintVertexBuffer) {
            this.paintVertexBuffer.destroy();
        }
    }

    interpolationFactor(currentZoom: number) {
        if (this.useIntegerZoom) {
            return this.expression.interpolationFactor(Math.floor(currentZoom), this.zoom, this.zoom + 1);
        } else {
            return this.expression.interpolationFactor(currentZoom, this.zoom, this.zoom + 1);
        }
    }

    setUniforms(context: Context, program: Program, globals: GlobalProperties) {
        context.gl.uniform1f(program.uniforms[`a_${this.name}_t`], this.interpolationFactor(globals.zoom));
    }
}

/**
 * ProgramConfiguration contains the logic for binding style layer properties and tile
 * layer feature data into GL program uniforms and vertex attributes.
 *
 * Non-data-driven property values are bound to shader uniforms. Data-driven property
 * values are bound to vertex attributes. In order to support a uniform GLSL syntax over
 * both, [Mapbox GL Shaders](https://github.com/mapbox/mapbox-gl-shaders) defines a `#pragma`
 * abstraction, which ProgramConfiguration is responsible for implementing. At runtime,
 * it examines the attributes of a particular layer, combines this with fixed knowledge
 * about how layers of the particular type are implemented, and determines which uniforms
 * and vertex attributes will be required. It can then substitute the appropriate text
 * into the shader source code, create and link a program, and bind the uniforms and
 * vertex attributes in preparation for drawing.
 *
 * When a vector tile is parsed, this same configuration information is used to
 * populate the attribute buffers needed for data-driven styling using the zoom
 * level and feature property data.
 *
 * @private
 */
export default class ProgramConfiguration {
    binders: { [string]: Binder<any> };
    cacheKey: string;
    layoutAttributes: Array<StructArrayMember>;

    _buffers: Array<VertexBuffer>;

    constructor() {
        this.binders = {};
        this.cacheKey = '';

        this._buffers = [];
    }

    static createDynamic<Layer: TypedStyleLayer>(layer: Layer, zoom: number, filterProperties: (string) => boolean) {
        const self = new ProgramConfiguration();
        const keys = [];

        for (const property in layer.paint._values) {
            if (!filterProperties(property)) continue;
            const value = layer.paint.get(property);
            if (!(value instanceof PossiblyEvaluatedPropertyValue) || !value.property.specification['property-function']) {
                continue;
            }
            const name = paintAttributeName(property, layer.type);
            const type = value.property.specification.type;
            const useIntegerZoom = value.property.useIntegerZoom;

            if (value.value.kind === 'constant') {
                self.binders[property] = new ConstantBinder(value.value, name, type);
                keys.push(`/u_${name}`);
            } else if (value.value.kind === 'source') {
                self.binders[property] = new SourceExpressionBinder(value.value, name, type);
                keys.push(`/a_${name}`);
            } else {
                self.binders[property] = new CompositeExpressionBinder(value.value, name, type, useIntegerZoom, zoom);
                keys.push(`/z_${name}`);
            }
        }

        self.cacheKey = keys.sort().join('');

        return self;
    }

    populatePaintArrays(length: number, feature: Feature) {
        for (const property in this.binders) {
            this.binders[property].populatePaintArray(length, feature);
        }
    }

    defines(): Array<string> {
        const result = [];
        for (const property in this.binders) {
            result.push.apply(result, this.binders[property].defines());
        }
        return result;
    }

    setUniforms<Properties: Object>(context: Context, program: Program, properties: PossiblyEvaluated<Properties>, globals: GlobalProperties) {
        for (const property in this.binders) {
            const binder = this.binders[property];
            binder.setUniforms(context, program, globals, properties.get(property));
        }
    }

    getPaintVertexBuffers(): Array<VertexBuffer> {
        return this._buffers;
    }

    upload(context: Context) {
        for (const property in this.binders) {
            this.binders[property].upload(context);
        }

        const buffers = [];
        for (const property in this.binders) {
            const binder = this.binders[property];
            if ((binder instanceof SourceExpressionBinder ||
                binder instanceof CompositeExpressionBinder) &&
                binder.paintVertexBuffer
            ) {
                buffers.push(binder.paintVertexBuffer);
            }
        }
        this._buffers = buffers;
    }

    destroy() {
        for (const property in this.binders) {
            this.binders[property].destroy();
        }
    }
}

export class ProgramConfigurationSet<Layer: TypedStyleLayer> {
    programConfigurations: {[string]: ProgramConfiguration};

    constructor(layoutAttributes: Array<StructArrayMember>, layers: $ReadOnlyArray<Layer>, zoom: number, filterProperties: (string) => boolean = () => true) {
        this.programConfigurations = {};
        for (const layer of layers) {
            this.programConfigurations[layer.id] = ProgramConfiguration.createDynamic(layer, zoom, filterProperties);
            this.programConfigurations[layer.id].layoutAttributes = layoutAttributes;
        }
    }

    populatePaintArrays(length: number, feature: Feature) {
        for (const key in this.programConfigurations) {
            this.programConfigurations[key].populatePaintArrays(length, feature);
        }
    }

    get(layerId: string) {
        return this.programConfigurations[layerId];
    }

    upload(context: Context) {
        for (const layerId in this.programConfigurations) {
            this.programConfigurations[layerId].upload(context);
        }
    }

    destroy() {
        for (const layerId in this.programConfigurations) {
            this.programConfigurations[layerId].destroy();
        }
    }
}

// paint property arrays
function paintAttributeName(property, type) {
    const attributeNameExceptions = {
        'text-opacity': 'opacity',
        'icon-opacity': 'opacity',
        'text-color': 'fill_color',
        'icon-color': 'fill_color',
        'text-halo-color': 'halo_color',
        'icon-halo-color': 'halo_color',
        'text-halo-blur': 'halo_blur',
        'icon-halo-blur': 'halo_blur',
        'text-halo-width': 'halo_width',
        'icon-halo-width': 'halo_width',
        'line-gap-width': 'gapwidth'
    };
    return attributeNameExceptions[property] ||
        property.replace(`${type}-`, '').replace(/-/g, '_');
}

register('ConstantBinder', ConstantBinder);
register('SourceExpressionBinder', SourceExpressionBinder);
register('CompositeExpressionBinder', CompositeExpressionBinder);
register('ProgramConfiguration', ProgramConfiguration, {omit: ['_buffers']});
register('ProgramConfigurationSet', ProgramConfigurationSet);
