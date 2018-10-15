import _plotly_utils.basevalidators


class ScattergeoValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='scattergeo', parent_name='', **kwargs):
        super(ScattergeoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Scattergeo'),
            data_docs=kwargs.pop(
                'data_docs', """
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". "toself"
                connects the endpoints of the trace (or each
                segment of the trace if it has gaps) into a
                closed shape.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            geo
                Sets a reference between this trace's
                geospatial coordinates and a geographic map. If
                "geo" (the default value), the geospatial
                coordinates refer to `layout.geo`. If "geo2",
                the geospatial coordinates refer to
                `layout.geo2`, and so on.
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
                plotly.graph_objs.scattergeo.Hoverlabel
                instance or dict with compatible properties
            hovertext
                Sets hover text elements associated with each
                (lon,lat) pair or item in `locations`. If a
                single string, the same string appears over all
                the data points. If an array of string, the
                items are mapped in order to the this trace's
                (lon,lat) or `locations` coordinates. To be
                seen, trace `hoverinfo` must contain a "text"
                flag.
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
            lat
                Sets the latitude coordinates (in degrees
                North).
            latsrc
                Sets the source reference on plot.ly for  lat .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                plotly.graph_objs.scattergeo.Line instance or
                dict with compatible properties
            locationmode
                Determines the set of locations used to match
                entries in `locations` to regions on the map.
            locations
                Sets the coordinates via location IDs or names.
                Coordinates correspond to the centroid of each
                location given. See `locationmode` for more
                info.
            locationssrc
                Sets the source reference on plot.ly for
                locations .
            lon
                Sets the longitude coordinates (in degrees
                East).
            lonsrc
                Sets the source reference on plot.ly for  lon .
            marker
                plotly.graph_objs.scattergeo.Marker instance or
                dict with compatible properties
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                plotly.graph_objs.scattergeo.Selected instance
                or dict with compatible properties
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
                plotly.graph_objs.scattergeo.Stream instance or
                dict with compatible properties
            text
                Sets text elements associated with each
                (lon,lat) pair or item in `locations`. If a
                single string, the same string appears over all
                the data points. If an array of string, the
                items are mapped in order to the this trace's
                (lon,lat) or `locations` coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            uid

            unselected
                plotly.graph_objs.scattergeo.Unselected
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
"""
            ),
            **kwargs
        )
