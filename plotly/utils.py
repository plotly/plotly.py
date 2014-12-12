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
    from sage.all import RR, ZZ
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


### Custom JSON encoders ###
class NotEncodable(Exception):
    pass


class _plotlyJSONEncoder(json.JSONEncoder):
    def numpyJSONEncoder(self, obj):
        if not _numpy_imported:
            raise NotEncodable

        if type(obj).__module__.split('.')[0] == numpy.__name__:
            l = obj.tolist()
            try:
                return self.datetimeJSONEncoder(l)
            except NotEncodable:
                return l
        else:
            raise NotEncodable

    def datetimeJSONEncoder(self, obj):
        """
        if datetime or iterable of datetimes,
        convert to a string that plotly understands
        format as %Y-%m-%d %H:%M:%S.%f,
                  %Y-%m-%d %H:%M:%S, or
                  %Y-%m-%d
        depending on what non-zero resolution was provided
        """

        if _pandas_imported and obj is pandas.NaT:
            return None

        if isinstance(obj, (datetime.datetime, datetime.date)):
            if obj.microsecond:
                return obj.strftime('%Y-%m-%d %H:%M:%S.%f')
            elif any((obj.second, obj.minute, obj.hour)):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            else:
                return obj.strftime('%Y-%m-%d')
        elif isinstance(obj[0], (datetime.datetime, datetime.date)):
            return [o.strftime(
                    '%Y-%m-%d %H:%M:%S.%f') if o.microsecond else
                    o.strftime('%Y-%m-%d %H:%M:%S') if any((o.second, o.minute, o.hour)) else
                    o.strftime('%Y-%m-%d')
                    for o in obj]
        else:
            raise NotEncodable

    def pandasJSONEncoder(self, obj):
        if not _pandas_imported:
            raise NotEncodable

        if isinstance(obj, pandas.Series):
            serializable_list = []
            for li in list(obj):
                try:
                    json.dumps(li)
                    serializable_list.append(li)
                except TypeError:
                    serializable_list.append(self.default(li))

            return serializable_list
        elif isinstance(obj, pandas.Index):
            return obj.tolist()
        elif obj is pandas.NaT:
            return None
        else:
            raise NotEncodable

    def sageJSONEncoder(self, obj):
        if not _sage_imported:
            raise NotEncodable

        if obj in RR:
            return float(obj)
        elif obj in ZZ:
            return int(obj)
        else:
            raise NotEncodable

    def builtinJSONEncoder(self, obj):
        '''
        Provide an API for folks to write their own
        JSON encoders for their objects that they wanna
        send to Plotly: this is an object's `to_plotly_json` method

        Used for grid_objs.Column objects.
        '''
        try:
            return obj.to_plotly_json()
        except AttributeError:
            raise NotEncodable

    def default(self, obj):
        encoders = (self.builtinJSONEncoder,
                    self.datetimeJSONEncoder,
                    self.numpyJSONEncoder,
                    self.pandasJSONEncoder,
                    self.sageJSONEncoder)
        for encoder in encoders:
            try:
                return encoder(obj)
            except NotEncodable:
                pass

        raise TypeError(repr(obj) + " is not JSON serializable")


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
