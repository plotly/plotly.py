from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Title(BaseTraceHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used for `title`. Note that the title's font used
        to be set by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.pie.title.Font
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
        plotly.graph_objs.pie.title.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # position
    # --------
    @property
    def position(self):
        """
        Specifies the location of the `title`. Note that the title's
        position used to be set by the now deprecated `titleposition`
        attribute.
    
        The 'position' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle center',
                'bottom left', 'bottom center', 'bottom right']

        Returns
        -------
        Any
        """
        return self['position']

    @position.setter
    def position(self, val):
        self['position'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of the pie chart. If it is empty, no title is
        displayed. Note that before the existence of `title.text`, the
        title's contents used to be defined as the `title` attribute
        itself. This behavior has been deprecated.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'pie'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets the font used for `title`. Note that the title's
            font used to be set by the now deprecated `titlefont`
            attribute.
        position
            Specifies the location of the `title`. Note that the
            title's position used to be set by the now deprecated
            `titleposition` attribute.
        text
            Sets the title of the pie chart. If it is empty, no
            title is displayed. Note that before the existence of
            `title.text`, the title's contents used to be defined
            as the `title` attribute itself. This behavior has been
            deprecated.
        """

    def __init__(
        self, arg=None, font=None, position=None, text=None, **kwargs
    ):
        """
        Construct a new Title object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Title
        font
            Sets the font used for `title`. Note that the title's
            font used to be set by the now deprecated `titlefont`
            attribute.
        position
            Specifies the location of the `title`. Note that the
            title's position used to be set by the now deprecated
            `titleposition` attribute.
        text
            Sets the title of the pie chart. If it is empty, no
            title is displayed. Note that before the existence of
            `title.text`, the title's contents used to be defined
            as the `title` attribute itself. This behavior has been
            deprecated.

        Returns
        -------
        Title
        """
        super(Title, self).__init__('title')

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
The first argument to the plotly.graph_objs.pie.Title 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Title"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.pie import (title as v_title)

        # Initialize validators
        # ---------------------
        self._validators['font'] = v_title.FontValidator()
        self._validators['position'] = v_title.PositionValidator()
        self._validators['text'] = v_title.TextValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('font', None)
        self['font'] = font if font is not None else _v
        _v = arg.pop('position', None)
        self['position'] = position if position is not None else _v
        _v = arg.pop('text', None)
        self['text'] = text if text is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
