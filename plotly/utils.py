"""
utils
=====

Low-level functionality NOT intended for users to EVER use.

"""

import json
import os.path
import sys


### general file setup tools ###

def load_json_dict(filename, *args):
    """Checks if file exists. Returns {} if something fails."""
    data = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
            except:
                pass # TODO: issue a warning and bubble it up
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
    """Will error if filename is not appropriate, but it's checked elsewhere.
    """
    if isinstance(json_dict, dict):
        with open(filename, "w") as f:
            f.write(json.dumps(json_dict, indent=4))
    else:
        raise TypeError("json_dict was not a dictionay. couldn't save.")


### Custom JSON encoders ###
class _plotlyJSONEncoder(json.JSONEncoder):
    def numpyJSONEncoder(self, obj):
        try:
            import numpy
            if type(obj).__module__.split('.')[0] == numpy.__name__:
                l = obj.tolist()
                d = self.datetimeJSONEncoder(l)
                return d if d is not None else l
        except:
            pass
        return None

    def datetimeJSONEncoder(self, obj):
        # if datetime or iterable of datetimes, convert to a string that plotly understands
        # format as %Y-%m-%d %H:%M:%S.%f, %Y-%m-%d %H:%M:%S, or %Y-%m-%d depending on what non-zero resolution was provided
        import datetime
        try:
            if isinstance(obj, (datetime.datetime, datetime.date)):
                if obj.microsecond != 0:
                    return obj.strftime('%Y-%m-%d %H:%M:%S.%f')
                elif obj.second != 0 or obj.minute != 0 or obj.hour != 0:
                    return obj.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    return obj.strftime('%Y-%m-%d')
            elif isinstance(obj[0], (datetime.datetime, datetime.date)):
                return [o.strftime(
                        '%Y-%m-%d %H:%M:%S.%f') if o.microsecond != 0 else
                        o.strftime('%Y-%m-%d %H:%M:%S') if o.second != 0 or o.minute != 0 or o.hour != 0 else
                        o.strftime('%Y-%m-%d')
                        for o in obj]
        except:
            pass
        return None

    def pandasJSONEncoder(self, obj):
        try:
            import pandas
            if isinstance(obj, pandas.Series):
                return obj.tolist()
        except:
            pass
        return None

    def sageJSONEncoder(self, obj):
        try:
            from sage.all import RR, ZZ
            if obj in RR:
                return float(obj)
            elif obj in ZZ:
                return int(obj)
        except:
            pass
        return None

    def default(self, obj):
        try:
            return json.dumps(obj)
        except TypeError as e:
            encoders = (self.datetimeJSONEncoder, self.numpyJSONEncoder,
                        self.pandasJSONEncoder, self.sageJSONEncoder)
            for encoder in encoders:
                s = encoder(obj)
                if s is not None:
                    return s
            raise e
        return json.JSONEncoder.default(self, obj)


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
