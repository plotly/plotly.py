from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Header(BaseTraceHierarchyType):

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
        return self['align']

    @align.setter
    def align(self, val):
        self['align'] = val

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
        return self['alignsrc']

    @alignsrc.setter
    def alignsrc(self, val):
        self['alignsrc'] = val

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
                    specific color or an array of colors.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .

        Returns
        -------
        plotly.graph_objs.table.header.Fill
        """
        return self['fill']

    @fill.setter
    def fill(self, val):
        self['fill'] = val

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
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # format
    # ------
    @property
    def format(self):
        """
        Sets the cell value formatting rule using d3 formatting mini-
        language which is similar to those of Python. See https://githu
        b.com/d3/d3-format/blob/master/README.md#locale_format
    
        The 'format' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['format']

    @format.setter
    def format(self, val):
        self['format'] = val

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
        return self['formatsrc']

    @formatsrc.setter
    def formatsrc(self, val):
        self['formatsrc'] = val

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
        return self['height']

    @height.setter
    def height(self, val):
        self['height'] = val

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
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

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
        return self['prefix']

    @prefix.setter
    def prefix(self, val):
        self['prefix'] = val

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
        return self['prefixsrc']

    @prefixsrc.setter
    def prefixsrc(self, val):
        self['prefixsrc'] = val

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
        return self['suffix']

    @suffix.setter
    def suffix(self, val):
        self['suffix'] = val

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
        return self['suffixsrc']

    @suffixsrc.setter
    def suffixsrc(self, val):
        self['suffixsrc'] = val

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
        return self['values']

    @values.setter
    def values(self, val):
        self['values'] = val

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
        return self['valuessrc']

    @valuessrc.setter
    def valuessrc(self, val):
        self['valuessrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'table'

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
            plotly.graph_objs.table.header.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objs.table.header.Font instance or dict
            with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        formatsrc
            Sets the source reference on plot.ly for  format .
        height
            The height of cells.
        line
            plotly.graph_objs.table.header.Line instance or dict
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
            plotly.graph_objs.table.header.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objs.table.header.Font instance or dict
            with compatible properties
        format
            Sets the cell value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        formatsrc
            Sets the source reference on plot.ly for  format .
        height
            The height of cells.
        line
            plotly.graph_objs.table.header.Line instance or dict
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
        super(Header, self).__init__('header')

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
The first argument to the plotly.graph_objs.table.Header 
constructor must be a dict or 
an instance of plotly.graph_objs.table.Header"""
            )

        # Import validators
        # -----------------
        from plotly.validators.table import (header as v_header)

        # Initialize validators
        # ---------------------
        self._validators['align'] = v_header.AlignValidator()
        self._validators['alignsrc'] = v_header.AlignsrcValidator()
        self._validators['fill'] = v_header.FillValidator()
        self._validators['font'] = v_header.FontValidator()
        self._validators['format'] = v_header.FormatValidator()
        self._validators['formatsrc'] = v_header.FormatsrcValidator()
        self._validators['height'] = v_header.HeightValidator()
        self._validators['line'] = v_header.LineValidator()
        self._validators['prefix'] = v_header.PrefixValidator()
        self._validators['prefixsrc'] = v_header.PrefixsrcValidator()
        self._validators['suffix'] = v_header.SuffixValidator()
        self._validators['suffixsrc'] = v_header.SuffixsrcValidator()
        self._validators['values'] = v_header.ValuesValidator()
        self._validators['valuessrc'] = v_header.ValuessrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('align', None)
        self.align = align if align is not None else _v
        _v = arg.pop('alignsrc', None)
        self.alignsrc = alignsrc if alignsrc is not None else _v
        _v = arg.pop('fill', None)
        self.fill = fill if fill is not None else _v
        _v = arg.pop('font', None)
        self.font = font if font is not None else _v
        _v = arg.pop('format', None)
        self.format = format if format is not None else _v
        _v = arg.pop('formatsrc', None)
        self.formatsrc = formatsrc if formatsrc is not None else _v
        _v = arg.pop('height', None)
        self.height = height if height is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('prefix', None)
        self.prefix = prefix if prefix is not None else _v
        _v = arg.pop('prefixsrc', None)
        self.prefixsrc = prefixsrc if prefixsrc is not None else _v
        _v = arg.pop('suffix', None)
        self.suffix = suffix if suffix is not None else _v
        _v = arg.pop('suffixsrc', None)
        self.suffixsrc = suffixsrc if suffixsrc is not None else _v
        _v = arg.pop('values', None)
        self.values = values if values is not None else _v
        _v = arg.pop('valuessrc', None)
        self.valuessrc = valuessrc if valuessrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
