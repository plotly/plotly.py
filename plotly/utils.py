"""
utils
=====

Low-level functionality NOT intended for users to EVER use.

"""

import json
import os.path


### general file setup tools ###

def load_json(filename, *args):
    if os.path.getsize(filename) > 0:
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except:
                # TODO: issue a warning and bubble it up
                data = ""
    else:
        data = ""
    if len(args) and data:
        return {key: data[key] for key in args}
    else:
        return data


def save_json(filename, json_obj):
    with open(filename, "w") as f:
        f.write(json.dumps(json_obj, indent=4))


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
                if isinstance(entry, unicode):
                    try:
                        coll[no] = str(entry)
                    except UnicodeEncodeError:
                        pass
    elif isinstance(coll, dict):
        keys, vals = coll.keys(), coll.values()
        for key, val in zip(keys, vals):
            if isinstance(val, (dict, list)):
                coll[key] = decode_unicode(val)
            elif isinstance(val, unicode):
                try:
                    coll[key] = str(val)
                except UnicodeEncodeError:
                    pass
            coll[str(key)] = coll.pop(key)
    return coll