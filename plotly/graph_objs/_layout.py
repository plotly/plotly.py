from plotly.basedatatypes import BaseLayoutType
import copy


class Layout(BaseLayoutType):

    # angularaxis
    # -----------
    @property
    def angularaxis(self):
        """
        The 'angularaxis' property is an instance of AngularAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.AngularAxis
          - A dict of string/value properties that will be passed
            to the AngularAxis constructor
    
            Supported dict properties:
                
                domain
                    Polar chart subplots are not supported yet.
                    This key has currently no effect.
                endpadding
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots.
                range
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Defines the start
                    and end point of this angular axis.
                showline
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Determines whether
                    or not the line bounding this angular axis will
                    be shown on the figure.
                showticklabels
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Determines whether
                    or not the angular axis ticks will feature tick
                    labels.
                tickcolor
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the color of
                    the tick lines on this angular axis.
                ticklen
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the length of
                    the tick lines on this angular axis.
                tickorientation
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the
                    orientation (from the paper perspective) of the
                    angular axis tick labels.
                ticksuffix
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the length of
                    the tick lines on this angular axis.
                visible
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Determines whether
                    or not this axis will be visible.

        Returns
        -------
        plotly.graph_objs.layout.AngularAxis
        """
        return self['angularaxis']

    @angularaxis.setter
    def angularaxis(self, val):
        self['angularaxis'] = val

    # annotations
    # -----------
    @property
    def annotations(self):
        """
        The 'annotations' property is a tuple of instances of
        Annotation that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.Annotation
          - A list or tuple of dicts of string/value properties that
            will be passed to the Annotation constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the `text`
                    within the box. Has an effect only if `text`
                    spans more two or more lines (i.e. `text`
                    contains one or more <br> HTML tags) or if an
                    explicit width is set to override the text
                    width.
                arrowcolor
                    Sets the color of the annotation arrow.
                arrowhead
                    Sets the end annotation arrow head style.
                arrowside
                    Sets the annotation arrow head position.
                arrowsize
                    Sets the size of the end annotation arrow head,
                    relative to `arrowwidth`. A value of 1
                    (default) gives a head about 3x as wide as the
                    line.
                arrowwidth
                    Sets the width (in px) of annotation arrow
                    line.
                ax
                    Sets the x component of the arrow tail about
                    the arrow head. If `axref` is `pixel`, a
                    positive (negative)  component corresponds to
                    an arrow pointing from right to left (left to
                    right). If `axref` is an axis, this is an
                    absolute value on that axis, like `x`, NOT a
                    relative value.
                axref
                    Indicates in what terms the tail of the
                    annotation (ax,ay)  is specified. If `pixel`,
                    `ax` is a relative offset in pixels  from `x`.
                    If set to an x axis id (e.g. "x" or "x2"), `ax`
                    is  specified in the same terms as that axis.
                    This is useful  for trendline annotations which
                    should continue to indicate  the correct trend
                    when zoomed.
                ay
                    Sets the y component of the arrow tail about
                    the arrow head. If `ayref` is `pixel`, a
                    positive (negative)  component corresponds to
                    an arrow pointing from bottom to top (top to
                    bottom). If `ayref` is an axis, this is an
                    absolute value on that axis, like `y`, NOT a
                    relative value.
                ayref
                    Indicates in what terms the tail of the
                    annotation (ax,ay)  is specified. If `pixel`,
                    `ay` is a relative offset in pixels  from `y`.
                    If set to a y axis id (e.g. "y" or "y2"), `ay`
                    is  specified in the same terms as that axis.
                    This is useful  for trendline annotations which
                    should continue to indicate  the correct trend
                    when zoomed.
                bgcolor
                    Sets the background color of the annotation.
                bordercolor
                    Sets the color of the border enclosing the
                    annotation `text`.
                borderpad
                    Sets the padding (in px) between the `text` and
                    the enclosing border.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the annotation `text`.
                captureevents
                    Determines whether the annotation text box
                    captures mouse move and click events, or allows
                    those events to pass through to data points in
                    the plot that may be behind the annotation. By
                    default `captureevents` is False unless
                    `hovertext` is provided. If you use the event
                    `plotly_clickannotation` without `hovertext`
                    you must explicitly enable `captureevents`.
                clicktoshow
                    Makes this annotation respond to clicks on the
                    plot. If you click a data point that exactly
                    matches the `x` and `y` values of this
                    annotation, and it is hidden (visible: false),
                    it will appear. In "onoff" mode, you must click
                    the same point again to make it disappear, so
                    if you click multiple points, you can show
                    multiple annotations. In "onout" mode, a click
                    anywhere else in the plot (on another data
                    point or not) will hide this annotation. If you
                    need to show/hide this annotation in response
                    to different `x` or `y` values, you can set
                    `xclick` and/or `yclick`. This is useful for
                    example to label the side of a bar. To label
                    markers though, `standoff` is preferred over
                    `xclick` and `yclick`.
                font
                    Sets the annotation text font.
                height
                    Sets an explicit height for the text box. null
                    (default) lets the text set the box height.
                    Taller text will be clipped.
                hoverlabel
                    plotly.graph_objs.layout.annotation.Hoverlabel
                    instance or dict with compatible properties
                hovertext
                    Sets text to appear when hovering over this
                    annotation. If omitted or blank, no hover label
                    will appear.
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                opacity
                    Sets the opacity of the annotation (text +
                    arrow).
                showarrow
                    Determines whether or not the annotation is
                    drawn with an arrow. If True, `text` is placed
                    near the arrow's tail. If False, `text` lines
                    up with the `x` and `y` provided.
                standoff
                    Sets a distance, in pixels, to move the end
                    arrowhead away from the position it is pointing
                    at, for example to point at the edge of a
                    marker independent of zoom. Note that this
                    shortens the arrow from the `ax` / `ay` vector,
                    in contrast to `xshift` / `yshift` which moves
                    everything by this amount.
                startarrowhead
                    Sets the start annotation arrow head style.
                startarrowsize
                    Sets the size of the start annotation arrow
                    head, relative to `arrowwidth`. A value of 1
                    (default) gives a head about 3x as wide as the
                    line.
                startstandoff
                    Sets a distance, in pixels, to move the start
                    arrowhead away from the position it is pointing
                    at, for example to point at the edge of a
                    marker independent of zoom. Note that this
                    shortens the arrow from the `ax` / `ay` vector,
                    in contrast to `xshift` / `yshift` which moves
                    everything by this amount.
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
                text
                    Sets the text associated with this annotation.
                    Plotly uses a subset of HTML tags to do things
                    like newline (<br>), bold (<b></b>), italics
                    (<i></i>), hyperlinks (<a href='...'></a>).
                    Tags <em>, <sup>, <sub> <span> are also
                    supported.
                textangle
                    Sets the angle at which the `text` is drawn
                    with respect to the horizontal.
                valign
                    Sets the vertical alignment of the `text`
                    within the box. Has an effect only if an
                    explicit height is set to override the text
                    height.
                visible
                    Determines whether or not this annotation is
                    visible.
                width
                    Sets an explicit width for the text box. null
                    (default) lets the text set the box width.
                    Wider text will be clipped. There is no
                    automatic wrapping; use <br> to start a new
                    line.
                x
                    Sets the annotation's x position. If the axis
                    `type` is "log", then you must take the log of
                    your desired range. If the axis `type` is
                    "date", it should be date strings, like date
                    data, though Date objects and unix milliseconds
                    will be accepted and converted to strings. If
                    the axis `type` is "category", it should be
                    numbers, using the scale where each category is
                    assigned a serial number from zero in the order
                    it appears.
                xanchor
                    Sets the text box's horizontal position anchor
                    This anchor binds the `x` position to the
                    "left", "center" or "right" of the annotation.
                    For example, if `x` is set to 1, `xref` to
                    "paper" and `xanchor` to "right" then the
                    right-most portion of the annotation lines up
                    with the right-most edge of the plotting area.
                    If "auto", the anchor is equivalent to "center"
                    for data-referenced annotations or if there is
                    an arrow, whereas for paper-referenced with no
                    arrow, the anchor picked corresponds to the
                    closest side.
                xclick
                    Toggle this annotation when clicking a data
                    point whose `x` value is `xclick` rather than
                    the annotation's `x` value.
                xref
                    Sets the annotation's x coordinate axis. If set
                    to an x axis id (e.g. "x" or "x2"), the `x`
                    position refers to an x coordinate If set to
                    "paper", the `x` position refers to the
                    distance from the left side of the plotting
                    area in normalized coordinates where 0 (1)
                    corresponds to the left (right) side.
                xshift
                    Shifts the position of the whole annotation and
                    arrow to the right (positive) or left
                    (negative) by this many pixels.
                y
                    Sets the annotation's y position. If the axis
                    `type` is "log", then you must take the log of
                    your desired range. If the axis `type` is
                    "date", it should be date strings, like date
                    data, though Date objects and unix milliseconds
                    will be accepted and converted to strings. If
                    the axis `type` is "category", it should be
                    numbers, using the scale where each category is
                    assigned a serial number from zero in the order
                    it appears.
                yanchor
                    Sets the text box's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the annotation.
                    For example, if `y` is set to 1, `yref` to
                    "paper" and `yanchor` to "top" then the top-
                    most portion of the annotation lines up with
                    the top-most edge of the plotting area. If
                    "auto", the anchor is equivalent to "middle"
                    for data-referenced annotations or if there is
                    an arrow, whereas for paper-referenced with no
                    arrow, the anchor picked corresponds to the
                    closest side.
                yclick
                    Toggle this annotation when clicking a data
                    point whose `y` value is `yclick` rather than
                    the annotation's `y` value.
                yref
                    Sets the annotation's y coordinate axis. If set
                    to an y axis id (e.g. "y" or "y2"), the `y`
                    position refers to an y coordinate If set to
                    "paper", the `y` position refers to the
                    distance from the bottom of the plotting area
                    in normalized coordinates where 0 (1)
                    corresponds to the bottom (top).
                yshift
                    Shifts the position of the whole annotation and
                    arrow up (positive) or down (negative) by this
                    many pixels.

        Returns
        -------
        tuple[plotly.graph_objs.layout.Annotation]
        """
        return self['annotations']

    @annotations.setter
    def annotations(self, val):
        self['annotations'] = val

    # annotationdefaults
    # ------------------
    @property
    def annotationdefaults(self):
        """
        When used in a template (as
        layout.template.layout.annotationdefaults), sets the default
        property values to use for elements of layout.annotations
    
        The 'annotationdefaults' property is an instance of Annotation
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Annotation
          - A dict of string/value properties that will be passed
            to the Annotation constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.Annotation
        """
        return self['annotationdefaults']

    @annotationdefaults.setter
    def annotationdefaults(self, val):
        self['annotationdefaults'] = val

    # autosize
    # --------
    @property
    def autosize(self):
        """
        Determines whether or not a layout width or height that has
        been left undefined by the user is initialized on each
        relayout. Note that, regardless of this attribute, an undefined
        layout width or height is always initialized on the first call
        to plot.
    
        The 'autosize' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autosize']

    @autosize.setter
    def autosize(self, val):
        self['autosize'] = val

    # bargap
    # ------
    @property
    def bargap(self):
        """
        Sets the gap (in plot fraction) between bars of adjacent
        location coordinates.
    
        The 'bargap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['bargap']

    @bargap.setter
    def bargap(self, val):
        self['bargap'] = val

    # bargroupgap
    # -----------
    @property
    def bargroupgap(self):
        """
        Sets the gap (in plot fraction) between bars of the same
        location coordinate.
    
        The 'bargroupgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['bargroupgap']

    @bargroupgap.setter
    def bargroupgap(self, val):
        self['bargroupgap'] = val

    # barmode
    # -------
    @property
    def barmode(self):
        """
        Determines how bars at the same location coordinate are
        displayed on the graph. With "stack", the bars are stacked on
        top of one another With "relative", the bars are stacked on top
        of one another, with negative values below the axis, positive
        values above With "group", the bars are plotted next to one
        another centered around the shared location. With "overlay",
        the bars are plotted over one another, you might need to an
        "opacity" to see multiple bars.
    
        The 'barmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['stack', 'group', 'overlay', 'relative']

        Returns
        -------
        Any
        """
        return self['barmode']

    @barmode.setter
    def barmode(self, val):
        self['barmode'] = val

    # barnorm
    # -------
    @property
    def barnorm(self):
        """
        Sets the normalization for bar traces on the graph. With
        "fraction", the value of each bar is divided by the sum of all
        values at that location coordinate. "percent" is the same but
        multiplied by 100 to show percentages.
    
        The 'barnorm' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['', 'fraction', 'percent']

        Returns
        -------
        Any
        """
        return self['barnorm']

    @barnorm.setter
    def barnorm(self, val):
        self['barnorm'] = val

    # boxgap
    # ------
    @property
    def boxgap(self):
        """
        Sets the gap (in plot fraction) between boxes of adjacent
        location coordinates.
    
        The 'boxgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['boxgap']

    @boxgap.setter
    def boxgap(self, val):
        self['boxgap'] = val

    # boxgroupgap
    # -----------
    @property
    def boxgroupgap(self):
        """
        Sets the gap (in plot fraction) between boxes of the same
        location coordinate.
    
        The 'boxgroupgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['boxgroupgap']

    @boxgroupgap.setter
    def boxgroupgap(self, val):
        self['boxgroupgap'] = val

    # boxmode
    # -------
    @property
    def boxmode(self):
        """
        Determines how boxes at the same location coordinate are
        displayed on the graph. If "group", the boxes are plotted next
        to one another centered around the shared location. If
        "overlay", the boxes are plotted over one another, you might
        need to set "opacity" to see them multiple boxes.
    
        The 'boxmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['group', 'overlay']

        Returns
        -------
        Any
        """
        return self['boxmode']

    @boxmode.setter
    def boxmode(self, val):
        self['boxmode'] = val

    # calendar
    # --------
    @property
    def calendar(self):
        """
        Sets the default calendar system to use for interpreting and
        displaying dates throughout the plot.
    
        The 'calendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['calendar']

    @calendar.setter
    def calendar(self, val):
        self['calendar'] = val

    # clickmode
    # ---------
    @property
    def clickmode(self):
        """
        Determines the mode of single click interactions. "event" is
        the default value and emits the `plotly_click` event. In
        addition this mode emits the `plotly_selected` event in drag
        modes "lasso" and "select", but with no event data attached
        (kept for compatibility reasons). The "select" flag enables
        selecting single data points via click. This mode also supports
        persistent selections, meaning that pressing Shift while
        clicking, adds to / subtracts from an existing selection.
        "select" with `hovermode`: "x" can be confusing, consider
        explicitly setting `hovermode`: "closest" when using this
        feature. Selection events are sent accordingly as long as
        "event" flag is set as well. When the "event" flag is missing,
        `plotly_click` and `plotly_selected` events are not fired.
    
        The 'clickmode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['event', 'select'] joined with '+' characters
            (e.g. 'event+select')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self['clickmode']

    @clickmode.setter
    def clickmode(self, val):
        self['clickmode'] = val

    # colorway
    # --------
    @property
    def colorway(self):
        """
        Sets the default trace colors.
    
        The 'colorway' property is a colorlist that may be specified
        as a tuple, list, one-dimensional numpy array, or pandas Series of valid
        color strings

        Returns
        -------
        list
        """
        return self['colorway']

    @colorway.setter
    def colorway(self, val):
        self['colorway'] = val

    # datarevision
    # ------------
    @property
    def datarevision(self):
        """
        If provided, a changed value tells `Plotly.react` that one or
        more data arrays has changed. This way you can modify arrays
        in-place rather than making a complete new copy for an
        incremental change. If NOT provided, `Plotly.react` assumes
        that data arrays are being treated as immutable, thus any data
        array with a different identity from its predecessor contains
        new data.
    
        The 'datarevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['datarevision']

    @datarevision.setter
    def datarevision(self, val):
        self['datarevision'] = val

    # direction
    # ---------
    @property
    def direction(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the direction corresponding to positive angles
        in legacy polar charts.
    
        The 'direction' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['clockwise', 'counterclockwise']

        Returns
        -------
        Any
        """
        return self['direction']

    @direction.setter
    def direction(self, val):
        self['direction'] = val

    # dragmode
    # --------
    @property
    def dragmode(self):
        """
        Determines the mode of drag interactions. "select" and "lasso"
        apply only to scatter traces with markers or text. "orbit" and
        "turntable" apply only to 3D scenes.
    
        The 'dragmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['zoom', 'pan', 'select', 'lasso', 'orbit', 'turntable']

        Returns
        -------
        Any
        """
        return self['dragmode']

    @dragmode.setter
    def dragmode(self, val):
        self['dragmode'] = val

    # extendpiecolors
    # ---------------
    @property
    def extendpiecolors(self):
        """
        If `true`, the pie slice colors (whether given by `piecolorway`
        or inherited from `colorway`) will be extended to three times
        its original length by first repeating every color 20% lighter
        then each color 20% darker. This is intended to reduce the
        likelihood of reusing the same color when you have many slices,
        but you can set `false` to disable. Colors provided in the
        trace, using `marker.colors`, are never extended.
    
        The 'extendpiecolors' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['extendpiecolors']

    @extendpiecolors.setter
    def extendpiecolors(self, val):
        self['extendpiecolors'] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the global font. Note that fonts used in traces and other
        layout components inherit from the global font.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # geo
    # ---
    @property
    def geo(self):
        """
        The 'geo' property is an instance of Geo
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Geo
          - A dict of string/value properties that will be passed
            to the Geo constructor
    
            Supported dict properties:
                
                bgcolor
                    Set the background color of the map
                center
                    plotly.graph_objs.layout.geo.Center instance or
                    dict with compatible properties
                coastlinecolor
                    Sets the coastline color.
                coastlinewidth
                    Sets the coastline stroke width (in px).
                countrycolor
                    Sets line color of the country boundaries.
                countrywidth
                    Sets line width (in px) of the country
                    boundaries.
                domain
                    plotly.graph_objs.layout.geo.Domain instance or
                    dict with compatible properties
                framecolor
                    Sets the color the frame.
                framewidth
                    Sets the stroke width (in px) of the frame.
                lakecolor
                    Sets the color of the lakes.
                landcolor
                    Sets the land mass color.
                lataxis
                    plotly.graph_objs.layout.geo.Lataxis instance
                    or dict with compatible properties
                lonaxis
                    plotly.graph_objs.layout.geo.Lonaxis instance
                    or dict with compatible properties
                oceancolor
                    Sets the ocean color
                projection
                    plotly.graph_objs.layout.geo.Projection
                    instance or dict with compatible properties
                resolution
                    Sets the resolution of the base layers. The
                    values have units of km/mm e.g. 110 corresponds
                    to a scale ratio of 1:110,000,000.
                rivercolor
                    Sets color of the rivers.
                riverwidth
                    Sets the stroke width (in px) of the rivers.
                scope
                    Set the scope of the map.
                showcoastlines
                    Sets whether or not the coastlines are drawn.
                showcountries
                    Sets whether or not country boundaries are
                    drawn.
                showframe
                    Sets whether or not a frame is drawn around the
                    map.
                showlakes
                    Sets whether or not lakes are drawn.
                showland
                    Sets whether or not land masses are filled in
                    color.
                showocean
                    Sets whether or not oceans are filled in color.
                showrivers
                    Sets whether or not rivers are drawn.
                showsubunits
                    Sets whether or not boundaries of subunits
                    within countries (e.g. states, provinces) are
                    drawn.
                subunitcolor
                    Sets the color of the subunits boundaries.
                subunitwidth
                    Sets the stroke width (in px) of the subunits
                    boundaries.

        Returns
        -------
        plotly.graph_objs.layout.Geo
        """
        return self['geo']

    @geo.setter
    def geo(self, val):
        self['geo'] = val

    # grid
    # ----
    @property
    def grid(self):
        """
        The 'grid' property is an instance of Grid
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Grid
          - A dict of string/value properties that will be passed
            to the Grid constructor
    
            Supported dict properties:
                
                columns
                    The number of columns in the grid. If you
                    provide a 2D `subplots` array, the length of
                    its longest row is used as the default. If you
                    give an `xaxes` array, its length is used as
                    the default. But it's also possible to have a
                    different length, if you want to leave a row at
                    the end for non-cartesian subplots.
                domain
                    plotly.graph_objs.layout.grid.Domain instance
                    or dict with compatible properties
                pattern
                    If no `subplots`, `xaxes`, or `yaxes` are given
                    but we do have `rows` and `columns`, we can
                    generate defaults using consecutive axis IDs,
                    in two ways: "coupled" gives one x axis per
                    column and one y axis per row. "independent"
                    uses a new xy pair for each cell, left-to-right
                    across each row then iterating rows according
                    to `roworder`.
                roworder
                    Is the first row the top or the bottom? Note
                    that columns are always enumerated from left to
                    right.
                rows
                    The number of rows in the grid. If you provide
                    a 2D `subplots` array or a `yaxes` array, its
                    length is used as the default. But it's also
                    possible to have a different length, if you
                    want to leave a row at the end for non-
                    cartesian subplots.
                subplots
                    Used for freeform grids, where some axes may be
                    shared across subplots but others are not. Each
                    entry should be a cartesian subplot id, like
                    "xy" or "x3y2", or "" to leave that cell empty.
                    You may reuse x axes within the same column,
                    and y axes within the same row. Non-cartesian
                    subplots and traces that support `domain` can
                    place themselves in this grid separately using
                    the `gridcell` attribute.
                xaxes
                    Used with `yaxes` when the x and y axes are
                    shared across columns and rows. Each entry
                    should be an x axis id like "x", "x2", etc., or
                    "" to not put an x axis in that column. Entries
                    other than "" must be unique. Ignored if
                    `subplots` is present. If missing but `yaxes`
                    is present, will generate consecutive IDs.
                xgap
                    Horizontal space between grid cells, expressed
                    as a fraction of the total width available to
                    one cell. Defaults to 0.1 for coupled-axes
                    grids and 0.2 for independent grids.
                xside
                    Sets where the x axis labels and titles go.
                    "bottom" means the very bottom of the grid.
                    "bottom plot" is the lowest plot that each x
                    axis is used in. "top" and "top plot" are
                    similar.
                yaxes
                    Used with `yaxes` when the x and y axes are
                    shared across columns and rows. Each entry
                    should be an y axis id like "y", "y2", etc., or
                    "" to not put a y axis in that row. Entries
                    other than "" must be unique. Ignored if
                    `subplots` is present. If missing but `xaxes`
                    is present, will generate consecutive IDs.
                ygap
                    Vertical space between grid cells, expressed as
                    a fraction of the total height available to one
                    cell. Defaults to 0.1 for coupled-axes grids
                    and 0.3 for independent grids.
                yside
                    Sets where the y axis labels and titles go.
                    "left" means the very left edge of the grid.
                    *left plot* is the leftmost plot that each y
                    axis is used in. "right" and *right plot* are
                    similar.

        Returns
        -------
        plotly.graph_objs.layout.Grid
        """
        return self['grid']

    @grid.setter
    def grid(self, val):
        self['grid'] = val

    # height
    # ------
    @property
    def height(self):
        """
        Sets the plot's height (in px).
    
        The 'height' property is a number and may be specified as:
          - An int or float in the interval [10, inf]

        Returns
        -------
        int|float
        """
        return self['height']

    @height.setter
    def height(self, val):
        self['height'] = val

    # hiddenlabels
    # ------------
    @property
    def hiddenlabels(self):
        """
        The 'hiddenlabels' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['hiddenlabels']

    @hiddenlabels.setter
    def hiddenlabels(self, val):
        self['hiddenlabels'] = val

    # hiddenlabelssrc
    # ---------------
    @property
    def hiddenlabelssrc(self):
        """
        Sets the source reference on plot.ly for  hiddenlabels .
    
        The 'hiddenlabelssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hiddenlabelssrc']

    @hiddenlabelssrc.setter
    def hiddenlabelssrc(self, val):
        self['hiddenlabelssrc'] = val

    # hidesources
    # -----------
    @property
    def hidesources(self):
        """
        Determines whether or not a text link citing the data source is
        placed at the bottom-right cored of the figure. Has only an
        effect only on graphs that have been generated via forked
        graphs from the plotly service (at https://plot.ly or on-
        premise).
    
        The 'hidesources' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['hidesources']

    @hidesources.setter
    def hidesources(self, val):
        self['hidesources'] = val

    # hoverdistance
    # -------------
    @property
    def hoverdistance(self):
        """
        Sets the default distance (in pixels) to look for data to add
        hover labels (-1 means no cutoff, 0 means no looking for data).
        This is only a real distance for hovering on point-like
        objects, like scatter points. For area-like objects (bars,
        scatter fills, etc) hovering is on inside the area and off
        outside, but these objects will not supersede hover on point-
        like objects in case of conflict.
    
        The 'hoverdistance' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['hoverdistance']

    @hoverdistance.setter
    def hoverdistance(self, val):
        self['hoverdistance'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the background color of all hover labels
                    on graph
                bordercolor
                    Sets the border color of all hover labels on
                    graph.
                font
                    Sets the default hover label font used by all
                    traces on the graph.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.

        Returns
        -------
        plotly.graph_objs.layout.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # hovermode
    # ---------
    @property
    def hovermode(self):
        """
        Determines the mode of hover interactions. If `clickmode`
        includes the "select" flag, `hovermode` defaults to "closest".
        If `clickmode` lacks the "select" flag, it defaults to "x" or
        "y" (depending on the trace's `orientation` value) for plots
        based on cartesian coordinates. For anything else the default
        value is "closest".
    
        The 'hovermode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['x', 'y', 'closest', False]

        Returns
        -------
        Any
        """
        return self['hovermode']

    @hovermode.setter
    def hovermode(self, val):
        self['hovermode'] = val

    # images
    # ------
    @property
    def images(self):
        """
        The 'images' property is a tuple of instances of
        Image that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.Image
          - A list or tuple of dicts of string/value properties that
            will be passed to the Image constructor
    
            Supported dict properties:
                
                layer
                    Specifies whether images are drawn below or
                    above traces. When `xref` and `yref` are both
                    set to `paper`, image is drawn below the entire
                    plot area.
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
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
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
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
                    a x axis id (e.g. "x" or "x2"), the `x`
                    position refers to an x data coordinate If set
                    to "paper", the `x` position refers to the
                    distance from the left of plot in normalized
                    coordinates where 0 (1) corresponds to the left
                    (right).
                y
                    Sets the image's y position. When `yref` is set
                    to `paper`, units are sized relative to the
                    plot height. See `yref` for more info
                yanchor
                    Sets the anchor for the y position.
                yref
                    Sets the images's y coordinate axis. If set to
                    a y axis id (e.g. "y" or "y2"), the `y`
                    position refers to a y data coordinate. If set
                    to "paper", the `y` position refers to the
                    distance from the bottom of the plot in
                    normalized coordinates where 0 (1) corresponds
                    to the bottom (top).

        Returns
        -------
        tuple[plotly.graph_objs.layout.Image]
        """
        return self['images']

    @images.setter
    def images(self, val):
        self['images'] = val

    # imagedefaults
    # -------------
    @property
    def imagedefaults(self):
        """
        When used in a template (as
        layout.template.layout.imagedefaults), sets the default
        property values to use for elements of layout.images
    
        The 'imagedefaults' property is an instance of Image
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Image
          - A dict of string/value properties that will be passed
            to the Image constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.Image
        """
        return self['imagedefaults']

    @imagedefaults.setter
    def imagedefaults(self, val):
        self['imagedefaults'] = val

    # legend
    # ------
    @property
    def legend(self):
        """
        The 'legend' property is an instance of Legend
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Legend
          - A dict of string/value properties that will be passed
            to the Legend constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the legend background color.
                bordercolor
                    Sets the color of the border enclosing the
                    legend.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the legend.
                font
                    Sets the font used to text the legend items.
                orientation
                    Sets the orientation of the legend.
                tracegroupgap
                    Sets the amount of vertical space (in px)
                    between legend groups.
                traceorder
                    Determines the order at which the legend items
                    are displayed. If "normal", the items are
                    displayed top-to-bottom in the same order as
                    the input data. If "reversed", the items are
                    displayed in the opposite order as "normal". If
                    "grouped", the items are displayed in groups
                    (when a trace `legendgroup` is provided). if
                    "grouped+reversed", the items are displayed in
                    the opposite order as "grouped".
                x
                    Sets the x position (in normalized coordinates)
                    of the legend.
                xanchor
                    Sets the legend's horizontal position anchor.
                    This anchor binds the `x` position to the
                    "left", "center" or "right" of the legend.
                y
                    Sets the y position (in normalized coordinates)
                    of the legend.
                yanchor
                    Sets the legend's vertical position anchor This
                    anchor binds the `y` position to the "top",
                    "middle" or "bottom" of the legend.

        Returns
        -------
        plotly.graph_objs.layout.Legend
        """
        return self['legend']

    @legend.setter
    def legend(self, val):
        self['legend'] = val

    # mapbox
    # ------
    @property
    def mapbox(self):
        """
        The 'mapbox' property is an instance of Mapbox
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Mapbox
          - A dict of string/value properties that will be passed
            to the Mapbox constructor
    
            Supported dict properties:
                
                accesstoken
                    Sets the mapbox access token to be used for
                    this mapbox map. Alternatively, the mapbox
                    access token can be set in the configuration
                    options under `mapboxAccessToken`.
                bearing
                    Sets the bearing angle of the map (in degrees
                    counter-clockwise from North).
                center
                    plotly.graph_objs.layout.mapbox.Center instance
                    or dict with compatible properties
                domain
                    plotly.graph_objs.layout.mapbox.Domain instance
                    or dict with compatible properties
                layers
                    plotly.graph_objs.layout.mapbox.Layer instance
                    or dict with compatible properties
                layerdefaults
                    When used in a template (as
                    layout.template.layout.mapbox.layerdefaults),
                    sets the default property values to use for
                    elements of layout.mapbox.layers
                pitch
                    Sets the pitch angle of the map (in degrees,
                    where 0 means perpendicular to the surface of
                    the map).
                style
                    Sets the Mapbox map style. Either input one of
                    the default Mapbox style names or the URL to a
                    custom style or a valid Mapbox style JSON.
                zoom
                    Sets the zoom level of the map.

        Returns
        -------
        plotly.graph_objs.layout.Mapbox
        """
        return self['mapbox']

    @mapbox.setter
    def mapbox(self, val):
        self['mapbox'] = val

    # margin
    # ------
    @property
    def margin(self):
        """
        The 'margin' property is an instance of Margin
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Margin
          - A dict of string/value properties that will be passed
            to the Margin constructor
    
            Supported dict properties:
                
                autoexpand
    
                b
                    Sets the bottom margin (in px).
                l
                    Sets the left margin (in px).
                pad
                    Sets the amount of padding (in px) between the
                    plotting area and the axis lines
                r
                    Sets the right margin (in px).
                t
                    Sets the top margin (in px).

        Returns
        -------
        plotly.graph_objs.layout.Margin
        """
        return self['margin']

    @margin.setter
    def margin(self, val):
        self['margin'] = val

    # modebar
    # -------
    @property
    def modebar(self):
        """
        The 'modebar' property is an instance of Modebar
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Modebar
          - A dict of string/value properties that will be passed
            to the Modebar constructor
    
            Supported dict properties:
                
                activecolor
                    Sets the color of the active or hovered on
                    icons in the modebar.
                bgcolor
                    Sets the background color of the modebar.
                color
                    Sets the color of the icons in the modebar.
                orientation
                    Sets the orientation of the modebar.

        Returns
        -------
        plotly.graph_objs.layout.Modebar
        """
        return self['modebar']

    @modebar.setter
    def modebar(self, val):
        self['modebar'] = val

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Rotates the entire polar by the given angle in legacy
        polar charts.
    
        The 'orientation' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self['orientation']

    @orientation.setter
    def orientation(self, val):
        self['orientation'] = val

    # paper_bgcolor
    # -------------
    @property
    def paper_bgcolor(self):
        """
        Sets the color of paper where the graph is drawn.
    
        The 'paper_bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['paper_bgcolor']

    @paper_bgcolor.setter
    def paper_bgcolor(self, val):
        self['paper_bgcolor'] = val

    # piecolorway
    # -----------
    @property
    def piecolorway(self):
        """
        Sets the default pie slice colors. Defaults to the main
        `colorway` used for trace colors. If you specify a new list
        here it can still be extended with lighter and darker colors,
        see `extendpiecolors`.
    
        The 'piecolorway' property is a colorlist that may be specified
        as a tuple, list, one-dimensional numpy array, or pandas Series of valid
        color strings

        Returns
        -------
        list
        """
        return self['piecolorway']

    @piecolorway.setter
    def piecolorway(self, val):
        self['piecolorway'] = val

    # plot_bgcolor
    # ------------
    @property
    def plot_bgcolor(self):
        """
        Sets the color of plotting area in-between x and y axes.
    
        The 'plot_bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['plot_bgcolor']

    @plot_bgcolor.setter
    def plot_bgcolor(self, val):
        self['plot_bgcolor'] = val

    # polar
    # -----
    @property
    def polar(self):
        """
        The 'polar' property is an instance of Polar
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Polar
          - A dict of string/value properties that will be passed
            to the Polar constructor
    
            Supported dict properties:
                
                angularaxis
                    plotly.graph_objs.layout.polar.AngularAxis
                    instance or dict with compatible properties
                bargap
                    Sets the gap between bars of adjacent location
                    coordinates. Values are unitless, they
                    represent fractions of the minimum difference
                    in bar positions in the data.
                barmode
                    Determines how bars at the same location
                    coordinate are displayed on the graph. With
                    "stack", the bars are stacked on top of one
                    another With "overlay", the bars are plotted
                    over one another, you might need to an
                    "opacity" to see multiple bars.
                bgcolor
                    Set the background color of the subplot
                domain
                    plotly.graph_objs.layout.polar.Domain instance
                    or dict with compatible properties
                gridshape
                    Determines if the radial axis grid lines and
                    angular axis line are drawn as "circular"
                    sectors or as "linear" (polygon) sectors. Has
                    an effect only when the angular axis has `type`
                    "category". Note that `radialaxis.angle` is
                    snapped to the angle of the closest vertex when
                    `gridshape` is "circular" (so that radial axis
                    scale is the same as the data scale).
                hole
                    Sets the fraction of the radius to cut out of
                    the polar subplot.
                radialaxis
                    plotly.graph_objs.layout.polar.RadialAxis
                    instance or dict with compatible properties
                sector
                    Sets angular span of this polar subplot with
                    two angles (in degrees). Sector are assumed to
                    be spanned in the counterclockwise direction
                    with 0 corresponding to rightmost limit of the
                    polar subplot.

        Returns
        -------
        plotly.graph_objs.layout.Polar
        """
        return self['polar']

    @polar.setter
    def polar(self, val):
        self['polar'] = val

    # radialaxis
    # ----------
    @property
    def radialaxis(self):
        """
        The 'radialaxis' property is an instance of RadialAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.RadialAxis
          - A dict of string/value properties that will be passed
            to the RadialAxis constructor
    
            Supported dict properties:
                
                domain
                    Polar chart subplots are not supported yet.
                    This key has currently no effect.
                endpadding
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots.
                orientation
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the
                    orientation (an angle with respect to the
                    origin) of the radial axis.
                range
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Defines the start
                    and end point of this radial axis.
                showline
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Determines whether
                    or not the line bounding this radial axis will
                    be shown on the figure.
                showticklabels
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Determines whether
                    or not the radial axis ticks will feature tick
                    labels.
                tickcolor
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the color of
                    the tick lines on this radial axis.
                ticklen
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the length of
                    the tick lines on this radial axis.
                tickorientation
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the
                    orientation (from the paper perspective) of the
                    radial axis tick labels.
                ticksuffix
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Sets the length of
                    the tick lines on this radial axis.
                visible
                    Legacy polar charts are deprecated! Please
                    switch to "polar" subplots. Determines whether
                    or not this axis will be visible.

        Returns
        -------
        plotly.graph_objs.layout.RadialAxis
        """
        return self['radialaxis']

    @radialaxis.setter
    def radialaxis(self, val):
        self['radialaxis'] = val

    # scene
    # -----
    @property
    def scene(self):
        """
        The 'scene' property is an instance of Scene
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Scene
          - A dict of string/value properties that will be passed
            to the Scene constructor
    
            Supported dict properties:
                
                annotations
                    plotly.graph_objs.layout.scene.Annotation
                    instance or dict with compatible properties
                annotationdefaults
                    When used in a template (as layout.template.lay
                    out.scene.annotationdefaults), sets the default
                    property values to use for elements of
                    layout.scene.annotations
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

        Returns
        -------
        plotly.graph_objs.layout.Scene
        """
        return self['scene']

    @scene.setter
    def scene(self, val):
        self['scene'] = val

    # selectdirection
    # ---------------
    @property
    def selectdirection(self):
        """
        When "dragmode" is set to "select", this limits the selection
        of the drag to horizontal, vertical or diagonal. "h" only
        allows horizontal selection, "v" only vertical, "d" only
        diagonal and "any" sets no limit.
    
        The 'selectdirection' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['h', 'v', 'd', 'any']

        Returns
        -------
        Any
        """
        return self['selectdirection']

    @selectdirection.setter
    def selectdirection(self, val):
        self['selectdirection'] = val

    # separators
    # ----------
    @property
    def separators(self):
        """
        Sets the decimal and thousand separators. For example, *. *
        puts a '.' before decimals and a space between thousands. In
        English locales, dflt is ".," but other locales may alter this
        default.
    
        The 'separators' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['separators']

    @separators.setter
    def separators(self, val):
        self['separators'] = val

    # shapes
    # ------
    @property
    def shapes(self):
        """
        The 'shapes' property is a tuple of instances of
        Shape that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.Shape
          - A list or tuple of dicts of string/value properties that
            will be passed to the Shape constructor
    
            Supported dict properties:
                
                fillcolor
                    Sets the color filling the shape's interior.
                layer
                    Specifies whether shapes are drawn below or
                    above traces.
                line
                    plotly.graph_objs.layout.shape.Line instance or
                    dict with compatible properties
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                opacity
                    Sets the opacity of the shape.
                path
                    For `type` "path" - a valid SVG path with the
                    pixel values replaced by data values in
                    `xsizemode`/`ysizemode` being "scaled" and
                    taken unmodified as pixels relative to
                    `xanchor` and `yanchor` in case of "pixel" size
                    mode. There are a few restrictions / quirks
                    only absolute instructions, not relative. So
                    the allowed segments are: M, L, H, V, Q, C, T,
                    S, and Z arcs (A) are not allowed because
                    radius rx and ry are relative. In the future we
                    could consider supporting relative commands,
                    but we would have to decide on how to handle
                    date and log axes. Note that even as is, Q and
                    C Bezier paths that are smooth on linear axes
                    may not be smooth on log, and vice versa. no
                    chained "polybezier" commands - specify the
                    segment type for each one. On category axes,
                    values are numbers scaled to the serial numbers
                    of categories because using the categories
                    themselves there would be no way to describe
                    fractional positions On data axes: because
                    space and T are both normal components of path
                    strings, we can't use either to separate date
                    from time parts. Therefore we'll use underscore
                    for this purpose: 2015-02-21_13:45:56.789
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
                type
                    Specifies the shape type to be drawn. If
                    "line", a line is drawn from (`x0`,`y0`) to
                    (`x1`,`y1`) with respect to the axes' sizing
                    mode. If "circle", a circle is drawn from
                    ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
                    (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2
                    -`y0`)|) with respect to the axes' sizing mode.
                    If "rect", a rectangle is drawn linking
                    (`x0`,`y0`), (`x1`,`y0`), (`x1`,`y1`),
                    (`x0`,`y1`), (`x0`,`y0`) with respect to the
                    axes' sizing mode. If "path", draw a custom SVG
                    path using `path`. with respect to the axes'
                    sizing mode.
                visible
                    Determines whether or not this shape is
                    visible.
                x0
                    Sets the shape's starting x position. See
                    `type` and `xsizemode` for more info.
                x1
                    Sets the shape's end x position. See `type` and
                    `xsizemode` for more info.
                xanchor
                    Only relevant in conjunction with `xsizemode`
                    set to "pixel". Specifies the anchor point on
                    the x axis to which `x0`, `x1` and x
                    coordinates within `path` are relative to. E.g.
                    useful to attach a pixel sized shape to a
                    certain data value. No effect when `xsizemode`
                    not set to "pixel".
                xref
                    Sets the shape's x coordinate axis. If set to
                    an x axis id (e.g. "x" or "x2"), the `x`
                    position refers to an x coordinate. If set to
                    "paper", the `x` position refers to the
                    distance from the left side of the plotting
                    area in normalized coordinates where 0 (1)
                    corresponds to the left (right) side. If the
                    axis `type` is "log", then you must take the
                    log of your desired range. If the axis `type`
                    is "date", then you must convert the date to
                    unix time in milliseconds.
                xsizemode
                    Sets the shapes's sizing mode along the x axis.
                    If set to "scaled", `x0`, `x1` and x
                    coordinates within `path` refer to data values
                    on the x axis or a fraction of the plot area's
                    width (`xref` set to "paper"). If set to
                    "pixel", `xanchor` specifies the x position in
                    terms of data or plot fraction but `x0`, `x1`
                    and x coordinates within `path` are pixels
                    relative to `xanchor`. This way, the shape can
                    have a fixed width while maintaining a position
                    relative to data or plot fraction.
                y0
                    Sets the shape's starting y position. See
                    `type` and `ysizemode` for more info.
                y1
                    Sets the shape's end y position. See `type` and
                    `ysizemode` for more info.
                yanchor
                    Only relevant in conjunction with `ysizemode`
                    set to "pixel". Specifies the anchor point on
                    the y axis to which `y0`, `y1` and y
                    coordinates within `path` are relative to. E.g.
                    useful to attach a pixel sized shape to a
                    certain data value. No effect when `ysizemode`
                    not set to "pixel".
                yref
                    Sets the annotation's y coordinate axis. If set
                    to an y axis id (e.g. "y" or "y2"), the `y`
                    position refers to an y coordinate If set to
                    "paper", the `y` position refers to the
                    distance from the bottom of the plotting area
                    in normalized coordinates where 0 (1)
                    corresponds to the bottom (top).
                ysizemode
                    Sets the shapes's sizing mode along the y axis.
                    If set to "scaled", `y0`, `y1` and y
                    coordinates within `path` refer to data values
                    on the y axis or a fraction of the plot area's
                    height (`yref` set to "paper"). If set to
                    "pixel", `yanchor` specifies the y position in
                    terms of data or plot fraction but `y0`, `y1`
                    and y coordinates within `path` are pixels
                    relative to `yanchor`. This way, the shape can
                    have a fixed height while maintaining a
                    position relative to data or plot fraction.

        Returns
        -------
        tuple[plotly.graph_objs.layout.Shape]
        """
        return self['shapes']

    @shapes.setter
    def shapes(self, val):
        self['shapes'] = val

    # shapedefaults
    # -------------
    @property
    def shapedefaults(self):
        """
        When used in a template (as
        layout.template.layout.shapedefaults), sets the default
        property values to use for elements of layout.shapes
    
        The 'shapedefaults' property is an instance of Shape
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Shape
          - A dict of string/value properties that will be passed
            to the Shape constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.Shape
        """
        return self['shapedefaults']

    @shapedefaults.setter
    def shapedefaults(self, val):
        self['shapedefaults'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not a legend is drawn. Default is `true`
        if there is a trace to show and any of these: a) Two or more
        traces would by default be shown in the legend. b) One pie
        trace is shown in the legend. c) One trace is explicitly given
        with `showlegend: true`.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # sliders
    # -------
    @property
    def sliders(self):
        """
        The 'sliders' property is a tuple of instances of
        Slider that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.Slider
          - A list or tuple of dicts of string/value properties that
            will be passed to the Slider constructor
    
            Supported dict properties:
                
                active
                    Determines which button (by index starting from
                    0) is considered active.
                activebgcolor
                    Sets the background color of the slider grip
                    while dragging.
                bgcolor
                    Sets the background color of the slider.
                bordercolor
                    Sets the color of the border enclosing the
                    slider.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the slider.
                currentvalue
                    plotly.graph_objs.layout.slider.Currentvalue
                    instance or dict with compatible properties
                font
                    Sets the font of the slider step labels.
                len
                    Sets the length of the slider This measure
                    excludes the padding of both ends. That is, the
                    slider's length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this slider length is set in
                    units of plot "fraction" or in *pixels. Use
                    `len` to set the value.
                minorticklen
                    Sets the length in pixels of minor step tick
                    marks
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                pad
                    Set the padding of the slider component along
                    each side.
                steps
                    plotly.graph_objs.layout.slider.Step instance
                    or dict with compatible properties
                stepdefaults
                    When used in a template (as
                    layout.template.layout.slider.stepdefaults),
                    sets the default property values to use for
                    elements of layout.slider.steps
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
                tickcolor
                    Sets the color of the border enclosing the
                    slider.
                ticklen
                    Sets the length in pixels of step tick marks
                tickwidth
                    Sets the tick width (in px).
                transition
                    plotly.graph_objs.layout.slider.Transition
                    instance or dict with compatible properties
                visible
                    Determines whether or not the slider is
                    visible.
                x
                    Sets the x position (in normalized coordinates)
                    of the slider.
                xanchor
                    Sets the slider's horizontal position anchor.
                    This anchor binds the `x` position to the
                    "left", "center" or "right" of the range
                    selector.
                y
                    Sets the y position (in normalized coordinates)
                    of the slider.
                yanchor
                    Sets the slider's vertical position anchor This
                    anchor binds the `y` position to the "top",
                    "middle" or "bottom" of the range selector.

        Returns
        -------
        tuple[plotly.graph_objs.layout.Slider]
        """
        return self['sliders']

    @sliders.setter
    def sliders(self, val):
        self['sliders'] = val

    # sliderdefaults
    # --------------
    @property
    def sliderdefaults(self):
        """
        When used in a template (as
        layout.template.layout.sliderdefaults), sets the default
        property values to use for elements of layout.sliders
    
        The 'sliderdefaults' property is an instance of Slider
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Slider
          - A dict of string/value properties that will be passed
            to the Slider constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.Slider
        """
        return self['sliderdefaults']

    @sliderdefaults.setter
    def sliderdefaults(self, val):
        self['sliderdefaults'] = val

    # spikedistance
    # -------------
    @property
    def spikedistance(self):
        """
        Sets the default distance (in pixels) to look for data to draw
        spikelines to (-1 means no cutoff, 0 means no looking for
        data). As with hoverdistance, distance does not apply to area-
        like objects. In addition, some objects can be hovered on but
        will not generate spikelines, such as scatter fills.
    
        The 'spikedistance' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['spikedistance']

    @spikedistance.setter
    def spikedistance(self, val):
        self['spikedistance'] = val

    # template
    # --------
    @property
    def template(self):
        """
        Default attributes to be applied to the plot. This should be a
        dict with format: `{'layout': layoutTemplate, 'data':
        {trace_type: [traceTemplate, ...], ...}}` where
        `layoutTemplate` is a dict matching the structure of
        `figure.layout` and `traceTemplate` is a dict matching the
        structure of the trace with type `trace_type` (e.g. 'scatter').
        Alternatively, this may be specified as an instance of
        plotly.graph_objs.layout.Template.  Trace templates are applied
        cyclically to traces of each type. Container arrays (eg
        `annotations`) have special handling: An object ending in
        `defaults` (eg `annotationdefaults`) is applied to each array
        item. But if an item has a `templateitemname` key we look in
        the template array for an item with matching `name` and apply
        that instead. If no matching `name` is found we mark the item
        invisible. Any named template item not referenced is appended
        to the end of the array, so this can be used to add a watermark
        annotation or a logo image, for example. To omit one of these
        items on the plot, make an item with matching
        `templateitemname` and `visible: false`.
    
        The 'template' property is an instance of Template
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Template
          - A dict of string/value properties that will be passed
            to the Template constructor
    
            Supported dict properties:
                
                data
                    plotly.graph_objs.layout.template.Data instance
                    or dict with compatible properties
                layout
                    plotly.graph_objs.layout.template.Layout
                    instance or dict with compatible properties
    
          - The name of a registered template where current registered templates
            are stored in the plotly.io.templates configuration object. The names
            of all registered templates can be retrieved with:
                >>> import plotly.io as pio
                >>> list(pio.templates)
          - A string containing multiple registered template names, joined on '+'
            characters (e.g. 'template1+template2'). In this case the resulting
            template is computed by merging together the collection of registered 
            templates

        Returns
        -------
        plotly.graph_objs.layout.Template
        """
        return self['template']

    @template.setter
    def template(self, val):
        self['template'] = val

    # ternary
    # -------
    @property
    def ternary(self):
        """
        The 'ternary' property is an instance of Ternary
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Ternary
          - A dict of string/value properties that will be passed
            to the Ternary constructor
    
            Supported dict properties:
                
                aaxis
                    plotly.graph_objs.layout.ternary.Aaxis instance
                    or dict with compatible properties
                baxis
                    plotly.graph_objs.layout.ternary.Baxis instance
                    or dict with compatible properties
                bgcolor
                    Set the background color of the subplot
                caxis
                    plotly.graph_objs.layout.ternary.Caxis instance
                    or dict with compatible properties
                domain
                    plotly.graph_objs.layout.ternary.Domain
                    instance or dict with compatible properties
                sum
                    The number each triplet should sum to, and the
                    maximum range of each axis

        Returns
        -------
        plotly.graph_objs.layout.Ternary
        """
        return self['ternary']

    @ternary.setter
    def ternary(self, val):
        self['ternary'] = val

    # title
    # -----
    @property
    def title(self):
        """
        Sets the plot's title.
    
        The 'title' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['title']

    @title.setter
    def title(self, val):
        self['title'] = val

    # titlefont
    # ---------
    @property
    def titlefont(self):
        """
        Sets the title font.
    
        The 'titlefont' property is an instance of Titlefont
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Titlefont
          - A dict of string/value properties that will be passed
            to the Titlefont constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.Titlefont
        """
        return self['titlefont']

    @titlefont.setter
    def titlefont(self, val):
        self['titlefont'] = val

    # updatemenus
    # -----------
    @property
    def updatemenus(self):
        """
        The 'updatemenus' property is a tuple of instances of
        Updatemenu that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.Updatemenu
          - A list or tuple of dicts of string/value properties that
            will be passed to the Updatemenu constructor
    
            Supported dict properties:
                
                active
                    Determines which button (by index starting from
                    0) is considered active.
                bgcolor
                    Sets the background color of the update menu
                    buttons.
                bordercolor
                    Sets the color of the border enclosing the
                    update menu.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the update menu.
                buttons
                    plotly.graph_objs.layout.updatemenu.Button
                    instance or dict with compatible properties
                buttondefaults
                    When used in a template (as layout.template.lay
                    out.updatemenu.buttondefaults), sets the
                    default property values to use for elements of
                    layout.updatemenu.buttons
                direction
                    Determines the direction in which the buttons
                    are laid out, whether in a dropdown menu or a
                    row/column of buttons. For `left` and `up`, the
                    buttons will still appear in left-to-right or
                    top-to-bottom order respectively.
                font
                    Sets the font of the update menu button text.
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                pad
                    Sets the padding around the buttons or dropdown
                    menu.
                showactive
                    Highlights active dropdown item or active
                    button if true.
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
                type
                    Determines whether the buttons are accessible
                    via a dropdown menu or whether the buttons are
                    stacked horizontally or vertically
                visible
                    Determines whether or not the update menu is
                    visible.
                x
                    Sets the x position (in normalized coordinates)
                    of the update menu.
                xanchor
                    Sets the update menu's horizontal position
                    anchor. This anchor binds the `x` position to
                    the "left", "center" or "right" of the range
                    selector.
                y
                    Sets the y position (in normalized coordinates)
                    of the update menu.
                yanchor
                    Sets the update menu's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the range
                    selector.

        Returns
        -------
        tuple[plotly.graph_objs.layout.Updatemenu]
        """
        return self['updatemenus']

    @updatemenus.setter
    def updatemenus(self, val):
        self['updatemenus'] = val

    # updatemenudefaults
    # ------------------
    @property
    def updatemenudefaults(self):
        """
        When used in a template (as
        layout.template.layout.updatemenudefaults), sets the default
        property values to use for elements of layout.updatemenus
    
        The 'updatemenudefaults' property is an instance of Updatemenu
        that may be specified as:
          - An instance of plotly.graph_objs.layout.Updatemenu
          - A dict of string/value properties that will be passed
            to the Updatemenu constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.Updatemenu
        """
        return self['updatemenudefaults']

    @updatemenudefaults.setter
    def updatemenudefaults(self, val):
        self['updatemenudefaults'] = val

    # violingap
    # ---------
    @property
    def violingap(self):
        """
        Sets the gap (in plot fraction) between violins of adjacent
        location coordinates.
    
        The 'violingap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['violingap']

    @violingap.setter
    def violingap(self, val):
        self['violingap'] = val

    # violingroupgap
    # --------------
    @property
    def violingroupgap(self):
        """
        Sets the gap (in plot fraction) between violins of the same
        location coordinate.
    
        The 'violingroupgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['violingroupgap']

    @violingroupgap.setter
    def violingroupgap(self, val):
        self['violingroupgap'] = val

    # violinmode
    # ----------
    @property
    def violinmode(self):
        """
        Determines how violins at the same location coordinate are
        displayed on the graph. If "group", the violins are plotted
        next to one another centered around the shared location. If
        "overlay", the violins are plotted over one another, you might
        need to set "opacity" to see them multiple violins.
    
        The 'violinmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['group', 'overlay']

        Returns
        -------
        Any
        """
        return self['violinmode']

    @violinmode.setter
    def violinmode(self, val):
        self['violinmode'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the plot's width (in px).
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [10, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        The 'xaxis' property is an instance of XAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.XAxis
          - A dict of string/value properties that will be passed
            to the XAxis constructor
    
            Supported dict properties:
                
                anchor
                    If set to an opposite-letter axis id (e.g.
                    `x2`, `y`), this axis is bound to the
                    corresponding opposite-letter axis. If set to
                    "free", this axis' position is determined by
                    `position`.
                automargin
                    Determines whether long tick labels
                    automatically grow the figure margins.
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                constrain
                    If this axis needs to be compressed (either due
                    to its own `scaleanchor` and `scaleratio` or
                    those of the other axis), determines how that
                    happens: by increasing the "range" (default),
                    or by decreasing the "domain".
                constraintoward
                    If this axis needs to be compressed (either due
                    to its own `scaleanchor` and `scaleratio` or
                    those of the other axis), determines which
                    direction we push the originally specified plot
                    area. Options are "left", "center" (default),
                    and "right" for x axes, and "top", "middle"
                    (default), and "bottom" for y axes.
                domain
                    Sets the domain of this axis (in plot
                    fraction).
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to "log" and "date"
                    axes. If the axis `type` is "log", then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. "log"
                    has several special values; "L<f>", where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use "D1" (all
                    digits) or "D2" (only 2 and 5). `tick0` is
                    ignored for "D1" and "D2". If the axis `type`
                    is "date", then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. "date" also has special values
                    "M<n>" gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to "2000-01-15" and `dtick` to "M3". To
                    set ticks every 4 years, set `dtick` to "M48"
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                fixedrange
                    Determines whether or not this axis is zoom-
                    able. If true, then zoom is disabled.
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If True, the axis lines are mirrored. If
                    "ticks", the axis lines and ticks are mirrored.
                    If False, mirroring is disable. If "all", axis
                    lines are mirrored on all shared-axes subplots.
                    If "allticks", axis lines and ticks are
                    mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                overlaying
                    If set a same-letter axis id, this axis is
                    overlaid on top of the corresponding same-
                    letter axis, with traces and axes visible for
                    both axes. If False, this axis does not overlay
                    any same-letter axes. In this case, for axes
                    with overlapping domains only the highest-
                    numbered axis will be visible.
                position
                    Sets the position of this axis in the plotting
                    space (in normalized coordinates). Only has an
                    effect if `anchor` is set to "free".
                range
                    Sets the range of this axis. If the axis `type`
                    is "log", then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is "date", it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is "category", it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If "normal", the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If "nonnegative", the range is non-
                    negative, regardless of the input data. Applies
                    only to linear axes.
                rangeselector
                    plotly.graph_objs.layout.xaxis.Rangeselector
                    instance or dict with compatible properties
                rangeslider
                    plotly.graph_objs.layout.xaxis.Rangeslider
                    instance or dict with compatible properties
                scaleanchor
                    If set to another axis id (e.g. `x2`, `y`), the
                    range of this axis changes together with the
                    range of the corresponding axis such that the
                    scale of pixels per unit is in a constant
                    ratio. Both axes are still zoomable, but when
                    you zoom one, the other will zoom the same
                    amount, keeping a fixed midpoint. `constrain`
                    and `constraintoward` determine how we enforce
                    the constraint. You can chain these, ie `yaxis:
                    {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}`
                    but you can only link axes of the same `type`.
                    The linked axis can have the opposite letter
                    (to constrain the aspect ratio) or the same
                    letter (to match scales across subplots). Loops
                    (`yaxis: {scaleanchor: *x*}, xaxis:
                    {scaleanchor: *y*}` or longer) are redundant
                    and the last constraint encountered will be
                    ignored to avoid possible inconsistent
                    constraints via `scaleratio`.
                scaleratio
                    If this axis is linked to another by
                    `scaleanchor`, this determines the pixel to
                    unit scale ratio. For example, if this value is
                    10, then every unit on this axis spans 10 times
                    the number of pixels as a unit on the linked
                    axis. Use this for example to create an
                    elevation profile where the vertical scale is
                    exaggerated a fixed amount with respect to the
                    horizontal.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Determines whether or not spikes (aka
                    droplines) are drawn for this axis. Note: This
                    only takes affect when hovermode = closest
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                side
                    Determines whether a x (y) axis is positioned
                    at the "bottom" ("left") or "top" ("right") of
                    the plotting area.
                spikecolor
                    Sets the spike color. If undefined, will use
                    the series color
                spikedash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                spikemode
                    Determines the drawing mode for the spike line
                    If "toaxis", the line is drawn from the data
                    point to the axis the  series is plotted on. If
                    "across", the line is drawn across the entire
                    plot area, and supercedes "toaxis". If
                    "marker", then a marker dot is drawn on the
                    axis the series is plotted on
                spikesnap
                    Determines whether spikelines are stuck to the
                    cursor or to the closest datapoints.
                spikethickness
                    Sets the width (in px) of the zero line.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    "log", then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is "date", it should be a date
                    string, like date data. If the axis `type` is
                    "category", it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    plotly.graph_objs.layout.xaxis.Tickformatstop
                    instance or dict with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.xaxis.tickformatstopdefaults), sets the
                    default property values to use for elements of
                    layout.xaxis.tickformatstops
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If "auto",
                    the number of ticks is set via `nticks`. If
                    "linear", the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` ("linear" is the default
                    value if `tick0` and `dtick` are provided). If
                    "array", the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    ("array" is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    "", this axis' ticks are not drawn. If
                    "outside" ("inside"), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to "array". Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to "array". Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If True, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.XAxis
        """
        return self['xaxis']

    @xaxis.setter
    def xaxis(self, val):
        self['xaxis'] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        The 'yaxis' property is an instance of YAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.YAxis
          - A dict of string/value properties that will be passed
            to the YAxis constructor
    
            Supported dict properties:
                
                anchor
                    If set to an opposite-letter axis id (e.g.
                    `x2`, `y`), this axis is bound to the
                    corresponding opposite-letter axis. If set to
                    "free", this axis' position is determined by
                    `position`.
                automargin
                    Determines whether long tick labels
                    automatically grow the figure margins.
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                constrain
                    If this axis needs to be compressed (either due
                    to its own `scaleanchor` and `scaleratio` or
                    those of the other axis), determines how that
                    happens: by increasing the "range" (default),
                    or by decreasing the "domain".
                constraintoward
                    If this axis needs to be compressed (either due
                    to its own `scaleanchor` and `scaleratio` or
                    those of the other axis), determines which
                    direction we push the originally specified plot
                    area. Options are "left", "center" (default),
                    and "right" for x axes, and "top", "middle"
                    (default), and "bottom" for y axes.
                domain
                    Sets the domain of this axis (in plot
                    fraction).
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to "log" and "date"
                    axes. If the axis `type` is "log", then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. "log"
                    has several special values; "L<f>", where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use "D1" (all
                    digits) or "D2" (only 2 and 5). `tick0` is
                    ignored for "D1" and "D2". If the axis `type`
                    is "date", then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. "date" also has special values
                    "M<n>" gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to "2000-01-15" and `dtick` to "M3". To
                    set ticks every 4 years, set `dtick` to "M48"
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                fixedrange
                    Determines whether or not this axis is zoom-
                    able. If true, then zoom is disabled.
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If True, the axis lines are mirrored. If
                    "ticks", the axis lines and ticks are mirrored.
                    If False, mirroring is disable. If "all", axis
                    lines are mirrored on all shared-axes subplots.
                    If "allticks", axis lines and ticks are
                    mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                overlaying
                    If set a same-letter axis id, this axis is
                    overlaid on top of the corresponding same-
                    letter axis, with traces and axes visible for
                    both axes. If False, this axis does not overlay
                    any same-letter axes. In this case, for axes
                    with overlapping domains only the highest-
                    numbered axis will be visible.
                position
                    Sets the position of this axis in the plotting
                    space (in normalized coordinates). Only has an
                    effect if `anchor` is set to "free".
                range
                    Sets the range of this axis. If the axis `type`
                    is "log", then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is "date", it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is "category", it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If "normal", the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If "nonnegative", the range is non-
                    negative, regardless of the input data. Applies
                    only to linear axes.
                scaleanchor
                    If set to another axis id (e.g. `x2`, `y`), the
                    range of this axis changes together with the
                    range of the corresponding axis such that the
                    scale of pixels per unit is in a constant
                    ratio. Both axes are still zoomable, but when
                    you zoom one, the other will zoom the same
                    amount, keeping a fixed midpoint. `constrain`
                    and `constraintoward` determine how we enforce
                    the constraint. You can chain these, ie `yaxis:
                    {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}`
                    but you can only link axes of the same `type`.
                    The linked axis can have the opposite letter
                    (to constrain the aspect ratio) or the same
                    letter (to match scales across subplots). Loops
                    (`yaxis: {scaleanchor: *x*}, xaxis:
                    {scaleanchor: *y*}` or longer) are redundant
                    and the last constraint encountered will be
                    ignored to avoid possible inconsistent
                    constraints via `scaleratio`.
                scaleratio
                    If this axis is linked to another by
                    `scaleanchor`, this determines the pixel to
                    unit scale ratio. For example, if this value is
                    10, then every unit on this axis spans 10 times
                    the number of pixels as a unit on the linked
                    axis. Use this for example to create an
                    elevation profile where the vertical scale is
                    exaggerated a fixed amount with respect to the
                    horizontal.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Determines whether or not spikes (aka
                    droplines) are drawn for this axis. Note: This
                    only takes affect when hovermode = closest
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                side
                    Determines whether a x (y) axis is positioned
                    at the "bottom" ("left") or "top" ("right") of
                    the plotting area.
                spikecolor
                    Sets the spike color. If undefined, will use
                    the series color
                spikedash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                spikemode
                    Determines the drawing mode for the spike line
                    If "toaxis", the line is drawn from the data
                    point to the axis the  series is plotted on. If
                    "across", the line is drawn across the entire
                    plot area, and supercedes "toaxis". If
                    "marker", then a marker dot is drawn on the
                    axis the series is plotted on
                spikesnap
                    Determines whether spikelines are stuck to the
                    cursor or to the closest datapoints.
                spikethickness
                    Sets the width (in px) of the zero line.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    "log", then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is "date", it should be a date
                    string, like date data. If the axis `type` is
                    "category", it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    plotly.graph_objs.layout.yaxis.Tickformatstop
                    instance or dict with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.yaxis.tickformatstopdefaults), sets the
                    default property values to use for elements of
                    layout.yaxis.tickformatstops
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If "auto",
                    the number of ticks is set via `nticks`. If
                    "linear", the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` ("linear" is the default
                    value if `tick0` and `dtick` are provided). If
                    "array", the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    ("array" is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    "", this axis' ticks are not drawn. If
                    "outside" ("inside"), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to "array". Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to "array". Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If True, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.YAxis
        """
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return ''

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        angularaxis
            plotly.graph_objs.layout.AngularAxis instance or dict
            with compatible properties
        annotations
            plotly.graph_objs.layout.Annotation instance or dict
            with compatible properties
        annotationdefaults
            When used in a template (as
            layout.template.layout.annotationdefaults), sets the
            default property values to use for elements of
            layout.annotations
        autosize
            Determines whether or not a layout width or height that
            has been left undefined by the user is initialized on
            each relayout. Note that, regardless of this attribute,
            an undefined layout width or height is always
            initialized on the first call to plot.
        bargap
            Sets the gap (in plot fraction) between bars of
            adjacent location coordinates.
        bargroupgap
            Sets the gap (in plot fraction) between bars of the
            same location coordinate.
        barmode
            Determines how bars at the same location coordinate are
            displayed on the graph. With "stack", the bars are
            stacked on top of one another With "relative", the bars
            are stacked on top of one another, with negative values
            below the axis, positive values above With "group", the
            bars are plotted next to one another centered around
            the shared location. With "overlay", the bars are
            plotted over one another, you might need to an
            "opacity" to see multiple bars.
        barnorm
            Sets the normalization for bar traces on the graph.
            With "fraction", the value of each bar is divided by
            the sum of all values at that location coordinate.
            "percent" is the same but multiplied by 100 to show
            percentages.
        boxgap
            Sets the gap (in plot fraction) between boxes of
            adjacent location coordinates.
        boxgroupgap
            Sets the gap (in plot fraction) between boxes of the
            same location coordinate.
        boxmode
            Determines how boxes at the same location coordinate
            are displayed on the graph. If "group", the boxes are
            plotted next to one another centered around the shared
            location. If "overlay", the boxes are plotted over one
            another, you might need to set "opacity" to see them
            multiple boxes.
        calendar
            Sets the default calendar system to use for
            interpreting and displaying dates throughout the plot.
        clickmode
            Determines the mode of single click interactions.
            "event" is the default value and emits the
            `plotly_click` event. In addition this mode emits the
            `plotly_selected` event in drag modes "lasso" and
            "select", but with no event data attached (kept for
            compatibility reasons). The "select" flag enables
            selecting single data points via click. This mode also
            supports persistent selections, meaning that pressing
            Shift while clicking, adds to / subtracts from an
            existing selection. "select" with `hovermode`: "x" can
            be confusing, consider explicitly setting `hovermode`:
            "closest" when using this feature. Selection events are
            sent accordingly as long as "event" flag is set as
            well. When the "event" flag is missing, `plotly_click`
            and `plotly_selected` events are not fired.
        colorway
            Sets the default trace colors.
        datarevision
            If provided, a changed value tells `Plotly.react` that
            one or more data arrays has changed. This way you can
            modify arrays in-place rather than making a complete
            new copy for an incremental change. If NOT provided,
            `Plotly.react` assumes that data arrays are being
            treated as immutable, thus any data array with a
            different identity from its predecessor contains new
            data.
        direction
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the direction corresponding to
            positive angles in legacy polar charts.
        dragmode
            Determines the mode of drag interactions. "select" and
            "lasso" apply only to scatter traces with markers or
            text. "orbit" and "turntable" apply only to 3D scenes.
        extendpiecolors
            If `true`, the pie slice colors (whether given by
            `piecolorway` or inherited from `colorway`) will be
            extended to three times its original length by first
            repeating every color 20% lighter then each color 20%
            darker. This is intended to reduce the likelihood of
            reusing the same color when you have many slices, but
            you can set `false` to disable. Colors provided in the
            trace, using `marker.colors`, are never extended.
        font
            Sets the global font. Note that fonts used in traces
            and other layout components inherit from the global
            font.
        geo
            plotly.graph_objs.layout.Geo instance or dict with
            compatible properties
        grid
            plotly.graph_objs.layout.Grid instance or dict with
            compatible properties
        height
            Sets the plot's height (in px).
        hiddenlabels

        hiddenlabelssrc
            Sets the source reference on plot.ly for  hiddenlabels
            .
        hidesources
            Determines whether or not a text link citing the data
            source is placed at the bottom-right cored of the
            figure. Has only an effect only on graphs that have
            been generated via forked graphs from the plotly
            service (at https://plot.ly or on-premise).
        hoverdistance
            Sets the default distance (in pixels) to look for data
            to add hover labels (-1 means no cutoff, 0 means no
            looking for data). This is only a real distance for
            hovering on point-like objects, like scatter points.
            For area-like objects (bars, scatter fills, etc)
            hovering is on inside the area and off outside, but
            these objects will not supersede hover on point-like
            objects in case of conflict.
        hoverlabel
            plotly.graph_objs.layout.Hoverlabel instance or dict
            with compatible properties
        hovermode
            Determines the mode of hover interactions. If
            `clickmode` includes the "select" flag, `hovermode`
            defaults to "closest". If `clickmode` lacks the
            "select" flag, it defaults to "x" or "y" (depending on
            the trace's `orientation` value) for plots based on
            cartesian coordinates. For anything else the default
            value is "closest".
        images
            plotly.graph_objs.layout.Image instance or dict with
            compatible properties
        imagedefaults
            When used in a template (as
            layout.template.layout.imagedefaults), sets the default
            property values to use for elements of layout.images
        legend
            plotly.graph_objs.layout.Legend instance or dict with
            compatible properties
        mapbox
            plotly.graph_objs.layout.Mapbox instance or dict with
            compatible properties
        margin
            plotly.graph_objs.layout.Margin instance or dict with
            compatible properties
        modebar
            plotly.graph_objs.layout.Modebar instance or dict with
            compatible properties
        orientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Rotates the entire polar by the given
            angle in legacy polar charts.
        paper_bgcolor
            Sets the color of paper where the graph is drawn.
        piecolorway
            Sets the default pie slice colors. Defaults to the main
            `colorway` used for trace colors. If you specify a new
            list here it can still be extended with lighter and
            darker colors, see `extendpiecolors`.
        plot_bgcolor
            Sets the color of plotting area in-between x and y
            axes.
        polar
            plotly.graph_objs.layout.Polar instance or dict with
            compatible properties
        radialaxis
            plotly.graph_objs.layout.RadialAxis instance or dict
            with compatible properties
        scene
            plotly.graph_objs.layout.Scene instance or dict with
            compatible properties
        selectdirection
            When "dragmode" is set to "select", this limits the
            selection of the drag to horizontal, vertical or
            diagonal. "h" only allows horizontal selection, "v"
            only vertical, "d" only diagonal and "any" sets no
            limit.
        separators
            Sets the decimal and thousand separators. For example,
            *. * puts a '.' before decimals and a space between
            thousands. In English locales, dflt is ".," but other
            locales may alter this default.
        shapes
            plotly.graph_objs.layout.Shape instance or dict with
            compatible properties
        shapedefaults
            When used in a template (as
            layout.template.layout.shapedefaults), sets the default
            property values to use for elements of layout.shapes
        showlegend
            Determines whether or not a legend is drawn. Default is
            `true` if there is a trace to show and any of these: a)
            Two or more traces would by default be shown in the
            legend. b) One pie trace is shown in the legend. c) One
            trace is explicitly given with `showlegend: true`.
        sliders
            plotly.graph_objs.layout.Slider instance or dict with
            compatible properties
        sliderdefaults
            When used in a template (as
            layout.template.layout.sliderdefaults), sets the
            default property values to use for elements of
            layout.sliders
        spikedistance
            Sets the default distance (in pixels) to look for data
            to draw spikelines to (-1 means no cutoff, 0 means no
            looking for data). As with hoverdistance, distance does
            not apply to area-like objects. In addition, some
            objects can be hovered on but will not generate
            spikelines, such as scatter fills.
        template
            Default attributes to be applied to the plot. This
            should be a dict with format: `{'layout':
            layoutTemplate, 'data': {trace_type: [traceTemplate,
            ...], ...}}` where `layoutTemplate` is a dict matching
            the structure of `figure.layout` and `traceTemplate` is
            a dict matching the structure of the trace with type
            `trace_type` (e.g. 'scatter'). Alternatively, this may
            be specified as an instance of
            plotly.graph_objs.layout.Template.  Trace templates are
            applied cyclically to traces of each type. Container
            arrays (eg `annotations`) have special handling: An
            object ending in `defaults` (eg `annotationdefaults`)
            is applied to each array item. But if an item has a
            `templateitemname` key we look in the template array
            for an item with matching `name` and apply that
            instead. If no matching `name` is found we mark the
            item invisible. Any named template item not referenced
            is appended to the end of the array, so this can be
            used to add a watermark annotation or a logo image, for
            example. To omit one of these items on the plot, make
            an item with matching `templateitemname` and `visible:
            false`.
        ternary
            plotly.graph_objs.layout.Ternary instance or dict with
            compatible properties
        title
            Sets the plot's title.
        titlefont
            Sets the title font.
        updatemenus
            plotly.graph_objs.layout.Updatemenu instance or dict
            with compatible properties
        updatemenudefaults
            When used in a template (as
            layout.template.layout.updatemenudefaults), sets the
            default property values to use for elements of
            layout.updatemenus
        violingap
            Sets the gap (in plot fraction) between violins of
            adjacent location coordinates.
        violingroupgap
            Sets the gap (in plot fraction) between violins of the
            same location coordinate.
        violinmode
            Determines how violins at the same location coordinate
            are displayed on the graph. If "group", the violins are
            plotted next to one another centered around the shared
            location. If "overlay", the violins are plotted over
            one another, you might need to set "opacity" to see
            them multiple violins.
        width
            Sets the plot's width (in px).
        xaxis
            plotly.graph_objs.layout.XAxis instance or dict with
            compatible properties
        yaxis
            plotly.graph_objs.layout.YAxis instance or dict with
            compatible properties
        """

    def __init__(
        self,
        arg=None,
        angularaxis=None,
        annotations=None,
        annotationdefaults=None,
        autosize=None,
        bargap=None,
        bargroupgap=None,
        barmode=None,
        barnorm=None,
        boxgap=None,
        boxgroupgap=None,
        boxmode=None,
        calendar=None,
        clickmode=None,
        colorway=None,
        datarevision=None,
        direction=None,
        dragmode=None,
        extendpiecolors=None,
        font=None,
        geo=None,
        grid=None,
        height=None,
        hiddenlabels=None,
        hiddenlabelssrc=None,
        hidesources=None,
        hoverdistance=None,
        hoverlabel=None,
        hovermode=None,
        images=None,
        imagedefaults=None,
        legend=None,
        mapbox=None,
        margin=None,
        modebar=None,
        orientation=None,
        paper_bgcolor=None,
        piecolorway=None,
        plot_bgcolor=None,
        polar=None,
        radialaxis=None,
        scene=None,
        selectdirection=None,
        separators=None,
        shapes=None,
        shapedefaults=None,
        showlegend=None,
        sliders=None,
        sliderdefaults=None,
        spikedistance=None,
        template=None,
        ternary=None,
        title=None,
        titlefont=None,
        updatemenus=None,
        updatemenudefaults=None,
        violingap=None,
        violingroupgap=None,
        violinmode=None,
        width=None,
        xaxis=None,
        yaxis=None,
        **kwargs
    ):
        """
        Construct a new Layout object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Layout
        angularaxis
            plotly.graph_objs.layout.AngularAxis instance or dict
            with compatible properties
        annotations
            plotly.graph_objs.layout.Annotation instance or dict
            with compatible properties
        annotationdefaults
            When used in a template (as
            layout.template.layout.annotationdefaults), sets the
            default property values to use for elements of
            layout.annotations
        autosize
            Determines whether or not a layout width or height that
            has been left undefined by the user is initialized on
            each relayout. Note that, regardless of this attribute,
            an undefined layout width or height is always
            initialized on the first call to plot.
        bargap
            Sets the gap (in plot fraction) between bars of
            adjacent location coordinates.
        bargroupgap
            Sets the gap (in plot fraction) between bars of the
            same location coordinate.
        barmode
            Determines how bars at the same location coordinate are
            displayed on the graph. With "stack", the bars are
            stacked on top of one another With "relative", the bars
            are stacked on top of one another, with negative values
            below the axis, positive values above With "group", the
            bars are plotted next to one another centered around
            the shared location. With "overlay", the bars are
            plotted over one another, you might need to an
            "opacity" to see multiple bars.
        barnorm
            Sets the normalization for bar traces on the graph.
            With "fraction", the value of each bar is divided by
            the sum of all values at that location coordinate.
            "percent" is the same but multiplied by 100 to show
            percentages.
        boxgap
            Sets the gap (in plot fraction) between boxes of
            adjacent location coordinates.
        boxgroupgap
            Sets the gap (in plot fraction) between boxes of the
            same location coordinate.
        boxmode
            Determines how boxes at the same location coordinate
            are displayed on the graph. If "group", the boxes are
            plotted next to one another centered around the shared
            location. If "overlay", the boxes are plotted over one
            another, you might need to set "opacity" to see them
            multiple boxes.
        calendar
            Sets the default calendar system to use for
            interpreting and displaying dates throughout the plot.
        clickmode
            Determines the mode of single click interactions.
            "event" is the default value and emits the
            `plotly_click` event. In addition this mode emits the
            `plotly_selected` event in drag modes "lasso" and
            "select", but with no event data attached (kept for
            compatibility reasons). The "select" flag enables
            selecting single data points via click. This mode also
            supports persistent selections, meaning that pressing
            Shift while clicking, adds to / subtracts from an
            existing selection. "select" with `hovermode`: "x" can
            be confusing, consider explicitly setting `hovermode`:
            "closest" when using this feature. Selection events are
            sent accordingly as long as "event" flag is set as
            well. When the "event" flag is missing, `plotly_click`
            and `plotly_selected` events are not fired.
        colorway
            Sets the default trace colors.
        datarevision
            If provided, a changed value tells `Plotly.react` that
            one or more data arrays has changed. This way you can
            modify arrays in-place rather than making a complete
            new copy for an incremental change. If NOT provided,
            `Plotly.react` assumes that data arrays are being
            treated as immutable, thus any data array with a
            different identity from its predecessor contains new
            data.
        direction
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the direction corresponding to
            positive angles in legacy polar charts.
        dragmode
            Determines the mode of drag interactions. "select" and
            "lasso" apply only to scatter traces with markers or
            text. "orbit" and "turntable" apply only to 3D scenes.
        extendpiecolors
            If `true`, the pie slice colors (whether given by
            `piecolorway` or inherited from `colorway`) will be
            extended to three times its original length by first
            repeating every color 20% lighter then each color 20%
            darker. This is intended to reduce the likelihood of
            reusing the same color when you have many slices, but
            you can set `false` to disable. Colors provided in the
            trace, using `marker.colors`, are never extended.
        font
            Sets the global font. Note that fonts used in traces
            and other layout components inherit from the global
            font.
        geo
            plotly.graph_objs.layout.Geo instance or dict with
            compatible properties
        grid
            plotly.graph_objs.layout.Grid instance or dict with
            compatible properties
        height
            Sets the plot's height (in px).
        hiddenlabels

        hiddenlabelssrc
            Sets the source reference on plot.ly for  hiddenlabels
            .
        hidesources
            Determines whether or not a text link citing the data
            source is placed at the bottom-right cored of the
            figure. Has only an effect only on graphs that have
            been generated via forked graphs from the plotly
            service (at https://plot.ly or on-premise).
        hoverdistance
            Sets the default distance (in pixels) to look for data
            to add hover labels (-1 means no cutoff, 0 means no
            looking for data). This is only a real distance for
            hovering on point-like objects, like scatter points.
            For area-like objects (bars, scatter fills, etc)
            hovering is on inside the area and off outside, but
            these objects will not supersede hover on point-like
            objects in case of conflict.
        hoverlabel
            plotly.graph_objs.layout.Hoverlabel instance or dict
            with compatible properties
        hovermode
            Determines the mode of hover interactions. If
            `clickmode` includes the "select" flag, `hovermode`
            defaults to "closest". If `clickmode` lacks the
            "select" flag, it defaults to "x" or "y" (depending on
            the trace's `orientation` value) for plots based on
            cartesian coordinates. For anything else the default
            value is "closest".
        images
            plotly.graph_objs.layout.Image instance or dict with
            compatible properties
        imagedefaults
            When used in a template (as
            layout.template.layout.imagedefaults), sets the default
            property values to use for elements of layout.images
        legend
            plotly.graph_objs.layout.Legend instance or dict with
            compatible properties
        mapbox
            plotly.graph_objs.layout.Mapbox instance or dict with
            compatible properties
        margin
            plotly.graph_objs.layout.Margin instance or dict with
            compatible properties
        modebar
            plotly.graph_objs.layout.Modebar instance or dict with
            compatible properties
        orientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Rotates the entire polar by the given
            angle in legacy polar charts.
        paper_bgcolor
            Sets the color of paper where the graph is drawn.
        piecolorway
            Sets the default pie slice colors. Defaults to the main
            `colorway` used for trace colors. If you specify a new
            list here it can still be extended with lighter and
            darker colors, see `extendpiecolors`.
        plot_bgcolor
            Sets the color of plotting area in-between x and y
            axes.
        polar
            plotly.graph_objs.layout.Polar instance or dict with
            compatible properties
        radialaxis
            plotly.graph_objs.layout.RadialAxis instance or dict
            with compatible properties
        scene
            plotly.graph_objs.layout.Scene instance or dict with
            compatible properties
        selectdirection
            When "dragmode" is set to "select", this limits the
            selection of the drag to horizontal, vertical or
            diagonal. "h" only allows horizontal selection, "v"
            only vertical, "d" only diagonal and "any" sets no
            limit.
        separators
            Sets the decimal and thousand separators. For example,
            *. * puts a '.' before decimals and a space between
            thousands. In English locales, dflt is ".," but other
            locales may alter this default.
        shapes
            plotly.graph_objs.layout.Shape instance or dict with
            compatible properties
        shapedefaults
            When used in a template (as
            layout.template.layout.shapedefaults), sets the default
            property values to use for elements of layout.shapes
        showlegend
            Determines whether or not a legend is drawn. Default is
            `true` if there is a trace to show and any of these: a)
            Two or more traces would by default be shown in the
            legend. b) One pie trace is shown in the legend. c) One
            trace is explicitly given with `showlegend: true`.
        sliders
            plotly.graph_objs.layout.Slider instance or dict with
            compatible properties
        sliderdefaults
            When used in a template (as
            layout.template.layout.sliderdefaults), sets the
            default property values to use for elements of
            layout.sliders
        spikedistance
            Sets the default distance (in pixels) to look for data
            to draw spikelines to (-1 means no cutoff, 0 means no
            looking for data). As with hoverdistance, distance does
            not apply to area-like objects. In addition, some
            objects can be hovered on but will not generate
            spikelines, such as scatter fills.
        template
            Default attributes to be applied to the plot. This
            should be a dict with format: `{'layout':
            layoutTemplate, 'data': {trace_type: [traceTemplate,
            ...], ...}}` where `layoutTemplate` is a dict matching
            the structure of `figure.layout` and `traceTemplate` is
            a dict matching the structure of the trace with type
            `trace_type` (e.g. 'scatter'). Alternatively, this may
            be specified as an instance of
            plotly.graph_objs.layout.Template.  Trace templates are
            applied cyclically to traces of each type. Container
            arrays (eg `annotations`) have special handling: An
            object ending in `defaults` (eg `annotationdefaults`)
            is applied to each array item. But if an item has a
            `templateitemname` key we look in the template array
            for an item with matching `name` and apply that
            instead. If no matching `name` is found we mark the
            item invisible. Any named template item not referenced
            is appended to the end of the array, so this can be
            used to add a watermark annotation or a logo image, for
            example. To omit one of these items on the plot, make
            an item with matching `templateitemname` and `visible:
            false`.
        ternary
            plotly.graph_objs.layout.Ternary instance or dict with
            compatible properties
        title
            Sets the plot's title.
        titlefont
            Sets the title font.
        updatemenus
            plotly.graph_objs.layout.Updatemenu instance or dict
            with compatible properties
        updatemenudefaults
            When used in a template (as
            layout.template.layout.updatemenudefaults), sets the
            default property values to use for elements of
            layout.updatemenus
        violingap
            Sets the gap (in plot fraction) between violins of
            adjacent location coordinates.
        violingroupgap
            Sets the gap (in plot fraction) between violins of the
            same location coordinate.
        violinmode
            Determines how violins at the same location coordinate
            are displayed on the graph. If "group", the violins are
            plotted next to one another centered around the shared
            location. If "overlay", the violins are plotted over
            one another, you might need to set "opacity" to see
            them multiple violins.
        width
            Sets the plot's width (in px).
        xaxis
            plotly.graph_objs.layout.XAxis instance or dict with
            compatible properties
        yaxis
            plotly.graph_objs.layout.YAxis instance or dict with
            compatible properties

        Returns
        -------
        Layout
        """
        super(Layout, self).__init__('layout')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Layout 
constructor must be a dict or 
an instance of plotly.graph_objs.Layout"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (layout as v_layout)

        # Initialize validators
        # ---------------------
        self._validators['angularaxis'] = v_layout.AngularAxisValidator()
        self._validators['annotations'] = v_layout.AnnotationsValidator()
        self._validators['annotationdefaults'] = v_layout.AnnotationValidator()
        self._validators['autosize'] = v_layout.AutosizeValidator()
        self._validators['bargap'] = v_layout.BargapValidator()
        self._validators['bargroupgap'] = v_layout.BargroupgapValidator()
        self._validators['barmode'] = v_layout.BarmodeValidator()
        self._validators['barnorm'] = v_layout.BarnormValidator()
        self._validators['boxgap'] = v_layout.BoxgapValidator()
        self._validators['boxgroupgap'] = v_layout.BoxgroupgapValidator()
        self._validators['boxmode'] = v_layout.BoxmodeValidator()
        self._validators['calendar'] = v_layout.CalendarValidator()
        self._validators['clickmode'] = v_layout.ClickmodeValidator()
        self._validators['colorway'] = v_layout.ColorwayValidator()
        self._validators['datarevision'] = v_layout.DatarevisionValidator()
        self._validators['direction'] = v_layout.DirectionValidator()
        self._validators['dragmode'] = v_layout.DragmodeValidator()
        self._validators['extendpiecolors'
                        ] = v_layout.ExtendpiecolorsValidator()
        self._validators['font'] = v_layout.FontValidator()
        self._validators['geo'] = v_layout.GeoValidator()
        self._validators['grid'] = v_layout.GridValidator()
        self._validators['height'] = v_layout.HeightValidator()
        self._validators['hiddenlabels'] = v_layout.HiddenlabelsValidator()
        self._validators['hiddenlabelssrc'
                        ] = v_layout.HiddenlabelssrcValidator()
        self._validators['hidesources'] = v_layout.HidesourcesValidator()
        self._validators['hoverdistance'] = v_layout.HoverdistanceValidator()
        self._validators['hoverlabel'] = v_layout.HoverlabelValidator()
        self._validators['hovermode'] = v_layout.HovermodeValidator()
        self._validators['images'] = v_layout.ImagesValidator()
        self._validators['imagedefaults'] = v_layout.ImageValidator()
        self._validators['legend'] = v_layout.LegendValidator()
        self._validators['mapbox'] = v_layout.MapboxValidator()
        self._validators['margin'] = v_layout.MarginValidator()
        self._validators['modebar'] = v_layout.ModebarValidator()
        self._validators['orientation'] = v_layout.OrientationValidator()
        self._validators['paper_bgcolor'] = v_layout.PaperBgcolorValidator()
        self._validators['piecolorway'] = v_layout.PiecolorwayValidator()
        self._validators['plot_bgcolor'] = v_layout.PlotBgcolorValidator()
        self._validators['polar'] = v_layout.PolarValidator()
        self._validators['radialaxis'] = v_layout.RadialAxisValidator()
        self._validators['scene'] = v_layout.SceneValidator()
        self._validators['selectdirection'
                        ] = v_layout.SelectdirectionValidator()
        self._validators['separators'] = v_layout.SeparatorsValidator()
        self._validators['shapes'] = v_layout.ShapesValidator()
        self._validators['shapedefaults'] = v_layout.ShapeValidator()
        self._validators['showlegend'] = v_layout.ShowlegendValidator()
        self._validators['sliders'] = v_layout.SlidersValidator()
        self._validators['sliderdefaults'] = v_layout.SliderValidator()
        self._validators['spikedistance'] = v_layout.SpikedistanceValidator()
        self._validators['template'] = v_layout.TemplateValidator()
        self._validators['ternary'] = v_layout.TernaryValidator()
        self._validators['title'] = v_layout.TitleValidator()
        self._validators['titlefont'] = v_layout.TitlefontValidator()
        self._validators['updatemenus'] = v_layout.UpdatemenusValidator()
        self._validators['updatemenudefaults'] = v_layout.UpdatemenuValidator()
        self._validators['violingap'] = v_layout.ViolingapValidator()
        self._validators['violingroupgap'] = v_layout.ViolingroupgapValidator()
        self._validators['violinmode'] = v_layout.ViolinmodeValidator()
        self._validators['width'] = v_layout.WidthValidator()
        self._validators['xaxis'] = v_layout.XAxisValidator()
        self._validators['yaxis'] = v_layout.YAxisValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('angularaxis', None)
        self['angularaxis'] = angularaxis if angularaxis is not None else _v
        _v = arg.pop('annotations', None)
        self['annotations'] = annotations if annotations is not None else _v
        _v = arg.pop('annotationdefaults', None)
        self['annotationdefaults'
            ] = annotationdefaults if annotationdefaults is not None else _v
        _v = arg.pop('autosize', None)
        self['autosize'] = autosize if autosize is not None else _v
        _v = arg.pop('bargap', None)
        self['bargap'] = bargap if bargap is not None else _v
        _v = arg.pop('bargroupgap', None)
        self['bargroupgap'] = bargroupgap if bargroupgap is not None else _v
        _v = arg.pop('barmode', None)
        self['barmode'] = barmode if barmode is not None else _v
        _v = arg.pop('barnorm', None)
        self['barnorm'] = barnorm if barnorm is not None else _v
        _v = arg.pop('boxgap', None)
        self['boxgap'] = boxgap if boxgap is not None else _v
        _v = arg.pop('boxgroupgap', None)
        self['boxgroupgap'] = boxgroupgap if boxgroupgap is not None else _v
        _v = arg.pop('boxmode', None)
        self['boxmode'] = boxmode if boxmode is not None else _v
        _v = arg.pop('calendar', None)
        self['calendar'] = calendar if calendar is not None else _v
        _v = arg.pop('clickmode', None)
        self['clickmode'] = clickmode if clickmode is not None else _v
        _v = arg.pop('colorway', None)
        self['colorway'] = colorway if colorway is not None else _v
        _v = arg.pop('datarevision', None)
        self['datarevision'] = datarevision if datarevision is not None else _v
        _v = arg.pop('direction', None)
        self['direction'] = direction if direction is not None else _v
        _v = arg.pop('dragmode', None)
        self['dragmode'] = dragmode if dragmode is not None else _v
        _v = arg.pop('extendpiecolors', None)
        self['extendpiecolors'
            ] = extendpiecolors if extendpiecolors is not None else _v
        _v = arg.pop('font', None)
        self['font'] = font if font is not None else _v
        _v = arg.pop('geo', None)
        self['geo'] = geo if geo is not None else _v
        _v = arg.pop('grid', None)
        self['grid'] = grid if grid is not None else _v
        _v = arg.pop('height', None)
        self['height'] = height if height is not None else _v
        _v = arg.pop('hiddenlabels', None)
        self['hiddenlabels'] = hiddenlabels if hiddenlabels is not None else _v
        _v = arg.pop('hiddenlabelssrc', None)
        self['hiddenlabelssrc'
            ] = hiddenlabelssrc if hiddenlabelssrc is not None else _v
        _v = arg.pop('hidesources', None)
        self['hidesources'] = hidesources if hidesources is not None else _v
        _v = arg.pop('hoverdistance', None)
        self['hoverdistance'
            ] = hoverdistance if hoverdistance is not None else _v
        _v = arg.pop('hoverlabel', None)
        self['hoverlabel'] = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('hovermode', None)
        self['hovermode'] = hovermode if hovermode is not None else _v
        _v = arg.pop('images', None)
        self['images'] = images if images is not None else _v
        _v = arg.pop('imagedefaults', None)
        self['imagedefaults'
            ] = imagedefaults if imagedefaults is not None else _v
        _v = arg.pop('legend', None)
        self['legend'] = legend if legend is not None else _v
        _v = arg.pop('mapbox', None)
        self['mapbox'] = mapbox if mapbox is not None else _v
        _v = arg.pop('margin', None)
        self['margin'] = margin if margin is not None else _v
        _v = arg.pop('modebar', None)
        self['modebar'] = modebar if modebar is not None else _v
        _v = arg.pop('orientation', None)
        self['orientation'] = orientation if orientation is not None else _v
        _v = arg.pop('paper_bgcolor', None)
        self['paper_bgcolor'
            ] = paper_bgcolor if paper_bgcolor is not None else _v
        _v = arg.pop('piecolorway', None)
        self['piecolorway'] = piecolorway if piecolorway is not None else _v
        _v = arg.pop('plot_bgcolor', None)
        self['plot_bgcolor'] = plot_bgcolor if plot_bgcolor is not None else _v
        _v = arg.pop('polar', None)
        self['polar'] = polar if polar is not None else _v
        _v = arg.pop('radialaxis', None)
        self['radialaxis'] = radialaxis if radialaxis is not None else _v
        _v = arg.pop('scene', None)
        self['scene'] = scene if scene is not None else _v
        _v = arg.pop('selectdirection', None)
        self['selectdirection'
            ] = selectdirection if selectdirection is not None else _v
        _v = arg.pop('separators', None)
        self['separators'] = separators if separators is not None else _v
        _v = arg.pop('shapes', None)
        self['shapes'] = shapes if shapes is not None else _v
        _v = arg.pop('shapedefaults', None)
        self['shapedefaults'
            ] = shapedefaults if shapedefaults is not None else _v
        _v = arg.pop('showlegend', None)
        self['showlegend'] = showlegend if showlegend is not None else _v
        _v = arg.pop('sliders', None)
        self['sliders'] = sliders if sliders is not None else _v
        _v = arg.pop('sliderdefaults', None)
        self['sliderdefaults'
            ] = sliderdefaults if sliderdefaults is not None else _v
        _v = arg.pop('spikedistance', None)
        self['spikedistance'
            ] = spikedistance if spikedistance is not None else _v
        _v = arg.pop('template', None)
        _v = template if template is not None else _v
        if _v is not None:
            self['template'] = _v
        _v = arg.pop('ternary', None)
        self['ternary'] = ternary if ternary is not None else _v
        _v = arg.pop('title', None)
        self['title'] = title if title is not None else _v
        _v = arg.pop('titlefont', None)
        self['titlefont'] = titlefont if titlefont is not None else _v
        _v = arg.pop('updatemenus', None)
        self['updatemenus'] = updatemenus if updatemenus is not None else _v
        _v = arg.pop('updatemenudefaults', None)
        self['updatemenudefaults'
            ] = updatemenudefaults if updatemenudefaults is not None else _v
        _v = arg.pop('violingap', None)
        self['violingap'] = violingap if violingap is not None else _v
        _v = arg.pop('violingroupgap', None)
        self['violingroupgap'
            ] = violingroupgap if violingroupgap is not None else _v
        _v = arg.pop('violinmode', None)
        self['violinmode'] = violinmode if violinmode is not None else _v
        _v = arg.pop('width', None)
        self['width'] = width if width is not None else _v
        _v = arg.pop('xaxis', None)
        self['xaxis'] = xaxis if xaxis is not None else _v
        _v = arg.pop('yaxis', None)
        self['yaxis'] = yaxis if yaxis is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
