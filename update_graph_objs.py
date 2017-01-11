from __future__ import print_function

from plotly.graph_objs import graph_objs_tools
from plotly.graph_reference import ARRAYS, CLASSES

FLAG = '# AUTO-GENERATED BELOW. DO NOT EDIT! See makefile.'


def get_non_generated_file_lines():
    """
    Copy each line up to our special FLAG line and return.

    :raises: (ValueError) If the FLAG isn't found.
    :return: (list) The lines we're copying.
    """

    lines_to_copy = []
    flag_found = False
    with open('./plotly/graph_objs/graph_objs.py', 'r') as f:
        for line_to_copy in f:
            if line_to_copy.startswith(FLAG):
                flag_found = True
                break
            lines_to_copy.append(line_to_copy)
    if not flag_found:
        raise ValueError(
            'Failed to find flag:\n"{}"\nin graph_objs_tools.py.'.format(FLAG)
        )
    return lines_to_copy


def print_figure_patch(f):
    """Print a patch to our Figure object into the given open file."""

    print(
        '''
    def __init__(self, *args, **kwargs):
        super(Figure, self).__init__(*args, **kwargs)
        if 'data' not in self:
            self.data = Data(_parent=self, _parent_key='data')

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        Flattening may increase the utility of the result.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        return self.data.get_data(flatten=flatten)

    def to_dataframe(self):
        """
        Create a dataframe with trace names and keys as column names.

        :return: (DataFrame)

        """
        data = self.get_data(flatten=True)
        from pandas import DataFrame, Series
        return DataFrame(
            dict([(k, Series(v)) for k, v in data.items()]))

    def print_grid(self):
        """
        Print a visual layout of the figure's axes arrangement.

        This is only valid for figures that are created
        with plotly.tools.make_subplots.

        """
        try:
            grid_str = self.__dict__['_grid_str']
        except AttributeError:
            raise Exception("Use plotly.tools.make_subplots "
                            "to create a subplot grid.")
        print(grid_str)

    def append_trace(self, trace, row, col):
        """
        Add a trace to your figure bound to axes at the row, col index.

        The row, col index is generated from figures created with
        plotly.tools.make_subplots and can be viewed with
        Figure.print_grid.

        :param (dict) trace: The data trace to be bound.
        :param (int) row: Subplot row index (see Figure.print_grid).
        :param (int) col: Subplot column index (see Figure.print_grid).

        Example:
        # stack two subplots vertically
        fig = tools.make_subplots(rows=2)

        This is the format of your plot grid:
        [ (1,1) x1,y1 ]
        [ (2,1) x2,y2 ]

        fig.append_trace(Scatter(x=[1,2,3], y=[2,1,2]), 1, 1)
        fig.append_trace(Scatter(x=[1,2,3], y=[2,1,2]), 2, 1)

        """
        try:
            grid_ref = self._grid_ref
        except AttributeError:
            raise Exception("In order to use Figure.append_trace, "
                            "you must first use "
                            "plotly.tools.make_subplots "
                            "to create a subplot grid.")
        if row <= 0:
            raise Exception("Row value is out of range. "
                            "Note: the starting cell is (1, 1)")
        if col <= 0:
            raise Exception("Col value is out of range. "
                            "Note: the starting cell is (1, 1)")
        try:
            ref = grid_ref[row-1][col-1]
        except IndexError:
            raise Exception("The (row, col) pair sent is out of "
                            "range. Use Figure.print_grid to view the "
                            "subplot grid. ")
        if 'scene' in ref[0]:
            trace['scene'] = ref[0]
            if ref[0] not in self['layout']:
                raise Exception("Something went wrong. "
                                "The scene object for ({r},{c}) "
                                "subplot cell "
                                "got deleted.".format(r=row, c=col))
        else:
            xaxis_key = "xaxis{ref}".format(ref=ref[0][1:])
            yaxis_key = "yaxis{ref}".format(ref=ref[1][1:])
            if (xaxis_key not in self['layout']
                    or yaxis_key not in self['layout']):
                raise Exception("Something went wrong. "
                                "An axis object for ({r},{c}) subplot "
                                "cell got deleted."
                                .format(r=row, c=col))
            trace['xaxis'] = ref[0]
            trace['yaxis'] = ref[1]
        self['data'] += [trace]
''', file=f, end=''
    )


