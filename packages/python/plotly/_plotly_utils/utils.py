import decimal
import json as _json
import sys
import re

from _plotly_utils.optional_imports import get_module
from _plotly_utils.basevalidators import ImageUriValidator


PY36_OR_LATER = sys.version_info >= (3, 6)


class PlotlyJSONEncoder(_json.JSONEncoder):
    """
    Meant to be passed as the `cls` kwarg to json.dumps(obj, cls=..)

    See PlotlyJSONEncoder.default for more implementation information.

    Additionally, this encoder overrides nan functionality so that 'Inf',
    'NaN' and '-Inf' encode to 'null'. Which is stricter JSON than the Python
    version.

    """

    def coerce_to_strict(self, const):
        """
        This is used to ultimately *encode* into strict JSON, see `encode`

        """
        # before python 2.7, 'true', 'false', 'null', were include here.
        if const in ("Infinity", "-Infinity", "NaN"):
            return None
        else:
            return const

    def encode(self, o):
        """
        Load and then dump the result using parse_constant kwarg

        Note that setting invalid separators will cause a failure at this step.

        """

        # this will raise errors in a normal-expected way
        encoded_o = super(PlotlyJSONEncoder, self).encode(o)

        # now:
        #    1. `loads` to switch Infinity, -Infinity, NaN to None
        #    2. `dumps` again so you get 'null' instead of extended JSON
        try:
            new_o = _json.loads(encoded_o, parse_constant=self.coerce_to_strict)
        except ValueError:

            # invalid separators will fail here. raise a helpful exception
            raise ValueError(
                "Encoding into strict JSON failed. Did you set the separators "
                "valid JSON separators?"
            )
        else:
            return _json.dumps(
                new_o,
                sort_keys=self.sort_keys,
                indent=self.indent,
                separators=(self.item_separator, self.key_separator),
            )

    def default(self, obj):
        """
        Accept an object (of unknown type) and try to encode with priority:
        1. builtin:     user-defined objects
        2. sage:        sage math cloud
        3. pandas:      dataframes/series
        4. numpy:       ndarrays
        5. datetime:    time/datetime objects

        Each method throws a NotEncoded exception if it fails.

        The default method will only get hit if the object is not a type that
        is naturally encoded by json:

            Normal objects:
                dict                object
                list, tuple         array
                str, unicode        string
                int, long, float    number
                True                true
                False               false
                None                null

            Extended objects:
                float('nan')        'NaN'
                float('infinity')   'Infinity'
                float('-infinity')  '-Infinity'

        Therefore, we only anticipate either unknown iterables or values here.

        """
        # TODO: The ordering if these methods is *very* important. Is this OK?
        encoding_methods = (
            self.encode_as_plotly,
            self.encode_as_sage,
            self.encode_as_numpy,
            self.encode_as_pandas,
            self.encode_as_datetime,
            self.encode_as_date,
            self.encode_as_list,  # because some values have `tolist` do last.
            self.encode_as_decimal,
            self.encode_as_pil,
        )
        for encoding_method in encoding_methods:
            try:
                return encoding_method(obj)
            except NotEncodable:
                pass
        return _json.JSONEncoder.default(self, obj)

    @staticmethod
    def encode_as_plotly(obj):
        """Attempt to use a builtin `to_plotly_json` method."""
        try:
            return obj.to_plotly_json()
        except AttributeError:
            raise NotEncodable

    @staticmethod
    def encode_as_list(obj):
        """Attempt to use `tolist` method to convert to normal Python list."""
        if hasattr(obj, "tolist"):
            return obj.tolist()
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_sage(obj):
        """Attempt to convert sage.all.RR to floats and sage.all.ZZ to ints"""
        sage_all = get_module("sage.all")
        if not sage_all:
            raise NotEncodable

        if obj in sage_all.RR:
            return float(obj)
        elif obj in sage_all.ZZ:
            return int(obj)
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_pandas(obj):
        """Attempt to convert pandas.NaT"""
        pandas = get_module("pandas")
        if not pandas:
            raise NotEncodable

        if obj is pandas.NaT:
            return None
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_numpy(obj):
        """Attempt to convert numpy.ma.core.masked"""
        numpy = get_module("numpy")
        if not numpy:
            raise NotEncodable

        if obj is numpy.ma.core.masked:
            return float("nan")
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_datetime(obj):
        """Convert datetime objects to iso-format strings"""
        try:
            return obj.isoformat()
        except AttributeError:
            raise NotEncodable

    @staticmethod
    def encode_as_date(obj):
        """Attempt to convert to utc-iso time string using date methods."""
        try:
            time_string = obj.isoformat()
        except AttributeError:
            raise NotEncodable
        else:
            return iso_to_plotly_time_string(time_string)

    @staticmethod
    def encode_as_decimal(obj):
        """Attempt to encode decimal by converting it to float"""
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_pil(obj):
        """Attempt to convert PIL.Image.Image to base64 data uri"""
        image = get_module("PIL.Image")
        if image is not None and isinstance(obj, image.Image):
            return ImageUriValidator.pil_image_to_uri(obj)
        else:
            raise NotEncodable


class NotEncodable(Exception):
    pass


def iso_to_plotly_time_string(iso_string):
    """Remove timezone info and replace 'T' delimeter with ' ' (ws)."""
    # make sure we don't send timezone info to plotly
    if (iso_string.split("-")[:3] is "00:00") or (iso_string.split("+")[0] is "00:00"):
        raise Exception(
            "Plotly won't accept timestrings with timezone info.\n"
            "All timestrings are assumed to be in UTC."
        )

    iso_string = iso_string.replace("-00:00", "").replace("+00:00", "")

    if iso_string.endswith("T00:00:00"):
        return iso_string.replace("T00:00:00", "")
    else:
        return iso_string.replace("T", " ")


def template_doc(**names):
    def _decorator(func):
        if not sys.version_info[:2] == (3, 2):
            if func.__doc__ is not None:
                func.__doc__ = func.__doc__.format(**names)
        return func

    return _decorator


def _natural_sort_strings(vals, reverse=False):
    def key(v):
        v_parts = re.split(r"(\d+)", v)
        for i in range(len(v_parts)):
            try:
                v_parts[i] = int(v_parts[i])
            except ValueError:
                # not an int
                pass
        return tuple(v_parts)

    return sorted(vals, key=key, reverse=reverse)
