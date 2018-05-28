from plotly.basedatatypes import BaseTraceHierarchyType


class Cells(BaseTraceHierarchyType):

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
    
        The 'alignsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

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
          - An instance of plotly.graph_objs.table.cells.Fill
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
        plotly.graph_objs.table.cells.Fill
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
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
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
        list, one-dimensional numpy array, or pandas Series

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
    
        The 'formatsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

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
    
        The 'prefixsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

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
    
        The 'suffixsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

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
        Cell values. `values[m][n]` represents the value of the `n`th
        point in column `m`, therefore the `values[m]` vector length
        for all columns must be the same (longer vectors will be
        truncated). Each value must be a finite number or a string.
    
        The 'values' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

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
    
        The 'valuessrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

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
            plotly.graph_objs.table.cells.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objs.table.cells.Font instance or dict
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
            plotly.graph_objs.table.cells.Line instance or dict
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
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        alignsrc
            Sets the source reference on plot.ly for  align .
        fill
            plotly.graph_objs.table.cells.Fill instance or dict
            with compatible properties
        font
            plotly.graph_objs.table.cells.Font instance or dict
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
            plotly.graph_objs.table.cells.Line instance or dict
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
        super(Cells, self).__init__('cells')

        # Import validators
        # -----------------
        from plotly.validators.table import (cells as v_cells)

        # Initialize validators
        # ---------------------
        self._validators['align'] = v_cells.AlignValidator()
        self._validators['alignsrc'] = v_cells.AlignsrcValidator()
        self._validators['fill'] = v_cells.FillValidator()
        self._validators['font'] = v_cells.FontValidator()
        self._validators['format'] = v_cells.FormatValidator()
        self._validators['formatsrc'] = v_cells.FormatsrcValidator()
        self._validators['height'] = v_cells.HeightValidator()
        self._validators['line'] = v_cells.LineValidator()
        self._validators['prefix'] = v_cells.PrefixValidator()
        self._validators['prefixsrc'] = v_cells.PrefixsrcValidator()
        self._validators['suffix'] = v_cells.SuffixValidator()
        self._validators['suffixsrc'] = v_cells.SuffixsrcValidator()
        self._validators['values'] = v_cells.ValuesValidator()
        self._validators['valuessrc'] = v_cells.ValuessrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.align = align
        self.alignsrc = alignsrc
        self.fill = fill
        self.font = font
        self.format = format
        self.formatsrc = formatsrc
        self.height = height
        self.line = line
        self.prefix = prefix
        self.prefixsrc = prefixsrc
        self.suffix = suffix
        self.suffixsrc = suffixsrc
        self.values = values
        self.valuessrc = valuessrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
