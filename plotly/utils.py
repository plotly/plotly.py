"""
utils
=====

Low-level functionality NOT intended for users to EVER use.

"""
from __future__ import absolute_import

import json
import os.path
import re
import sys
import threading

import pytz


from . exceptions import PlotlyError

try:
    import numpy
    _numpy_imported = True
except ImportError:
    _numpy_imported = False

try:
    import pandas
    _pandas_imported = True
except ImportError:
    _pandas_imported = False

try:
    import sage.all
    _sage_imported = True
except ImportError:
    _sage_imported = False


### incase people are using threading, we lock file reads
lock = threading.Lock()


### general file setup tools ###

def load_json_dict(filename, *args):
    """Checks if file exists. Returns {} if something fails."""
    data = {}
    if os.path.exists(filename):
        lock.acquire()
        with open(filename, "r") as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
            except:
                data = {}  # TODO: issue a warning and bubble it up
        lock.release()
        if args:
            return {key: data[key] for key in args if key in data}
    return data


def save_json_dict(filename, json_dict):
    """Save json to file. Error if path DNE, not a dict, or invalid json."""
    if isinstance(json_dict, dict):
        # this will raise a TypeError if something goes wrong
        json_string = json.dumps(json_dict, indent=4)
        lock.acquire()
        with open(filename, "w") as f:
            f.write(json_string)
        lock.release()
    else:
        raise TypeError("json_dict was not a dictionary. not saving.")


def ensure_file_exists(filename):
    """Given a valid filename, make sure it exists (will create if DNE)."""
    if not os.path.exists(filename):
        head, tail = os.path.split(filename)
        ensure_dir_exists(head)
        with open(filename, 'w') as f:
            pass  # just create the file


def ensure_dir_exists(directory):
    """Given a valid directory path, make sure it exists."""
    if dir:
        if not os.path.isdir(directory):
            os.makedirs(directory)


def iso_to_plotly_time_string(iso_string):
    """Remove timezone info and replace 'T' delimeter with ' ' (ws)."""
    # make sure we don't send timezone info to plotly
    if (iso_string.split('-')[:3] is '00:00') or\
            (iso_string.split('+')[0] is '00:00'):
        raise Exception("Plotly won't accept timestrings with timezone info.\n"
                        "All timestrings are assumed to be in UTC.")

    iso_string = iso_string.replace('-00:00', '').replace('+00:00', '')

    if iso_string.endswith('T00:00:00'):
        return iso_string.replace('T00:00:00', '')
    else:
        return iso_string.replace('T', ' ')


### Custom JSON encoders ###
class NotEncodable(Exception):
    pass


class PlotlyJSONEncoder(json.JSONEncoder):
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
        if const in ('Infinity', '-Infinity', 'NaN'):
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
            new_o = json.loads(encoded_o, parse_constant=self.coerce_to_strict)
        except ValueError:

            # invalid separators will fail here. raise a helpful exception
            raise ValueError(
                "Encoding into strict JSON failed. Did you set the separators "
                "valid JSON separators?"
            )
        else:
            return json.dumps(new_o, sort_keys=self.sort_keys,
                              indent=self.indent,
                              separators=(self.item_separator,
                                          self.key_separator))

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
            self.encode_as_list  # because some values have `tolist` do last.
        )
        for encoding_method in encoding_methods:
            try:
                return encoding_method(obj)
            except NotEncodable:
                pass
        return json.JSONEncoder.default(self, obj)

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
        if hasattr(obj, 'tolist'):
            return obj.tolist()
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_sage(obj):
        """Attempt to convert sage.all.RR to floats and sage.all.ZZ to ints"""
        if not _sage_imported:
            raise NotEncodable

        if obj in sage.all.RR:
            return float(obj)
        elif obj in sage.all.ZZ:
            return int(obj)
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_pandas(obj):
        """Attempt to convert pandas.NaT"""
        if not _pandas_imported:
            raise NotEncodable

        if obj is pandas.NaT:
            return None
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_numpy(obj):
        """Attempt to convert numpy.ma.core.masked"""
        if not _numpy_imported:
            raise NotEncodable

        if obj is numpy.ma.core.masked:
            return float('nan')
        else:
            raise NotEncodable

    @staticmethod
    def encode_as_datetime(obj):
        """Attempt to convert to utc-iso time string using datetime methods."""

        # first we need to get this into utc
        try:
            obj = obj.astimezone(pytz.utc)
        except ValueError:
            # we'll get a value error if trying to convert with naive datetime
            pass
        except TypeError:
            # pandas throws a typeerror here instead of a value error, it's OK
            pass
        except AttributeError:
            # we'll get an attribute error if astimezone DNE
            raise NotEncodable

        # now we need to get a nicely formatted time string
        try:
            time_string = obj.isoformat()
        except AttributeError:
            raise NotEncodable
        else:
            return iso_to_plotly_time_string(time_string)

    @staticmethod
    def encode_as_date(obj):
        """Attempt to convert to utc-iso time string using date methods."""
        try:
            time_string = obj.isoformat()
        except AttributeError:
            raise NotEncodable
        else:
            return iso_to_plotly_time_string(time_string)


