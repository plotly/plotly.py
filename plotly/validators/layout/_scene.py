import _plotly_utils.basevalidators


class SceneValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='scene', parent_name='layout', **kwargs):
        super(SceneValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Scene',
            data_docs="""
            annotations
                plotly.graph_objs.layout.scene.Annotation
                instance or dict with compatible properties
            aspectmode
                If "cube", this scene's axes are drawn as a
                cube, regardless of the axes' ranges. If
                "data", this scene's axes are drawn in
                proportion with the axes' ranges. If "manual",
                this scene's axes are drawn in proportion with
                the input of "aspectratio" (the default
                behavior if "aspectratio" is provided). If
                "auto", this scene's axes are drawn using the
                results of "data" except when one axis is more
                than four times the size of the two others,
                where in that case the results of "cube" are
                used.
            aspectratio
                Sets this scene's axis aspectratio.
            bgcolor

            camera
                plotly.graph_objs.layout.scene.Camera instance
                or dict with compatible properties
            domain
                plotly.graph_objs.layout.scene.Domain instance
                or dict with compatible properties
            dragmode
                Determines the mode of drag interactions for
                this scene.
            hovermode
                Determines the mode of hover interactions for
                this scene.
            xaxis
                plotly.graph_objs.layout.scene.XAxis instance
                or dict with compatible properties
            yaxis
                plotly.graph_objs.layout.scene.YAxis instance
                or dict with compatible properties
            zaxis
                plotly.graph_objs.layout.scene.ZAxis instance
                or dict with compatible properties
""",
            **kwargs
        )
