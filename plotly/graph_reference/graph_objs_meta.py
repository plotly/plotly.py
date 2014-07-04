#
# ----------------------- Plotly graph object meta ------------------------------
#
# Welcome to the ultimate reference of Plotly's JSON graph format.
#
# Philosophy:
#
# * ALL plotly keys should be placed a single JSON file.
#
# * A fully described key is an object with the keys:
#   (1) 'required', (2) 'type', (3) 'val_types', and (4) 'description',
#
#   - and additionally (5) streamable, (6) example and (7) code.
#
# * All keys that are contained in more than 1 object has a
#   corresponding shortcut function (`make_ `) or dictionary (`drop_ `).
#
# -------------------------------------------------------------------------------
#
# Contents -----------------
#
# Section -- Required modules
#
# Section  -- Shortcuts Definitions:
#
# * Inventory of value types repeated over several keys
#   - search for `$val_types`
#
# * Inventory of shortcuts for repeated keys of meta-generating functions
#   - search for `$shortcuts--` for top of the section
#   - search for e.g. `$shortcut-x` for shortcut of specific key
#
# Section -- Graph Objects Meta:
#
# * 'Trace' graph objects (search for `$graph-objs-meta-trace`):
#   - Scatter (search for `$scatter`)
#   - Bar ( `$bar`)
#   - Histogram ( `$histogram`)
#   - Bar ( `$box`)
#   - Heatmap ( `$heatmap`)
#   - Contour ( `$contour`)
#   - Histogram2d ( `$histogram2d`)
#   - Histogram2dContour ( `$histogram2dcontour`)
#   - Area ( `$Area`)
#
# * 'Auxiliary trace' graph objects ( `$graph-objs-meta-trace-aux`):
#   - ErrorY (search for `$error_y`)
#   - ErrorX ( `$error_x`)
#   - XBins ( `$xbins`)
#   - YBins ( `$ybins`)
#   - Contours ( `$contours`)
#   - Stream ( `$stream`)
#
# * 'Style' graph objects ( `$graph-objs-meta-style`)
#   - Marker (search for `$marker`)
#   - Line ( `$line`)
#   - Font ( `$font`)
#
# * 'Axis' graph objects ( `$graph-objs-meta-layout-axis`)
#   - XAxis (search for `$xaxis`)
#   - YAxis ( `$yaxis`)
#   - RadialAxis  ( `$radialaxis`)
#   - AngularAxis ( `$angularaxis`)
#
# * Other 'auxiliary layout' graph objects ( `$graph-objs-meta-layout-aux`)
#   - Legend (search for `$legend`)
#   - ColorBar ( `$colorbar`)
#   - Margin ( `$margin`)
#   - Annotation ( `$annotation`)
#
# * Layout ( `$layout`)
#
# * Figure ( `$figure`)
#
# * Other graph objects ( `$graph-objs-meta-others`)
#   - Data (search for `$plotlydata`)
#   - Annotations ( `$annotations`)
#   - Trace ( `$trace`)
#   - PlotlyList ( `$plotlylist`)
#   - PlotlyDict ( `$plotlydict`)
#   - PlotlyTrace ( `$plotlytrace`)
#
# Section -- Write to JSON
#
# ===============================================================================

## Required modules

# Use ordered dictionaries to list graph object keys
from collections import OrderedDict

# -------------------------------------------------------------------------------


## Shortcut definitions

# $val_types
#
# List of value types repeated over several keys

# $val_types-number
# Use this to format key accepting numbers
def _number(lt=None, le=None, gt=None, ge=None, list=False):
    if any((all((lt is not None, le is not None)),
            all((gt is not None, ge is not None)))):
        raise Exception("over-constrained number definition")
    if [lt, le, gt, ge] == [None, None, None, None]:
        out = "number"
    elif lt is not None and ([ge, gt] == [None, None]):
        out = "number: x < {lt}".format(lt=lt)
    elif le is not None and ([ge, gt] == [None, None]):
        out = "number: x <= {le}".format(le=le)
    elif gt is not None and ([le, lt] == [None, None]):
        out = "number: x > {gt}".format(gt=gt)
    elif ge is not None and ([le, lt] == [None, None]):
        out = "number: x >= {ge}".format(ge=ge)
    elif (lt is not None) and (gt is not None):
        out = "number: x in ({gt}, {lt})".format(gt=gt, lt=lt)
    elif (lt is not None) and (ge is not None):
        out = "number: x in [{ge}, {lt})".format(ge=ge, lt=lt)
    elif (le is not None) and (gt is not None):
        out = "number: x in ({gt}, {le}]".format(gt=gt, le=le)
    elif (le is not None) and (ge is not None):
        out = "number: x in [{ge}, {le}]".format(le=le, ge=ge)
    if list:
        return out+", or list of these numbers"
    else:
        return out

# $val_types-required-when
# Use this for conditional booleans (e.g. for 'required' values)
def _required_when(when):
    if type(when)==str:
        to_be = 'is'
    elif type(when)==list:
        when=','.join(when[0:-1])+' and '+when[-1]
        to_be = 'are'
    return " when {key} {to_be} unset".format(key=when,to_be=to_be)

# $val_types-dict
val_types = dict(
    bool="boolean: True | False",
    required_when= _required_when,
    color="string describing color",
    string="string",
    number= _number,
    data_array="array-like of numbers, strings, datetimes",
    string_array="array-like of strings",
    color_array="array-like of string describing color",
    matrix="matrix-like: list of lists, numpy.matrix",
    object="dictionary-like",
)

# -------------------------------------------------------------------------------

# $shortcuts--
#
# List of shortcuts for repeated keys of meta-generating functions

# $shortcut-shortcuts

# $shortcut-output
def output(_required, _type, _val_types, _description, **kwargs):
    '''
    Outputs a dictionary of key-value pairs, given the keys.
    (pos. arg. 1) _required: value of 'required' key
    (pos. arg. 2) _type: value of 'type' key
    (pos. arg. 3) _val_types: value of 'val_types' key
    (pos. arg. 4) _description: value of 'description' key
    (keyword args) kwargs: dictionary of additional key-value pairs
    '''
    _dict = dict(
        required= _required,
        type= _type,
        val_types= _val_types,
        description= _description)
    if len(kwargs):
        for k, v in kwargs.iteritems():
            _dict[k] = v
    return _dict

# $shortcut-x
def make_x(obj):
    _required=dict(
        scatter=val_types['required_when'](["'y'","'r'","'t'"]),
        bar=val_types['required_when'](["'y'","'r'","'t'"]),
        histogram=val_types['required_when'](["'y'","'r'","'t'"]),
        box=False,
        heatmap=False,
        contour=False,
        histogram2d=True,
        histogram2dcontour=True,
    )
    _type='data'
    _val_types=val_types['data_array']
    _description=dict(
        scatter="The x coordinates of the points of this scatter trace. "
            "If 'x' is linked to an list or array of strings, "
            "then the x coordinates are integers [0,1,2,3, ...] labeled "
            "on the x-axis by the list or array of strings linked to 'x'.",
        bar="The x coordinates of the bars. "
            "If 'x' is linked to an list or array of strings, "
            "then the x coordinates are integers [0,1,2,3, ...] labeled "
            "on the x-axis by the list or array of strings linked to 'x'. "
            "If 'y' is not set, the bars are plotted horizontally, "
            "with their length determined by the list or array linked to 'x'.",
        histogram="The data sample to be binned (done by Plotly) on the x-axis "
                  "and plotted as vertical bars.",
        box="Usually, you do not need to set this value as "
            "plotly will handle box locations for you. However "
            "this allows you to have fine control over the "
            "location data for the box. Unlike making a bar, "
            "a box plot is made of many y values. Therefore, "
            "to give location data to the values you place in "
            "'y', the length of 'x' must equal the length of 'y'. "
            "when making multiple box plots, you can concatenate "
            "the data sets for each box into a single 'y' array. "
            "then, the entries in 'x' define which box plot each "
            "entry in 'y' belongs to. When making a single box "
            "plot, you must set each entry in 'x' to the same "
            "value, see 'x0' for a more practical way to handle "
            "this case. If you don't include 'x', the box will "
            "simply be assigned a location.",
        heatmap="This array-like value contains the horizontal coordinates "
                "referring to the columns of the 'z' matrix. "
                "if strings, the x-labels are spaced evenly."
                "if the dimensions of z are (n x m), "
                "the length of the 'x' array should be 'm'.",
        histogram2d="The data sample to be binned on the x-axis and "
                    "whose distribution (computed by Plotly) will correspond "
                    "to the x-coordinates of this 2D histogram trace."
    )
    _description['contour']= _description['heatmap']
    _description['histogram2dcontour']= _description['histogram2d']
    _streamable=True
    if obj=='box':      # TO DO! Sub 'code' for example link?
        _code=''.join([">>> y0 = [1,2,3,1,1]",
                       ">>> y1 = [3,2,1,2,3]",
                       ">>> y = y0+y1  # N.B. list not numpy arrays here",
                       ">>> x = [0,0,0,0,0,1,1,1,1,1]  # len(x) == len(y)",
                       ">>> Box(y=y, x=x, name='two boxes SHARE this name.')"
                      ])
        return output(_required[obj],_type,_val_types,_description[obj],
                      streamable=_streamable,code=_code)
    else:
        return output(_required[obj],_type,_val_types,_description[obj],
                      streamable=_streamable)

