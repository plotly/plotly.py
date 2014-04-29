"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from ... graph_objs import graph_objs
from ... plotly import plotly as py
from ... import exceptions


# username for tests: 'plotlyimagetest'
# password for account: 'password'
# api_key for account: '786r5mecv0'


def compare_with_raw(obj, raw_obj, parents=None):
    if isinstance(obj, dict):
        for key in raw_obj:
            if key not in obj:
                if not is_trivial(raw_obj[key]):
                    msg = ""
                    if parents is not None:
                        msg += "->".join(parents) + "->"
                    msg += key + " not in obj\n"
                    print msg
            elif isinstance(raw_obj[key], (dict, list)) and len(raw_obj[key]):
                if parents is None:
                    compare_with_raw(obj[key],
                                     raw_obj[key],
                                     parents=[key])
                else:
                    compare_with_raw(obj[key],
                                     raw_obj[key],
                                     parents=parents + [key])

            else:
                if raw_obj[key] != obj[key]:
                    msg = ""
                    if parents is not None:
                        msg += "->".join(parents) + "->"
                    msg += key + " not equal!\n"
                    msg += "    raw: {} != obj: {}\n".format(raw_obj[key],
                                                             obj[key])
                    print msg
    elif isinstance(obj, list):
        for entry, entry_raw in zip(obj, raw_obj):
            if isinstance(entry, (dict, list)):
                try:
                    coll_name = graph_objs.NAME_TO_KEY[entry.__class__
                        .__name__]
                except KeyError:
                    coll_name = entry.__class__.__name__
                if parents is None:
                    compare_with_raw(entry,
                                     entry_raw,
                                     parents=[coll_name])
                else:
                    compare_with_raw(entry,
                                     entry_raw,
                                     parents=parents + [coll_name])
            else:
                if entry != entry_raw:
                    msg = ""
                    if parents is not None:
                        msg += "->".join(parents) + "->"
                    msg += "->[]->\n"
                    msg += "    obj: {} != raw_obj: {}\n".format(entry,
                                                                 entry_raw)
                    print msg


def is_trivial(obj):
    if isinstance(obj, (dict, list)):
        if len(obj):
            if isinstance(obj, dict):
                tests = (is_trivial(obj[key]) for key in obj)
                return all(tests)
            elif isinstance(obj, list):
                tests = (is_trivial(entry) for entry in obj)
                return all(tests)
            else:
                return False
        else:
            return True
    else:
        return False


def test_all():
    run_test = True
    end_file = 20
    polar_plots = [6, 7, 8]
    skip = range(0)
    if run_test:
        py.sign_in('plotlyimagetest', '786r5mecv0')
        file_id = 0
        while True:
            fig, fig_raw = None, None
            while (file_id in polar_plots) or (file_id in skip):
                print "    skipping file number: {}".format(file_id)
                file_id += 1
            try:
                print "testing file numer: {}".format(file_id)
                print "######################\n\n"
                fig = py.get_figure('plotlyimagetest', str(file_id))
                fig_raw = py.get_figure('plotlyimagetest',
                                        str(file_id),
                                        raw=True)
            except exceptions.PlotlyError:
                pass
            if (fig is None) and (fig_raw is None):
                print "    couldn't find file number: {}".format(file_id)
            else:
                compare_with_raw(fig, fig_raw, parents=['figure'])
            file_id += 1
            if file_id > end_file:
                break
        raise exceptions.PlotlyError("This error was generated to see the "
                                     "above print out...")



