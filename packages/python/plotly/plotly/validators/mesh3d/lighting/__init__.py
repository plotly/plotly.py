import _plotly_utils.basevalidators


class VertexnormalsepsilonValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self,
        plotly_name="vertexnormalsepsilon",
        parent_name="mesh3d.lighting",
        **kwargs
    ):
        super(VertexnormalsepsilonValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SpecularValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="specular", parent_name="mesh3d.lighting", **kwargs):
        super(SpecularValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 2),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RoughnessValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="roughness", parent_name="mesh3d.lighting", **kwargs
    ):
        super(RoughnessValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FresnelValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="fresnel", parent_name="mesh3d.lighting", **kwargs):
        super(FresnelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 5),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FacenormalsepsilonValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="facenormalsepsilon", parent_name="mesh3d.lighting", **kwargs
    ):
        super(FacenormalsepsilonValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DiffuseValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="diffuse", parent_name="mesh3d.lighting", **kwargs):
        super(DiffuseValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AmbientValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="ambient", parent_name="mesh3d.lighting", **kwargs):
        super(AmbientValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
