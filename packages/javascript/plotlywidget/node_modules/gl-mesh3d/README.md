gl-mesh3d
=====================
Visualization module for meshes/point clouds/graphs.

# Example

```javascript
var createScene = require('gl-plot3d')
var createMesh  = require('gl-mesh3d')
var bunny       = require('bunny')

var scene = createScene()

var mesh = createMesh({
  gl:         scene.gl,
  cells:      bunny.cells,
  positions:  bunny.positions,
  colormap:   'jet'
})

scene.add(mesh)
```

[Try out the example in your browser](http://gl-vis.github.io/gl-mesh3d/)

# Install

```
npm i gl-mesh3d
```
    
# Basic interface

## Constructor

#### `var mesh = require('gl-mesh3d')(params)`
Creates a simplicial complex that can be drawn directly in a WebGL context.

* `params` is an object that has the following properties:

    + `gl` A reference to the WebGL context
    + `cells` *(Required)* An indexed list of vertices, edges and/or faces.
    + `positions` *(Required)* An array of positions for the mesh, encoded as arrays
    + `vertexColors` A list of per vertex color attributes encoded as length 3 rgb arrays
    + `vertexUVs`
    + `cellUVs`
    + `vertexIntensity`
    + `colormap`
    + `vertexIntensityBounds` intensity range for the colormap
    + `cellIntensity`
    + `cellColors` A list of per cell color attributes
    + `meshColor` A constant color for the entire mesh
    + `vertexNormals` An array of per vertex normals
    + `cellNormals` An array of per cell normals
    + `useFacetNormals` A flag which if set to `true` forces `cellNormals` to be computed
    + `pointSizes` An array of point sizes
    + `pointSize` A single point size float
    + `ambientLight` ambient light color * intensity
    + `diffuseLight` diffuse light color * intensity
    + `specularLight` specular light color
    + `lightPosition` location of light
    + `roughness` surface roughness
    + `fresnel` surface glossiness/"rim light" factor
    + `opacity` surface opacity

**Returns** A renderable mesh object

## Update

#### `mesh.update(params)`
Updates the contents of the simplicial complex in place.

* `params` is a list of parameters which are in the same format as the constructor

## Properties

#### `mesh.lightPosition`
The 3D position of the directional light source

#### `mesh.ambientLight`
Ambient light color

#### `mesh.diffuseLight`
Diffuse light color

#### `mesh.specularLight`
Specular light color

#### `mesh.roughness`
Mesh surface roughness

#### `mesh.fresnel`
Fresnel parameter

#### `mesh.vertexNormalsEpsilon`
Epsilon for vertex normals calculation

#### `mesh.faceNormalsEpsilon`
Epsilon for face normals calculation

#### `mesh.opacity`
Opacity

# Credits
(c) 2013-2015 Mikola Lysenko. MIT License