### unicode stuff ###
def decode_unicode(coll):
    if isinstance(coll, list):
        for no, entry in enumerate(coll):
            if isinstance(entry, (dict, list)):
                coll[no] = decode_unicode(entry)
            else:
                if isinstance(entry, str):
                    try:
                        coll[no] = str(entry)
                    except UnicodeEncodeError:
                        pass
    elif isinstance(coll, dict):
        keys, vals = list(coll.keys()), list(coll.values())
        for key, val in zip(keys, vals):
            if isinstance(val, (dict, list)):
                coll[key] = decode_unicode(val)
            elif isinstance(val, str):
                try:
                    coll[key] = str(val)
                except UnicodeEncodeError:
                    pass
            coll[str(key)] = coll.pop(key)
    return coll


### docstring templating ###
def template_doc(**names):
    def _decorator(func):
        if sys.version[:3] != '3.2':
            if func.__doc__ is not None:
                func.__doc__ = func.__doc__.format(**names)
        return func
    return _decorator


def get_first_duplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
        else:
            return item
    return None


### source key
def is_source_key(key):
    src_regex = re.compile(r'.+src$')
    if src_regex.match(key) is not None:
        return True
    else:
        return False


def node_generator(node, path=()):
    """
    General, node-yielding generator.

    Yields (node, path) tuples when it finds values that are dict
    instances.

    A path is a sequence of hashable values that can be used as either keys to
    a mapping (dict) or indices to a sequence (list). A path is always wrt to
    some object. Given an object, a path explains how to get from the top level
    of that object to a nested value in the object.

    :param (dict) node: Part of a dict to be traversed.
    :param (tuple[str]) path: Defines the path of the current node.
    :return: (Generator)

    Example:

        >>> for node, path in node_generator({'a': {'b': 5}}):
        >>>     print node, path
        {'a': {'b': 5}} ()
        {'b': 5} ('a', )

    """
    if not isinstance(node, dict):
        return  # in case it's called with a non-dict node at top level
    yield node, path
    for key, val in node.items():
        if isinstance(val, dict):
            for item in node_generator(val, path + (key, )):
                yield item


def get_by_path(obj, path):
    """
    Iteratively get on obj for each key in path.

    :param (list|dict) obj: The top-level object.
    :param (tuple[str]|tuple[int]) path: Keys to access parts of obj.

    :return: (*)

    Example:

        >>> figure = {'data': [{'x': [5]}]}
        >>> path = ('data', 0, 'x')
        >>> get_by_path(figure, path)  # [5]

    """
    for key in path:
        obj = obj[key]
    return obj


### validation
def validate_world_readable_and_sharing_settings(option_set):
    if ('world_readable' in option_set and
        option_set['world_readable'] is True and
        'sharing' in option_set and
        option_set['sharing'] is not None and
            option_set['sharing'] != 'public'):
        raise PlotlyError(
            "Looks like you are setting your plot privacy to both "
            "public and private.\n If you set world_readable as True, "
            "sharing can only be set to 'public'")
    elif ('world_readable' in option_set and
          option_set['world_readable'] is False and
          'sharing' in option_set and
          option_set['sharing'] == 'public'):
        raise PlotlyError(
            "Looks like you are setting your plot privacy to both "
            "public and private.\n If you set world_readable as "
            "False, sharing can only be set to 'private' or 'secret'")
    elif ('sharing' in option_set and
          option_set['sharing'] not in ['public', 'private', 'secret', None]):
        raise PlotlyError(
            "The 'sharing' argument only accepts one of the following "
            "strings:\n'public' -- for public plots\n"
            "'private' -- for private plots\n"
            "'secret' -- for private plots that can be shared with a "
            "secret url"
        )


def set_sharing_and_world_readable(option_set):
    if 'world_readable' in option_set and 'sharing' not in option_set:
        option_set['sharing'] = (
            'public' if option_set['world_readable'] else 'private')

    elif 'sharing' in option_set and 'world_readable' not in option_set:
        if option_set['sharing'] == 'public':
            option_set['world_readable'] = True
        else:
            option_set['world_readable'] = False
