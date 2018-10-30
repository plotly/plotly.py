from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Template(BaseLayoutHierarchyType):

    # data
    # ----
    @property
    def data(self):
        """
        The 'data' property is an instance of Data
        that may be specified as:
          - An instance of plotly.graph_objs.layout.template.Data
          - A dict of string/value properties that will be passed
            to the Data constructor
    
            Supported dict properties:
                
                area
                    plotly.graph_objs.layout.template.data.Area
                    instance or dict with compatible properties
                barpolar
                    plotly.graph_objs.layout.template.data.Barpolar
                    instance or dict with compatible properties
                bar
                    plotly.graph_objs.layout.template.data.Bar
                    instance or dict with compatible properties
                box
                    plotly.graph_objs.layout.template.data.Box
                    instance or dict with compatible properties
                candlestick
                    plotly.graph_objs.layout.template.data.Candlest
                    ick instance or dict with compatible properties
                carpet
                    plotly.graph_objs.layout.template.data.Carpet
                    instance or dict with compatible properties
                choropleth
                    plotly.graph_objs.layout.template.data.Chorople
                    th instance or dict with compatible properties
                cone
                    plotly.graph_objs.layout.template.data.Cone
                    instance or dict with compatible properties
                contourcarpet
                    plotly.graph_objs.layout.template.data.Contourc
                    arpet instance or dict with compatible
                    properties
                contour
                    plotly.graph_objs.layout.template.data.Contour
                    instance or dict with compatible properties
                heatmapgl
                    plotly.graph_objs.layout.template.data.Heatmapg
                    l instance or dict with compatible properties
                heatmap
                    plotly.graph_objs.layout.template.data.Heatmap
                    instance or dict with compatible properties
                histogram2dcontour
                    plotly.graph_objs.layout.template.data.Histogra
                    m2dContour instance or dict with compatible
                    properties
                histogram2d
                    plotly.graph_objs.layout.template.data.Histogra
                    m2d instance or dict with compatible properties
                histogram
                    plotly.graph_objs.layout.template.data.Histogra
                    m instance or dict with compatible properties
                mesh3d
                    plotly.graph_objs.layout.template.data.Mesh3d
                    instance or dict with compatible properties
                ohlc
                    plotly.graph_objs.layout.template.data.Ohlc
                    instance or dict with compatible properties
                parcats
                    plotly.graph_objs.layout.template.data.Parcats
                    instance or dict with compatible properties
                parcoords
                    plotly.graph_objs.layout.template.data.Parcoord
                    s instance or dict with compatible properties
                pie
                    plotly.graph_objs.layout.template.data.Pie
                    instance or dict with compatible properties
                pointcloud
                    plotly.graph_objs.layout.template.data.Pointclo
                    ud instance or dict with compatible properties
                sankey
                    plotly.graph_objs.layout.template.data.Sankey
                    instance or dict with compatible properties
                scatter3d
                    plotly.graph_objs.layout.template.data.Scatter3
                    d instance or dict with compatible properties
                scattercarpet
                    plotly.graph_objs.layout.template.data.Scatterc
                    arpet instance or dict with compatible
                    properties
                scattergeo
                    plotly.graph_objs.layout.template.data.Scatterg
                    eo instance or dict with compatible properties
                scattergl
                    plotly.graph_objs.layout.template.data.Scatterg
                    l instance or dict with compatible properties
                scattermapbox
                    plotly.graph_objs.layout.template.data.Scatterm
                    apbox instance or dict with compatible
                    properties
                scatterpolargl
                    plotly.graph_objs.layout.template.data.Scatterp
                    olargl instance or dict with compatible
                    properties
                scatterpolar
                    plotly.graph_objs.layout.template.data.Scatterp
                    olar instance or dict with compatible
                    properties
                scatter
                    plotly.graph_objs.layout.template.data.Scatter
                    instance or dict with compatible properties
                scatterternary
                    plotly.graph_objs.layout.template.data.Scattert
                    ernary instance or dict with compatible
                    properties
                splom
                    plotly.graph_objs.layout.template.data.Splom
                    instance or dict with compatible properties
                streamtube
                    plotly.graph_objs.layout.template.data.Streamtu
                    be instance or dict with compatible properties
                surface
                    plotly.graph_objs.layout.template.data.Surface
                    instance or dict with compatible properties
                table
                    plotly.graph_objs.layout.template.data.Table
                    instance or dict with compatible properties
                violin
                    plotly.graph_objs.layout.template.data.Violin
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.layout.template.Data
        """
        return self['data']

    @data.setter
    def data(self, val):
        self['data'] = val

    # layout
    # ------
    @property
    def layout(self):
        """
        The 'layout' property is an instance of Layout
        that may be specified as:
          - An instance of plotly.graph_objs.layout.template.Layout
          - A dict of string/value properties that will be passed
            to the Layout constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.template.Layout
        """
        return self['layout']

    @layout.setter
    def layout(self, val):
        self['layout'] = val

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
        data
            plotly.graph_objs.layout.template.Data instance or dict
            with compatible properties
        layout
            plotly.graph_objs.layout.template.Layout instance or
            dict with compatible properties
        """

    def __init__(self, arg=None, data=None, layout=None, **kwargs):
        """
        Construct a new Template object
        
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

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Template
        data
            plotly.graph_objs.layout.template.Data instance or dict
            with compatible properties
        layout
            plotly.graph_objs.layout.template.Layout instance or
            dict with compatible properties

        Returns
        -------
        Template
        """
        super(Template, self).__init__('template')

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
The first argument to the plotly.graph_objs.layout.Template 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Template"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout import (template as v_template)

        # Initialize validators
        # ---------------------
        self._validators['data'] = v_template.DataValidator()
        self._validators['layout'] = v_template.LayoutValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('data', None)
        self['data'] = data if data is not None else _v
        _v = arg.pop('layout', None)
        self['layout'] = layout if layout is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
