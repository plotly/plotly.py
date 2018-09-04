import _plotly_utils.basevalidators


class StreamtubeValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='streamtube', parent_name='', **kwargs):
        super(StreamtubeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Streamtube',
            data_docs="""
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                u/v/w norm) or the bounds set in `cmin` and
                `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmin` must be set as well.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmax` must be set as well.
            colorbar
                plotly.graph_objs.streamtube.ColorBar instance
                or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)', [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
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
                plotly.graph_objs.streamtube.Hoverlabel
                instance or dict with compatible properties
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
                plotly.graph_objs.streamtube.Lighting instance
                or dict with compatible properties
            lightposition
                plotly.graph_objs.streamtube.Lightposition
                instance or dict with compatible properties
            maxdisplayed
                The maximum number of displayed segments in a
                streamtube.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
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
            sizeref
                The scaling factor for the streamtubes. The
                default is 1, which avoids two max divergence
                tubes from touching at adjacent starting
                positions.
            starts
                plotly.graph_objs.streamtube.Starts instance or
                dict with compatible properties
            stream
                plotly.graph_objs.streamtube.Stream instance or
                dict with compatible properties
            text
                Sets a text element associated with this trace.
                If trace `hoverinfo` contains a "text" flag,
                this text element will be seen in all hover
                labels. Note that streamtube traces do not
                support array `text` values.
            u
                Sets the x components of the vector field.
            uid

            usrc
                Sets the source reference on plot.ly for  u .
            v
                Sets the y components of the vector field.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            vsrc
                Sets the source reference on plot.ly for  v .
            w
                Sets the z components of the vector field.
            wsrc
                Sets the source reference on plot.ly for  w .
            x
                Sets the x coordinates of the vector field.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates of the vector field.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates of the vector field.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            **kwargs
        )
