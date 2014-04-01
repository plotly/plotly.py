from mako.template import Template
from mako.runtime import Context

from graph_objs_meta import *

fout = open('graph_objs.py', 'w')

mytemplate = Template(filename='_graph_objs.py')


def add_doc(obj, tabsize=4):
    # add in base_doc, obj_info['doc']
    doc = ""
    for line in INFO[obj]['doc'].splitlines()[:-1]:
        doc += line.lstrip() + '\n'
    doc += INFO[obj]['doc'].splitlines()[-1].lstrip()

    # add a 'Valid keys' list if a valid keys list exists...
    if len(INFO[obj]['valid']) > 0:
        doc += "Valid keys:\n\n"
        for key in INFO[obj]['valid']:
            doc += "\t{} ({}): \n\t\t{}\n".format(key,
                                                  INFO[obj]['types'][key],
                                                  INFO[obj]['descriptors'][key])

    # add leading whitespace for proper docstring formatting
    formatted_doc = ""
    for lino, line in enumerate(doc.splitlines()):
        if lino == 0:
            formatted_doc += line + '\n'
        else:
            formatted_doc += '\t' + line + '\n'
    return formatted_doc.expandtabs(tabsize)

# def add_tab(in_str, tabsize=4):
#     out_str = ""
#     for lino, line in enumerate(in_str.splitlines()):
#         if lino == 0:
#             out_str += line + '\n'
#         else:
#             out_str += '\t' + line + '\n'
#     return out_str.expandtabs(tabsize)
#
#
# def add_base(base_doc):
#     out_str = ""
#     for line in base_doc.splitlines()[:-1]:
#         out_str += line.lstrip() + '\n'
#     out_str += base_doc.splitlines()[-1].lstrip()
#     return out_str
#
#
# def add_valid_keys(info, tabsize=4):
#     string = "Valid keys:\n\n"
#     for key in info['valid']:
#         string += "\t{} ({}): \n\t\t{}\n".format(key, info['types'][key],
#                                                  info['descriptions'][key])
#     return string.expandtabs(tabsize)

# docs = dict(
#     plotly_dict="""A base class for all objects that style a figure in plotly.
#
#     A PlotlyDict can be instantiated like any dict object. This class offers
#     some useful recursive methods that can be used by higher-level subclasses
#     and containers so long as all plot objects are instantiated as a subclass
#     of PlotlyDict. Each PlotlyDict should be instantiated with a `kind`
#     keyword argument. This defines the special _info dictionary for the
#     object.
#
#     Any available methods that hold for a dict hold for a PlotlyDict.
#     """,
#
    # plotly_list="""A container for PlotlyDicts, inherits from standard list.
    #
    # Plotly uses lists and dicts as collections to hold information about a
    # figure. This container is simply a list that understands some plotly
    # language and apes the methods in a PlotlyDict, passing them on to its
    # constituents.
    #
    # It can be initialized like any other list so long as the entries are all
    # PlotlyDict objects or subclasses thereof.
    #
    # Any available methods that hold for a list object hold for a PlotlyList.
    # """,
#
#
#
#     data="""A general data class for plotly.
#
#     This class is meant to hold any type of allowable plotly data.
#
#          """,
#
# )

ctx = Context(fout, add_doc=add_doc)

mytemplate.render_context(ctx)
fout.close()
