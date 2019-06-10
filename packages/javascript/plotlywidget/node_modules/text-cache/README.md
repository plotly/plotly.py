text-cache
==========
A cache of generated vector font meshes.  This is an internal module used to share generated fonts/glyphs across gl-vis packages.

# API

#### `require('text-cache')(font, str)`
Generates a vectorized text mesh.

* `font` is the font to use
* `str` is the string to generate

**Returns** A triangulation encoding the vectorized text string.

# License
(c) 2015 Mikola Lysenko. MIT License
