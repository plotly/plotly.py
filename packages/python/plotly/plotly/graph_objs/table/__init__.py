from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Stream(_BaseTraceHierarchyType):

    # maxpoints
    # ---------
    @property
    def maxpoints(self):
        """
        Sets the maximum number of points to keep on the plots from an
        incoming stream. If `maxpoints` is set to 50, only the newest
        50 points will be displayed on the plot.
    
        The 'maxpoints' property is a number and may be specified as:
          - An int or float in the interval [0, 10000]

        Returns
        -------
        int|float
        """
        return self["maxpoints"]

    @maxpoints.setter
    def maxpoints(self, val):
        self["maxpoints"] = val

    # token
    # -----
    @property
    def token(self):
        """
        The stream id number links a data trace on a plot with a
        stream. See https://plot.ly/settings for more details.
    
        The 'token' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["token"]

    @token.setter
    def token(self, val):
        self["token"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "table"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.
        """

    def __init__(self, arg=None, maxpoints=None, token=None, **kwargs):
        """
        Construct a new Stream object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.table.Stream
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.

        Returns
        -------
        Stream
        """
        super(Stream, self).__init__("stream")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.table.Stream 
constructor must be a dict or 
an instance of plotly.graph_objs.table.Stream"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.table import stream as v_stream

        # Initialize validators
        # ---------------------
        self._validators["maxpoints"] = v_stream.MaxpointsValidator()
        self._validators["token"] = v_stream.TokenValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("maxpoints", None)
        self["maxpoints"] = maxpoints if maxpoints is not None else _v
        _v = arg.pop("token", None)
        self["token"] = token if token is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Hoverlabel(_BaseTraceHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the text content within hover
        label box. Has an effect only if the hover label text spans
        more two or more lines
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'auto']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # alignsrc
    # --------
    @property
    def alignsrc(self):
        """
        Sets the source reference on plot.ly for  align .
    
        The 'alignsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the hover labels for this trace
    
        The 'bgcolor' property is a color and may be specified as:
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
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bgcolorsrc
    # ----------
    @property
    def bgcolorsrc(self):
        """
        Sets the source reference on plot.ly for  bgcolor .
    
        The 'bgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bgcolorsrc"]

    @bgcolorsrc.setter
    def bgcolorsrc(self, val):
        self["bgcolorsrc"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the border color of the hover labels for this trace.
    
        The 'bordercolor' property is a color and may be specified as:
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
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # bordercolorsrc
    # --------------
    @property
    def bordercolorsrc(self):
        """
        Sets the source reference on plot.ly for  bordercolor .
    
        The 'bordercolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bordercolorsrc"]

    @bordercolorsrc.setter
    def bordercolorsrc(self, val):
        self["bordercolorsrc"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used in hover labels.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.table.hoverlabel.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
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
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.table.hoverlabel.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # namelength
    # ----------
    @property
    def namelength(self):
        """
        Sets the default length (in number of characters) of the trace
        name in the hover labels for all traces. -1 shows the whole
        name regardless of length. 0-3 shows the first 0-3 characters,
        and an integer >3 will show the whole name if it is less than
        that many characters, but if it is longer, will truncate to
        `namelength - 3` characters and add an ellipsis.
    
        The 'namelength' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|numpy.ndarray
        """
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    # namelengthsrc
    # -------------
    @property
    def namelengthsrc(self):
        """
        Sets the source reference on plot.ly for  namelength .
    
        The 'namelengthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["namelengthsrc"]

    @namelengthsrc.setter
    def namelengthsrc(self, val):
        self["namelengthsrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "table"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on plot.ly for  align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on plot.ly for  bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on plot.ly for  bordercolor .
        font
            Sets the font used in hover labels.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        namelengthsrc
            Sets the source reference on plot.ly for  namelength .
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        bgcolor=None,
        bgcolorsrc=None,
        bordercolor=None,
        bordercolorsrc=None,
        font=None,
        namelength=None,
        namelengthsrc=None,
        **kwargs
    ):
        """
        Construct a new Hoverlabel object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.table.Hoverlabel
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on plot.ly for  align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on plot.ly for  bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on plot.ly for  bordercolor .
        font
            Sets the font used in hover labels.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        namelengthsrc
            Sets the source reference on plot.ly for  namelength .

        Returns
        -------
        Hoverlabel
        """
        super(Hoverlabel, self).__init__("hoverlabel")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.table.Hoverlabel 
constructor must be a dict or 
an instance of plotly.graph_objs.table.Hoverlabel"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.table import hoverlabel as v_hoverlabel

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_hoverlabel.AlignValidator()
        self._validators["alignsrc"] = v_hoverlabel.AlignsrcValidator()
        self._validators["bgcolor"] = v_hoverlabel.BgcolorValidator()
        self._validators["bgcolorsrc"] = v_hoverlabel.BgcolorsrcValidator()
        self._validators["bordercolor"] = v_hoverlabel.BordercolorValidator()
        self._validators["bordercolorsrc"] = v_hoverlabel.BordercolorsrcValidator()
        self._validators["font"] = v_hoverlabel.FontValidator()
        self._validators["namelength"] = v_hoverlabel.NamelengthValidator()
        self._validators["namelengthsrc"] = v_hoverlabel.NamelengthsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("alignsrc", None)
        self["alignsrc"] = alignsrc if alignsrc is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bgcolorsrc", None)
        self["bgcolorsrc"] = bgcolorsrc if bgcolorsrc is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("bordercolorsrc", None)
        self["bordercolorsrc"] = bordercolorsrc if bordercolorsrc is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("namelength", None)
        self["namelength"] = namelength if namelength is not None else _v
        _v = arg.pop("namelengthsrc", None)
        self["namelengthsrc"] = namelengthsrc if namelengthsrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Header(_BaseTraceHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the `text` within the box. Has
        an effect only if `text` spans more two or more lines (i.e.
        `text` contains one or more <br> HTML tags) or if an explicit
        width is set to override the text width.
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # alignsrc
    # --------
    @property
    def alignsrc(self):
        """
        Sets the source reference on plot.ly for  align .
    
        The 'alignsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    # fill
    # ----
    @property
    def fill(self):
        """
        The 'fill' property is an instance of Fill
        that may be specified as:
          - An instance of plotly.graph_objs.table.header.Fill
          - A dict of string/value properties that will be passed
            to the Fill constructor
    
            Supported dict properties:
                
                color
                    Sets the cell fill color. It accepts either a
                    specific color or an array of colors or a 2D
                    array of colors.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .

        Returns
        -------
        plotly.graph_objs.table.header.Fill
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    # font
    # ----
    @property
    def font(self):
        """
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.table.header.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
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
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.table.header.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # format
    # ------
    @property
    def format(self):
        """
        Sets the cell value formatting rule using d3 formatting mini-
        language which is similar to those of Python. See
        https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format
    
        The 'format' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["format"]

    @format.setter
    def format(self, val):
        self["format"] = val

    # formatsrc
    # ---------
    @property
    def formatsrc(self):
        """
        Sets the source reference on plot.ly for  format .
    
        The 'formatsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["formatsrc"]

    @formatsrc.setter
    def formatsrc(self, val):
        self["formatsrc"] = val

    # height
    # ------
    @property
    def height(self):
        """
        The height of cells.
    
        The 'height' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["height"]

    @height.setter
    def height(self, val):
        self["height"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.table.header.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
    
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.table.header.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # prefix
    # ------
    @property
    def prefix(self):
        """
        Prefix for cell values.
    
        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    # prefixsrc
    # ---------
    @property
    def prefixsrc(self):
        """
        Sets the source reference on plot.ly for  prefix .
    
        The 'prefixsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["prefixsrc"]

    @prefixsrc.setter
    def prefixsrc(self, val):
        self["prefixsrc"] = val

    # suffix
    # ------
    @property
    def suffix(self):
        """
        Suffix for cell values.
    
        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    # suffixsrc
    # ---------
    @property
    def suffixsrc(self):
        """
        Sets the source reference on plot.ly for  suffix .
    
        The 'suffixsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["suffixsrc"]

    @suffixsrc.setter
    def suffixsrc(self, val):
        self["suffixsrc"] = val

    # values
    # ------
    @property
    def values(self):
        """
        Header cell values. `values[m][n]` represents the value of the
        `n`th point in column `m`, therefore the `values[m]` vector
        length for all columns must be the same (longer vectors will be
        truncated). Each value must be a finite number or a string.
    
        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    # valuessrc
    # ---------
    @property
    def valuessrc(self):
        """
        Sets the source reference on plot.ly for  values .
    
        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["valuessrc"]

    @valuessrc.setter
    def valuessrc(self, val):
        self["valuessrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "table"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        alignsrc
            Sets the source reference on plot.ly for  align .
        fill
            plotly.graph_objects.table.header.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objects.table.header.Font instance or dict
            with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        formatsrc
            Sets the source reference on plot.ly for  format .
        height
            The height of cells.
        line
            plotly.graph_objects.table.header.Line instance or dict
            with compatible properties
        prefix
            Prefix for cell values.
        prefixsrc
            Sets the source reference on plot.ly for  prefix .
        suffix
            Suffix for cell values.
        suffixsrc
            Sets the source reference on plot.ly for  suffix .
        values
            Header cell values. `values[m][n]` represents the value
            of the `n`th point in column `m`, therefore the
            `values[m]` vector length for all columns must be the
            same (longer vectors will be truncated). Each value
            must be a finite number or a string.
        valuessrc
            Sets the source reference on plot.ly for  values .
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        fill=None,
        font=None,
        format=None,
        formatsrc=None,
        height=None,
        line=None,
        prefix=None,
        prefixsrc=None,
        suffix=None,
        suffixsrc=None,
        values=None,
        valuessrc=None,
        **kwargs
    ):
        """
        Construct a new Header object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.table.Header
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        alignsrc
            Sets the source reference on plot.ly for  align .
        fill
            plotly.graph_objects.table.header.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objects.table.header.Font instance or dict
            with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        formatsrc
            Sets the source reference on plot.ly for  format .
        height
            The height of cells.
        line
            plotly.graph_objects.table.header.Line instance or dict
            with compatible properties
        prefix
            Prefix for cell values.
        prefixsrc
            Sets the source reference on plot.ly for  prefix .
        suffix
            Suffix for cell values.
        suffixsrc
            Sets the source reference on plot.ly for  suffix .
        values
            Header cell values. `values[m][n]` represents the value
            of the `n`th point in column `m`, therefore the
            `values[m]` vector length for all columns must be the
            same (longer vectors will be truncated). Each value
            must be a finite number or a string.
        valuessrc
            Sets the source reference on plot.ly for  values .

        Returns
        -------
        Header
        """
        super(Header, self).__init__("header")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.table.Header 
constructor must be a dict or 
an instance of plotly.graph_objs.table.Header"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.table import header as v_header

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_header.AlignValidator()
        self._validators["alignsrc"] = v_header.AlignsrcValidator()
        self._validators["fill"] = v_header.FillValidator()
        self._validators["font"] = v_header.FontValidator()
        self._validators["format"] = v_header.FormatValidator()
        self._validators["formatsrc"] = v_header.FormatsrcValidator()
        self._validators["height"] = v_header.HeightValidator()
        self._validators["line"] = v_header.LineValidator()
        self._validators["prefix"] = v_header.PrefixValidator()
        self._validators["prefixsrc"] = v_header.PrefixsrcValidator()
        self._validators["suffix"] = v_header.SuffixValidator()
        self._validators["suffixsrc"] = v_header.SuffixsrcValidator()
        self._validators["values"] = v_header.ValuesValidator()
        self._validators["valuessrc"] = v_header.ValuessrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("alignsrc", None)
        self["alignsrc"] = alignsrc if alignsrc is not None else _v
        _v = arg.pop("fill", None)
        self["fill"] = fill if fill is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("format", None)
        self["format"] = format if format is not None else _v
        _v = arg.pop("formatsrc", None)
        self["formatsrc"] = formatsrc if formatsrc is not None else _v
        _v = arg.pop("height", None)
        self["height"] = height if height is not None else _v
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v
        _v = arg.pop("prefix", None)
        self["prefix"] = prefix if prefix is not None else _v
        _v = arg.pop("prefixsrc", None)
        self["prefixsrc"] = prefixsrc if prefixsrc is not None else _v
        _v = arg.pop("suffix", None)
        self["suffix"] = suffix if suffix is not None else _v
        _v = arg.pop("suffixsrc", None)
        self["suffixsrc"] = suffixsrc if suffixsrc is not None else _v
        _v = arg.pop("values", None)
        self["values"] = values if values is not None else _v
        _v = arg.pop("valuessrc", None)
        self["valuessrc"] = valuessrc if valuessrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Domain(_BaseTraceHierarchyType):

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this table trace .
    
        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["column"]

    @column.setter
    def column(self, val):
        self["column"] = val

    # row
    # ---
    @property
    def row(self):
        """
        If there is a layout grid, use the domain for this row in the
        grid for this table trace .
    
        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["row"]

    @row.setter
    def row(self, val):
        self["row"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this table trace (in plot
        fraction).
    
        The 'x' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this table trace (in plot
        fraction).
    
        The 'y' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "table"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this table trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this table trace .
        x
            Sets the horizontal domain of this table trace (in plot
            fraction).
        y
            Sets the vertical domain of this table trace (in plot
            fraction).
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.table.Domain
        column
            If there is a layout grid, use the domain for this
            column in the grid for this table trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this table trace .
        x
            Sets the horizontal domain of this table trace (in plot
            fraction).
        y
            Sets the vertical domain of this table trace (in plot
            fraction).

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__("domain")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.table.Domain 
constructor must be a dict or 
an instance of plotly.graph_objs.table.Domain"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.table import domain as v_domain

        # Initialize validators
        # ---------------------
        self._validators["column"] = v_domain.ColumnValidator()
        self._validators["row"] = v_domain.RowValidator()
        self._validators["x"] = v_domain.XValidator()
        self._validators["y"] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("column", None)
        self["column"] = column if column is not None else _v
        _v = arg.pop("row", None)
        self["row"] = row if row is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Cells(_BaseTraceHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the `text` within the box. Has
        an effect only if `text` spans more two or more lines (i.e.
        `text` contains one or more <br> HTML tags) or if an explicit
        width is set to override the text width.
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # alignsrc
    # --------
    @property
    def alignsrc(self):
        """
        Sets the source reference on plot.ly for  align .
    
        The 'alignsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    # fill
    # ----
    @property
    def fill(self):
        """
        The 'fill' property is an instance of Fill
        that may be specified as:
          - An instance of plotly.graph_objs.table.cells.Fill
          - A dict of string/value properties that will be passed
            to the Fill constructor
    
            Supported dict properties:
                
                color
                    Sets the cell fill color. It accepts either a
                    specific color or an array of colors or a 2D
                    array of colors.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .

        Returns
        -------
        plotly.graph_objs.table.cells.Fill
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    # font
    # ----
    @property
    def font(self):
        """
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.table.cells.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
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
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.table.cells.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # format
    # ------
    @property
    def format(self):
        """
        Sets the cell value formatting rule using d3 formatting mini-
        language which is similar to those of Python. See
        https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format
    
        The 'format' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["format"]

    @format.setter
    def format(self, val):
        self["format"] = val

    # formatsrc
    # ---------
    @property
    def formatsrc(self):
        """
        Sets the source reference on plot.ly for  format .
    
        The 'formatsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["formatsrc"]

    @formatsrc.setter
    def formatsrc(self, val):
        self["formatsrc"] = val

    # height
    # ------
    @property
    def height(self):
        """
        The height of cells.
    
        The 'height' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["height"]

    @height.setter
    def height(self, val):
        self["height"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.table.cells.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
    
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.table.cells.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # prefix
    # ------
    @property
    def prefix(self):
        """
        Prefix for cell values.
    
        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    # prefixsrc
    # ---------
    @property
    def prefixsrc(self):
        """
        Sets the source reference on plot.ly for  prefix .
    
        The 'prefixsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["prefixsrc"]

    @prefixsrc.setter
    def prefixsrc(self, val):
        self["prefixsrc"] = val

    # suffix
    # ------
    @property
    def suffix(self):
        """
        Suffix for cell values.
    
        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    # suffixsrc
    # ---------
    @property
    def suffixsrc(self):
        """
        Sets the source reference on plot.ly for  suffix .
    
        The 'suffixsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["suffixsrc"]

    @suffixsrc.setter
    def suffixsrc(self, val):
        self["suffixsrc"] = val

    # values
    # ------
    @property
    def values(self):
        """
        Cell values. `values[m][n]` represents the value of the `n`th
        point in column `m`, therefore the `values[m]` vector length
        for all columns must be the same (longer vectors will be
        truncated). Each value must be a finite number or a string.
    
        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    # valuessrc
    # ---------
    @property
    def valuessrc(self):
        """
        Sets the source reference on plot.ly for  values .
    
        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["valuessrc"]

    @valuessrc.setter
    def valuessrc(self, val):
        self["valuessrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "table"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        alignsrc
            Sets the source reference on plot.ly for  align .
        fill
            plotly.graph_objects.table.cells.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objects.table.cells.Font instance or dict
            with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        formatsrc
            Sets the source reference on plot.ly for  format .
        height
            The height of cells.
        line
            plotly.graph_objects.table.cells.Line instance or dict
            with compatible properties
        prefix
            Prefix for cell values.
        prefixsrc
            Sets the source reference on plot.ly for  prefix .
        suffix
            Suffix for cell values.
        suffixsrc
            Sets the source reference on plot.ly for  suffix .
        values
            Cell values. `values[m][n]` represents the value of the
            `n`th point in column `m`, therefore the `values[m]`
            vector length for all columns must be the same (longer
            vectors will be truncated). Each value must be a finite
            number or a string.
        valuessrc
            Sets the source reference on plot.ly for  values .
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        fill=None,
        font=None,
        format=None,
        formatsrc=None,
        height=None,
        line=None,
        prefix=None,
        prefixsrc=None,
        suffix=None,
        suffixsrc=None,
        values=None,
        valuessrc=None,
        **kwargs
    ):
        """
        Construct a new Cells object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.table.Cells
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        alignsrc
            Sets the source reference on plot.ly for  align .
        fill
            plotly.graph_objects.table.cells.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objects.table.cells.Font instance or dict
            with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        formatsrc
            Sets the source reference on plot.ly for  format .
        height
            The height of cells.
        line
            plotly.graph_objects.table.cells.Line instance or dict
            with compatible properties
        prefix
            Prefix for cell values.
        prefixsrc
            Sets the source reference on plot.ly for  prefix .
        suffix
            Suffix for cell values.
        suffixsrc
            Sets the source reference on plot.ly for  suffix .
        values
            Cell values. `values[m][n]` represents the value of the
            `n`th point in column `m`, therefore the `values[m]`
            vector length for all columns must be the same (longer
            vectors will be truncated). Each value must be a finite
            number or a string.
        valuessrc
            Sets the source reference on plot.ly for  values .

        Returns
        -------
        Cells
        """
        super(Cells, self).__init__("cells")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.table.Cells 
constructor must be a dict or 
an instance of plotly.graph_objs.table.Cells"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.table import cells as v_cells

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_cells.AlignValidator()
        self._validators["alignsrc"] = v_cells.AlignsrcValidator()
        self._validators["fill"] = v_cells.FillValidator()
        self._validators["font"] = v_cells.FontValidator()
        self._validators["format"] = v_cells.FormatValidator()
        self._validators["formatsrc"] = v_cells.FormatsrcValidator()
        self._validators["height"] = v_cells.HeightValidator()
        self._validators["line"] = v_cells.LineValidator()
        self._validators["prefix"] = v_cells.PrefixValidator()
        self._validators["prefixsrc"] = v_cells.PrefixsrcValidator()
        self._validators["suffix"] = v_cells.SuffixValidator()
        self._validators["suffixsrc"] = v_cells.SuffixsrcValidator()
        self._validators["values"] = v_cells.ValuesValidator()
        self._validators["valuessrc"] = v_cells.ValuessrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("alignsrc", None)
        self["alignsrc"] = alignsrc if alignsrc is not None else _v
        _v = arg.pop("fill", None)
        self["fill"] = fill if fill is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("format", None)
        self["format"] = format if format is not None else _v
        _v = arg.pop("formatsrc", None)
        self["formatsrc"] = formatsrc if formatsrc is not None else _v
        _v = arg.pop("height", None)
        self["height"] = height if height is not None else _v
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v
        _v = arg.pop("prefix", None)
        self["prefix"] = prefix if prefix is not None else _v
        _v = arg.pop("prefixsrc", None)
        self["prefixsrc"] = prefixsrc if prefixsrc is not None else _v
        _v = arg.pop("suffix", None)
        self["suffix"] = suffix if suffix is not None else _v
        _v = arg.pop("suffixsrc", None)
        self["suffixsrc"] = suffixsrc if suffixsrc is not None else _v
        _v = arg.pop("values", None)
        self["values"] = values if values is not None else _v
        _v = arg.pop("valuessrc", None)
        self["valuessrc"] = valuessrc if valuessrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.graph_objs.table import hoverlabel
from plotly.graph_objs.table import header
from plotly.graph_objs.table import cells
