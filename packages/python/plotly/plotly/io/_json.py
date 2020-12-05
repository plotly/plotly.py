from __future__ import absolute_import

from six import string_types
import json
import decimal


from plotly.io._utils import validate_coerce_fig_to_dict, validate_coerce_output_type
from _plotly_utils.utils import iso_to_plotly_time_string
from _plotly_utils.optional_imports import get_module
from _plotly_utils.basevalidators import ImageUriValidator


# Orca configuration class
# ------------------------
class JsonConfig(object):
    _valid_encoders = ("legacy", "json", "orjson", "auto")

    def __init__(self):
        self._default_encoder = "auto"

    @property
    def default_encoder(self):
        return self._default_encoder

    @default_encoder.setter
    def default_encoder(self, val):
        if val not in JsonConfig._valid_encoders:
            raise ValueError(
                "Supported JSON encoders include {valid}\n"
                "    Received {val}".format(valid=JsonConfig._valid_encoders, val=val)
            )

        if val == "orjson":
            orjson = get_module("orjson")
            if orjson is None:
                raise ValueError(
                    "The orjson encoder requires the orjson package"
                )

        self._default_encoder = val


config = JsonConfig()


def coerce_to_strict(const):
    """
    This is used to ultimately *encode* into strict JSON, see `encode`

    """
    # before python 2.7, 'true', 'false', 'null', were include here.
    if const in ("Infinity", "-Infinity", "NaN"):
        return None
    else:
        return const


def to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None):
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

    engine: str (default None)
        The JSON encoding engine to use. One of:
          - "json" for a rewritten encoder based on the built-in Python json module
          - "orjson" for a fast encoder the requires the orjson package
          - "legacy" for the legacy JSON encoder.
        If not specified, the default encoder is set to the current value of
        plotly.io.json.config.default_encoder.

    Returns
    -------
    str
        Representation of figure as a JSON string
    """
    orjson = get_module("orjson", should_load=True)

    # Validate figure
    # ---------------
    fig_dict = validate_coerce_fig_to_dict(fig, validate, clone=False)

    # Remove trace uid
    # ----------------
    if remove_uids:
        for trace in fig_dict.get("data", []):
            trace.pop("uid", None)

    # Determine json engine
    if engine is None:
        engine = config.default_encoder

    if engine == "auto":
        if orjson is not None:
            engine = "orjson"
        else:
            engine = "json"
    elif engine not in ["orjson", "json", "legacy"]:
        raise ValueError("Invalid json engine: %s" % engine)

    modules = {"sage_all": get_module("sage.all", should_load=False),
               "np": get_module("numpy", should_load=False),
               "pd": get_module("pandas", should_load=False),
               "image": get_module("PIL.Image", should_load=False)}

    orjson = get_module("orjson", should_load=True)

    # Dump to a JSON string and return
    # --------------------------------
    if engine in ("json", "legacy"):
        opts = {"sort_keys": True}
        if pretty:
            opts["indent"] = 2
        else:
            # Remove all whitespace
            opts["separators"] = (",", ":")

        if engine == "json":
            cleaned = clean_to_json_compatible(
                fig_dict, numpy_allowed=False,
                non_finite_allowed=False,
                datetime_allowed=False,
                modules=modules,
            )
            encoded_o = json.dumps(cleaned, **opts)

            if not ("NaN" in encoded_o or "Infinity" in encoded_o):
                return encoded_o

            # now:
            #    1. `loads` to switch Infinity, -Infinity, NaN to None
            #    2. `dumps` again so you get 'null' instead of extended JSON
            try:
                new_o = json.loads(encoded_o, parse_constant=coerce_to_strict)
            except ValueError:

                # invalid separators will fail here. raise a helpful exception
                raise ValueError(
                    "Encoding into strict JSON failed. Did you set the separators "
                    "valid JSON separators?"
                )
            else:
                return json.dumps(new_o, **opts)
        else:
            from _plotly_utils.utils import PlotlyJSONEncoder
            return json.dumps(fig_dict, cls=PlotlyJSONEncoder, **opts)
    elif engine == "orjson":
        opts = (orjson.OPT_SORT_KEYS
                | orjson.OPT_SERIALIZE_NUMPY
                | orjson.OPT_OMIT_MICROSECONDS
                )

        if pretty:
            opts |= orjson.OPT_INDENT_2

        cleaned = clean_to_json_compatible(
            fig_dict, numpy_allowed=True,
            non_finite_allowed=True,
            datetime_allowed=True,
            modules=modules,
        )
        return orjson.dumps(cleaned, option=opts).decode("utf8")


def write_json(fig, file, validate=True, pretty=False, remove_uids=True, engine=None):
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

    engine: str (default None)
        The JSON encoding engine to use. One of:
          - "json" for a rewritten encoder based on the built-in Python json module
          - "orjson" for a fast encoder the requires the orjson package
          - "legacy" for the legacy JSON encoder.
        If not specified, the default encoder is set to the current value of
        plotly.io.json.config.default_encoder.
    Returns
    -------
    None
    """

    # Get JSON string
    # ---------------
    # Pass through validate argument and let to_json handle validation logic
    json_str = to_json(fig, validate=validate, pretty=pretty, remove_uids=remove_uids, engine=engine)

    # Check if file is a string
    # -------------------------
    file_is_str = isinstance(file, string_types)

    # Open file
    # ---------
    if file_is_str:
        with open(file, "w") as f:
            f.write(json_str)
    else:
        file.write(json_str)


