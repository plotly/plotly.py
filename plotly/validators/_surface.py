import _plotly_utils.basevalidators


class SurfaceValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='surface', parent_name='', **kwargs):
        super(SurfaceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Surface',
            data_docs="""
            autocolorscale
                Determines whether or not the colorscale is
                picked using the sign of the input z values.
            cauto
                Determines the whether or not the color domain
                is computed with respect to the input data.
            cmax
                Sets the upper bound of color domain.
            cmin
                Sets the lower bound of color domain.
            colorbar
                plotly.graph_objs.surface.ColorBar instance or
                dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)', [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in z space, use zmin and zmax
            contours
                plotly.graph_objs.surface.Contours instance or
                dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, *scatter* traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hidesurface
                Determines whether or not a surface is drawn.
                For example, set `hidesurface` to *false*
                `contours.x.show` to *true* and
                `contours.y.show` to *true* to draw a wire
                frame plot.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                plotly.graph_objs.surface.Hoverlabel instance
                or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                plotly.graph_objs.surface.Lighting instance or
                dict with compatible properties
            lightposition
                plotly.graph_objs.surface.Lightposition
                instance or dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface.
            reversescale
                Reverses the colorscale.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If *scene*
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If *scene2*, the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                plotly.graph_objs.surface.Stream instance or
                dict with compatible properties
            surfacecolor
                Sets the surface color values, used for setting
                a color scale independent of `z`.
            surfacecolorsrc
                Sets the source reference on plot.ly for
                surfacecolor .
            text
                Sets the text elements associated with each z
                value. If trace `hoverinfo` contains a *text*
                flag and *hovertext* is not set, these elements
                will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            uid

            visible
                Determines whether or not this trace is
                visible. If *legendonly*, the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the x coordinates.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates.
            zcalendar
                Sets the calendar system to use with `z` date
                data.
            zsrc
                Sets the source reference on plot.ly for  z .""",
            **kwargs
        )
