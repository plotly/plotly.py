"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from nose.tools import raises
from ... import graph_objs
from ... exceptions import PlotlyError
from copy import copy

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


# def test_trace():
#     polar_plots = [6, 7, 8]
#     skip = range(0)
#     import plotly.plotly as py
#     py.sign_in('plotlyimagetest', '786r5mecv0')
#     file_id = 0
#     while True:
#         while (file_id in polar_plots) or (file_id in skip):
#             print "    skipping file number: {}".format(file_id)
#             file_id += 1
#         try:
#             print "testing file numer: {}".format(file_id)
#             print "######################\n\n"
#             fig_raw = py.get_figure('plotlyimagetest', str(file_id), raw=True)
#         except:
#             pass
#         if fig_raw is None:
#             print "    couldn't find file number: {}".format(file_id)
#         try:
#             for entry in fig_raw['data']:
#                 for key in entry:
#                     if key not in graph_objs.INFO['trace']:
#                         print "ADD THIS KEY TO TRACE! -> {}".format(key)
#                         raise PlotlyError
#         except KeyError:
#             pass
#         file_id += 1
#         if file_id > 1:
#             break


def test_all():
    polar_plots = [6, 7, 8]
    skip = range(0)
    import pprint
    import plotly.plotly as py
    py.sign_in('plotlyimagetest', '786r5mecv0')
    file_id = 0
    while True:
        while (file_id in polar_plots) or (file_id in skip):
            print "    skipping file number: {}".format(file_id)
            file_id += 1
        try:
            print "testing file numer: {}".format(file_id)
            print "######################\n\n"
            fig = py.get_figure('plotlyimagetest', str(file_id))
            fig_raw = py.get_figure('plotlyimagetest', str(file_id), raw=True)
        except:
            pass
        if (fig is None) and (fig_raw is None):
            print "    couldn't find file number: {}".format(file_id)
        else:
            compare_with_raw(fig, fig_raw, parents=['figure'])
            # for entry, entry_raw in zip(fig['data'], fig_raw['data']):
            #     if entry.__class__.__name__ == 'Trace':
            #         print 'file number {} had this graph_obj:\n'.format(file_id)
            #         pp = pprint.PrettyPrinter(indent=4)
            #         pp.pprint(entry)
            #         print "\n\n#########################################\n\n"
            #         print 'file number {} had this raw_obj:\n'.format(file_id)
            #         pp.pprint(entry_raw)
            #         missing = [key for key in entry
            #                    if key not in graph_objs.INFO[entry['type']]]
            #         print 'missing keys from type: {}\n {}'.format(
            #             entry['type'], missing)
            #         raise PlotlyError
        file_id += 1
        if file_id > 46:
            break
    raise PlotlyError("see above print out...")


