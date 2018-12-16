import _plotly_utils.basevalidators


class BarValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='bar', parent_name='', **kwargs):
        super(BarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Bar'),
            data_docs=kwargs.pop(
                'data_docs', """
            base
                Sets where the bar base is drawn (in position
                axis units). In "stack" or "relative" barmode,
                traces that set "base" will be excluded and
                drawn in "overlay" mode instead.
            basesrc
                Sets the source reference on plot.ly for  base
                .
            cliponaxis
                Determines whether the text nodes are clipped
                about the subplot axes. To show the text nodes
                above axis lines and tick labels, make sure to
                set `xaxis.layer` and `yaxis.layer` to *below
                traces*.
            constraintext
                Constrain the size of text inside or outside a
                bar to be no larger than the bar itself.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            error_x
                plotly.graph_objs.bar.ErrorX instance or dict
                with compatible properties
            error_y
                plotly.graph_objs.bar.ErrorY instance or dict
                with compatible properties
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
                plotly.graph_objs.bar.Hoverlabel instance or
                dict with compatible properties
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextfont
                Sets the font used for `text` lying inside the
                bar.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                plotly.graph_objs.bar.Marker instance or dict
                with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            offset
                Shifts the position where the bar is drawn (in
                position axis units). In "group" barmode,
                traces that set "offset" will be excluded and
                drawn in "overlay" mode instead.
            offsetsrc
                Sets the source reference on plot.ly for
                offset .
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the bars. With "v"
                ("h"), the value of the each bar spans along
                the vertical (horizontal).
            outsidetextfont
                Sets the font used for `text` lying outside the
                bar.
            r
                r coordinates in scatter traces are
                deprecated!Please switch to the "scatterpolar"
                trace type.Sets the radial coordinatesfor
                legacy polar chart only.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                plotly.graph_objs.bar.Selected instance or dict
                with compatible properties
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
            stream
                plotly.graph_objs.bar.Stream instance or dict
                with compatible properties
            t
                t coordinates in scatter traces are
                deprecated!Please switch to the "scatterpolar"
                trace type.Sets the angular coordinatesfor
                legacy polar chart only.
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the font used for `text`.
            textposition
                Specifies the location of the `text`. "inside"
                positions `text` inside, next to the bar end
                (rotated and scaled if needed). "outside"
                positions `text` outside, next to the bar end
                (scaled if needed), unless there is another bar
                stacked on this one, then the text gets pushed
                inside. "auto" tries to position `text` inside
                the bar, but if the bar is too small and no bar
                is stacked on this one the text is moved
                outside.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            tsrc
                Sets the source reference on plot.ly for  t .
            uid

            unselected
                plotly.graph_objs.bar.Unselected instance or
                dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            width
                Sets the bar width (in position axis units).
            widthsrc
                Sets the source reference on plot.ly for  width
                .
            x
                Sets the x coordinates.
            x0
                Alternate to `x`. Builds a linear space of x
                coordinates. Use with `dx` where `x0` is the
                starting coordinate and `dx` the step.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates.
            y0
                Alternate to `y`. Builds a linear space of y
                coordinates. Use with `dy` where `y0` is the
                starting coordinate and `dy` the step.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
"""
            ),
            **kwargs
        )
