from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Title(BaseTraceHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets this color bar's title font. Note that the title's font
        used to be set by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.scattergeo.marker.colorbar.title.Font
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
        plotly.graph_objs.scattergeo.marker.colorbar.title.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # side
    # ----
    @property
    def side(self):
        """
        Determines the location of color bar's title with respect to
        the color bar. Note that the title's location used to be set by
        the now deprecated `titleside` attribute.
    
        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['right', 'top', 'bottom']

        Returns
        -------
        Any
        """
        return self['side']

    @side.setter
    def side(self, val):
        self['side'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of the color bar. Note that before the existence
        of `title.text`, the title's contents used to be defined as the
        `title` attribute itself. This behavior has been deprecated.
    
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
        return 'scattergeo.marker.colorbar'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets this color bar's title font. Note that the title's
            font used to be set by the now deprecated `titlefont`
            attribute.
        side
            Determines the location of color bar's title with
            respect to the color bar. Note that the title's
            location used to be set by the now deprecated
            `titleside` attribute.
        text
            Sets the title of the color bar. Note that before the
            existence of `title.text`, the title's contents used to
            be defined as the `title` attribute itself. This
            behavior has been deprecated.
        """

    def __init__(self, arg=None, font=None, side=None, text=None, **kwargs):
        """
        Construct a new Title object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.scattergeo.marker.colorbar.Title
        font
            Sets this color bar's title font. Note that the title's
            font used to be set by the now deprecated `titlefont`
            attribute.
        side
            Determines the location of color bar's title with
            respect to the color bar. Note that the title's
            location used to be set by the now deprecated
            `titleside` attribute.
        text
            Sets the title of the color bar. Note that before the
            existence of `title.text`, the title's contents used to
            be defined as the `title` attribute itself. This
            behavior has been deprecated.

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
The first argument to the plotly.graph_objs.scattergeo.marker.colorbar.Title 
constructor must be a dict or 
an instance of plotly.graph_objs.scattergeo.marker.colorbar.Title"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.scattergeo.marker.colorbar import (
            title as v_title
        )

        # Initialize validators
        # ---------------------
        self._validators['font'] = v_title.FontValidator()
        self._validators['side'] = v_title.SideValidator()
        self._validators['text'] = v_title.TextValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('font', None)
        self['font'] = font if font is not None else _v
        _v = arg.pop('side', None)
        self['side'] = side if side is not None else _v
        _v = arg.pop('text', None)
        self['text'] = text if text is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
