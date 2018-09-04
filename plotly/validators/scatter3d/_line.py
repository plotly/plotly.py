import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='line', parent_name='scatter3d', **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Line',
            data_docs="""
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `line.colorscale`. Has an effect
                only if in `line.color`is set to a numerical
                array. In case `colorscale` is unspecified or
                `autocolorscale` is true, the default  palette
                will be chosen according to whether numbers in
                the `color` array are all positive, all
                negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `line.color`) or the bounds set in
                `line.cmin` and `line.cmax`  Has an effect only
                if in `line.color`is set to a numerical array.
                Defaults to `false` when `line.cmin` and
                `line.cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Has
                an effect only if in `line.color`is set to a
                numerical array. Value should have the same
                units as in `line.color` and if set,
                `line.cmin` must be set as well.
            cmin
                Sets the lower bound of the color domain. Has
                an effect only if in `line.color`is set to a
                numerical array. Value should have the same
                units as in `line.color` and if set,
                `line.cmax` must be set as well.
            color
                Sets thelinecolor. It accepts either a specific
                color or an array of numbers that are mapped to
                the colorscale relative to the max and min
                values of the array or relative to `line.cmin`
                and `line.cmax` if set.
            colorscale
                Sets the colorscale. Has an effect only if in
                `line.color`is set to a numerical array. The
                colorscale must be an array containing arrays
                mapping a normalized value to an rgb, rgba,
                hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                control the bounds of the colorscale in color
                space, use`line.cmin` and `line.cmax`.
                Alternatively, `colorscale` may be a palette
                name string of the following list: Greys,YlGnBu
                ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,R
                ainbow,Portland,Jet,Hot,Blackbody,Earth,Electri
                c,Viridis,Cividis.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            dash
                Sets the dash style of the lines.
            reversescale
                Reverses the color mapping if true. Has an
                effect only if in `line.color`is set to a
                numerical array. If true, `line.cmin` will
                correspond to the last color in the array and
                `line.cmax` will correspond to the first color.
            width
                Sets the line width (in px).
""",
            **kwargs
        )
