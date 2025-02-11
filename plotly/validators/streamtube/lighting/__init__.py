import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._vertexnormalsepsilon.VertexnormalsepsilonValidator",
        "._specular.SpecularValidator",
        "._roughness.RoughnessValidator",
        "._fresnel.FresnelValidator",
        "._facenormalsepsilon.FacenormalsepsilonValidator",
        "._diffuse.DiffuseValidator",
        "._ambient.AmbientValidator",
    ],
)
