"""
utils
=====

Low-level functionality NOT intended for users to EVER use.

"""

import json
import os.path
import sys
import threading
import re
import datetime
import pytz

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
            d = dict()
            for key in args:
                if key in data:
                    d[key] = data[key]
            return d
            # TODO: replace with below if we drop Python 2.6 compatibility
            # return {key: data[key] for key in args if key in data}
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

    """

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
