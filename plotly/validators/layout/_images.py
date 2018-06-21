import _plotly_utils.basevalidators


class ImagesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(self, plotly_name='images', parent_name='layout', **kwargs):
        super(ImagesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Image',
            data_docs="""
            layer
                Specifies whether images are drawn below or
                above traces. When `xref` and `yref` are both
                set to `paper`, image is drawn below the entire
                plot area.
            opacity
                Sets the opacity of the image.
            sizex
                Sets the image container size horizontally. The
                image will be sized based on the `position`
                value. When `xref` is set to `paper`, units are
                sized relative to the plot width.
            sizey
                Sets the image container size vertically. The
                image will be sized based on the `position`
                value. When `yref` is set to `paper`, units are
                sized relative to the plot height.
            sizing
                Specifies which dimension of the image to
                constrain.
            source
                Specifies the URL of the image to be used. The
                URL must be accessible from the domain where
                the plot code is run, and can be either
                relative or absolute.
            visible
                Determines whether or not this image is
                visible.
            x
                Sets the image's x position. When `xref` is set
                to `paper`, units are sized relative to the
                plot height. See `xref` for more info
            xanchor
                Sets the anchor for the x position
            xref
                Sets the images's x coordinate axis. If set to
                a x axis id (e.g. *x* or *x2*), the `x`
                position refers to an x data coordinate If set
                to *paper*, the `x` position refers to the
                distance from the left of plot in normalized
                coordinates where *0* (*1*) corresponds to the
                left (right).
            y
                Sets the image's y position. When `yref` is set
                to `paper`, units are sized relative to the
                plot height. See `yref` for more info
            yanchor
                Sets the anchor for the y position.
            yref
                Sets the images's y coordinate axis. If set to
                a y axis id (e.g. *y* or *y2*), the `y`
                position refers to a y data coordinate. If set
                to *paper*, the `y` position refers to the
                distance from the bottom of the plot in
                normalized coordinates where *0* (*1*)
                corresponds to the bottom (top).""",
            **kwargs
        )
