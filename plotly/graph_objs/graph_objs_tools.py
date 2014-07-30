from __future__ import absolute_import
from plotly import utils
import textwrap
import sys
if sys.version[:3] == '2.6':
    from ordereddict import OrderedDict
    import simplejson as json
else:
    from collections import OrderedDict
    import json


from pkg_resources import resource_string
s = resource_string('plotly',
                    'graph_reference/graph_objs_meta.json').decode('utf-8')
INFO = json.loads(s, object_pairs_hook=OrderedDict)

INFO = utils.decode_unicode(INFO)


# define how to map from keys in INFO to a class
# mapping: (n->m, m < n)
KEY_TO_NAME = dict(
    plotlylist='PlotlyList',
    data='Data',
    angularaxis='AngularAxis',
    annotations='Annotations',
    area='Area',
    plotlydict='PlotlyDict',
    plotlytrace='PlotlyTrace',
    bar='Bar',
    box='Box',
    contour='Contour',
    heatmap='Heatmap',
    histogram='Histogram',
    histogram2d='Histogram2d',
    histogram2dcontour='Histogram2dContour',
    scatter='Scatter',
    annotation='Annotation',
    colorbar='ColorBar',
    contours='Contours',
    error_x='ErrorX',
    error_y='ErrorY',
    figure='Figure',
    font='Font',
    layout='Layout',
    legend='Legend',
    line='Line',
    margin='Margin',
    marker='Marker',
    radialaxis='RadialAxis',
    stream='Stream',
    trace='Trace',
    textfont='Font',
    tickfont='Font',
    titlefont='Font',
    xaxis='XAxis',
    xbins='XBins',
    yaxis='YAxis',
    ybins='YBins'
)

# define how to map from a class name to a key name in INFO
# mapping: (n->n)
NAME_TO_KEY = dict(
    PlotlyList='plotlylist',
    Data='data',
    AngularAxis='angularaxis',
    Annotations='annotations',
    PlotlyDict='plotlydict',
    PlotlyTrace='plotlytrace',
    Area='area',
    Bar='bar',
    Box='box',
    Contour='contour',
    Heatmap='heatmap',
    Histogram='histogram',
    Histogram2d='histogram2d',
    Histogram2dContour='histogram2dcontour',
    Scatter='scatter',
    Annotation='annotation',
    ColorBar='colorbar',
    Contours='contours',
    ErrorX='error_x',
    ErrorY='error_y',
    Figure='figure',
    Font='font',
    Layout='layout',
    Legend='legend',
    Line='line',
    Margin='margin',
    Marker='marker',
    RadialAxis='radialaxis',
    Stream='stream',
    Trace='trace',
    XAxis='xaxis',
    XBins='xbins',
    YAxis='yaxis',
    YBins='ybins'
)

# define how to map from a class name to a base class name
# mapping: (n->3)
NAME_TO_BASE = dict(
    Data='PlotlyList',
    Annotations='PlotlyList',
    AngularAxis='PlotlyDict',
    Annotation='PlotlyDict',
    ColorBar='PlotlyDict',
    Contours='PlotlyDict',
    ErrorX='PlotlyDict',
    ErrorY='PlotlyDict',
    Figure='PlotlyDict',
    Font='PlotlyDict',
    Layout='PlotlyDict',
    Legend='PlotlyDict',
    Line='PlotlyDict',
    Margin='PlotlyDict',
    Marker='PlotlyDict',
    RadialAxis='PlotlyDict',
    Stream='PlotlyDict',
    XAxis='PlotlyDict',
    XBins='PlotlyDict',
    YAxis='PlotlyDict',
    YBins='PlotlyDict',
    Area='PlotlyTrace',
    Bar='PlotlyTrace',
    Box='PlotlyTrace',
    Contour='PlotlyTrace',
    Heatmap='PlotlyTrace',
    Histogram='PlotlyTrace',
    Histogram2d='PlotlyTrace',
    Histogram2dContour='PlotlyTrace',
    Scatter='PlotlyTrace'
)


def update_keys(keys):
    """Change keys we used to support to their new equivalent."""
    updated_keys = list()
    for key in keys:
        if key in translations:
            updated_keys += [translations[key]]
        else:
            updated_keys += [key]
    return updated_keys

translations = dict(
    scl="colorscale",
    reversescl="reversescale"
)

def make_list_doc(name):
    doc = ("A list-like object representing a {0} object in a "
           "figure.\n\n".format(name))  # initial doc here?
    tab_size = 4
    min_indent = min([len(a) - len(b)
                      for a, b in zip(doc.splitlines(),
                                      [l.lstrip()
                                       for l in doc.splitlines()])])
    doc = "".join([line[min_indent:] + '\n' for line in doc.splitlines()])
    # Add section header for method list...
    doc += "Quick method reference:\n\n"
    doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
        ["update(changes)", "strip_style()", "get_data()",
         "to_graph_objs()", "validate()", "to_string()",
         "force_clean()"]) + "\n\n"
    return doc.expandtabs(tab_size)


