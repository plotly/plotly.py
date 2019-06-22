from plotly.graph_objs import Layout

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Data(_BaseLayoutHierarchyType):

    # area
    # ----
    @property
    def area(self):
        """
        The 'area' property is a tuple of instances of
        Area that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Area
          - A list or tuple of dicts of string/value properties that
            will be passed to the Area constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Area]
        """
        return self["area"]

    @area.setter
    def area(self, val):
        self["area"] = val

    # barpolar
    # --------
    @property
    def barpolar(self):
        """
        The 'barpolar' property is a tuple of instances of
        Barpolar that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Barpolar
          - A list or tuple of dicts of string/value properties that
            will be passed to the Barpolar constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Barpolar]
        """
        return self["barpolar"]

    @barpolar.setter
    def barpolar(self, val):
        self["barpolar"] = val

    # bar
    # ---
    @property
    def bar(self):
        """
        The 'bar' property is a tuple of instances of
        Bar that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Bar
          - A list or tuple of dicts of string/value properties that
            will be passed to the Bar constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Bar]
        """
        return self["bar"]

    @bar.setter
    def bar(self, val):
        self["bar"] = val

    # box
    # ---
    @property
    def box(self):
        """
        The 'box' property is a tuple of instances of
        Box that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Box
          - A list or tuple of dicts of string/value properties that
            will be passed to the Box constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Box]
        """
        return self["box"]

    @box.setter
    def box(self, val):
        self["box"] = val

    # candlestick
    # -----------
    @property
    def candlestick(self):
        """
        The 'candlestick' property is a tuple of instances of
        Candlestick that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Candlestick
          - A list or tuple of dicts of string/value properties that
            will be passed to the Candlestick constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Candlestick]
        """
        return self["candlestick"]

    @candlestick.setter
    def candlestick(self, val):
        self["candlestick"] = val

    # carpet
    # ------
    @property
    def carpet(self):
        """
        The 'carpet' property is a tuple of instances of
        Carpet that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Carpet
          - A list or tuple of dicts of string/value properties that
            will be passed to the Carpet constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Carpet]
        """
        return self["carpet"]

    @carpet.setter
    def carpet(self, val):
        self["carpet"] = val

    # choropleth
    # ----------
    @property
    def choropleth(self):
        """
        The 'choropleth' property is a tuple of instances of
        Choropleth that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Choropleth
          - A list or tuple of dicts of string/value properties that
            will be passed to the Choropleth constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Choropleth]
        """
        return self["choropleth"]

    @choropleth.setter
    def choropleth(self, val):
        self["choropleth"] = val

    # cone
    # ----
    @property
    def cone(self):
        """
        The 'cone' property is a tuple of instances of
        Cone that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Cone
          - A list or tuple of dicts of string/value properties that
            will be passed to the Cone constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Cone]
        """
        return self["cone"]

    @cone.setter
    def cone(self, val):
        self["cone"] = val

    # contourcarpet
    # -------------
    @property
    def contourcarpet(self):
        """
        The 'contourcarpet' property is a tuple of instances of
        Contourcarpet that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Contourcarpet
          - A list or tuple of dicts of string/value properties that
            will be passed to the Contourcarpet constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Contourcarpet]
        """
        return self["contourcarpet"]

    @contourcarpet.setter
    def contourcarpet(self, val):
        self["contourcarpet"] = val

    # contour
    # -------
    @property
    def contour(self):
        """
        The 'contour' property is a tuple of instances of
        Contour that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Contour
          - A list or tuple of dicts of string/value properties that
            will be passed to the Contour constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Contour]
        """
        return self["contour"]

    @contour.setter
    def contour(self, val):
        self["contour"] = val

    # funnelarea
    # ----------
    @property
    def funnelarea(self):
        """
        The 'funnelarea' property is a tuple of instances of
        Funnelarea that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Funnelarea
          - A list or tuple of dicts of string/value properties that
            will be passed to the Funnelarea constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Funnelarea]
        """
        return self["funnelarea"]

    @funnelarea.setter
    def funnelarea(self, val):
        self["funnelarea"] = val

    # funnel
    # ------
    @property
    def funnel(self):
        """
        The 'funnel' property is a tuple of instances of
        Funnel that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Funnel
          - A list or tuple of dicts of string/value properties that
            will be passed to the Funnel constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Funnel]
        """
        return self["funnel"]

    @funnel.setter
    def funnel(self, val):
        self["funnel"] = val

    # heatmapgl
    # ---------
    @property
    def heatmapgl(self):
        """
        The 'heatmapgl' property is a tuple of instances of
        Heatmapgl that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Heatmapgl
          - A list or tuple of dicts of string/value properties that
            will be passed to the Heatmapgl constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Heatmapgl]
        """
        return self["heatmapgl"]

    @heatmapgl.setter
    def heatmapgl(self, val):
        self["heatmapgl"] = val

    # heatmap
    # -------
    @property
    def heatmap(self):
        """
        The 'heatmap' property is a tuple of instances of
        Heatmap that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Heatmap
          - A list or tuple of dicts of string/value properties that
            will be passed to the Heatmap constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Heatmap]
        """
        return self["heatmap"]

    @heatmap.setter
    def heatmap(self, val):
        self["heatmap"] = val

    # histogram2dcontour
    # ------------------
    @property
    def histogram2dcontour(self):
        """
        The 'histogram2dcontour' property is a tuple of instances of
        Histogram2dContour that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Histogram2dContour
          - A list or tuple of dicts of string/value properties that
            will be passed to the Histogram2dContour constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Histogram2dContour]
        """
        return self["histogram2dcontour"]

    @histogram2dcontour.setter
    def histogram2dcontour(self, val):
        self["histogram2dcontour"] = val

    # histogram2d
    # -----------
    @property
    def histogram2d(self):
        """
        The 'histogram2d' property is a tuple of instances of
        Histogram2d that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Histogram2d
          - A list or tuple of dicts of string/value properties that
            will be passed to the Histogram2d constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Histogram2d]
        """
        return self["histogram2d"]

    @histogram2d.setter
    def histogram2d(self, val):
        self["histogram2d"] = val

    # histogram
    # ---------
    @property
    def histogram(self):
        """
        The 'histogram' property is a tuple of instances of
        Histogram that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Histogram
          - A list or tuple of dicts of string/value properties that
            will be passed to the Histogram constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Histogram]
        """
        return self["histogram"]

    @histogram.setter
    def histogram(self, val):
        self["histogram"] = val

    # isosurface
    # ----------
    @property
    def isosurface(self):
        """
        The 'isosurface' property is a tuple of instances of
        Isosurface that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Isosurface
          - A list or tuple of dicts of string/value properties that
            will be passed to the Isosurface constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Isosurface]
        """
        return self["isosurface"]

    @isosurface.setter
    def isosurface(self, val):
        self["isosurface"] = val

    # mesh3d
    # ------
    @property
    def mesh3d(self):
        """
        The 'mesh3d' property is a tuple of instances of
        Mesh3d that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Mesh3d
          - A list or tuple of dicts of string/value properties that
            will be passed to the Mesh3d constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Mesh3d]
        """
        return self["mesh3d"]

    @mesh3d.setter
    def mesh3d(self, val):
        self["mesh3d"] = val

    # ohlc
    # ----
    @property
    def ohlc(self):
        """
        The 'ohlc' property is a tuple of instances of
        Ohlc that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Ohlc
          - A list or tuple of dicts of string/value properties that
            will be passed to the Ohlc constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Ohlc]
        """
        return self["ohlc"]

    @ohlc.setter
    def ohlc(self, val):
        self["ohlc"] = val

    # parcats
    # -------
    @property
    def parcats(self):
        """
        The 'parcats' property is a tuple of instances of
        Parcats that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Parcats
          - A list or tuple of dicts of string/value properties that
            will be passed to the Parcats constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Parcats]
        """
        return self["parcats"]

    @parcats.setter
    def parcats(self, val):
        self["parcats"] = val

    # parcoords
    # ---------
    @property
    def parcoords(self):
        """
        The 'parcoords' property is a tuple of instances of
        Parcoords that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Parcoords
          - A list or tuple of dicts of string/value properties that
            will be passed to the Parcoords constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Parcoords]
        """
        return self["parcoords"]

    @parcoords.setter
    def parcoords(self, val):
        self["parcoords"] = val

    # pie
    # ---
    @property
    def pie(self):
        """
        The 'pie' property is a tuple of instances of
        Pie that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Pie
          - A list or tuple of dicts of string/value properties that
            will be passed to the Pie constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Pie]
        """
        return self["pie"]

    @pie.setter
    def pie(self, val):
        self["pie"] = val

    # pointcloud
    # ----------
    @property
    def pointcloud(self):
        """
        The 'pointcloud' property is a tuple of instances of
        Pointcloud that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Pointcloud
          - A list or tuple of dicts of string/value properties that
            will be passed to the Pointcloud constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Pointcloud]
        """
        return self["pointcloud"]

    @pointcloud.setter
    def pointcloud(self, val):
        self["pointcloud"] = val

    # sankey
    # ------
    @property
    def sankey(self):
        """
        The 'sankey' property is a tuple of instances of
        Sankey that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Sankey
          - A list or tuple of dicts of string/value properties that
            will be passed to the Sankey constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Sankey]
        """
        return self["sankey"]

    @sankey.setter
    def sankey(self, val):
        self["sankey"] = val

    # scatter3d
    # ---------
    @property
    def scatter3d(self):
        """
        The 'scatter3d' property is a tuple of instances of
        Scatter3d that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatter3d
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatter3d constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatter3d]
        """
        return self["scatter3d"]

    @scatter3d.setter
    def scatter3d(self, val):
        self["scatter3d"] = val

    # scattercarpet
    # -------------
    @property
    def scattercarpet(self):
        """
        The 'scattercarpet' property is a tuple of instances of
        Scattercarpet that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattercarpet
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattercarpet constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattercarpet]
        """
        return self["scattercarpet"]

    @scattercarpet.setter
    def scattercarpet(self, val):
        self["scattercarpet"] = val

    # scattergeo
    # ----------
    @property
    def scattergeo(self):
        """
        The 'scattergeo' property is a tuple of instances of
        Scattergeo that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattergeo
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattergeo constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattergeo]
        """
        return self["scattergeo"]

    @scattergeo.setter
    def scattergeo(self, val):
        self["scattergeo"] = val

    # scattergl
    # ---------
    @property
    def scattergl(self):
        """
        The 'scattergl' property is a tuple of instances of
        Scattergl that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattergl
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattergl constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattergl]
        """
        return self["scattergl"]

    @scattergl.setter
    def scattergl(self, val):
        self["scattergl"] = val

    # scattermapbox
    # -------------
    @property
    def scattermapbox(self):
        """
        The 'scattermapbox' property is a tuple of instances of
        Scattermapbox that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattermapbox
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattermapbox constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattermapbox]
        """
        return self["scattermapbox"]

    @scattermapbox.setter
    def scattermapbox(self, val):
        self["scattermapbox"] = val

    # scatterpolargl
    # --------------
    @property
    def scatterpolargl(self):
        """
        The 'scatterpolargl' property is a tuple of instances of
        Scatterpolargl that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatterpolargl
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatterpolargl constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatterpolargl]
        """
        return self["scatterpolargl"]

    @scatterpolargl.setter
    def scatterpolargl(self, val):
        self["scatterpolargl"] = val

    # scatterpolar
    # ------------
    @property
    def scatterpolar(self):
        """
        The 'scatterpolar' property is a tuple of instances of
        Scatterpolar that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatterpolar
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatterpolar constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatterpolar]
        """
        return self["scatterpolar"]

    @scatterpolar.setter
    def scatterpolar(self, val):
        self["scatterpolar"] = val

    # scatter
    # -------
    @property
    def scatter(self):
        """
        The 'scatter' property is a tuple of instances of
        Scatter that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatter
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatter constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatter]
        """
        return self["scatter"]

    @scatter.setter
    def scatter(self, val):
        self["scatter"] = val

    # scatterternary
    # --------------
    @property
    def scatterternary(self):
        """
        The 'scatterternary' property is a tuple of instances of
        Scatterternary that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatterternary
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatterternary constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatterternary]
        """
        return self["scatterternary"]

    @scatterternary.setter
    def scatterternary(self, val):
        self["scatterternary"] = val

    # splom
    # -----
    @property
    def splom(self):
        """
        The 'splom' property is a tuple of instances of
        Splom that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Splom
          - A list or tuple of dicts of string/value properties that
            will be passed to the Splom constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Splom]
        """
        return self["splom"]

    @splom.setter
    def splom(self, val):
        self["splom"] = val

    # streamtube
    # ----------
    @property
    def streamtube(self):
        """
        The 'streamtube' property is a tuple of instances of
        Streamtube that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Streamtube
          - A list or tuple of dicts of string/value properties that
            will be passed to the Streamtube constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Streamtube]
        """
        return self["streamtube"]

    @streamtube.setter
    def streamtube(self, val):
        self["streamtube"] = val

    # sunburst
    # --------
    @property
    def sunburst(self):
        """
        The 'sunburst' property is a tuple of instances of
        Sunburst that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Sunburst
          - A list or tuple of dicts of string/value properties that
            will be passed to the Sunburst constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Sunburst]
        """
        return self["sunburst"]

    @sunburst.setter
    def sunburst(self, val):
        self["sunburst"] = val

    # surface
    # -------
    @property
    def surface(self):
        """
        The 'surface' property is a tuple of instances of
        Surface that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Surface
          - A list or tuple of dicts of string/value properties that
            will be passed to the Surface constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Surface]
        """
        return self["surface"]

    @surface.setter
    def surface(self, val):
        self["surface"] = val

    # table
    # -----
    @property
    def table(self):
        """
        The 'table' property is a tuple of instances of
        Table that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Table
          - A list or tuple of dicts of string/value properties that
            will be passed to the Table constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Table]
        """
        return self["table"]

    @table.setter
    def table(self, val):
        self["table"] = val

    # violin
    # ------
    @property
    def violin(self):
        """
        The 'violin' property is a tuple of instances of
        Violin that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Violin
          - A list or tuple of dicts of string/value properties that
            will be passed to the Violin constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Violin]
        """
        return self["violin"]

    @violin.setter
    def violin(self, val):
        self["violin"] = val

    # volume
    # ------
    @property
    def volume(self):
        """
        The 'volume' property is a tuple of instances of
        Volume that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Volume
          - A list or tuple of dicts of string/value properties that
            will be passed to the Volume constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Volume]
        """
        return self["volume"]

    @volume.setter
    def volume(self, val):
        self["volume"] = val

    # waterfall
    # ---------
    @property
    def waterfall(self):
        """
        The 'waterfall' property is a tuple of instances of
        Waterfall that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Waterfall
          - A list or tuple of dicts of string/value properties that
            will be passed to the Waterfall constructor
    
            Supported dict properties:

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Waterfall]
        """
        return self["waterfall"]

    @waterfall.setter
    def waterfall(self, val):
        self["waterfall"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.template"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        area
            A tuple of plotly.graph_objects.Area instances or dicts
            with compatible properties
        barpolar
            A tuple of plotly.graph_objects.Barpolar instances or
            dicts with compatible properties
        bar
            A tuple of plotly.graph_objects.Bar instances or dicts
            with compatible properties
        box
            A tuple of plotly.graph_objects.Box instances or dicts
            with compatible properties
        candlestick
            A tuple of plotly.graph_objects.Candlestick instances
            or dicts with compatible properties
        carpet
            A tuple of plotly.graph_objects.Carpet instances or
            dicts with compatible properties
        choropleth
            A tuple of plotly.graph_objects.Choropleth instances or
            dicts with compatible properties
        cone
            A tuple of plotly.graph_objects.Cone instances or dicts
            with compatible properties
        contourcarpet
            A tuple of plotly.graph_objects.Contourcarpet instances
            or dicts with compatible properties
        contour
            A tuple of plotly.graph_objects.Contour instances or
            dicts with compatible properties
        funnelarea
            A tuple of plotly.graph_objects.Funnelarea instances or
            dicts with compatible properties
        funnel
            A tuple of plotly.graph_objects.Funnel instances or
            dicts with compatible properties
        heatmapgl
            A tuple of plotly.graph_objects.Heatmapgl instances or
            dicts with compatible properties
        heatmap
            A tuple of plotly.graph_objects.Heatmap instances or
            dicts with compatible properties
        histogram2dcontour
            A tuple of plotly.graph_objects.Histogram2dContour
            instances or dicts with compatible properties
        histogram2d
            A tuple of plotly.graph_objects.Histogram2d instances
            or dicts with compatible properties
        histogram
            A tuple of plotly.graph_objects.Histogram instances or
            dicts with compatible properties
        isosurface
            A tuple of plotly.graph_objects.Isosurface instances or
            dicts with compatible properties
        mesh3d
            A tuple of plotly.graph_objects.Mesh3d instances or
            dicts with compatible properties
        ohlc
            A tuple of plotly.graph_objects.Ohlc instances or dicts
            with compatible properties
        parcats
            A tuple of plotly.graph_objects.Parcats instances or
            dicts with compatible properties
        parcoords
            A tuple of plotly.graph_objects.Parcoords instances or
            dicts with compatible properties
        pie
            A tuple of plotly.graph_objects.Pie instances or dicts
            with compatible properties
        pointcloud
            A tuple of plotly.graph_objects.Pointcloud instances or
            dicts with compatible properties
        sankey
            A tuple of plotly.graph_objects.Sankey instances or
            dicts with compatible properties
        scatter3d
            A tuple of plotly.graph_objects.Scatter3d instances or
            dicts with compatible properties
        scattercarpet
            A tuple of plotly.graph_objects.Scattercarpet instances
            or dicts with compatible properties
        scattergeo
            A tuple of plotly.graph_objects.Scattergeo instances or
            dicts with compatible properties
        scattergl
            A tuple of plotly.graph_objects.Scattergl instances or
            dicts with compatible properties
        scattermapbox
            A tuple of plotly.graph_objects.Scattermapbox instances
            or dicts with compatible properties
        scatterpolargl
            A tuple of plotly.graph_objects.Scatterpolargl
            instances or dicts with compatible properties
        scatterpolar
            A tuple of plotly.graph_objects.Scatterpolar instances
            or dicts with compatible properties
        scatter
            A tuple of plotly.graph_objects.Scatter instances or
            dicts with compatible properties
        scatterternary
            A tuple of plotly.graph_objects.Scatterternary
            instances or dicts with compatible properties
        splom
            A tuple of plotly.graph_objects.Splom instances or
            dicts with compatible properties
        streamtube
            A tuple of plotly.graph_objects.Streamtube instances or
            dicts with compatible properties
        sunburst
            A tuple of plotly.graph_objects.Sunburst instances or
            dicts with compatible properties
        surface
            A tuple of plotly.graph_objects.Surface instances or
            dicts with compatible properties
        table
            A tuple of plotly.graph_objects.Table instances or
            dicts with compatible properties
        violin
            A tuple of plotly.graph_objects.Violin instances or
            dicts with compatible properties
        volume
            A tuple of plotly.graph_objects.Volume instances or
            dicts with compatible properties
        waterfall
            A tuple of plotly.graph_objects.Waterfall instances or
            dicts with compatible properties
        """

    def __init__(
        self,
        arg=None,
        area=None,
        barpolar=None,
        bar=None,
        box=None,
        candlestick=None,
        carpet=None,
        choropleth=None,
        cone=None,
        contourcarpet=None,
        contour=None,
        funnelarea=None,
        funnel=None,
        heatmapgl=None,
        heatmap=None,
        histogram2dcontour=None,
        histogram2d=None,
        histogram=None,
        isosurface=None,
        mesh3d=None,
        ohlc=None,
        parcats=None,
        parcoords=None,
        pie=None,
        pointcloud=None,
        sankey=None,
        scatter3d=None,
        scattercarpet=None,
        scattergeo=None,
        scattergl=None,
        scattermapbox=None,
        scatterpolargl=None,
        scatterpolar=None,
        scatter=None,
        scatterternary=None,
        splom=None,
        streamtube=None,
        sunburst=None,
        surface=None,
        table=None,
        violin=None,
        volume=None,
        waterfall=None,
        **kwargs
    ):
        """
        Construct a new Data object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.template.Data
        area
            A tuple of plotly.graph_objects.Area instances or dicts
            with compatible properties
        barpolar
            A tuple of plotly.graph_objects.Barpolar instances or
            dicts with compatible properties
        bar
            A tuple of plotly.graph_objects.Bar instances or dicts
            with compatible properties
        box
            A tuple of plotly.graph_objects.Box instances or dicts
            with compatible properties
        candlestick
            A tuple of plotly.graph_objects.Candlestick instances
            or dicts with compatible properties
        carpet
            A tuple of plotly.graph_objects.Carpet instances or
            dicts with compatible properties
        choropleth
            A tuple of plotly.graph_objects.Choropleth instances or
            dicts with compatible properties
        cone
            A tuple of plotly.graph_objects.Cone instances or dicts
            with compatible properties
        contourcarpet
            A tuple of plotly.graph_objects.Contourcarpet instances
            or dicts with compatible properties
        contour
            A tuple of plotly.graph_objects.Contour instances or
            dicts with compatible properties
        funnelarea
            A tuple of plotly.graph_objects.Funnelarea instances or
            dicts with compatible properties
        funnel
            A tuple of plotly.graph_objects.Funnel instances or
            dicts with compatible properties
        heatmapgl
            A tuple of plotly.graph_objects.Heatmapgl instances or
            dicts with compatible properties
        heatmap
            A tuple of plotly.graph_objects.Heatmap instances or
            dicts with compatible properties
        histogram2dcontour
            A tuple of plotly.graph_objects.Histogram2dContour
            instances or dicts with compatible properties
        histogram2d
            A tuple of plotly.graph_objects.Histogram2d instances
            or dicts with compatible properties
        histogram
            A tuple of plotly.graph_objects.Histogram instances or
            dicts with compatible properties
        isosurface
            A tuple of plotly.graph_objects.Isosurface instances or
            dicts with compatible properties
        mesh3d
            A tuple of plotly.graph_objects.Mesh3d instances or
            dicts with compatible properties
        ohlc
            A tuple of plotly.graph_objects.Ohlc instances or dicts
            with compatible properties
        parcats
            A tuple of plotly.graph_objects.Parcats instances or
            dicts with compatible properties
        parcoords
            A tuple of plotly.graph_objects.Parcoords instances or
            dicts with compatible properties
        pie
            A tuple of plotly.graph_objects.Pie instances or dicts
            with compatible properties
        pointcloud
            A tuple of plotly.graph_objects.Pointcloud instances or
            dicts with compatible properties
        sankey
            A tuple of plotly.graph_objects.Sankey instances or
            dicts with compatible properties
        scatter3d
            A tuple of plotly.graph_objects.Scatter3d instances or
            dicts with compatible properties
        scattercarpet
            A tuple of plotly.graph_objects.Scattercarpet instances
            or dicts with compatible properties
        scattergeo
            A tuple of plotly.graph_objects.Scattergeo instances or
            dicts with compatible properties
        scattergl
            A tuple of plotly.graph_objects.Scattergl instances or
            dicts with compatible properties
        scattermapbox
            A tuple of plotly.graph_objects.Scattermapbox instances
            or dicts with compatible properties
        scatterpolargl
            A tuple of plotly.graph_objects.Scatterpolargl
            instances or dicts with compatible properties
        scatterpolar
            A tuple of plotly.graph_objects.Scatterpolar instances
            or dicts with compatible properties
        scatter
            A tuple of plotly.graph_objects.Scatter instances or
            dicts with compatible properties
        scatterternary
            A tuple of plotly.graph_objects.Scatterternary
            instances or dicts with compatible properties
        splom
            A tuple of plotly.graph_objects.Splom instances or
            dicts with compatible properties
        streamtube
            A tuple of plotly.graph_objects.Streamtube instances or
            dicts with compatible properties
        sunburst
            A tuple of plotly.graph_objects.Sunburst instances or
            dicts with compatible properties
        surface
            A tuple of plotly.graph_objects.Surface instances or
            dicts with compatible properties
        table
            A tuple of plotly.graph_objects.Table instances or
            dicts with compatible properties
        violin
            A tuple of plotly.graph_objects.Violin instances or
            dicts with compatible properties
        volume
            A tuple of plotly.graph_objects.Volume instances or
            dicts with compatible properties
        waterfall
            A tuple of plotly.graph_objects.Waterfall instances or
            dicts with compatible properties

        Returns
        -------
        Data
        """
        super(Data, self).__init__("data")

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
The first argument to the plotly.graph_objs.layout.template.Data 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.template.Data"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.template import data as v_data

        # Initialize validators
        # ---------------------
        self._validators["area"] = v_data.AreasValidator()
        self._validators["barpolar"] = v_data.BarpolarsValidator()
        self._validators["bar"] = v_data.BarsValidator()
        self._validators["box"] = v_data.BoxsValidator()
        self._validators["candlestick"] = v_data.CandlesticksValidator()
        self._validators["carpet"] = v_data.CarpetsValidator()
        self._validators["choropleth"] = v_data.ChoroplethsValidator()
        self._validators["cone"] = v_data.ConesValidator()
        self._validators["contourcarpet"] = v_data.ContourcarpetsValidator()
        self._validators["contour"] = v_data.ContoursValidator()
        self._validators["funnelarea"] = v_data.FunnelareasValidator()
        self._validators["funnel"] = v_data.FunnelsValidator()
        self._validators["heatmapgl"] = v_data.HeatmapglsValidator()
        self._validators["heatmap"] = v_data.HeatmapsValidator()
        self._validators["histogram2dcontour"] = v_data.Histogram2dContoursValidator()
        self._validators["histogram2d"] = v_data.Histogram2dsValidator()
        self._validators["histogram"] = v_data.HistogramsValidator()
        self._validators["isosurface"] = v_data.IsosurfacesValidator()
        self._validators["mesh3d"] = v_data.Mesh3dsValidator()
        self._validators["ohlc"] = v_data.OhlcsValidator()
        self._validators["parcats"] = v_data.ParcatssValidator()
        self._validators["parcoords"] = v_data.ParcoordssValidator()
        self._validators["pie"] = v_data.PiesValidator()
        self._validators["pointcloud"] = v_data.PointcloudsValidator()
        self._validators["sankey"] = v_data.SankeysValidator()
        self._validators["scatter3d"] = v_data.Scatter3dsValidator()
        self._validators["scattercarpet"] = v_data.ScattercarpetsValidator()
        self._validators["scattergeo"] = v_data.ScattergeosValidator()
        self._validators["scattergl"] = v_data.ScatterglsValidator()
        self._validators["scattermapbox"] = v_data.ScattermapboxsValidator()
        self._validators["scatterpolargl"] = v_data.ScatterpolarglsValidator()
        self._validators["scatterpolar"] = v_data.ScatterpolarsValidator()
        self._validators["scatter"] = v_data.ScattersValidator()
        self._validators["scatterternary"] = v_data.ScatterternarysValidator()
        self._validators["splom"] = v_data.SplomsValidator()
        self._validators["streamtube"] = v_data.StreamtubesValidator()
        self._validators["sunburst"] = v_data.SunburstsValidator()
        self._validators["surface"] = v_data.SurfacesValidator()
        self._validators["table"] = v_data.TablesValidator()
        self._validators["violin"] = v_data.ViolinsValidator()
        self._validators["volume"] = v_data.VolumesValidator()
        self._validators["waterfall"] = v_data.WaterfallsValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("area", None)
        self["area"] = area if area is not None else _v
        _v = arg.pop("barpolar", None)
        self["barpolar"] = barpolar if barpolar is not None else _v
        _v = arg.pop("bar", None)
        self["bar"] = bar if bar is not None else _v
        _v = arg.pop("box", None)
        self["box"] = box if box is not None else _v
        _v = arg.pop("candlestick", None)
        self["candlestick"] = candlestick if candlestick is not None else _v
        _v = arg.pop("carpet", None)
        self["carpet"] = carpet if carpet is not None else _v
        _v = arg.pop("choropleth", None)
        self["choropleth"] = choropleth if choropleth is not None else _v
        _v = arg.pop("cone", None)
        self["cone"] = cone if cone is not None else _v
        _v = arg.pop("contourcarpet", None)
        self["contourcarpet"] = contourcarpet if contourcarpet is not None else _v
        _v = arg.pop("contour", None)
        self["contour"] = contour if contour is not None else _v
        _v = arg.pop("funnelarea", None)
        self["funnelarea"] = funnelarea if funnelarea is not None else _v
        _v = arg.pop("funnel", None)
        self["funnel"] = funnel if funnel is not None else _v
        _v = arg.pop("heatmapgl", None)
        self["heatmapgl"] = heatmapgl if heatmapgl is not None else _v
        _v = arg.pop("heatmap", None)
        self["heatmap"] = heatmap if heatmap is not None else _v
        _v = arg.pop("histogram2dcontour", None)
        self["histogram2dcontour"] = (
            histogram2dcontour if histogram2dcontour is not None else _v
        )
        _v = arg.pop("histogram2d", None)
        self["histogram2d"] = histogram2d if histogram2d is not None else _v
        _v = arg.pop("histogram", None)
        self["histogram"] = histogram if histogram is not None else _v
        _v = arg.pop("isosurface", None)
        self["isosurface"] = isosurface if isosurface is not None else _v
        _v = arg.pop("mesh3d", None)
        self["mesh3d"] = mesh3d if mesh3d is not None else _v
        _v = arg.pop("ohlc", None)
        self["ohlc"] = ohlc if ohlc is not None else _v
        _v = arg.pop("parcats", None)
        self["parcats"] = parcats if parcats is not None else _v
        _v = arg.pop("parcoords", None)
        self["parcoords"] = parcoords if parcoords is not None else _v
        _v = arg.pop("pie", None)
        self["pie"] = pie if pie is not None else _v
        _v = arg.pop("pointcloud", None)
        self["pointcloud"] = pointcloud if pointcloud is not None else _v
        _v = arg.pop("sankey", None)
        self["sankey"] = sankey if sankey is not None else _v
        _v = arg.pop("scatter3d", None)
        self["scatter3d"] = scatter3d if scatter3d is not None else _v
        _v = arg.pop("scattercarpet", None)
        self["scattercarpet"] = scattercarpet if scattercarpet is not None else _v
        _v = arg.pop("scattergeo", None)
        self["scattergeo"] = scattergeo if scattergeo is not None else _v
        _v = arg.pop("scattergl", None)
        self["scattergl"] = scattergl if scattergl is not None else _v
        _v = arg.pop("scattermapbox", None)
        self["scattermapbox"] = scattermapbox if scattermapbox is not None else _v
        _v = arg.pop("scatterpolargl", None)
        self["scatterpolargl"] = scatterpolargl if scatterpolargl is not None else _v
        _v = arg.pop("scatterpolar", None)
        self["scatterpolar"] = scatterpolar if scatterpolar is not None else _v
        _v = arg.pop("scatter", None)
        self["scatter"] = scatter if scatter is not None else _v
        _v = arg.pop("scatterternary", None)
        self["scatterternary"] = scatterternary if scatterternary is not None else _v
        _v = arg.pop("splom", None)
        self["splom"] = splom if splom is not None else _v
        _v = arg.pop("streamtube", None)
        self["streamtube"] = streamtube if streamtube is not None else _v
        _v = arg.pop("sunburst", None)
        self["sunburst"] = sunburst if sunburst is not None else _v
        _v = arg.pop("surface", None)
        self["surface"] = surface if surface is not None else _v
        _v = arg.pop("table", None)
        self["table"] = table if table is not None else _v
        _v = arg.pop("violin", None)
        self["violin"] = violin if violin is not None else _v
        _v = arg.pop("volume", None)
        self["volume"] = volume if volume is not None else _v
        _v = arg.pop("waterfall", None)
        self["waterfall"] = waterfall if waterfall is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.graph_objs.layout.template import data
