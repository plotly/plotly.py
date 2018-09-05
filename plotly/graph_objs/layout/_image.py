from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Image(BaseLayoutHierarchyType):

    # layer
    # -----
    @property
    def layer(self):
        """
        Specifies whether images are drawn below or above traces. When
        `xref` and `yref` are both set to `paper`, image is drawn below
        the entire plot area.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['below', 'above']

        Returns
        -------
        Any
        """
        return self['layer']

    @layer.setter
    def layer(self, val):
        self['layer'] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the image.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # sizex
    # -----
    @property
    def sizex(self):
        """
        Sets the image container size horizontally. The image will be
        sized based on the `position` value. When `xref` is set to
        `paper`, units are sized relative to the plot width.
    
        The 'sizex' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['sizex']

    @sizex.setter
    def sizex(self, val):
        self['sizex'] = val

    # sizey
    # -----
    @property
    def sizey(self):
        """
        Sets the image container size vertically. The image will be
        sized based on the `position` value. When `yref` is set to
        `paper`, units are sized relative to the plot height.
    
        The 'sizey' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['sizey']

    @sizey.setter
    def sizey(self, val):
        self['sizey'] = val

    # sizing
    # ------
    @property
    def sizing(self):
        """
        Specifies which dimension of the image to constrain.
    
        The 'sizing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fill', 'contain', 'stretch']

        Returns
        -------
        Any
        """
        return self['sizing']

    @sizing.setter
    def sizing(self, val):
        self['sizing'] = val

    # source
    # ------
    @property
    def source(self):
        """
        Specifies the URL of the image to be used. The URL must be
        accessible from the domain where the plot code is run, and can
        be either relative or absolute.
    
        The 'source' property is an image URI that may be specified as:
          - A remote image URI string
            (e.g. 'http://www.somewhere.com/image.png')
          - A data URI image string
            (e.g. 'data:image/png;base64,iVBORw0KGgoAAAANSU')
          - A PIL.Image.Image object which will be immediately converted
            to a data URI image string
            See http://pillow.readthedocs.io/en/latest/reference/Image.html

        Returns
        -------
        str
        """
        return self['source']

    @source.setter
    def source(self, val):
        self['source'] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['templateitemname']

    @templateitemname.setter
    def templateitemname(self, val):
        self['templateitemname'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this image is visible.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the image's x position. When `xref` is set to `paper`,
        units are sized relative to the plot height. See `xref` for
        more info
    
        The 'x' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the anchor for the x position
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the images's x coordinate axis. If set to a x axis id
        (e.g. "x" or "x2"), the `x` position refers to an x data
        coordinate If set to "paper", the `x` position refers to the
        distance from the left of plot in normalized coordinates where
        0 (1) corresponds to the left (right).
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['xref']

    @xref.setter
    def xref(self, val):
        self['xref'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the image's y position. When `yref` is set to `paper`,
        units are sized relative to the plot height. See `yref` for
        more info
    
        The 'y' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the anchor for the y position.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the images's y coordinate axis. If set to a y axis id
        (e.g. "y" or "y2"), the `y` position refers to a y data
        coordinate. If set to "paper", the `y` position refers to the
        distance from the bottom of the plot in normalized coordinates
        where 0 (1) corresponds to the bottom (top).
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['yref']

    @yref.setter
    def yref(self, val):
        self['yref'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        layer
            Specifies whether images are drawn below or above
            traces. When `xref` and `yref` are both set to `paper`,
            image is drawn below the entire plot area.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the image.
        sizex
            Sets the image container size horizontally. The image
            will be sized based on the `position` value. When
            `xref` is set to `paper`, units are sized relative to
            the plot width.
        sizey
            Sets the image container size vertically. The image
            will be sized based on the `position` value. When
            `yref` is set to `paper`, units are sized relative to
            the plot height.
        sizing
            Specifies which dimension of the image to constrain.
        source
            Specifies the URL of the image to be used. The URL must
            be accessible from the domain where the plot code is
            run, and can be either relative or absolute.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this image is visible.
        x
            Sets the image's x position. When `xref` is set to
            `paper`, units are sized relative to the plot height.
            See `xref` for more info
        xanchor
            Sets the anchor for the x position
        xref
            Sets the images's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            data coordinate If set to "paper", the `x` position
            refers to the distance from the left of plot in
            normalized coordinates where 0 (1) corresponds to the
            left (right).
        y
            Sets the image's y position. When `yref` is set to
            `paper`, units are sized relative to the plot height.
            See `yref` for more info
        yanchor
            Sets the anchor for the y position.
        yref
            Sets the images's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            data coordinate. If set to "paper", the `y` position
            refers to the distance from the bottom of the plot in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top).
        """

    def __init__(
        self,
        arg=None,
        layer=None,
        name=None,
        opacity=None,
        sizex=None,
        sizey=None,
        sizing=None,
        source=None,
        templateitemname=None,
        visible=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        **kwargs
    ):
        """
        Construct a new Image object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Image
        layer
            Specifies whether images are drawn below or above
            traces. When `xref` and `yref` are both set to `paper`,
            image is drawn below the entire plot area.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the image.
        sizex
            Sets the image container size horizontally. The image
            will be sized based on the `position` value. When
            `xref` is set to `paper`, units are sized relative to
            the plot width.
        sizey
            Sets the image container size vertically. The image
            will be sized based on the `position` value. When
            `yref` is set to `paper`, units are sized relative to
            the plot height.
        sizing
            Specifies which dimension of the image to constrain.
        source
            Specifies the URL of the image to be used. The URL must
            be accessible from the domain where the plot code is
            run, and can be either relative or absolute.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this image is visible.
        x
            Sets the image's x position. When `xref` is set to
            `paper`, units are sized relative to the plot height.
            See `xref` for more info
        xanchor
            Sets the anchor for the x position
        xref
            Sets the images's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            data coordinate If set to "paper", the `x` position
            refers to the distance from the left of plot in
            normalized coordinates where 0 (1) corresponds to the
            left (right).
        y
            Sets the image's y position. When `yref` is set to
            `paper`, units are sized relative to the plot height.
            See `yref` for more info
        yanchor
            Sets the anchor for the y position.
        yref
            Sets the images's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            data coordinate. If set to "paper", the `y` position
            refers to the distance from the bottom of the plot in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top).

        Returns
        -------
        Image
        """
        super(Image, self).__init__('images')

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
The first argument to the plotly.graph_objs.layout.Image 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Image"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout import (image as v_image)

        # Initialize validators
        # ---------------------
        self._validators['layer'] = v_image.LayerValidator()
        self._validators['name'] = v_image.NameValidator()
        self._validators['opacity'] = v_image.OpacityValidator()
        self._validators['sizex'] = v_image.SizexValidator()
        self._validators['sizey'] = v_image.SizeyValidator()
        self._validators['sizing'] = v_image.SizingValidator()
        self._validators['source'] = v_image.SourceValidator()
        self._validators['templateitemname'
                        ] = v_image.TemplateitemnameValidator()
        self._validators['visible'] = v_image.VisibleValidator()
        self._validators['x'] = v_image.XValidator()
        self._validators['xanchor'] = v_image.XanchorValidator()
        self._validators['xref'] = v_image.XrefValidator()
        self._validators['y'] = v_image.YValidator()
        self._validators['yanchor'] = v_image.YanchorValidator()
        self._validators['yref'] = v_image.YrefValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('layer', None)
        self.layer = layer if layer is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('sizex', None)
        self.sizex = sizex if sizex is not None else _v
        _v = arg.pop('sizey', None)
        self.sizey = sizey if sizey is not None else _v
        _v = arg.pop('sizing', None)
        self.sizing = sizing if sizing is not None else _v
        _v = arg.pop('source', None)
        self.source = source if source is not None else _v
        _v = arg.pop('templateitemname', None)
        self.templateitemname = templateitemname if templateitemname is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v
        _v = arg.pop('x', None)
        self.x = x if x is not None else _v
        _v = arg.pop('xanchor', None)
        self.xanchor = xanchor if xanchor is not None else _v
        _v = arg.pop('xref', None)
        self.xref = xref if xref is not None else _v
        _v = arg.pop('y', None)
        self.y = y if y is not None else _v
        _v = arg.pop('yanchor', None)
        self.yanchor = yanchor if yanchor is not None else _v
        _v = arg.pop('yref', None)
        self.yref = yref if yref is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
