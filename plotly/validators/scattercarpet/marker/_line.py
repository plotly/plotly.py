import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='line', parent_name='scattercarpet.marker', **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Line',
            data_docs="""
            autocolorscale
                Has an effect only if `color` is set to a
                numerical array. Determines whether the
                colorscale is a default palette
                (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Has an effect only if `color` is set to a
                numerical array and `cmin`, `cmax` are set by
                the user. In this case, it controls whether the
                range of colors in `colorscale` is mapped to
                the range of values in the `color` array
                (`cauto: true`), or the `cmin`/`cmax` values
                (`cauto: false`). Defaults to `false` when
                `cmin`, `cmax` are set by the user.
            cmax
                Has an effect only if `color` is set to a
                numerical array. Sets the upper bound of the
                color domain. Value should be associated to the
                `color` array index, and if set, `cmin` must be
                set as well.
            cmin
                Has an effect only if `color` is set to a
                numerical array. Sets the lower bound of the
                color domain. Value should be associated to the
                `color` array index, and if set, `cmax` must be
                set as well.
            color
                Sets the  color. It accepts either a specific
                color or an array of numbers that are mapped to
                the colorscale relative to the max and min
                values of the array or relative to `cmin` and
                `cmax` if set.
            colorscale
                Sets the colorscale and only has an effect if
                `color` is set to a numerical array. The
                colorscale must be an array containing arrays
                mapping a normalized value to an rgb, rgba,
                hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                control the bounds of the colorscale in color
                space, use `cmin` and `cmax`. Alternatively,
                `colorscale` may be a palette name string of
                the following list: Greys, YlGnBu, Greens,
                YlOrRd, Bluered, RdBu, Reds, Blues, Picnic,
                Rainbow, Portland, Jet, Hot, Blackbody, Earth,
                Electric, Viridis, Cividis
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            reversescale
                Has an effect only if `color` is set to a
                numerical array. Reverses the color mapping if
                true (`cmin` will correspond to the last color
                in the array and `cmax` will correspond to the
                first color).
            width
                Sets the width (in px) of the lines bounding
                the marker points.
            widthsrc
                Sets the source reference on plot.ly for  width
                .""",
            **kwargs
        )
