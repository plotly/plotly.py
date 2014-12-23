"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from plotly.graph_objs import graph_objs
from plotly.plotly import plotly as py
from plotly import exceptions
from nose.tools import raises
import six
import json

from unittest import TestCase
from unittest import skipIf


# username for tests: 'plotlyimagetest'
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
                    print(msg)
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
                    msg += "    raw: {0} != obj: {1}\n".format(raw_obj[key],
                                                               obj[key])
                    print(msg)
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
                    msg += "    obj: {0} != raw_obj: {1}\n".format(entry,
                                                                   entry_raw)
                    print(msg)


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
    elif obj is None:
        return True
    else:
        return False


def test_get_figure():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    file_id = 2
    py.sign_in(un, ak)
    print("getting: https://plot.ly/~{0}/{1}/".format(un, file_id))
    print("###########################################\n\n")
    fig = py.get_figure('PlotlyImageTest', str(file_id))


def test_get_figure_with_url():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/2/"
    py.sign_in(un, ak)
    print("getting: https://plot.ly/~PlotlyImageTest/2/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@raises(exceptions.PlotlyError)
def test_get_figure_invalid_1():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/a/"
    py.sign_in(un, ak)
    print("not getting: https://plot.ly/~PlotlyImageTest/a/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@raises(exceptions.PlotlyError)
def test_get_figure_invalid_2():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/-1/"
    py.sign_in(un, ak)
    print("not getting: https://plot.ly/~PlotlyImageTest/-1/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@raises(exceptions.PlotlyError)
def test_get_figure_does_not_exist():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/1000000000/"
    py.sign_in(un, ak)
    print("not getting: https://plot.ly/~PlotlyImageTest/1000000000/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


def test_get_figure_raw():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    file_id = 2
    py.sign_in(un, ak)
    print("getting: https://plot.ly/~{0}/{1}/".format(un, file_id))
    print("###########################################\n\n")
    fig = py.get_figure('PlotlyImageTest', str(file_id), raw=True)


def test_all():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    run_test = False
    end_file = 2
    polar_plots = [], #[6, 7, 8]
    skip = list(range(0))
    if run_test:
        py.sign_in(un, ak)
        file_id = 0
        while True:
            fig, fig_raw = None, None
            while (file_id in polar_plots) or (file_id in skip):
                print("    skipping: https://plot.ly/~{0}/{1}".format(
                    un, file_id))
                file_id += 1
            print("\n")
            try:
                print("testing: https://plot.ly/~{0}/{1}".format(un, file_id))
                print("###########################################\n\n")
                fig = py.get_figure('PlotlyImageTest', str(file_id))
                fig_raw = py.get_figure('PlotlyImageTest',
                                        str(file_id),
                                        raw=True)
            except exceptions.PlotlyError:
                pass
            if (fig is None) and (fig_raw is None):
                print("    couldn't find: https://plot.ly/{0}/{1}".format(
                    un, file_id))
            else:
                compare_with_raw(fig, fig_raw, parents=['figure'])
            file_id += 1
            if file_id > end_file:
                break
        raise exceptions.PlotlyError("This error was generated so that the "
                                     "following output is produced...")


class TestBytesVStrings(TestCase):

    @skipIf(not six.PY3, 'Decoding and missing escapes is only seen in PY3')
    def test_proper_escaping(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/91/"
        py.sign_in(un, ak)
        print("getting: https://plot.ly/~PlotlyImageTest/91/")
        print("###########################################\n\n")
        fig = py.get_figure(url)
