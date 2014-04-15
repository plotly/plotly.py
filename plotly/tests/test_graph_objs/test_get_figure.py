"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from nose.tools import raises
from ... import graph_objs
from ... exceptions import PlotlyError

# username for tests: 'plotlyimagetest'
# password for account: 'password'
# api_key for account: '786r5mecv0'


def compare_with_raw(obj, raw_obj):
    if isinstance(obj, dict):
        for key in raw_obj:
            if key not in obj:
                if not is_trivial(raw_obj[key]):
                    print "{} not in {}".format(key, obj.__class__.__name__)
                    import pprint
                    pp = pprint.PrettyPrinter(indent=4)
                    pp.pprint(raw_obj[key])
                    raise PlotlyError
            elif isinstance(raw_obj[key], (dict, list)) and len(raw_obj[key]):
                compare_with_raw(obj[key], raw_obj[key])
            else:
                if raw_obj[key] != obj[key]:
                    print "raw_obj: {name}[{key}] != obj: {name}[{key}]".format(
                        key=key, name=obj.__class__.__name__)
                    import pprint
                    pp = pprint.PrettyPrinter(indent=4)
                    pp.pprint(raw_obj[key])
                    print ('\n\n#########################################\n\n')
                    pp.pprint(obj[key])
                    raise PlotlyError
    elif isinstance(obj, list):
        for entry, entry_raw in zip(obj, raw_obj):
            if isinstance(entry, (dict, list)):
                compare_with_raw(entry, entry_raw)
            else:
                if entry != entry_raw:
                    print entry.__class__.__name__, entry, entry_raw
                    raise PlotlyError


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


# def test_get_cartesian_scatter():
#     import plotly.plotly as py
#     py.sign_in('plotlyimagetest', '786r5mecv0')
#     fig = py.get_figure('plotlyimagetest', '24')
#     fig_raw = py.get_figure('plotlyimagetest', '24', raw=True)
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fig)
#     print ('\n\n##########################################################\n\n')
#     pp.pprint(fig_raw)
#     compare_with_raw(fig, fig_raw)
#
#
# def test_get_bar():
#     import plotly.plotly as py
#     py.sign_in('plotlyimagetest', '786r5mecv0')
#     fig = py.get_figure('plotlyimagetest', '0')
#     fig_raw = py.get_figure('plotlyimagetest', '0', raw=True)
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fig)
#     print ('\n\n##########################################################\n\n')
#     pp.pprint(fig_raw)
#     compare_with_raw(fig, fig_raw)
#
#
# def test_get_histogramx():
#     import plotly.plotly as py
#     py.sign_in('plotlyimagetest', '786r5mecv0')
#     fig = py.get_figure('plotlyimagetest', '9')
#     fig_raw = py.get_figure('plotlyimagetest', '9', raw=True)
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fig)
#     print ('\n\n##########################################################\n\n')
#     pp.pprint(fig_raw)
#     compare_with_raw(fig, fig_raw)
#
#
# def test_get_histogram2d():
#     import plotly.plotly as py
#     py.sign_in('plotlyimagetest', '786r5mecv0')
#     fig = py.get_figure('plotlyimagetest', '21')
#     fig_raw = py.get_figure('plotlyimagetest', '21', raw=True)
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fig)
#     print ('\n\n##########################################################\n\n')
#     pp.pprint(fig_raw)
#     compare_with_raw(fig, fig_raw)
#
#
# def test_get_subplots():
#     import plotly.plotly as py
#     py.sign_in('plotlyimagetest', '786r5mecv0')
#     fig = py.get_figure('plotlyimagetest', '19')
#     fig_raw = py.get_figure('plotlyimagetest', '19', raw=True)
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fig)
#     print ('\n\n##########################################################\n\n')
#     pp.pprint(fig_raw)
#     compare_with_raw(fig, fig_raw)


def test_all():
    polar_plots = [6, 7, 8]
    come_back_to = []
    import pprint
    import plotly.plotly as py
    py.sign_in('plotlyimagetest', '786r5mecv0')
    file_id = 0
    while True:
        try:
            print "testing file numer: {}".format(file_id)
            fig = py.get_figure('plotlyimagetest', str(file_id))
            fig_raw = py.get_figure('plotlyimagetest', str(file_id), raw=True)
        except:
            pass
        if (fig is None) and (fig_raw is None):
            print "    couldn't find file number: {}".format(file_id)
        else:
            compare_with_raw(fig, fig_raw)
            # for entry, entry_raw in zip(fig['data'], fig_raw['data']):
            #     if entry.__class__.__name__ == 'Trace':
            #         print 'file number {} had this trace: \n'.format(file_id)
            #         pp = pprint.PrettyPrinter(indent=4)
            #         pp.pprint(entry)
            #         print "\n\n#########################################\n\n"
            #         pp.pprint(entry_raw)
            #         missing = [key for key in entry
            #                    if key not in graph_objs.INFO[entry['type']]]
            #         print 'missing keys from type: {}\n {}'.format(
            #             entry['type'], missing)
            #         raise PlotlyError
        file_id += 1
        while (file_id in polar_plots) or (file_id in come_back_to):
            print "    skipping file number: {}".format(file_id)
            file_id += 1
        if file_id > 50:
            break


