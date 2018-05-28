from plotly.basedatatypes import BaseFrameHierarchyType


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
        self.baseframe = baseframe
        self.data = data
        self.group = group
        self.layout = layout
        self.name = name
        self.traces = traces

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
