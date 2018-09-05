import _plotly_utils.basevalidators


class CameraValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='camera', parent_name='layout.scene', **kwargs
    ):
        super(CameraValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Camera',
            data_docs="""
            center
                Sets the (x,y,z) components of the 'center'
                camera vector This vector determines the
                translation (x,y,z) space about the center of
                this scene. By default, there is no such
                translation.
            eye
                Sets the (x,y,z) components of the 'eye' camera
                vector. This vector determines the view point
                about the origin of this scene.
            up
                Sets the (x,y,z) components of the 'up' camera
                vector. This vector determines the up direction
                of this scene with respect to the page. The
                default is *{x: 0, y: 0, z: 1}* which means
                that the z axis points up.
""",
            **kwargs
        )