# $shortcut-y
def make_y(obj):
    _required=dict(
        scatter=val_types['required_when'](["'x'","'r'","'t'"]),
        bar=val_types['required_when'](["'x'","'r'","'t'"]),
        histogram=val_types['required_when'](["'x'","'r'","'t'"]),
        box=True,
        heatmap=False,
        contour=False,
        histogram2d=True,
        histogram2dcontour=True,
    )
    _type='data'
    _val_types=val_types['data_array']
    _description=dict(
        scatter="The y coordinates of the points of this scatter trace. "
                "If 'y' is linked to an list or array of strings, "
                "then the y coordinates are integers [0,1,2,3, ...] labeled "
                "on the y-axis by the list or array of strings linked to 'y'.",
        histogram="The data sample to be binned (done by Plotly) on the y-axis "
                  "and plotted as horizontal bars.",
        bar="The y coordinates of the bars. "
            "If 'y' is linked to an list or array of strings, "
            "then the y coordinates are integers [0,1,2,3, ...] labeled "
            "on the y-axis by the list or array of strings linked to 'y'. "
            "If 'x' is not set, the bars are plotted vertically, "
            "with their length determined by the list or array linked to 'y'.",
        box="This array is used to define an individual "
            "box plot, or, a concatenation of multiple boxplots. "
            "Statistics from these numbers define the bounds of "
            "the box, the length of the whiskers, etc. For "
            "details on defining multiple boxes with locations "
            "see 'x'.",
        heatmap="This array-like value contains the vertical coordinates "
                "referring to the rows of the 'z' matrix. "
                "If strings, the y-labels are spaced evenly."
                "If the dimensions of z are (n x m), "
                "the length of the 'y' array should be 'n'.",
        histogram2d="The data sample to be binned on the y-axis and "
                    "whose distribution (computed by Plotly) will correspond "
                    "to the y-coordinates of this 2D histogram trace."
    )
    _description['contour']= _description['heatmap']
    _description['histogram2dcontour']= _description['histogram2d']
    _streamable=True
    return output(_required[obj],_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcut-z
def make_z(obj):
    _required=False # TO DO! How to phrase this?
    _type='data'
    _val_types=val_types['matrix']
    _description=dict(
        heatmap="The data that describes the mapping. "
                "The dimensions of the 'z' matrix are (n x m) "
                "where there are 'n' ROWS defining the "
                "number of partitions along the y-axis; this is equal to the "
                "length of the 'y' array. "
                "There are 'm' COLUMNS defining the number "
                "of partitions along the x-axis; "
                "this is equal to the length of the 'x' array. "
                "Therefore, the color of the cell z[i][j] is mapped to "
                "the ith partition of the y-axis (starting from the bottom "
                "of the plot) and the jth partition of the x-axis "
                "(starting from the left of the plot). "
                "In Python, a (non-numpy) matrix is best thought of as "
                "a list of lists (of lists, of lists, etc.). "
                "Therefore, running len(z) will give you the number "
                "of ROWS and running len(z[0]) will give you "
                "the number of COLUMNS. If you ARE using numpy, then running "
                "z.shape will give you the tuple, (n, m), e.g., (3, 5)."
    )
    _streamable=True
    _description['contour']= _description['heatmap']
    return output(_required,_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcut-r
def make_r(obj):
    _required=dict(
        scatter=val_types['required_when'](["'x'","'y'"]),
        bar=val_types['required_when'](["'x'","'y'"]),
        area=True
    )
    _type='data'
    _val_types=val_types['data_array']
    _description=dict(  # TO DO! Better description of how the coords work
        scatter="For Polar charts only. "
                "The radial coordinates of the points in this "
                "polar scatter trace.",
        bar="For Polar charts only. "
            "The radial coordinates of the bars in this polar bar trace",
        area="The radial coordinates of the circle sectors in this "
             "polar area trace.",
    )
    _streamable=True
    return output(_required[obj],_type,_val_types,_description[obj],
                 streamable=_streamable)

# $shortcut-t
def make_t(obj):
    _required=dict(
        scatter=val_types['required_when'](["'x'","'y'"]),
        bar=val_types['required_when'](["'x'","'y'"]),
        area=True
    )
    _type='data'
    _val_types=val_types['data_array']
    _description=dict(
        scatter="For Polar charts only. "
                "The angular coordinates of the points in this "
                "polar scatter trace.",
        bar="For Polar charts only. "
            "The angular coordinates of the bars in this polar bar trace.",
        area="The angular coordinates of the circle sectors in this "
             "polar area trace.",
    )
    _streamable=True
    return output(_required[obj],_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcuts-coordinates-alternative

# $shortcut-x0y0 $shortcut-x0 | $shortcut-y0
def make_x0y0(obj, x_or_y=False):
    _required=False
    _type='plot_info'  # TO DO! 'data' maybe?
    _val_types=val_types['number']()
    S={'x':['x',], 'y':['y',], False:['',]}
    s=S[x_or_y]
    _description=dict( # TO DO! Add scatter?
        box="The location of this box. When 'y' defines a single "
            "box, 'x0' can be used to set where this box is "
            "centered on the x-axis. If many boxes are set to "
            "appear at the same 'x0' location, they will form a "
            "box group.",
        heatmap="The location of the first coordinate of the {S0}-axis. "
                "Use with 'd{S0}' an alternative to an '{S0}' list/array. "
                "Has no effect if '{S0}' is set.".format(S0=s[0])
    )
    _description['contour']= _description['heatmap']
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-dxdy | $shortcut-dx | $shortcut-dy
def make_dxdy(obj, x_or_y=False):
    _required=False
    _type='plot_info'  # TO DO! 'data' maybe?
    _val_types=val_types['number']()
    S={'x':['x',], 'y':['y',], False:['',]}
    s=S[x_or_y]
    _description=dict( # TO DO! Add scatter?
        heatmap="Spacing between {S0}-axis coordinates. "
                "Use with '{S0}0' an alternative to an '{S0}' list/array. "
                "Has no effect if '{S0}' is set.".format(S0=s[0]),
    )
    _description['contour']= _description['heatmap']
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-xytype | $shortcut-xtype | $shortcut-ytype
def make_xytype(obj, x_or_y):
    _required=False
    _type='data'
    _val_types="'array' | 'scaled'",
    S={'x':['x','horizontal'], 'y':['y','vertical'], False:['',]}
    s=S[x_or_y]
    _description=dict(
        heatmap="If set to 'scaled' and '{S0}' is linked to a list/array, "
                "then the {S1} labels are scaled to a list "
                "of integers of unit step "
                "starting from 0.".format(S0=s[0],S1=s[1])
    )
    _description['contour']= _description['heatmap']
    return output(_required,_type,_val_types,_description[obj])

# $shortcuts-trace-aux

# $shortcut-text
def make_text(obj):
    _required=False
    _type='data'
    _val_types=val_types['data_array']
    _description=dict(
        scatter="The text elements associated with every (x,y) pair on "
                "the scatter plot. If the scatter 'mode' doesn't "
                "include 'text' then text will appear on hover only. If "
                "'text' is included in 'mode', the entries in 'text' "
                "will be rendered on the plot at the locations "
                "specified by their corresponding coordinate pair.",
        bar="The text elements associated with every bar in this trace "
            "The entries in 'text' will be rendered on the plot at the "
            "at the top of the bars in this trace."
    )
    _description['histogram']=_description['bar']
    _streamable=True
    return output(_required,_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcut-error | $shortcut-error_y | $shortcut-error_x
def make_error(obj, x_or_y):
    _required=False
    _type='object'
    _val_types=val_types['object']
    S={'x':['horizontal','x'], 'y':['vetical','y']}
    s=S[x_or_y]
    _description=dict(
        scatter="A dictionary-like object describing "
                "the {S0} error bars (i.e. along the {S1}-axis) "
                "that can be drawn "
                "from the (x, y) coordinates.".format(S0=s[0],S1=s[1]),
        bar="A dictionary-like object describing the {S0} error bars "
            "(i.e. along the {S1}-axis) that can "
            "be drawn from bar tops.".format(S0=s[0],S1=s[1])
    )
    _description['histogram']= _description['bar']
    _streamable=True
    return output(_required,_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcuts-trace-style

# $shortcut-orientation
def make_orientation(obj):
    _required=False
    _type='style'   # TO DO! 'plot_info' instead?
    _val_types=val_types['data_array']
    _description=dict(
        bar="This defines the direction of the bars. "
            "If set to 'v', the length of each bar will run vertically. "
            "If set to 'h', the length of each bar will run horizontally",
        histogram="Web GUI Artifact. Histogram orientation is determined "
                  "by which of 'x' or 'y' the data sample is linked to."
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-marker
def make_marker(obj):
    _required=False
    _type='object'
    _val_types=val_types['object']
    _description=dict(
        scatter="A dictionary-like object containing marker style "
                "parameters for this scatter trace. "
                "Has an effect only if 'mode' contains 'markers'.",
        bar="A dictionary-like object containing marker style "
            "parameters for this bar trace, for example, "
            "the bars' fill color, border width and border color.",
        box="A dictionary-like object containing marker style "
            "parameters for this the box points of box trace. "
            "Has an effect only 'boxpoints' is set to 'outliers' or 'all'.",
        area="A dictionary-like object containing marker style "
             "of the area sectors of this trace, for example the sector fill "
             "color and sector boundary line width and sector boundary color."
    )
    _description['histogram']= _description['bar']
    _streamable=True
    return output(_required,_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcut-line
def make_line(obj):
    _required=False
    _type='object'
    _val_types=val_types['object']
    _description=dict(
        scatter="A dictionary-like object containing line style "
                "parameters for this scatter trace. "
                "Has an effect only if 'mode' contains 'lines'.",
        bar="Artifact. Has no effect.",
        box="A dictionary-like object containing line style "
            "parameters for the border of this box trace "
            "(including the whiskers).",
        contour="A dictionary-like object containing line style "
                "parameters for contour lines of this contour trace "
                "(including line width, dash, color and smoothing level). "
                "Has no an effect if 'showlines' is set to False in Contours.",
        marker="A dictionary-like object describing the line belonging to "
               "the marker. For example, the line around each point "
               "in a scatter trace or the line around each bar in a "
               "bar trace.",
    )
    _description['histogram']= _description['bar']
    _description['histogram2dcontour']= _description['contour']
    _streamable=True
    return output(_required,_type,_val_types,_description[obj],
                  streamable=_streamable)

# $shortcut-opacity
def make_opacity(marker=False):
    _required=False
    _type="style"
    if not marker:
        _val_types=val_types['number'](ge=0, le=1)
        _description=''.join(["Sets the opacity, or transparency, ",
                              "of the entire object, ",
                              "also known as the alpha channel of colors. ",
                              "If the object's color is given in terms of ",
                              "'rgba' color ",
                              "model, 'opacity' is redundant."
                             ])
    else:
        _val_types=val_types['number'](ge=0, le=1, list=True)
        _description=''.join(["Sets the opacity, or transparency ",
                              "also known as the alpha channel of colors) ",
                              "of the marker points. ",
                              "If the marker points' ",
                              "color is given in terms of 'rgba' ",
                              "color model, this does not need to be defined. ",
                              "If 'opacity' is linked to a list or an array ",
                              "of numbers, opacity values are mapped to ",
                              "individual marker points in the ",
                              "same order as in the data lists or arrays."
                             ])
    return output(_required,_type,_val_types,_description)

# $shortcut-textfont
def make_textfont(obj):
    _required=False
    _type='object'
    _val_types=val_types['object']
    _description=dict(
        scatter="A dictionary-like object describing the font style "
                "of this scatter trace's text elements. This only has "
                "an effect if 'text' is an array of strings and "
                "'mode' is set to include 'text'.",
        bar="Not currently supported, has no effect."
    )
    _description['histogram']= _description['bar']
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-font
def make_font(obj):
    _required=False
    _type='object'
    _val_types=val_types['object']
    _description=dict(
        legend="A dictionary-like object describing the font "
               "settings within the legend.",
        annotation="A dictionary-like object describing the font "
                   "settings within this annotation.",
        layout="A dictionary-like object describing the global font "
               "settings for this figure (e.g. all axis titles and labels)."
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcuts-for-all-traces

# $shortcut-name
drop_name=dict(
    required=False,
    type='data',
    val_types=val_types['string'],
    description="The label associated with this trace. "
                "This name will appear in the legend, on hover and "
                "in the column header in the online spreadsheet."
)

# $shortcut-stream
drop_stream=dict(
    required=False,
    type='plot_info',
    val_types=val_types['object'],
    description="The stream dictionary-like object that initializes traces as "
                "writable-streams, for use with the real-time streaming "
                "API. Learn more here:\n"
                "https://plot.ly/python/streaming/"
)

# $shortcut-visible
drop_visible=dict(
    required=False,
    type='plot_info',
    val_types=val_types['bool'],
    description="Toggles whether or not this object will actually be "
                "visible in the rendered figure."
)

# $shortcuts-trace-and-layout

# $shortcut-showlegend
def make_showlegend(trace=False, layout=False):
    _required=False
    _type='style'
    _val_types=val_types['bool']
    if trace:
        _description=''.join(["Toggle whether or not this trace will be ",
                              "labeled in the legend."
                             ])
    elif layout:
        _description=''.join(["Toggle whether or not the legend will "
                              "be shown in this figure."
                             ])
    return output(_required,_type,_val_types,_description)

# $shortcut-axis | $shortcut-xaxis | $shortcut-yaxis
def make_axis(x_or_y, trace=False, layout=False):
    _required=False
    S={'x':['x','horizontal','X'], 'y':['y','vertical','Y']}
    s=S[x_or_y]
    if trace:
        _type='plot_info'
        _val_types="'{S0}1' | '{S0}2' | '{S0}3' | etc.".format(S0=s[0])
        _description=''.join(["This key determines which {S0}-axis ",
                              "the {S0}-coordinates of this trace will ",
                              "reference in the figure.  Values '{S0}1' ",
                              "and '{S0}' reference to layout['{S0}axis'], ",
                              "'{S0}2' references layout['{S0}axis2'], and ",
                              "so on. Note that '{S0}1' will always refer to ",
                              "layout['{S0}axis'] or layout['{S0}axis1'], ",
                              "they are the same."
                             ]).format(S0=s[0])
    elif layout:
        _type='object'
        _val_types=val_types['object']
        _description=''.join(["A dictionary-like object describing an ",
                              "{S0}-axis (i.e. an {S1} axis). ",
                              "The first {S2}Axis object can be entered into "
                              "layout by linking it to '{S0}axis' OR ",
                              "'{S0}axis1', both keys are identical to Plotly.  ",
                              " To create references other {S0}-axes, ",
                              "you need to define them in the layout ",
                              "dictionary-like object using keys '{S0}axis2', ",
                              "'{S0}axis3' and so on."
                             ]).format(S0=s[0],S1=s[1],S2=s[2])
    return output(_required,_type,_val_types,_description)

# $shortcut-type
def make_type(trace=False, axis=False, error=False):
    _required=False
    _type='plot_info'
    if trace:
        _val_types=trace
        _description=''.join(["Plotly identifier for this data's trace type. ",
                              " This defines how this ",
                              " data dictionary will be handled. ",
                              " For example, 'scatter' type expects ",
                              " x and y data-arrays corresponding to ",
                              "(x, y) coordinates whereas a 'histogram' ",
                              "only requires a single x or y array ",
                              " and a 'heatmap' type requires a z matrix."
                             ])
    elif axis:  # TO DO! Info on category
        _val_types="'linear' | 'log' | 'category'"
        _description="Defines format of this axis."
    elif error:
        _type='plot_info'  # TO DO! 'data' maybe?
        _val_types="'data' | 'percent' | 'constant' | 'sqrt'"
        _description=''.join(["Specify how the 'value' or 'array' key in ",
                              "this error bar will be used to render the bars. ",
                              "Using 'data' will set error bar lengths to the ",
                              "actual numbers specified in 'array'.  ",
                              "Using 'percent' will set bar lengths to the ",
                              "percent of error associated with 'value'. ",
                              "Using 'constant' will set each error ",
                              "bar length to the single value specified ",
                              "in 'value'. Using 'sqrt' will set ",
                              "each error bar length to the square root of ",
                              "the x data at each point ('value' and 'array' ",
                              "do not apply)."
                             ])
    return output(_required,_type,_val_types,_description)

# $shortcuts-histograms-specs

# $shortcut-histnorm
drop_histnorm=dict(
    required=False,
    type='plot_info',
    val_types="'' (or 'count') | 'percent' | 'probability' | 'density' | "
              "'probability density'",
    description="If histnorm is not specified, or histnorm='' ("
                "empty string), the height of each bar displays the "
                "frequency of occurrence, i.e., the number of times this "
                "value was found in the corresponding bin. If "
                "histnorm='percent', the height of each bar displays the "
                "percentage of total occurrences found within the "
                "corresponding bin. If histnorm='probability', the height "
                "of each bar displays the probability that an event will "
                "fall into the corresponding bin. If histnorm='density', "
                "the height of each bar is equal to the number of "
                "occurrences in a bin divided by the size of the bin "
                "interval such that summing the area of all bins will "
                "yield the total number of occurrences. If "
                "histnorm='probability density', the height of each bar "
                "is equal to the number of probability that an event will "
                "fall into the corresponding bin divided by the size of "
                "the bin interval such that summing the area of all bins "
                "will yield 1, i.e. an event must fall into one of the "
                "bins."
)

# $shortcut-autobin | $shortcut-autobinx | $shortcut-autobiny
def make_autobin(x_or_y):
    _required=False
    _type='plot_info'
    _val_types=val_types['bool']
    S={'x':['x','X'], 'y':['y','Y']}
    s=S[x_or_y]
    _description=''.join(["Toggle whether or not the {S0}-axis bin parameters ",
                          "are picked automatically by Plotly. ",
                          "Once 'autobin{S0}' is set to False, the {S0}-axis ",
                          "bins parameters can be declared ",
                          "in the {S1}Bins object."
                         ]).format(S0=s[0],S1=s[1])
    return output(_required,_type,_val_types,_description)

# $shortcut-nbins | $shortcut-nbinsx | $shortcut-nbinsy
def make_nbins(x_or_y):
    _required=False
    _type='style'    # TO DO! Shouldn't this be 'plot_info' ?
    _val_types=val_types['number'](gt=0)
    S={'x':['x',], 'y':['y',]}
    s=S[x_or_y]
    _description=''.join(["Specifies the number of {S0}-axis bins. ",
                          "No need to set 'autobin{S0}' to False ",
                          "for 'nbins{S0}' to apply."
                         ]).format(S0=s[0])
    return output(_required,_type,_val_types,_description)

# $shortcut-bins | $shortcut-xbins | $shortcut-ybins
def make_bins(x_or_y):
    _required=False
    _type='object'
    _val_types=val_types['object']
    S={'x':['x',], 'y':['y',]}
    s=S[x_or_y]
    _description=''.join(["A dictionary-like object defining the parameters ",
                          "of {S0}-axis bins of this trace, for example, ",
                          "the bin width and the bins' starting and  ",
                          "ending value. Has an effect only if ",
                          "'autobin{S0}'=False."
                         ]).format(S0=s[0])
    return output(_required,_type,_val_types,_description)

# $shortcuts-2d-specs

# $shortcut-colorbar
drop_colorbar=dict(
    required=False,
    type='object',
    val_types=val_types['object'],
    description="A dictionary-like object defining the parameters of "
                "the color bar associated with this trace "
                "(including its title, length and width)."
)

# $shortcut-scl
drop_scl=dict(
    required=False,
    type="style",
    val_types="array_like of value-color pairs | "
              "'Greys' | 'Greens' | 'Bluered' | 'Hot' | "
              "'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | "
              "'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'",
    description="The color scale. The strings are pre-defined color "
                "scales. For custom color scales, define a list of "
                "color-value pairs, where the first element of the pair "
                "corresponds to a normalized value of z from 0-1, "
                "i.e. (z-zmin)/ (zmax-zmin), and the second element of pair "
                "corresponds to a color.",
    examples=["Greys", [[0, "rgb(0,0,0)"], [1, "rgb(255,255,255)"]],
              [[0, "rgb(8, 29, 88)"], [0.125, "rgb(37, 52, 148)"],
               [0.25, "rgb(34, 94, 168)"], [0.375, "rgb(29, 145, 192)"],
               [0.5, "rgb(65, 182, 196)"], [0.625, "rgb(127, 205, 187)"],
               [0.75, "rgb(199, 233, 180)"], [0.875, "rgb(237, 248, 217)"],
               [1, "rgb(255, 255, 217)"]]]
)

# $shortcut-zauto
drop_zauto=dict(
    required=False,
    type='style',
    val_types=val_types['bool'],
    description="Toggle whether or not the default values "
                "of 'zmax' and 'zmax' can be overwritten."
)

# $shortcut-zminmax | $shortcut-zmin | $shortcut-zmax
def make_zminmax(min_or_max):
    _required=False
    _type='style'
    _val_types=val_types['number']()
    S={'min': 'minimum', 'max': 'maximum'}
    s=S[min_or_max]
    _description=''.join(["The value used as the {S0} in the color scale ",
                          "normalization in 'scl'. ",
                          "The default value is the {S0} of the ",
                          "'z' data values."
                         ]).format(S0=s)
    return output(_required,_type,_val_types,_description)

# $shortcut-reversescl
drop_reversescl=dict(
    required=False,
    type='style',
    val_types=val_types['bool'],
    description="Toggle whether or not the color scale will be reversed."
)

# $shortcut-showscale
drop_showscale=dict(
    required=False,
    type='style',
    val_types=val_types['bool'],
    description="Toggle whether or not the color scale associated with "
                "this mapping will be shown alongside the figure."
)

# $shortcuts-2d-specs-more

# $shortcut-zsmooth  # TO DO! Describe the 2 algorithms
drop_zsmooth=dict(
    required=False,
    type='style',
    val_types=" False | 'best' | 'fast' ",
    description="Choose between algorithms ('best' or 'fast') "
                "to smooth data linked to 'z'. "
                "The default value is False "
                "corresponding to no smoothing."
)

# $shortcut-autocontour
drop_autocontour=dict(
    required=False,
    type='style',
    val_types=val_types['bool'],
    description="Toggle whether or not the contour parameters are picked "
                "automatically by Plotly. "
                "If False, declare the contours parameters "
                "in the Contours object."
)

# $shortcut-ncontours
drop_ncontours=dict(
    required=False,
    type='style',
    val_types=val_types['number'](gt=1),
    description="Specifies the number of contours lines "
                "in the contour plot. "
                "No need to set 'autocontour' to False for 'ncontours' "
                "to apply."
)

# $shortcut-contours
drop_contours=dict(
    required=False,
    type='object',
    val_types=val_types['object'],
    description="A dictionary-like object defining the parameters of "
                "the contours of this trace."
)

# $shortcuts-color

# $example-color
examples_color = ["'green'", "'rgb(0, 255, 0)'",
                 "'rgba(0, 255, 0, 0.3)'",
                 "'hsl(120,100%,50%)'",
                 "'hsla(120,100%,50%,0.3)'"]

# $shortcut-color
def make_color(obj):
    _required=False
    _type='style'
    if obj=='marker':
        _val_types=val_types['color_array']
    else:
        _val_types=val_types['color']
    _description=dict(
        marker="Sets the color of the face of the marker object. "
               "If 'color' is linked to a list or an array of numbers, "
               "color values are mapped to individual marker points "
               "in the same order as in the data lists or arrays. "
               "To set the color of the marker's bordering line, "
               "use the 'line' key in Marker.",
        line="Sets the color of the line object. "
             "If linked within 'marker', sets the color of the marker's "
             "bordering line. "
             "If linked within, 'contours', sets the color of the "
             "contour lines.",
        font="Sets the color of the font. "
             "If linked in the first level of the layout object, set the "
             "color of the global font.",
        error="Sets the color of the error bars."
    )
    _streamable=True
    return output(_required,_type,_val_types,_description[obj],
                  streamable=_streamable,examples=examples_color)

# $shortcut-fillcolor
def make_fillcolor(obj):
    _required=False
    _type='style'
    _val_types=val_types['color']
    _description=dict(
            scatter="Sets the color that will appear "
                    "in the specified fill area (set in 'fill'). "
                    "Has no effect if 'fill' is set to 'none'.",
            box="Sets the color of the box interior."
    )
    return output(_required,_type,_val_types,_description[obj],
                  examples=examples_color)

# $shortcut-outlinecolor
def make_outlinecolor(obj):
    _required=False
    _type='style'
    _val_types=val_types['color']
    _description=dict(
        font="For polar chart only. Sets the color of the text's outline.",
        colorbar="The color of the outline surrounding this colorbar."
    )
    return output(_required,_type,_val_types,_description[obj],
                  examples=examples_color)

# $shortcut-bgcolor
def make_bgcolor(obj):
    _required=False
    _type='style'
    _val_types=val_types['color']
    _description=dict(
        legend="Sets the background (bg) color for the legend.",
        colorbar="Sets the background (bg) color for this colorbar.",
        annotation="Sets the background (bg) color for this annotation."
    )
    return output(_required,_type,_val_types,_description[obj],
                  examples=examples_color)

# $shortcut-bordercolor
def make_bordercolor(obj):
    _required=False
    _type='style'
    _val_types=val_types['color']
    _description=dict(
        legend="Sets the enclosing border color for the legend.",
        colorbar="Sets the color of the enclosing boarder of this colorbar.",
        annotation="The color of the enclosing boarder of this annotation."
    )
    return output(_required,_type,_val_types,_description[obj],
                  examples=examples_color)

# $shortcuts-dimensions

# $shortcut-size
def make_size(obj, x_or_y=False):
    _required=False
    _type=dict(
        marker='style',
        font='style',
        bins='plot_info',
        contours='plot_info'
    )
    if obj=='marker':
        _val_types=val_types['number'](gt=0,list=True)
    else:
        _val_types=val_types['number'](gt=0)
    S={'x': ['x',], 'y': ['y',], False:['',]}
    s=S[x_or_y]
    _description=dict(
        marker="Sets the size of the markers (in pixels). "
               "If 'size' is linked to a list or an array of numbers, "
               "size values are mapped to individual marker points "
               "in the same order as in the data lists or arrays.",
        font="Sets the size of font."
             "If linked in the first level of the layout object, set the "
             "color of the global font.",
        bins="Sets the size (i.e. their width) of each "
             "{S0}-axis bin.".format(S0=s[0]),
        contours="Sets the size of each contour level."
    )
    _streamable=True
    return output(_required,_type[obj],_val_types,_description[obj],
                  streamable=_streamable)

# $shortcut-startend | $shortcut-start | $shortcut-end
def make_startend(obj, start_or_end, x_or_y=False):
    _required=False
    _type='plot_info'
    _val_types=val_types['number'](gt=0)
    S_se={'start':['first','starting'], 'end':['last','end']}
    s_se=S_se[start_or_end]
    S_xy={'x': ['x',], 'y': ['y',], False:['',]}
    s_xy=S_xy[x_or_y]
    _description=dict(
        bins="Sets the {S_se1} point on the {S_xy0}-axis for the {S_se0} "
             "bin.".format(S_se0=s_se[0],S_se1=s_se[1],S_xy0=s_xy[0]),
        contours="Sets the value of the {S_se0} "
                 "contour level.".format(S_se0=s_se[0])
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-width
def make_width(obj):
    _required=False
    _type='style'
    _val_types=val_types['number'](ge=0)
    _description=dict(
        line="Sets the width (in pixels) of the line object.",
        error="Sets the width (in pixels) of the cross-bar at both ends of "
              "the error bars.",
        figure="The width in pixels of the figure you're creating."
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-thickness
def make_thickness(obj, x_or_y=False):
    _required=False
    _type='style'
    _val_types=val_types['number'](ge=0)
    S={'x': ['x',], 'y': ['y',], False:['',]}
    s=S[x_or_y]
    _description=dict(
        error="Sets the line thickness of the {S0} error bars.".format(S0=s[0]),
        colorbar="Sets the thickness of the line surrounding the colorbar."
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-borderwidth
def make_borderwidth(obj):
    _required=False
    _type='style'
    _val_types=val_types['number'](ge=0)
    _description=dict(
        legend="Sets the width of the border enclosing for the legend.",
        colorbar="Sets the width of the boarder enclosing this colorbar",
        annotation="Sets the width of the boarder enclosing this annotation"
    )
    return output(_required,_type,_val_types,_description[obj])


# $shortcuts-layout-misc

# $shortcut-title
def make_title(obj, x_or_y=False):
    _required=False
    _type='plot_info'
    _val_types=val_types['string']
    _description=dict(
            axis="The {}-axis title.".format(x_or_y),
            colorbar="The title of the colorbar.",
            layout="The title of the figure."
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcut-titlefont
def make_titlefont(obj, x_or_y=False):
    _required=False
    _type='plot_info'
    _val_types=val_types['string']
    _description=dict(
            axis="A dictionary-like object describing the font "
                 "settings of the {}-axis title.".format(x_or_y),
            colorbar="A dictionary-like object describing the font "
                     "settings of the colorbar title.",
            layout="A dictionary-like object describing the font "
                   "settings of the figure's title.",
    )
    return output(_required,_type,_val_types,_description[obj])

# $shortcuts-axis-other

# $shortcut-range
def make_range(what_axis):
    _required=False
    _type='style'          # TO DO! changed this!!!  was plot_info
    _val_types="number array of length 2"
    _description=''.join(["Defines the start and end point of "
                          "this {} axis."
                         ]).format(what_axis)
    _examples=[[-13, 20], [0, 1]]
    return output(_required,_type,_val_types,_description,
                  examples=_examples)

# $shortcut-domain
def make_domain(what_axis):
    _required=False
    _type='plot_info'
    _val_types="number array of length 2"
    _description=''.join(["Sets the domain of this {S} axis. "
                          "The available space "
                          "for this {S} axis to live in is  "
                          "from 0 to 1."
                         ]).format(S=what_axis)
    _examples=[[-13, 20], [0, 1]]
    return output(_required,_type,_val_types,_description,
                  examples=_examples)

# $shortcut-showline
drop_showline=dict(
    required=False,
    type='style',
    val_types=val_types['bool'],
    description="Toggle whether or not to show the label (i.e. bordering) "
                "line of the axis."
)

# $shortcuts-ticks

# $shortcut-autotick
def make_autotick(axis_or_colorbar):
    _required=False
    _type='style'
    _val_types=val_types['bool']
    _description=''.join(["Toggle whether or not the {S} ticks parameters ",
                          "are picked automatically by Plotly. ",
                          "Once 'autotick' is set to False, ",
                          "the {S} ticks parameters can be declared ",
                          "with 'ticks', 'tick0', 'dtick0' and other ",
                          "tick-related key in this {S} object.",
                         ]).format(S=axis_or_colorbar)
    return output(_required,_type,_val_types,_description)

# $shortcut-nticks
def make_nticks(axis_or_colorbar):
    _required=False
    _type='style'    # TO DO! Shouldn't this be 'plot_info' ?
    _val_types=val_types['number'](gt=0)
    _description=''.join(["Specifies the number of {S} ticks. ",
                          "No need to set 'autoticks' to False ",
                          "for 'nticks' to apply."
                         ]).format(S=axis_or_colorbar)
    return output(_required,_type,_val_types,_description)

# $shortcut-showticklabels
def make_showticklabels(what_ticks):
    _required=False
    _type='style'
    _val_types=val_types['bool']
    _description=''.join(["Toggle whether or not the {} ticks "
                          "will feature tick labels."
                         ]).format(what_ticks)
    return output(_required,_type,_val_types,_description)

# $shortcuts-refs-anchors

# $shortcut-xyref
def make_xyref(x_or_y):
    _required=False
    _type='plot_info'
    S={'x': ['x','left','right'], 'y':['y','bottom','top']}
    s=S[x_or_y]
    _val_types="'paper' | '{S0}1' | '{S0}2' | etc".format(S0=s[0])
    _description=''.join(["Sets the {S0} coordinate for this object ",
                          "refers to. If you reference an axis, e.g., ",
                          "'{S0}2', the object will move with pan-and-zoom ",
                          "to stay fixed to this point. If you reference ",
                          "the 'paper', it remains fixed regardless of ",
                          "pan-and-zoom. In other words, if set to 'paper', ",
                          "the '{S0}' location refers to the distance from ",
                          "the left side of the plotting area in normalized ",
                          "coordinates where 0=='{S1}' and 1=='{S2}'. ",
                          "If set to refer to an {S0}axis' object, e.g., ",
                          "'{S0}1', '{S0}2', '{S0}3', etc., the ",
                          "'{S0}' location will refer to the location in "
                          "terms of this axis."
                         ]).format(S0=s[0],S1=s[1],S2=s[2])
    return output(_required,_type,_val_types,_description)

# $shortcut-xyanchor
def make_xyanchor(x_or_y):
    _required=False
    _type='plot_info'
    _val_types={
        'x':"'left' | 'center' | 'right'",
        'y':"'bottom' | 'middle' | 'top'"
    }
    S={'x': ['x','left','right'], 'y':['y','bottom','top']}
    s=S[x_or_y]
    _description=''.join(["This defines the horizontal location on the object ",
                          "referenced by the '{S0}' (position) key. ",
                          "For example, if '{S0}'==1, ",
                          "'{S0}ref'='paper', and '{S0}anchor'='{S2}', ",
                          "the {S2}most portion of this object will line ",
                          "up with the {S2}most edge of the plotting area.",
                         ]).format(S0=s[0],S2=s[2])
    return output(_required,_type,_val_types[x_or_y],_description)

# $shortcuts-layout-position

# $shortcut-xy_layout
def make_xy_layout(obj, x_or_y):
    _required=False
    _type='plot_info'
    _val_types=val_types['number'](ge=0)
    _description=dict(
        legend="Sets the '{}' position of the legend.".format(x_or_y),
        colorbar="Sets the '{}' position of the colorbar "
                 "(in paper coordinates).".format(x_or_y),
        annotation="Sets the '{}' position of this annotations.".format(x_or_y)
    )
    return output(_required,_type,_val_types,_description[obj])


# -------------------------------------------------------------------------------


## Graph Objects Meta

# $graph-objs-meta
#
# Initialize the list of meta for all graph objects

META = []

# $graph-objs-meta-trace
#
# Meta of 'trace' graph objects (i.e. elements of data object)

# $scatter
META += [('scatter', OrderedDict([

    ('x', make_x('scatter')),

    ('y', make_y('scatter')),

    ('r', make_r('scatter')),

    ('t', make_t('scatter')),

    ('mode', dict(
        required=False,
        type='plot_info',
        val_types="'lines' | 'markers' | 'text' | 'lines+markers' | "
                  "'lines+text' | 'markers+text' | 'lines+markers+text'",
        description="Plotting mode (or style) for the scatter plot. If the "
                    "mode includes 'text' then the 'text' will appear at "
                    "the (x,y) points, otherwise it will appear on "
                    "hover."
    )),

    ('name', drop_name),

    ('text', make_text('scatter')),

    ('error_y', make_error('scatter','y')),

    ('error_x', make_error('scatter','x')),

    ('marker', make_marker('scatter')),

    ('line', make_line('scatter')),

    ('connectgaps', dict(
        required=False,
        type='plot_info',
        val_types=val_types['bool'],
        description="Toggle whether or not missing data points "
                    "(i.e. '' or NaNs) linked to 'x' and/or 'y', are "
                    "added in by Plotly using linear interpolation."
    )),

    ('fill', dict(
        required=False,
        type='style',
        val_types="'none' | 'tozeroy' | 'tonexty' | 'tozerox' | 'tonextx",
        description="Use to make area-style charts. "
                    "Determines which area to fill with a solid color."
                    "By default, the area will appear in a more-transparent "
                    "shape of the line color (or of the marker color if "
                    "'mode' does not contains 'lines')."
    )),

    ('fillcolor', make_fillcolor('scatter')),

    ('opacity', make_opacity()),

    ('textfont', make_textfont('scatter')),

    ('textposition', dict(
        required=False,
        type='style',
        val_types="'top left' | 'top' (or 'top center')| 'top right' | "
                  "'left' (or 'middle left') | '' (or 'middle center') |"
                  "'right' (or 'middle right') |"
                  "'bottom left' | 'bottom' (or 'bottom center') |"
                  "'bottom right'",
        description="Sets the position of the text elements "
                    "in the 'text' key with respect to the data points. "
                    "By default, the text elements are plotted directly "
                    "at the (x,y) coordinates."
    )),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('type', make_type('scatter'))

]))]

# $bar
META += [('bar', OrderedDict([

    ('x', make_x('bar')),

    ('y', make_y('bar')),

    ('r', make_r('bar')),

    ('t', make_t('bar')),

    ('name', drop_name),

    ('orientation', make_orientation('bar')),

    ('text', make_text('bar')),

    ('error_y', make_error('bar','y')),

    ('error_x', make_error('bar','x')),

    ('marker', make_marker('bar')),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('type', make_type('bar')),

    ('line', make_line('bar')),  # TO DO! Artifact?

    ('textfont', make_textfont('bar'))  # TO DO! Artifact?

]))]

# $histogram
META += [('histogram', OrderedDict([

    ('x', make_x('histogram')),

    ('y', make_y('histogram')),

    ('histnorm', drop_histnorm),

    ('name', drop_name),

    ('autobinx', make_autobin('x')),

    ('nbinsx', make_nbins('x')),

    ('xbins', make_bins('x')),

    ('autobiny', make_autobin('y')),

    ('nbinsy', make_nbins('y')),

    ('ybins', make_bins('y')),

    ('error_y', make_error('histogram','y')),

    ('error_x', make_error('histogram','x')),

    ('marker', make_marker('histogram')),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('type', make_type('histogram')),

    ('line', make_line('histogram')),  # TO DO! Artifact? Drop?

    ('orientation', make_orientation('histogram'))  # TO DO! Artifact Drop?

]))]

# $box
META += [('box', OrderedDict([

    ('y', make_y('box')),

    ('x0', make_x0y0('box')),

    ('x', make_x('box')),

    ('name', drop_name),

    ('boxpoints', dict(  # TO DO! What does 'suspectedoutliers' do?
        required=False,
        type='plot_info',
        val_types="'all' | 'outliers' | 'suspectedoutliers' | False",
        description="If 'all' then the 'y' points are shown with the box. "
                    "If 'outliers' then only the 'outliers' of the 'y' "
                    "points are shown. If False then no points are shown."
    )),

    ('boxmean', dict(
        required=False,
        type='style',
        val_types="False | True | 'sd'",
        description="If True then the mean of the y-points is shown as a "
                    "dashed line in the box. If 'sd', then the standard "
                    "deviation is also shown. If False, then no line "
                    "shown."
    )),

    ('jitter', dict(
        required=False,
        type='style',
        val_types="number in [0, 1]",
        description="Width of the jittered scatter. If 0, then the "
                    "boxpoints are aligned vertically, if 1 then the "
                    "points are randomly jittered horizontally up to the "
                    "width of the box."
    )),

    ('pointpos', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=-2, le=2),
        description="Horizontal position of the center of the boxpoints "
                    "relative to the center and width of the box."
    )),

    ('whiskerwidth', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0, le=1),
        description="Width of the whisker of the box relative to the box' "
                    "width (in normalized coordinates, e.g. if "
                    "'whiskerwidth' set 1, then the whiskers are as wide "
                    "as the box."
    )),

    ('fillcolor', make_fillcolor('box')),

    ('marker', make_marker('box')),

    ('line', make_line('box')),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('type', make_type('box'))

]))]

# $heatmap
META += [('heatmap', OrderedDict([

    ('z', make_z('heatmap')),

    ('x', make_x('heatmap')),

    ('y', make_y('heatmap')),

    ('name', drop_name),

    ('zauto', drop_zauto),

    ('zmin', make_zminmax('min')),

    ('zmax', make_zminmax('max')),

    ('scl', drop_scl),

    ('reversescl', drop_reversescl),

    ('showscale', drop_showscale),

    ('colorbar', drop_colorbar),

    ('zsmooth', drop_zsmooth),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('x0', make_x0y0('heatmap','x')),

    ('dx', make_dxdy('heatmap','x')),

    ('y0', make_x0y0('heatmap','y')),

    ('dy', make_dxdy('heatmap','y')),

    ('xtype', make_xytype('heatmap','x')),

    ('ytype', make_xytype('heatmap','y')),

    ('type', make_type('heatmap'))

]))]

# $contour
META += [('contour', OrderedDict([

    ('z', make_z('contour')),

    ('x', make_x('contour')),

    ('y', make_y('contour')),

    ('name', drop_name),

    ('zauto', drop_zauto),

    ('zmin', make_zminmax('min')),

    ('zmax', make_zminmax('max')),

    ('autocontour', drop_autocontour),

    ('ncontours', drop_ncontours),

    ('contours', drop_contours),

    ('line', make_line('contour')),

    ('scl', drop_scl),

    ('reversescl', drop_reversescl),

    ('showscale', drop_showscale),

    ('colorbar', drop_colorbar),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('x0', make_x0y0('heatmap','x')),

    ('dx', make_dxdy('heatmap','x')),

    ('y0', make_x0y0('heatmap','y')),

    ('dy', make_dxdy('heatmap','y')),

    ('xtype', make_xytype('heatmap','x')),

    ('ytype', make_xytype('heatmap','y')),

    ('type', make_type('contour'))

]))]

# $histogram2d
META += [('histogram2d', OrderedDict([

    ('x', make_x('histogram2d')),

    ('y', make_y('histogram2d')),

    ('histnorm', drop_histnorm),

    ('name', drop_name),

    ('autobinx', make_autobin('x')),

    ('nbinsx', make_nbins('x')),

    ('xbins', make_bins('x')),

    ('autobiny', make_autobin('y')),

    ('nbinsy', make_nbins('y')),

    ('ybins', make_bins('y')),

    ('scl', drop_scl),

    ('reversescl', drop_reversescl),

    ('showscale', drop_showscale),

    ('colorbar', drop_colorbar),

    ('zauto', drop_zauto),

    ('zmin', make_zminmax('min')),

    ('zmax', make_zminmax('max')),

    ('zsmooth', drop_zsmooth),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('type', make_type('histogram2d'))

]))]

# $histogram2dcontour
META += [('histogram2dcontour', OrderedDict([

    ('x', make_x('histogram2dcontour')),

    ('y', make_y('histogram2dcontour')),

    ('histnorm', drop_histnorm),

    ('name', drop_name),

    ('autobinx', make_autobin('x')),

    ('nbinsx', make_nbins('x')),

    ('xbins', make_bins('x')),

    ('autobiny', make_autobin('y')),

    ('nbinsy', make_nbins('y')),

    ('ybins', make_bins('y')),

    ('autocontour', drop_autocontour),

    ('ncontours', drop_ncontours),

    ('contours', drop_contours),

    ('line', make_line('histogram2dcontour')),

    ('scl', drop_scl),

    ('reversescl', drop_reversescl),

    ('showscale', drop_showscale),

    ('colorbar', drop_colorbar),

    ('zauto', drop_zauto),

    ('zmin', make_zminmax('min')),

    ('zmax', make_zminmax('max')),

    ('opacity', make_opacity()),

    ('xaxis', make_axis('x',trace=True)),

    ('yaxis', make_axis('y',trace=True)),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('type', make_type('histogram2dcontour'))

]))]

# $area
META += [('area', OrderedDict([  # TO DO! More testing, better descriptions

    ('r', make_r('area')),

    ('t', make_t('area')),

    ('name', drop_name),

    ('marker', make_marker('area')),

    ('showlegend', make_showlegend(trace=True)),

    ('stream', drop_stream),

    ('visible', drop_visible),

    ('angularaxis', dict(  # TO DO! How do polar axes this work?
        required=False,
        type='plot_info',
        val_types='',
        description='info coming soon'
    )),

    ('radialaxis', dict(  # TO DO! How do polar axes this work?
        required=False,
        type='plot_info',
        val_types='',
        description='info coming soon'
    )),

    ('type', make_type('area'))

]))]

# $graph-objs-meta-trace-aux
#
# Meta of auxiliary trace graph objects (linked to trace graph object keys)

# $error
#
# META generation for 'error_y' and 'error_x'
def meta_error(y_or_x):

    S={'y': ['y','vertically','up','down','above','below'],
       'x': ['x','horizontally','right','left','right of','left of']}
    s=S[y_or_x]

    meta=[

        ('type', make_type(error=True)),

        ('symmetric', dict(
            required=False,
            type='plot_info',
            val_types=val_types['bool'],
            description="Toggle whether or not error bars are the same length "
                        "in both directions ({S2} and {S3}). If not specified, "
                        "the error bars will be "
                        "symmetric.".format(S2=s[2],S3=s[3])
        )),

       ('array', dict(
           required=False,
           type='data',
           val_types=val_types['data_array'],
           description=''.join(["The array of corresponding to ",
                                "error bars' span to be drawn. ",
                                "Has only an effect if 'type' is set to ",
                                "'data'. Values in the array are plotted ",
                                "relative to the '{S0}' coordinates. ",
                                "For example, with '{S0}'=[1,2] and ",
                                "'array'=[1,2], the error bars will span ",
                                "{S1} from {S0}= 0 to 2 and {S0}= 0 to 4 if ",
                                "'symmetric'=True; and from {S0}= 1 to 2 and ",
                                "{S0}= 2 to 4 if 'symmetric' is set to False ",
                                "and 'arrayminus' is empty."
                               ]).format(S0=s[0],S1=s[1])
       )),

        ('value', dict(
            required=False,
            type='data',
            val_types=val_types['number'](ge=0),
            description="The value or percentage determining the error bars' "
                        "span, at all trace coordinates. "
                        "Has an effect if 'type' is set to 'value' or "
                        "'percent'. "
                        "If 'symmetric' is set to False, this value corresponds "
                        "to the span {S4} the trace of coordinates. "
                        "To specify multiple error bar lengths, "
                        "you should set 'type' to 'data' and "
                        "use the 'array' key instead.".format(S4=s[4])
        )),

        ('arrayminus', dict(
            required=False,
            type='data',
            val_types=val_types['number'](ge=0),
            description="Only functional when 'symmetric' is set to False. "
                        "Same as 'array' but corresponding to the span "
                        "of the error bars {S5} "
                        "the trace coordinates".format(S5=s[5])
        )),

        ('valueminus', dict(
            required=False,
            type='data',
            val_types=val_types['number'](ge=0),
            description=''.join(["Only functional when 'symmetric' ",
                                 "is set to False. ",
                                 "Same as 'value' but corresponding ",
                                 "to the span ",
                                 "of the error bars {S5} ",
                                 "the trace coordinates"]).format(S5=s[5])
        )),

        ('color', make_color('error')),

        ('thickness', make_thickness('error',y_or_x)),

        ('width', make_width('error')),

        ('opacity', make_opacity()),

    ]

    if y_or_x=='x':
        meta += [
            ('copy_ystyle', dict(
                required=False,
                type='style',
                val_types=val_types['bool'],
                description=''.join(["Toggle whether to set x error bar ",
                                     "style to the same style ",
                                     "(color, thickness, width, opacity) ",
                                     "as y error bars set in YAxis."
                                    ])
            ))]

    meta+=[

        ('visible', drop_visible),

        ('traceref', dict(   # TO DO! What does this do?
            required=False,
            type='plot_info',
            val_types='',
            description='more info coming soon'
        ))

    ]

    return [('error_{}'.format(y_or_x), OrderedDict(meta))]

# $error_y
META += meta_error('y')

# $error_x
META += meta_error('x')

# $bins
#
# META generation for 'xbins' and 'ybins'
def meta_bins(x_or_y):

    meta=[

        ('start', make_startend('bins','start',x_or_y)),

        ('end', make_startend('bins','end',x_or_y)),

        ('size', make_size('bins',x_or_y)),

    ]

    return [('{}bins'.format(x_or_y), OrderedDict(meta))]

# $xbins
META += meta_bins('x')

# $ybins
META += meta_bins('y')

# $contours
META += [('contours', OrderedDict([

    ('showlines', dict(
        required=False,
        type='style',
        val_types=val_types['bool'],
        description="Toggle whether or not the contour lines appear on the "
                    "plot."
    )),

    ('start', make_startend('contours','start','x')),

    ('end', make_startend('contours','end','x')),

    ('size', make_size('contours')),

    ('coloring', dict(
        required=False,
        type='plot_info',
        val_types=" 'fill' | 'heatmap' | 'lines' | 'none' ",
        description="Choose the coloring method for this contour trace. "
                    "The default value is 'fill' "
                    "where coloring is done evenly between each contour line. "
                    "'heatmap' colors on a grid point-by-grid point basis. "
                    "'lines' colors only the contour lines, each with "
                    "respect to the color scale. "
                    "'none' prints all contour lines with the same color; "
                    "choose their color in a Line object at the trace level "
                    "if desired."
    ))

]))]

# $stream
META += [('stream', OrderedDict([

    ('token', dict(  # TODO: these are public!! Is that OK?
        required=True,
        type='plot_info',
        val_types="A stream id number, see https://plot.ly/settings",
        description="This number links a data object on a plot with a "
                    "stream. In other words, any data object you create "
                    "can reference a 'stream'. If you stream data to "
                    "Plotly with the same stream id (token), Plotly knows "
                    "update this data object with the incoming data "
                    "stream."
    )),

    ('maxpoints', dict(
        required=False,
        type='plot_info',
        val_types=val_types['number'](gt=0),
        description="Sets the maximum number of points to keep on the "
                    "plots from an incoming stream. For example, "
                    "if 'maxpoints' is set to 50, only the newest 50 points "
                    "will be displayed on the plot."
    ))

]))]

# $graph-objs-meta-style
#
# Meta of graph objects corresponding to style features

# $marker
META += [('marker', OrderedDict([

    ('color', make_color('marker')),

    ('size', make_size('marker')),

    ('symbol', dict(
        required=False,
        type='style',
        val_types="'dot' | 'cross' | 'diamond' | 'square' "
                  "| 'triangle-down' | 'triangle-left' | 'triangle-right' "
                  "| 'triangle-up' | 'x' OR list of these string values",
        description="The symbol that is drawn on the plot for each marker. "
                    "Supported only in scatter trace. "
                    "If 'symbol' is linked to a list or an array of numbers, "
                    "symbol values are mapped to individual marker points "
                    "in the same order as in the data lists or arrays."
    )),

    ('line', make_line('marker')),

    ('opacity', make_opacity(marker=True)),

    ('colorscale', dict(  # TO DO! Check if right, example, merge with 'scl'?
        required=False,
        type="style",
        val_types="array_like of value-color pairs | "
                  "'Greys' | 'Greens' | 'Bluered' | 'Hot' | "
                  "'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | "
                  "'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'",
        description="The color scale. The strings are pre-defined color "
                    "scales. For custom color scales, define a list of "
                    "color-value pairs, where the first element of the pair "
                    "corresponds to a normalized value of the y coordinates "
                    "(for scatter traces) from 0-1 "
                    "and the second element of pair "
                    "corresponds to a color."
    )),

    ('sizemode', dict(  # TO DO! Better description
        required=False,
        type='style',
        val_types="'diameter' | 'area'",
        description="Scale the size each points with respect "
                    "to diameter or area. "
                    "Applies only to scatter traces."
    )),

    ('sizeref', dict(  # TO DO! Better description
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Select scale factor for the size of each point. "
                    "Applies only to scatter traces."
    )),

    ('maxdisplayed', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Set maximum number of displayed points for this "
                    "trace. Applies only to scatter traces."
    ))

]))]

# $line
META += [('line', OrderedDict([

    ('color', make_color('line')),

    ('width', make_width('line')),

    ('dash', dict(
        required=False,
        type='style',
        val_types="'dash' | 'dashdot' | 'dot' | 'solid'",
        description="Sets the drawing style of this line object."
    )),

    ('opacity', make_opacity()),

    ('smoothing', dict(     # TO DO! Better description
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="The amount of smoothing. "
                    "Applies only to contour traces "
                    "and scatter trace if 'shape' is set to 'spline'."
    )),

    ('shape', dict(         # TO DO! Better description
        required=False,
        type='style',
        val_types="'linear' | 'spline' | 'hv' | 'vh' | 'hvh' | 'vhv'",
        description="Choose the line shape between each coordinate pair. "
                    "Applies only to scatter traces."
    )),

    # ('thickness', dict()),  # TO DO! Does this exist somewhere?

]))]

# $font
META += [('font', OrderedDict([

    ('family', dict(
        required=False,
        val_types=" 'Courier New, monospace' | "
                  " 'Balto, sans-serif' | "
                  " 'Droid Sans, sans-serif' | "
                  " 'Droid Serif, serif' | "
                  " 'Droid Sans Mono, sans-serif' | "
                  " 'Georgia, serif' | "
                  " 'Gravitas One, cursive' | "
                  " 'Impact, Charcoal, sans-serif' | "
                  " 'Lucida Console, Monaco, monospace' | "
                  " 'Old Standard TT, serif' | "
                  " 'Open Sans, sans-serif' | "
                  " 'PT Sans Narrow, sans-serif' | "
                  " 'Raleway, sans-serif' | "
                  " 'Times New Roman, Times, serif' | "
                  " 'Verdana, sans-serif'",
        type='style',
        description="Sets the font family. "
                    "If linked in the first level of the layout object,  "
                    "set the color of the global font."
    )),

    ('size', make_size('font')),

    ('color', make_color('font')),

    ('outlinecolor', make_outlinecolor('font')),

]))]


# $graph-objs-meta-layout-axis
#
# Axis trace objects linked inside layout object

# $ticks        TO DO! Separate object for ticks?
#
# META generation for ticks (axis and colorbar)
def meta_ticks(axis_or_colorbar):

    meta= [

        ('ticks', dict(
            required=False,
            type='style',
            val_types="'' | 'inside' | 'outside'",
            description="Sets the format of tick visibility "
                        "on this {}.".format(axis_or_colorbar)
        )),

        ('showticklabels', make_showticklabels(axis_or_colorbar)),

        ('tick0', dict(
            required=False,
            type='plot_info',
            val_types=val_types['number'](),
            description="Sets the starting point of the ticks "
                        "of this {}.".format(axis_or_colorbar)
        )),

        ('dtick', dict(
            required=False,
            type='style',
            val_types=val_types['number'](),
            description="Sets the distance between ticks "
                        "on this {}.".format(axis_or_colorbar)
        )),

        ('ticklen', dict(
            required=False,
            type='style',
            val_types=val_types['number'](),  # Units?
            description="Sets the length of the tick lines "
                        "on this {}.".format(axis_or_colorbar)
        )),

        ('tickwidth', dict(
            required=False,
            type='style',
            val_types=val_types['number'](gt=0),
            description="Sets the width of the tick lines "
                        "on this {}.".format(axis_or_colorbar)
        )),

        ('tickcolor', dict(
            required=False,
            type='style',
            val_types=val_types['color'],
            description="Sets the color of the tick lines "
                        "on this {}.".format(axis_or_colorbar),
            examples=examples_color
        )),

        ('tickangle', dict(
            required=False,
            type='style',
            val_types=val_types['number'](le=90, ge=-90),
            description="Sets the angle in degrees of the ticks "
                        "on this {}.".format(axis_or_colorbar)
        )),

        ('tickfont', dict(
            required=False,
            type='object',
            val_types=val_types['object'],
            description="A dictionary-like object defining the parameters "
                        "of the ticks' font."
        )),

        ('exponentformat', dict(
            required=False,
            type='style',
            val_types="'none' | 'e' | 'E' | 'power' | 'SI' | 'B'",
            description="Sets how exponents show up. Here's how the number "
                        "1000000000 (1 billion) shows up in each. If set to "
                        "'none': 1,000,000,000. If set to 'e': 1e+9. If set "
                        "to 'E': 1E+9. If set to 'power': 1x10^9 (where the 9 "
                        "will appear super-scripted. If set to 'SI': 1G. If "
                        "set to 'B': 1B (useful when referring to currency."
        )),

        ('showexponent', dict(
            required=False,
            type='style',
            val_types="'all' | 'first' | 'last' | 'none'",
            description="If set to 'all', ALL exponents will be shown "
                        "appended to their significands. If set to 'first', "
                        "the first tick's exponent will be appended to its "
                        "significand, however no other exponents will "
                        "appear--only the significands. If set to 'last', "
                        "the last tick's exponent will be appended to its "
                        "significand, however no other exponents will "
                        "appear--only the significands. If set to 'none', "
                        "no exponents will appear, only the significands."
       ))

    ]

    return meta

# $axis
#
# META generation for 'xaxis' and 'yaxis'
def meta_axis(x_or_y):

    S={'x':['x','bottom','top','y'], 'y':['y','left','right','x']}
    s=S[x_or_y]

    meta=[

        ('title', make_title('axis',x_or_y)),

        ('titlefont', make_titlefont('axis',x_or_y)),

        ('range', dict(
            required=False,
            type='style',  # TO DO! changed this!!!  was plot_info
            val_types="number array of length 2",
            description="Defines the start and end point of "
                        "this {}-axis.".format(x_or_y),
            examples=[-13, 20]
        )),

        ('domain', dict(
            required=False,
            type='plot_info',
            val_types="number array of length 2",
            description="Sets the domain of this {}-axis. The available space "
                        "for this axis to live in is  "
                        "from 0 to 1.".format(x_or_y),
            examples=[0, 0.5]
        )),

        ('type', dict(   # Different enough from make_type()
            required=False,
            type='plot_info',
            val_types="'linear' | 'log' | 'category'",
            description="Sets the format of this axis."
        )),

        ('rangemode', dict(
            required=False,
            type='plot_info',
            val_types="string: 'normal' | 'tozero' | 'nonnegative'",
            description="Choose between Plotly's automated axis generation "
                        "modes: 'normal' (the default) sets the axis range "
                        "in relation to the extrema in the data object, "
                        "'tozero' extends the axes to {}=0 no matter "
                        "the data plotted and 'nonnegative' sets a "
                        "non-negative range no matter the data plotted."
        )),

        ('showgrid', dict(
            required=False,
            type='style',
            val_types=val_types['bool'],
            description="Toggle whether or not this axis features "
                        "grid lines."
        )),

        ('zeroline', dict(
            required=False,
            type='style',
            val_types=val_types['bool'],
            description="Toggle whether or not an additional grid line "
                        "(thicker than the other grid lines, by default) "
                        "will appear on this axis along {}=0.".format(x_or_y)
        )),

        ('showline', drop_showline),

        ('autotick', make_autotick('axis')),

        ('nticks', make_nticks('axis')),

        ]

    meta += meta_ticks('axis')

    meta+=[

        ('gridcolor', dict(
            required=False,
            type='style',
            val_types=val_types['color'],
            description="Sets the axis grid color.",
            examples=examples_color
        )),

        ('gridwidth', dict(
            required=False,
            type='style',
            val_types=val_types['number'](gt=0),
            description="Sets the grid width (in pixels)."
        )),

        ('zerolinecolor', dict(
            required=False,
            type='style',
            val_types=val_types['color'],
            description="Set the color of this axis' zeroline.",
            examples=examples_color
        )),

        ('zerolinewidth', dict(
            required=False,
            type='style',
            val_types=val_types['number'](gt=0),
            description="Sets the width of this axis' zeroline (in pixels)."
        )),

        ('linecolor', dict(
            required=False,
            type='style',
            val_types=val_types['color'],
            description="Defines the axis line color.",
            examples=examples_color
        )),

        ('linewidth', dict(
            required=False,
            type='style',
            val_types=val_types['number'](gt=0),
            description="Sets the width of the axis line (in pixels)"
        )),

        ('anchor', dict(
            required=False,
            type='plot_info',
            val_types="'{S3}' | 'free'".format(S3=s[3]),
            description="Sets whether the {S0}-axis will be anchored to its "
                        "corresponding {S3}-axis OR 'free' to appear  "
                        "anywhere in the vertical space of "
                        "the plot.".format(S0=s[0],S3=s[3])
        )),

        ('side', dict(
            required=False,
            type='style',
            val_types="'{S1}' | '{S2}'".format(S1=s[1],S2=s[2]),
            description="Set whether this {S0}-axis sits at the '{S1}' of the "
                        "plot or at the '{S2}' "
                        "of the plot.".format(S0=s[0],S1=s[1],S2=s[2])
        )),

        ('position', dict(
            required=False,
            type='style',
            val_types=val_types['number'](le=1, ge=0),
            description="Sets where the axis is positioned in the plotting "
                        "space. For example 'position'=0.5 will place this "
                        "axis in the exact center of the plotting space. This "
                        "only has functionality if 'anchor'='free'."
        )),

        ('mirror', dict(
            required=False,
            type='style',
            val_types=val_types['bool'],
            description="Toggle whether to mirror the axis line to the "
                        "opposite side of the plot."
        )),

        ('overlaying', dict(  # TO DO! What does this do?
            required=False,
            type='style',
            val_types='',
            description="more info coming soon."
        )),

        ('autorange', dict(  # TO DO! Artifact
            required=False,
            type='plot_info',
            val_types=val_types['bool'],
            #description="Toggle whether to let plotly autorange the axis."
            description="Artifact. If 'range' is set than Plotly's autorange "
                        "is overwritten."
        )),

        # ('drange', dict()),  # TO DO! What are these?
        # ('r0', dict()),

    ]

#    print meta
    return [('{}axis'.format(x_or_y), OrderedDict(meta))]

# $xaxis
META += meta_axis('x')

# $yaxis
META += meta_axis('y')

# $radialaxis
META += [('radialaxis', OrderedDict([ # TO DO! More testing, better description

    ('range', make_range('radial')),

    ('domain', make_domain('radial')),

    ('orientation', dict(
        required=False,
        type='plot_info',
        val_types=val_types['number'](ge=-360,le=360),
        description="Sets the orientation (an angle with respect to the origin) "
                    "of the radial axis."
    )),

    ('showline', drop_showline),

    ('showticklabels', make_showticklabels('radial axis')),

    ('tickorientation', dict(
        required=False,
        type='style',
        val_types="'horizontal' | 'vertical'",
        description="Choose the orientation (from the paper perspective) "
                    "of the radial axis tick labels."
    )),

    ('ticklen', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Sets the length of the tick lines "
                    "on this radial axis."
    )),

    ('tickcolor', dict(
        required=False,
        type='style',
        val_types=val_types['color'],
        description="Sets the color of the tick lines "
                    "on this radial axis.",
        examples=examples_color
    )),

    ('ticksuffix', dict(
        required=False,
        type='style',
        val_types=val_types['string'],
        description="Sets the length of the tick lines "
                    "on this radial axis."
    )),

    ('endpadding', dict(
        required=False,
        type='style',
        val_types=val_types['number'](),
        description="more info coming soon"
    )),

    ('visible', drop_visible)

]))]

# $angularaxis
META += [('angularaxis', OrderedDict([ # TO DO! More testing, better description

    ('range', make_range('angular')),

    #('domain', make_domain('angular')),  #TO DO! Does not apply, right?

    ('showline', drop_showline),

    ('showticklabels', make_showticklabels('angular axis')),

    ('tickorientation', dict(
        required=False,
        type='style',
        val_types="'horizontal' | 'vertical'",
        description="Choose the orientation (from the paper's perspective) "
                    "of the radial axis tick labels."
    )),

    ('tickcolor', dict(
        required=False,
        type='style',
        val_types=val_types['color'],
        description="Sets the color of the tick lines "
                    "on this angular axis.",
        examples=examples_color
    )),

    ('ticksuffix', dict(
        required=False,
        type='style',
        val_types=val_types['string'],
        description="Sets the length of the tick lines "
                    "on this angular axis."
    )),

    ('endpadding', dict(  # What does this do?
        required=False,
        type='style',
        val_types=val_types['number'](),
        description="more info coming soon"
    )),

    ('visible', drop_visible)

]))]


# $graph-objs-meta-layout-aux
#
# Other graph object linked inside layout object

# $legend
META += [('legend', OrderedDict([

    ('x', make_xy_layout('legend', 'x')),

    ('y', make_xy_layout('legend', 'y')),

    ('traceorder', dict(
        required=False,
        type='style',
        val_types="'normal' | 'reversed'",
        description="Trace order is set by the order of the data in "
                    "associated grid for the plot. This sets whether this "
                    "order is read from left-to-right or from "
                    "right-to-left.")),

    ('font', make_font('legend')),

    ('bgcolor', make_bgcolor('legend')),

    ('bordercolor', make_bordercolor('legend')),

    ('borderwidth', make_borderwidth('legend')),

    ('xref', make_xyref('x')),

    ('yref', make_xyref('y')),

    ('xanchor', make_xyanchor('x')),

    ('yanchor', make_xyanchor('y')),

    ('showlegend', make_showlegend(layout=True)), # TO DO! Redundant w/ 'layout'

]))]

# $colorbar
meta=[

     ('title', make_title('colorbar')),

     ('titleside', dict(
         required=False,
         type='plot_info',
         val_types="'right' | 'top' | 'bottom'",
         description="Location of colorbar title with respect "
                     "to the colorbar."
     )),

     ('titlefont', make_titlefont('colorbar')),

     ('thickness', make_thickness('colorbar')),

     ('thicknessmode', dict(
         required=False,
         type='style',
         val_types="string: 'pixels' | 'fraction' ",
         description="Sets thickness unit mode."
     )),

     ('len', dict(
         required=False,
         type='style',
         val_types=val_types['number'](ge=0),
         description="Sets the length of the colorbar."
     )),

     ('lenmode', dict(
         required=False,
         type='style',
         val_types="string: 'pixels' | 'fraction' ",
         description="Sets length unit mode."
     )),

     ('x', make_xy_layout('colorbar','x')),

     ('y', make_xy_layout('colorbar','y')),

     ('autotick', make_autotick('colorbar')),

     ('nticks', make_nticks('colorbar'))

     ]

meta+=meta_ticks('colorbar')

meta+=[

     ('xanchor', make_xyanchor('x')),

     ('xanchor', make_xyanchor('y')),

     ('bgcolor', make_bgcolor('colorbar')),

     ('outlinecolor', make_outlinecolor('colorbar')),

     ('outlinewidth', dict(
         required=False,
         type='style',
         val_types=val_types['number'](),
         description="The width of the outline surrounding this colorbar."
     )),

     ('borderwidth', make_borderwidth('colorbar')),

     ('xpad', dict(
         required=False,
         type='style',
         val_types=val_types['number'](le=50, ge=0),
         description="The amount of space (padding) between the colorbar and "
                     "the enclosing boarder in the x-direction."
     )),

     ('ypad', dict(
         required=False,
         type='style',
         val_types=val_types['number'](le=50, ge=0),
         description="The amount of space (padding) between the colorbar and "
                     "the enclosing boarder in the y-direction."
     ))

]

META += [('colorbar', OrderedDict(meta))]

# $margin
META += [('margin', OrderedDict([

    ('l', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Left margin size in pixels.")),

    ('r', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Right margin size in pixels.")),

    ('b', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Bottom margin size in pixels.")),

    ('t', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Top margin size in pixels.")),

    ('pad', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="The distance between edge of the plot and the "
                    "bounding rectangle that encloses the plot "
                    "(in pixels)."
    )),

    ('autoexpand', dict(  # TODO: ??
        required=False,
        type='style',
        val_types=val_types['bool'],
        description="more info coming soon"
    ))

]))]

# $annotation
META += [('annotation', OrderedDict([

    ('x', make_xy_layout('annotation','x')),

    ('y', make_xy_layout('annotation','y')),

    ('xref', make_xyref('x')),

    ('yref', make_xyref('y')),

    ('text', dict(      # Different enough from make_text()
        required=False,
        type='plot_info',
        val_types=val_types['string'],
        description='The text associated with this annotation.'
    )),

    ('font', make_font('annotation')),

    ('align', dict(
        required=False,
        type='plot_info',
        val_types="'left' | 'center' | 'right'",
        description="Sets the alignment of the text in the annotation."
    )),

    ('showarrow', dict(
        required=False,
        type='plot_info',
        val_types=val_types['bool'],
        description="Toggle whether or not the arrow associated with "
                    "this annotation with be shown."
    )),

    ('arrowhead', dict(
        required=False,
        type='style',
        val_types='0 | 1 | 2 | 3 | 4 | 5 | 6 | 7',
        description="Sets the arrowhead style. "
                    "Has an effect only if 'showarrow' is set to True."
    )),

    ('arrowsize', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="Scales the arrowhead's size. "
                    "Has an effect only if 'showarrow' is set to True."
    )),

    ('arrowwidth', dict(
        required=False,
        type='style',
        val_types=val_types['number'](gt=0),
        description="Sets the arrowhead's width (in pixels). "
                    "Has an effect only if 'showarrow' is set to True."
    )),

    ('arrowcolor', dict(
        required=False,
        type='style',
        val_types=val_types['color'],
        description="Sets the color of the arrowhead. "
                    "Has an effect only if 'showarrow' is set to True.",
        examples=examples_color
    )),

    ('ax', dict(            # TO DO! Better description
        required=False,
        type='plot_info',
        val_types=val_types['number'](),
        description="Position of the annotation text relative to the "
                    "arrowhead about the x-axis. "
                    "Has an effect only if 'showarrow' is set to True."
    )),

    ('ay', dict(            # TO DO! Better description
        required=False,
        type='plot_info',
        val_types=val_types['number'](),
        description="Position of the annotation text relative to the "
                    "arrowhead about the y-axis. "
                    "Has an effect only if 'showarrow' is set to True."
    )),

    ('bordercolor', make_bordercolor('annotation')),

    ('borderwidth', make_borderwidth('annotation')),

    ('borderpad', dict(
        required=False,
        type='style',
        val_types=val_types['number'](le=10, ge=0),
        description="The amount of space (padding) between the text and "
                    "the enclosing boarder.")),

    ('bgcolor', make_bgcolor('annotation')),

    ('opacity', make_opacity()),

    ('xanchor', make_xyanchor('x')),

    ('yanchor', make_xyanchor('y')),

    ('xatype', dict(    # TO DO! What does this do?
        required=False,
        type='style',
        val_types='',
        description="more info coming soon"
    )),

    ('yatype', dict(    # TO DO! What does this do?
        required=False,
        type='style',
        val_types='',
        description="more info coming soon"
    )),

    ('tag', dict(       # TO DO! What does this do?
        required=False,
        type='style',
        val_types='',
        description="more info coming soon"
    )),

    ('ref', dict(       # TO DO! What does this do?
        required=False,
        type='style',
        val_types='',
        description="more info coming soon"
    ))

]))]

# $layout
#
#
META += [('layout', OrderedDict([

    ('title', make_title('layout')),

    ('titlefont', make_titlefont('layout')),

    ('font', make_font('layout')),

    ('showlegend', make_showlegend(layout=True)),

    ('autosize', dict(
        required=False,
        type='style',
        val_types=val_types['bool'],
        description="Toggle whether or not the dimensions of the figure are "
                    "picked automatically by Plotly. "
                    "Once 'autosize' is set to False, the figure's dimensions "
                    "can be set with 'width' and 'height'.",
    )),

    ('width', dict(
        required=False,
        type='style',
        val_types=val_types['number'](gt=0),
        description="Sets the width in pixels of the figure you are "
                    "generating."
    )),

    ('height', dict(
        required=False,
        type='style',
        val_types=val_types['number'](gt=0),
        description="Sets the height in pixels of the figure you are "
                    "generating."
    )),

    ('xaxis', make_axis('x',layout=True)),

    ('yaxis', make_axis('y',layout=True)),

    ('legend', dict(
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A dictionary-like object containing the legend "
                    "parameters for this figure."
    )),

    ('annotations', dict(
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A list-like object that contains one or multiple "
                    "annotation dictionaries."
    )),

    ('margin', dict(
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A dictionary-like object containing the margin "
                    "parameters for this figure."
    )),

    ('paper_bgcolor', dict(
        required=False,
        type='style',
        val_types=val_types['color'],
        description="Sets the color of the figure's paper "
                    "(i.e. area representing the canvas of the figure).",
        examples=examples_color
    )),

    ('plot_bgcolor', dict(
        required=False,
        type='style',
        val_types=val_types['color'],
        description="Sets the background color of the plot (i.e. the area "
                    "laying inside this figure's axes.",
        examples=examples_color
    )),

    ('hovermode', dict(
        required=False,
        type='style',
        val_types="'closest' | 'x' | 'y'",
        description="Set what happens when a user hovers over the figure. "
                    "When set to 'x', all data sharing the same 'x' "
                    "coordinate will be shown on screen with "
                    "corresponding trace labels. When set to 'y' all data "
                    "sharing the same 'y' coordainte will be shown on the "
                    "screen with corresponding trace labels. When set to "
                    "'closest', information about the data point closest "
                    "to where the viewer is hovering will appear."
    )),

    ('dragmode', dict(
        required=False,
        type='style',
        val_types="'zoom' | 'pan'",
        description="Set what happens when a user preforms a mouse 'drag' "
                    "in the plot area. When set to 'zoom', a portion of "
                    "the plot will be highlighted, when the viewer "
                    "exits the drag, this highlighted section will be "
                    "zoomed in on. When set to 'pan', data in the plot "
                    "will move along with the viewers dragging motions. A "
                    "user can always depress the 'shift' key to access "
                    "the whatever functionality has not been set as the "
                    "default."
    )),

    ('barmode', dict(
        required=False,
        type='plot_info',
        val_types="'stack' | 'group' | 'overlay'",
        description="For bar and histogram plots only. "
                    "This sets how multiple bar objects are plotted "
                    "together. In other words, this defines how bars at "
                    "the same location appear on the plot. If set to "
                    "'stack' the bars are stacked ontop of one another. "
                    "If set to 'group', the bars are plotted next to one "
                    "another, centered around the shared location. If set "
                    "to 'overlay', the bars are simply plotted over one "
                    "another, you may need to set the opacity to see this."
    )),

    ('bargap', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="For bar and histogram plots only. "
                    "Sets the gap between bars (or sets of bars) at "
                    "different locations."
    )),

    ('bargroupgap', dict(
        required=False,
        type='style',
        val_types=val_types['number'](ge=0),
        description="For bar and histogram plots only. "
                    "Sets the gap between bars in the same group. "
                    "That is, when multiple bar objects are plotted and "
                    "share the same locations, this sets the distance "
                    "between bars at each location."
    )),

    ('boxmode', dict(
        required=False,
        type='plot_info',
        val_types="'overlay' | 'group'",
        description="For box plots only. "
                    "Sets how groups of box plots appear. "
                    "If set to 'overlay', a group of boxes "
                    "will be plotted directly on top of one "
                    "another at their specified location. "
                    "If set to 'group', the boxes will be "
                    "centered around their shared location, "
                    "but they will not overlap."
    )),

    ('radialaxis', dict(  # TO DO! How does this work?
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A dictionary-like object describing the radial axis "
                    "in a polar plot."
    )),

    ('angularaxis', dict( # TO DO! How does this work?
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A dictionary-like object describing the angular axis "
                    "in a polar plot."
    )),

    ('direction', dict(
        required=False,
        type='plot_info',
        val_types="'clockwise' | 'counterclockwise'",
        description="For polar plots only. "
                    "Choose the direction corresponding to "
                    "positive angular distances."
    )),

    ('orientation', dict(
        required=False,
        type='plot_info',
        val_types=val_types['number'](ge=-360,le=360),
        description="For polar plots only. "
                    "Sets the orientation of (i.e. rotate) the polar plot."
    )),

    ('defaultcolorrange', dict(  # TODO: polar only
        required=False,
        type='style',
        val_types=val_types['number'](ge=-360,le=360),
        description="For polar plots only. "
                    "More info coming soon."
    )),

    ('opacity', dict(  # TODO: polar only
        required=False,
        type='style',
        val_types=val_types['number'](le=1, ge=0),
        description="For polar plots only."
                    "Sets the opacity of the entire plot."
    )),

    ('needsEndSpacing', dict(  # TODO: polar only
        required=False,
        type='style',
        val_types='',
        description="For polar plots only. "
                    "info coming soon."
    )),

    ('categories', dict(  # TO DO! What does this do? Artifact?
        required=False,
        type='plot_info',
        val_types='',
        description='info coming soon'
    )),

    ('separators', dict(  # TO DO! What does this do?
        required=False,
        type='style',
        val_types='',
        description='info coming soon'
    )),

    ('labeloffset', dict(  # TO DO! Does this actually work?
        required=False,
        type='style',
        val_types='',
        description='info coming soon'
    )),

    ('hidesources', dict(  # TO DO! Artifact?
        required=False,
        type='plot_info',
        val_types='',
        description='more info coming soon'
    )),

    ('bardir', dict(    # TO DO! Artifact?
        required=False,
        type='plot_info',
        val_types='',
        description='more info coming soon'
    ))

]))]

# $figure
#
#
META += [('figure', OrderedDict([

    ('data', dict(
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A list-like array of the data trace(s) that is/are "
                    "to be visualized."
    )),

    ('layout', dict(
        required=False,
        type='object',
        val_types=val_types['object'],
        description="A dictionary-like object that contains the layout "
                    "parameters (e.g. information about the axis, "
                    "global settings and layout information "
                    "related to the rendering of the figure)."
    ))

]))]


# $graph-objs-meta-others
#
#

# $data (accepts no keys)
META += [('data', dict())]

# $annotations (accepts no keys)
META += [('annotations', dict())]

# $trace
META += [('trace', OrderedDict([  # TO DO! Why keep this?

    ('x', dict(type='data')),
    ('y', dict(type='data')),
    ('z', dict(type='data')),
    ('r', dict(type='data')),
    ('t', dict(type='data')),
    ('text', dict(type='data')),
    ('name', dict(type='data')),
    ('mode', dict(type='plot_info')),
    ('marker', dict(type='object')),
    ('line', dict(type='object')),
    ('fill', dict(type='style')),
    ('fillcolor', dict(type='style')),
    ('opacity', dict(type='style')),
    ('showlegend', dict(type='style')),
    ('xaxis', dict(type='plot_info')),
    ('yaxis', dict(type='plot_info')),
    ('angularaxis', dict()),
    ('radialaxis', dict()),
    ('error_y', dict(type='object')),
    ('error_x', dict(type='object')),
    ('textfont', dict(type='object')),
    ('type', dict(type='plot_info')),
    ('orientation', dict(type='plot_info')),
    ('boxpoints', dict(type='style')),
    ('jitter', dict(type='style')),
    ('pointpos', dict(type='style')),
    ('boxmean', dict(type='style')),
    ('whiskerwidth', dict(type='style')),
    ('scl', dict(type='style')),
    ('reversescl', dict(type='style')),
    ('colorbar', dict(type='object')),
    ('autobinx', dict(type='style')),
    ('autobiny', dict(type='style')),
    ('xbins', dict(type='object')),
    ('ybins', dict(type='object')),
    ('histnorm', dict(type='plot_info')),
    ('zmax', dict(type='plot_info')),
    ('zmin', dict(type='plot_info')),
    ('dx', dict()),
    ('dy', dict()),
    ('x0', dict()),
    ('y0', dict()),
    ('zauto', dict(type='plot_info')),
    ('hm_id', dict()),
    ('nbinsx', dict(type='style')),
    ('nbinsy', dict(type='style')),
    ('showscale', dict(type='style'))

]))]

# $plotlylist (accepts no keys)
META += [('plotlylist', dict())]

# $plotlydict (accepts no keys)
META += [('plotlydict', dict())] 

# $plotlytrace (accepts no keys)
META += [('plotlytrace', dict())]

# -------------------------------------------------------------------------------


## Write to json

#
INFO = OrderedDict(META)

if __name__ == "__main__":
    import json

    with open('graph_objs_meta.json', 'w') as f:
        f.write(json.dumps(INFO, indent=4, sort_keys=False))

    obj_keys = dict()
    for key, val in INFO.items():
        obj_keys[key] = val.keys()
        obj_keys[key].sort()
    with open('graph_objs_keys.json', 'w') as f:
        f.write(json.dumps(obj_keys, indent=4, sort_keys=True))

    checklist = dict()
    for key, val in INFO.items():
        checklist[key] = dict()
        for k in val:
            checklist[key][k] = dict()
            if 'required' not in INFO[key][k]:
                 checklist[key][k]['required'] = 'UNDOCUMENTED'
            if 'type' not in INFO[key][k]:
                checklist[key][k]['type'] = 'UNDOCUMENTED'
            if 'val_types' not in INFO[key][k]:
                checklist[key][k]['val_types'] = 'UNDOCUMENTED'
            if 'description' not in INFO[key][k]:
                checklist[key][k]['description'] = 'UNDOCUMENTED'
            if checklist[key][k] == dict():
                del checklist[key][k]
        if checklist[key] == dict():
            del checklist[key]
    with open('graph_objs_checklist.json', 'w') as f:
        f.write(json.dumps(checklist, indent=4, sort_keys=False))
