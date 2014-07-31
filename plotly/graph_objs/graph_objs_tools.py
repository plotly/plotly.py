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

OBJ_MAP = dict(
    PlotlyList=dict(
        base_name='list', info_key='plotlylist'),
    PlotlyDict=dict(
        base_name='dict', info_key='plotlydict'),
    PlotlyTrace=dict(
        base_name='PlotlyDict', info_key='plotlytrace'),
    Trace=dict(
        base_name='PlotlyTrace', info_key='trace'),
    Data=dict(
        base_name='PlotlyList', info_key='data'),
    Annotations=dict(
        base_name='PlotlyList', info_key='annotations'),
    AngularAxis=dict(
        base_name='PlotlyDict', info_key='angularaxis'),
    Annotation=dict(
        base_name='PlotlyDict', info_key='annotation'),
    ColorBar=dict(
        base_name='PlotlyDict', info_key='colorbar'),
    Contours=dict(
        base_name='PlotlyDict', info_key='contours'),
    ErrorX=dict(
        base_name='PlotlyDict', info_key='error_x'),
    ErrorY=dict(
        base_name='PlotlyDict', info_key='error_y'),
    Figure=dict(
        base_name='PlotlyDict', info_key='figure'),
    Font=dict(
        base_name='PlotlyDict', info_key='font'),
    # TitleFont=dict(
    #     base_name='PlotlyDict', info_key='titlefont'),
    # TextFont=dict(
    #     base_name='PlotlyDict', info_key='textfont'),
    Layout=dict(
        base_name='PlotlyDict', info_key='layout'),
    Legend=dict(
        base_name='PlotlyDict', info_key='legend'),
    Line=dict(
        base_name='PlotlyDict', info_key='line'),
    Margin=dict(
        base_name='PlotlyDict', info_key='margin'),
    Marker=dict(
        base_name='PlotlyDict', info_key='marker'),
    RadialAxis=dict(
        base_name='PlotlyDict', info_key='radialaxis'),
    Stream=dict(
        base_name='PlotlyDict', info_key='stream'),
    XAxis=dict(
        base_name='PlotlyDict', info_key='xaxis'),
    XBins=dict(
        base_name='PlotlyDict', info_key='xbins'),
    YAxis=dict(
        base_name='PlotlyDict', info_key='yaxis'),
    YBins=dict(
        base_name='PlotlyDict', info_key='ybins'),
    Area=dict(
        base_name='PlotlyTrace', info_key='area'),
    Bar=dict(
        base_name='PlotlyTrace', info_key='bar'),
    Box=dict(
        base_name='PlotlyTrace', info_key='box'),
    Contour=dict(
        base_name='PlotlyTrace', info_key='contour'),
    Heatmap=dict(
        base_name='PlotlyTrace', info_key='heatmap'),
    Histogram=dict(
        base_name='PlotlyTrace', info_key='histogram'),
    Histogram2d=dict(
        base_name='PlotlyTrace', info_key='histogram2d'),
    Histogram2dContour=dict(
        base_name='PlotlyTrace', info_key='histogram2dcontour'),
    Scatter=dict(
        base_name='PlotlyTrace', info_key='scatter')
)

NAME_TO_KEY = dict()
for _name, _obj_dict in OBJ_MAP.items():
    NAME_TO_KEY[_name] = _obj_dict['info_key']

KEY_TO_NAME = dict()
for _name, _key in NAME_TO_KEY.items():
    KEY_TO_NAME[_key] = _name
KEY_TO_NAME['textfont'] = 'Font'
KEY_TO_NAME['titlefont'] = 'Font'
KEY_TO_NAME['tickfont'] = 'Font'


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
                    val_types = ("{0} object | ".format(KEY_TO_NAME[key]) +
                                 val_types)
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