def make_dict_doc(name):
    # remove min indentation...
    doc = ("A dictionary-like object representing a {0} object in a "
           "figure.\n\n".format(name))  # initial doc here?
    obj_info = INFO[NAME_TO_KEY[name]]
    line_size = 76
    tab_size = 4
    min_indent = min([len(a) - len(b)
                      for a, b in zip(doc.splitlines(),
                                      [l.lstrip()
                                       for l in doc.splitlines()])])
    doc = "".join([line[min_indent:] + '\n' for line in doc.splitlines()])
    # Add section header for method list...
    doc += "Quick method reference:\n\n"
    doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
        ["update(changes)", "strip_style()", "get_data()",
         "to_graph_objs()", "validate()", "to_string()",
         "force_clean()"]) + "\n\n"
    # Add section header
    if len(obj_info):
        doc += "Valid keys:\n\n"
        # Add each key one-by-one and format
        width1 = line_size-tab_size
        width2 = line_size-2*tab_size
        width3 = line_size-3*tab_size
        undocumented = "Aw, snap! Undocumented!"
        for key in obj_info:
            # main portion of documentation
            try:
                required = str(obj_info[key]['required'])
            except KeyError:
                required = undocumented

            try:
                typ = str(obj_info[key]['type'])
            except KeyError:
                typ = undocumented

            try:
                val_types = str(obj_info[key]['val_types'])
                if typ == 'object':
                    val_types = "{0} object | ".format(KEY_TO_NAME[key])+\
                                val_types
            except KeyError:
                val_types = undocumented
            try:
                descr = str(obj_info[key]['description'])
            except KeyError:
                descr = undocumented
            str_1 = "{0} [required={1}] (value={2})".format(
                key, required, val_types)
            if "streamable" in obj_info[key] and obj_info[key]["streamable"]:
                str_1 += " (streamable)"
            str_1 += ":\n"
            str_1 = "\t" + "\n\t".join(textwrap.wrap(str_1,
                                                     width=width1)) + "\n"
            str_2 = "\t\t" + "\n\t\t".join(textwrap.wrap(descr,
                                           width=width2)) + "\n"
            doc += str_1 + str_2
            # if a user can run help on this value, tell them!
            if typ == "object":
                doc += "\n\t\tFor more, run `help(plotly.graph_objs.{0" \
                       "})`\n".format(KEY_TO_NAME[key])
            # if example usage exists, tell them!
            if 'examples' in obj_info[key]:
                ex = "\n\t\tExamples:\n" + "\t\t\t"
                ex += "\n\t\t\t".join(
                    textwrap.wrap(str(obj_info[key]['examples']),
                                  width=width3)) + "\n"
                doc += ex
            if 'code' in obj_info[key]:
                code = "\n\t\tCode snippet:"
                code += "\n\t\t\t>>>".join(
                    str(obj_info[key]['code']).split('>>>')) + "\n"
                doc += code
            doc += '\n'
    return doc.expandtabs(tab_size)


def make_trace_doc(name):
    # remove min indentation...
    doc = ("A dictionary-like object representing a {0} object in a "
           "figure.\n\n".format(name))  # initial doc here?
    obj_info = INFO[NAME_TO_KEY[name]]
    line_size = 76
    tab_size = 4
    min_indent = min([len(a) - len(b)
                      for a, b in zip(doc.splitlines(),
                                      [l.lstrip()
                                       for l in doc.splitlines()])])
    doc = "".join([line[min_indent:] + '\n' for line in doc.splitlines()])
    # Add section header for method list...
    doc += "Quick method reference:\n\n"
    doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
        ["update(changes)", "strip_style()", "get_data()",
         "to_graph_objs()", "validate()", "to_string()",
         "force_clean()"]) + "\n\n"
    # Add section header
    if len(obj_info):
        doc += "Valid keys:\n\n"
        # Add each key one-by-one and format
        width1 = line_size-tab_size
        width2 = line_size-2*tab_size
        width3 = line_size-3*tab_size
        undocumented = "Aw, snap! Undocumented!"
        for key in obj_info:
            # main portion of documentation
            try:
                required = str(obj_info[key]['required'])
            except KeyError:
                required = undocumented

            try:
                typ = str(obj_info[key]['type'])
            except KeyError:
                typ = undocumented

            try:
                val_types = str(obj_info[key]['val_types'])
                if typ == 'object':
                    val_types = "{0} object | ".format(KEY_TO_NAME[key])+\
                                val_types
            except KeyError:
                val_types = undocumented
            try:
                descr = str(obj_info[key]['description'])
            except KeyError:
                descr = undocumented
            str_1 = "{0} [required={1}] (value={2})".format(
                key, required, val_types)
            if "streamable" in obj_info[key] and obj_info[key]["streamable"]:
                str_1 += " (streamable)"
            str_1 += ":\n"
            str_1 = "\t" + "\n\t".join(textwrap.wrap(str_1,
                                                     width=width1)) + "\n"
            str_2 = "\t\t" + "\n\t\t".join(textwrap.wrap(descr,
                                           width=width2)) + "\n"
            doc += str_1 + str_2
            # if a user can run help on this value, tell them!
            if typ == "object":
                doc += "\n\t\tFor more, run `help(plotly.graph_objs.{0" \
                       "})`\n".format(KEY_TO_NAME[key])
            # if example usage exists, tell them!
            if 'examples' in obj_info[key]:
                ex = "\n\t\tExamples:\n" + "\t\t\t"
                ex += "\n\t\t\t".join(
                    textwrap.wrap(str(obj_info[key]['examples']),
                                  width=width3)) + "\n"
                doc += ex
            if 'code' in obj_info[key]:
                code = "\n\t\tCode snippet:"
                code += "\n\t\t\t>>>".join(
                    str(obj_info[key]['code']).split('>>>')) + "\n"
                doc += code
            doc += '\n'
    return doc.expandtabs(tab_size)