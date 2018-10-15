This package is for utilities that are used during code generation
and at runtime.  The reason for not placing these under the main plotly/
package is that this avoids the complications of importing the module
we're generating code into during code generation.

This module must be independent of (it must not import from) both
plotly/ and codegen/