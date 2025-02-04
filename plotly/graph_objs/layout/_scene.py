

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Scene(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout'
    _path_str = 'layout.scene'
    _valid_props = {"annotationdefaults", "annotations", "aspectmode", "aspectratio", "bgcolor", "camera", "domain", "dragmode", "hovermode", "uirevision", "xaxis", "yaxis", "zaxis"}

    # annotations
    # -----------
    @property
    def annotations(self):
        """
        The 'annotations' property is a tuple of instances of
        Annotation that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.scene.Annotation
          - A list or tuple of dicts of string/value properties that
            will be passed to the Annotation constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.scene.Annotation]
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
        layout.template.layout.scene.annotationdefaults), sets the
        default property values to use for elements of
        layout.scene.annotations

        The 'annotationdefaults' property is an instance of Annotation
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.Annotation`
          - A dict of string/value properties that will be passed
            to the Annotation constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.Annotation
        """
        return self['annotationdefaults']

    @annotationdefaults.setter
    def annotationdefaults(self, val):
        self['annotationdefaults'] = val

    # aspectmode
    # ----------
    @property
    def aspectmode(self):
        """
        If "cube", this scene's axes are drawn as a cube, regardless of
        the axes' ranges. If "data", this scene's axes are drawn in
        proportion with the axes' ranges. If "manual", this scene's
        axes are drawn in proportion with the input of "aspectratio"
        (the default behavior if "aspectratio" is provided). If "auto",
        this scene's axes are drawn using the results of "data" except
        when one axis is more than four times the size of the two
        others, where in that case the results of "cube" are used.

        The 'aspectmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'cube', 'data', 'manual']

        Returns
        -------
        Any
        """
        return self['aspectmode']

    @aspectmode.setter
    def aspectmode(self, val):
        self['aspectmode'] = val

    # aspectratio
    # -----------
    @property
    def aspectratio(self):
        """
        Sets this scene's axis aspectratio.

        The 'aspectratio' property is an instance of Aspectratio
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.Aspectratio`
          - A dict of string/value properties that will be passed
            to the Aspectratio constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.Aspectratio
        """
        return self['aspectratio']

    @aspectratio.setter
    def aspectratio(self, val):
        self['aspectratio'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # camera
    # ------
    @property
    def camera(self):
        """
        The 'camera' property is an instance of Camera
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.Camera`
          - A dict of string/value properties that will be passed
            to the Camera constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.Camera
        """
        return self['camera']

    @camera.setter
    def camera(self, val):
        self['camera'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # dragmode
    # --------
    @property
    def dragmode(self):
        """
        Determines the mode of drag interactions for this scene.

        The 'dragmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['orbit', 'turntable', 'zoom', 'pan', False]

        Returns
        -------
        Any
        """
        return self['dragmode']

    @dragmode.setter
    def dragmode(self, val):
        self['dragmode'] = val

    # hovermode
    # ---------
    @property
    def hovermode(self):
        """
        Determines the mode of hover interactions for this scene.

        The 'hovermode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['closest', False]

        Returns
        -------
        Any
        """
        return self['hovermode']

    @hovermode.setter
    def hovermode(self, val):
        self['hovermode'] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in camera
        attributes. Defaults to `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['uirevision']

    @uirevision.setter
    def uirevision(self, val):
        self['uirevision'] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        The 'xaxis' property is an instance of XAxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.XAxis`
          - A dict of string/value properties that will be passed
            to the XAxis constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.XAxis
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
          - An instance of :class:`plotly.graph_objs.layout.scene.YAxis`
          - A dict of string/value properties that will be passed
            to the YAxis constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.YAxis
        """
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # zaxis
    # -----
    @property
    def zaxis(self):
        """
        The 'zaxis' property is an instance of ZAxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.ZAxis`
          - A dict of string/value properties that will be passed
            to the ZAxis constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.ZAxis
        """
        return self['zaxis']

    @zaxis.setter
    def zaxis(self, val):
        self['zaxis'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        annotations
            A tuple of
            :class:`plotly.graph_objects.layout.scene.Annotation`
            instances or dicts with compatible properties
        annotationdefaults
            When used in a template (as
            layout.template.layout.scene.annotationdefaults), sets
            the default property values to use for elements of
            layout.scene.annotations
        aspectmode
            If "cube", this scene's axes are drawn as a cube,
            regardless of the axes' ranges. If "data", this scene's
            axes are drawn in proportion with the axes' ranges. If
            "manual", this scene's axes are drawn in proportion
            with the input of "aspectratio" (the default behavior
            if "aspectratio" is provided). If "auto", this scene's
            axes are drawn using the results of "data" except when
            one axis is more than four times the size of the two
            others, where in that case the results of "cube" are
            used.
        aspectratio
            Sets this scene's axis aspectratio.
        bgcolor

        camera
            :class:`plotly.graph_objects.layout.scene.Camera`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.scene.Domain`
            instance or dict with compatible properties
        dragmode
            Determines the mode of drag interactions for this
            scene.
        hovermode
            Determines the mode of hover interactions for this
            scene.
        uirevision
            Controls persistence of user-driven changes in camera
            attributes. Defaults to `layout.uirevision`.
        xaxis
            :class:`plotly.graph_objects.layout.scene.XAxis`
            instance or dict with compatible properties
        yaxis
            :class:`plotly.graph_objects.layout.scene.YAxis`
            instance or dict with compatible properties
        zaxis
            :class:`plotly.graph_objects.layout.scene.ZAxis`
            instance or dict with compatible properties
        """
    def __init__(self,
            arg=None,
            annotations=None,
            annotationdefaults=None,
            aspectmode=None,
            aspectratio=None,
            bgcolor=None,
            camera=None,
            domain=None,
            dragmode=None,
            hovermode=None,
            uirevision=None,
            xaxis=None,
            yaxis=None,
            zaxis=None,
            **kwargs
        ):
        """
        Construct a new Scene object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Scene`
        annotations
            A tuple of
            :class:`plotly.graph_objects.layout.scene.Annotation`
            instances or dicts with compatible properties
        annotationdefaults
            When used in a template (as
            layout.template.layout.scene.annotationdefaults), sets
            the default property values to use for elements of
            layout.scene.annotations
        aspectmode
            If "cube", this scene's axes are drawn as a cube,
            regardless of the axes' ranges. If "data", this scene's
            axes are drawn in proportion with the axes' ranges. If
            "manual", this scene's axes are drawn in proportion
            with the input of "aspectratio" (the default behavior
            if "aspectratio" is provided). If "auto", this scene's
            axes are drawn using the results of "data" except when
            one axis is more than four times the size of the two
            others, where in that case the results of "cube" are
            used.
        aspectratio
            Sets this scene's axis aspectratio.
        bgcolor

        camera
            :class:`plotly.graph_objects.layout.scene.Camera`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.scene.Domain`
            instance or dict with compatible properties
        dragmode
            Determines the mode of drag interactions for this
            scene.
        hovermode
            Determines the mode of hover interactions for this
            scene.
        uirevision
            Controls persistence of user-driven changes in camera
            attributes. Defaults to `layout.uirevision`.
        xaxis
            :class:`plotly.graph_objects.layout.scene.XAxis`
            instance or dict with compatible properties
        yaxis
            :class:`plotly.graph_objects.layout.scene.YAxis`
            instance or dict with compatible properties
        zaxis
            :class:`plotly.graph_objects.layout.scene.ZAxis`
            instance or dict with compatible properties

        Returns
        -------
        Scene
        """
        super().__init__('scene')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.layout.Scene
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Scene`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('annotations', arg, annotations)
        self._init_provided('annotationdefaults', arg, annotationdefaults)
        self._init_provided('aspectmode', arg, aspectmode)
        self._init_provided('aspectratio', arg, aspectratio)
        self._init_provided('bgcolor', arg, bgcolor)
        self._init_provided('camera', arg, camera)
        self._init_provided('domain', arg, domain)
        self._init_provided('dragmode', arg, dragmode)
        self._init_provided('hovermode', arg, hovermode)
        self._init_provided('uirevision', arg, uirevision)
        self._init_provided('xaxis', arg, xaxis)
        self._init_provided('yaxis', arg, yaxis)
        self._init_provided('zaxis', arg, zaxis)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
