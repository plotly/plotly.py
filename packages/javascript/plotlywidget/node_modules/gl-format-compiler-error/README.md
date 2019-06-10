# gl-format-compiler-error

Formats a webgl glsl compiler error. Use in conjunction with
[glsl-shader-name](https://www.npmjs.com/package/glsl-shader-name) to include your shader's 
name in the formatted error string.

## Example

```js
    var formatCompilerError = require('gl-format-compiler-error');
    
    ...
    
    var shader = gl.createShader(type)
    gl.shaderSource(shader, src)
    gl.compileShader(shader)
    if(!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        var errLog = gl.getShaderInfoLog(shader)
        var fmt = formatCompilerError(errLog, src, type);
        console.warn(fmt.long);
        throw new Error(fmt.short);
    }
```

yields warning:

```text
Error in vertex shader generic:
  13: 
  14: void main() {
  15:     bug;
^^^^: 'bug' : undeclared identifier

  17:     vUV = aUV;
  18:     vPos = vec3(uModel * vec4(aPosition, 1.0))
  19: }
^^^^: '}' : syntax error
```

and error:

```text
Uncaught Error: Error in vertex shader generic:
ERROR: 0:15: 'bug' : undeclared identifier 
ERROR: 0:19: '}' : syntax error 
```

## Usage

### Install

```sh
npm install gl-format-compiler-error --save
```

### API

```js
var formatCompilerError = require('gl-format-compiler-error');
```

#### `fmt = formatCompilerError(errLog, source, type)`

Takes `errLog` result from `gl.getShaderInfoLog`, the shader `source` string, and the `type` of shader,
either `gl.VERTEX_SHADER` or `gl.FRAGMENT_SHADER`. Returns an object that contains the long and short
form of the formatted error:

```js
{
    long: "long form error with code snippets",
    short: "short form error, similar to the original error log"
}
```