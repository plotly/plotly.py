from plotly.basedatatypes import BaseFrameHierarchyType
import copy


class Frame(BaseFrameHierarchyType):

    # baseframe
    # ---------
    @property
    def baseframe(self):
        """
        The name of the frame into which this frame's properties are
        merged before applying. This is used to unify properties and
        avoid needing to specify the same values for the same
        properties in multiple frames.
    
        The 'baseframe' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['baseframe']

    @baseframe.setter
    def baseframe(self, val):
        self['baseframe'] = val

    # data
    # ----
    @property
    def data(self):
        """
        A list of traces this frame modifies. The format is identical
        to the normal trace definition.

        Returns
        -------
        Any
        """
        return self['data']

    @data.setter
    def data(self, val):
        self['data'] = val

    # group
    # -----
    @property
    def group(self):
        """
        An identifier that specifies the group to which the frame
        belongs, used by animate to select a subset of frames.
    
        The 'group' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['group']

    @group.setter
    def group(self, val):
        self['group'] = val

    # layout
    # ------
    @property
    def layout(self):
        """
        Layout properties which this frame modifies. The format is
        identical to the normal layout definition.

        Returns
        -------
        Any
        """
        return self['layout']

    @layout.setter
    def layout(self, val):
        self['layout'] = val

    # name
    # ----
    @property
    def name(self):
        """
        A label by which to identify the frame
    
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

    # traces
    # ------
    @property
    def traces(self):
        """
        A list of trace indices that identify the respective traces in
        the data attribute
    
        The 'traces' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['traces']

    @traces.setter
    def traces(self, val):
        self['traces'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return ''

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        baseframe
            The name of the frame into which this frame's
            properties are merged before applying. This is used to
            unify properties and avoid needing to specify the same
            values for the same properties in multiple frames.
        data
            A list of traces this frame modifies. The format is
            identical to the normal trace definition.
        group
            An identifier that specifies the group to which the
            frame belongs, used by animate to select a subset of
            frames.
        layout
            Layout properties which this frame modifies. The format
            is identical to the normal layout definition.
        name
            A label by which to identify the frame
        traces
            A list of trace indices that identify the respective
            traces in the data attribute
        """

    def __init__(
        self,
        arg=None,
        baseframe=None,
        data=None,
        group=None,
        layout=None,
        name=None,
        traces=None,
        **kwargs
    ):
        """
        Construct a new Frame object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Frame
        baseframe
            The name of the frame into which this frame's
            properties are merged before applying. This is used to
            unify properties and avoid needing to specify the same
            values for the same properties in multiple frames.
        data
            A list of traces this frame modifies. The format is
            identical to the normal trace definition.
        group
            An identifier that specifies the group to which the
            frame belongs, used by animate to select a subset of
            frames.
        layout
            Layout properties which this frame modifies. The format
            is identical to the normal layout definition.
        name
            A label by which to identify the frame
        traces
            A list of trace indices that identify the respective
            traces in the data attribute

        Returns
        -------
        Frame
        """
        super(Frame, self).__init__('frames')

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
The first argument to the plotly.graph_objs.Frame 
constructor must be a dict or 
an instance of plotly.graph_objs.Frame"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (frame as v_frame)

        # Initialize validators
        # ---------------------
        self._validators['baseframe'] = v_frame.BaseframeValidator()
        self._validators['data'] = v_frame.DataValidator()
        self._validators['group'] = v_frame.GroupValidator()
        self._validators['layout'] = v_frame.LayoutValidator()
        self._validators['name'] = v_frame.NameValidator()
        self._validators['traces'] = v_frame.TracesValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('baseframe', None)
        self.baseframe = baseframe if baseframe is not None else _v
        _v = arg.pop('data', None)
        self.data = data if data is not None else _v
        _v = arg.pop('group', None)
        self.group = group if group is not None else _v
        _v = arg.pop('layout', None)
        self.layout = layout if layout is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('traces', None)
        self.traces = traces if traces is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