def print_data_patch(f):
    """Print a patch to our Data object into the given open file."""
    print(
        '''
    def _value_to_graph_object(self, index, value, _raise=True):

        if not isinstance(value, dict):
            if _raise:
                notes = ['Entry should subclass dict.']
                path = self._get_path() + (index, )
                raise exceptions.PlotlyListEntryError(self, path,
                                                      notes=notes)
            else:
                return

        item = value.get('type', 'scatter')
        if item not in graph_reference.ARRAYS['data']['items']:
            if _raise:
                path = self._get_path() + (0, )
                raise exceptions.PlotlyDataTypeError(self, path)

        return GraphObjectFactory.create(item, _raise=_raise,
                                         _parent=self,
                                         _parent_key=index, **value)

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        if flatten:
            data = [v.get_data(flatten=flatten) for v in self]
            d = {}
            taken_names = []
            for i, trace in enumerate(data):

                # we want to give the traces helpful names
                # however, we need to be sure they're unique too...
                trace_name = trace.pop('name', 'trace_{0}'.format(i))
                if trace_name in taken_names:
                    j = 1
                    new_trace_name = "{0}_{1}".format(trace_name, j)
                    while new_trace_name in taken_names:
                        new_trace_name = (
                            "{0}_{1}".format(trace_name, j)
                        )
                        j += 1
                    trace_name = new_trace_name
                taken_names.append(trace_name)

                # finish up the dot-concatenation
                for k, v in trace.items():
                    key = "{0}.{1}".format(trace_name, k)
                    d[key] = v
            return d
        else:
            return super(Data, self).get_data(flatten=flatten)
''', file=f, end=''
    )


def print_frames_patch(f):
    """Print a patch to our Frames object into the given open file."""
    print(
        '''
    def _value_to_graph_object(self, index, value, _raise=True):
        if isinstance(value, six.string_types):
            return value
        return super(Frames, self)._value_to_graph_object(index, value,
                                                          _raise=_raise)

    def to_string(self, level=0, indent=4, eol='\\n',
                  pretty=True, max_chars=80):
        """Get formatted string by calling `to_string` on children items."""
        if not len(self):
            return "{name}()".format(name=self._get_class_name())
        string = "{name}([{eol}{indent}".format(
            name=self._get_class_name(),
            eol=eol,
            indent=' ' * indent * (level + 1))
        for index, entry in enumerate(self):
            if isinstance(entry, six.string_types):
                string += repr(entry)
            else:
                string += entry.to_string(level=level+1,
                                          indent=indent,
                                          eol=eol,
                                          pretty=pretty,
                                          max_chars=max_chars)
            if index < len(self) - 1:
                string += ",{eol}{indent}".format(
                    eol=eol,
                    indent=' ' * indent * (level + 1))
        string += (
            "{eol}{indent}])").format(eol=eol, indent=' ' * indent * level)
        return string
''', file=f, end=''
    )


def print_class(name, f):
    class_dict = CLASSES[name]
    print('\n', file=f)
    object_name = class_dict['object_name']
    base_type = class_dict['base_type']

    # This is for backwards compat (e.g., Trace) and future changes.
    if object_name is None:
        print('class {}({}):'.format(name, base_type.__name__),
              file=f)
        print('    pass', file=f)
        return

    doc = graph_objs_tools.get_help(object_name)
    if object_name in ARRAYS:
        base_name = 'PlotlyList'
    else:
        base_name = 'PlotlyDict'
    print('class {}({}):'.format(name, base_name), file=f)
    doc_lines = doc.splitlines()
    print('    """', file=f)
    for doc_line in doc_lines:
        print('    ' + doc_line, file=f)
    print('\n    """', file=f)
    print("    _name = '{}'".format(object_name), file=f)
    if name == 'Figure':
        print_figure_patch(f)
    elif name == 'Data':
        print_data_patch(f)
    elif name == 'Frames':
        print_frames_patch(f)

copied_lines = get_non_generated_file_lines()
with open('./plotly/graph_objs/graph_objs.py', 'w') as graph_objs_file:

    # Keep things *exactly* as they were above our special FLAG.
    for line in copied_lines:
        print(line, file=graph_objs_file, end='')
    print(FLAG, file=graph_objs_file)

    # For each object in the plot schema, generate a class in the file.
    class_names = list(CLASSES.keys())
    class_names.sort()
    for class_name in class_names:
        print_class(class_name, graph_objs_file)

    # Finish off the file by only exporting plot-schema names.
    print('\n__all__ = [cls for cls in graph_reference.CLASSES.keys() '
          'if cls in globals()]', file=graph_objs_file)
