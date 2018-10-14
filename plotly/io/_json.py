from __future__ import absolute_import

from six import string_types
import json

from plotly.utils import PlotlyJSONEncoder
from plotly.io._utils import (validate_coerce_fig_to_dict,
                              validate_coerce_output_type)


def to_json(fig,
            validate=True,
            pretty=False,
            remove_uids=True):
    """
    Convert a figure to a JSON string representation

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    validate: bool (default True)
        True if the figure should be validated before being converted to
        JSON, False otherwise.

    pretty: bool (default False)
        True if JSON representation should be pretty-printed, False if
        representation should be as compact as possible.

    remove_uids: bool (default True)
        True if trace UIDs should be omitted from the JSON representation

    Returns
    -------
    str
        Representation of figure as a JSON string
    """
    # Validate figure
    # ---------------
    fig_dict = validate_coerce_fig_to_dict(fig, validate)

    # Remove trace uid
    # ----------------
    if remove_uids:
        for trace in fig_dict.get('data', []):
            trace.pop('uid', None)

    # Dump to a JSON string and return
    # --------------------------------
    opts = {'sort_keys': True}
    if pretty:
        opts['indent'] = 2
    else:
        # Remove all whitespace
        opts['separators'] = (',', ':')

    return json.dumps(fig_dict, cls=PlotlyJSONEncoder, **opts)


def write_json(fig, file, validate=True, pretty=False, remove_uids=True):
    """
    Convert a figure to JSON and write it to a file or writeable
    object

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    file: str or writeable
        A string representing a local file path or a writeable object
        (e.g. an open file descriptor)

    pretty: bool (default False)
        True if JSON representation should be pretty-printed, False if
        representation should be as compact as possible.

    remove_uids: bool (default True)
        True if trace UIDs should be omitted from the JSON representation

    Returns
    -------
    None
    """

    # Get JSON string
    # ---------------
    # Pass through validate argument and let to_json handle validation logic
    json_str = to_json(
        fig, validate=validate, pretty=pretty, remove_uids=remove_uids)

    # Check if file is a string
    # -------------------------
    file_is_str = isinstance(file, string_types)

    # Open file
    # ---------
    if file_is_str:
        with open(file, 'w') as f:
            f.write(json_str)
    else:
        file.write(json_str)


def from_json(value, output_type='Figure', skip_invalid=False):
    """
    Construct a figure from a JSON string

    Parameters
    ----------
    value: str
        String containing the JSON representation of a figure

    output_type: type or str (default 'Figure')
        The output figure type or type name.
        One of:  graph_objs.Figure, 'Figure',
                 graph_objs.FigureWidget, 'FigureWidget'

    skip_invalid: bool (default False)
        False if invalid figure properties should result in an exception.
        True if invalid figure properties should be silently ignored.

    Raises
    ------
    ValueError
        if value is not a string, or if skip_invalid=False and value contains
        invalid figure properties

    Returns
    -------
    Figure or FigureWidget
    """

    # Validate value
    # --------------
    if not isinstance(value, string_types):
        raise ValueError("""
from_json requires a string argument but received value of type {typ}
    Received value: {value}""".format(typ=type(value),
                                      value=value))

    # Decode JSON
    # -----------
    fig_dict = json.loads(value)

    # Validate coerce output type
    # ---------------------------
    cls = validate_coerce_output_type(output_type)

    # Create and return figure
    # ------------------------
    fig = cls(fig_dict, skip_invalid=skip_invalid)
    return fig


def read_json(file, output_type='Figure', skip_invalid=False):
    """
    Construct a figure from the JSON contents of a local file or readable
    Python object

    Parameters
    ----------
    file: str or readable
       A string containing the path to a local file or a read-able Python
       object (e.g. an open file descriptor)

    output_type: type or str (default 'Figure')
        The output figure type or type name.
        One of:  graph_objs.Figure, 'Figure',
                 graph_objs.FigureWidget, 'FigureWidget'

    skip_invalid: bool (default False)
        False if invalid figure properties should result in an exception.
        True if invalid figure properties should be silently ignored.

    Returns
    -------
    Figure or FigureWidget
    """

    # Check if file is a string
    # -------------------------
    # If it's a string we assume it's a local file path. If it's not a string
    # then we assume it's a read-able Python object
    file_is_str = isinstance(file, string_types)

    # Read file contents into JSON string
    # -----------------------------------
    if file_is_str:
        with open(file, 'r') as f:
            json_str = f.read()
    else:
        json_str = file.read()

    # Construct and return figure
    # ---------------------------
    return from_json(json_str,
                     skip_invalid=skip_invalid,
                     output_type=output_type)