def from_json(value, output_type="Figure", skip_invalid=False):
    """
    Construct a figure from a JSON string

    Parameters
    ----------
    value: str
        String containing the JSON representation of a figure

    output_type: type or str (default 'Figure')
        The output figure type or type name.
        One of:  graph_objs.Figure, 'Figure', graph_objs.FigureWidget, 'FigureWidget'

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
        raise ValueError(
            """
from_json requires a string argument but received value of type {typ}
    Received value: {value}""".format(
                typ=type(value), value=value
            )
        )

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


def read_json(file, output_type="Figure", skip_invalid=False):
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
        One of:  graph_objs.Figure, 'Figure', graph_objs.FigureWidget, 'FigureWidget'

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
        with open(file, "r") as f:
            json_str = f.read()
    else:
        json_str = file.read()

    # Construct and return figure
    # ---------------------------
    return from_json(json_str, skip_invalid=skip_invalid, output_type=output_type)


def clean_to_json_compatible(obj, **kwargs):
    # Try handling value as a scalar value that we have a conversion for.
    # Return immediately if we know we've hit a primitive value

    # unpack kwargs
    numpy_allowed = kwargs.get("numpy_allowed", False)
    non_finite_allowed = kwargs.get("non_finite_allowed", False)
    datetime_allowed = kwargs.get("datetime_allowed", False)

    modules = kwargs.get("modules", {})
    sage_all = modules["sage_all"]
    np = modules["np"]
    pd = modules["pd"]
    image = modules["image"]

    # Plotly
    try:
        obj = obj.to_plotly_json(clone=False)
    except (TypeError, NameError, ValueError):
        # Try without clone for backward compatibility
        obj = obj.to_plotly_json()
    except AttributeError:
        pass

    # Sage
    if sage_all is not None:
        if obj in sage_all.RR:
            return float(obj)
        elif obj in sage_all.ZZ:
            return int(obj)

    # numpy
    if np is not None:
        if obj is np.ma.core.masked:
            return float("nan")
        elif numpy_allowed and isinstance(obj, np.ndarray) and obj.dtype.kind in ("b", "i", "u", "f"):
            return obj

    # pandas
    if pd is not None:
        if obj is pd.NaT:
            return None
        elif isinstance(obj, pd.Series):
            if numpy_allowed and obj.dtype.kind in ("b", "i", "u", "f"):
                return obj.values
            elif datetime_allowed and obj.dtype.kind == "M":
                return obj.dt.to_pydatetime().tolist()


    # datetime and date
    if not datetime_allowed:
        try:
            # Is this cleanup still needed?
            return iso_to_plotly_time_string(obj.isoformat())
        except AttributeError:
            pass

    # Try .tolist() convertible
    try:
        # obj = obj.tolist()
        return obj.tolist()
    except AttributeError:
        pass

    # Do best we can with decimal
    if isinstance(obj, decimal.Decimal):
        return float(obj)

    # PIL
    if image is not None and isinstance(obj, image.Image):
        return ImageUriValidator.pil_image_to_uri(obj)

    # Recurse into lists and dictionaries
    if isinstance(obj, dict):
        return {k: clean_to_json_compatible(v, **kwargs) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        if obj:
            # Must process list recursively even though it may be slow
            return [clean_to_json_compatible(v, **kwargs) for v in obj]

    return obj
