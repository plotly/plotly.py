"""
dashboard_objs
==========

A module for creating and manipulating spectacle-presentation dashboards.
```
"""

import pprint

from plotly import exceptions, optional_imports

IPython = optional_imports.get_module('IPython')

paragraph_styles = {u'Body': {u'color': u'#3d3d3d',
                              u'fontFamily': u'Open Sans',
                              u'fontSize': 11,
                              u'fontStyle': u'normal',
                              u'fontWeight': 400,
                              u'lineHeight': u'normal',
                              u'minWidth': 20,
                              u'opacity': 1,
                              u'textAlign': u'center',
                              u'textDecoration': u'none'},
                    u'Body Small': {u'color': u'#3d3d3d',
                                    u'fontFamily': u'Open Sans',
                                    u'fontSize': 10,
                                    u'fontStyle': u'normal',
                                    u'fontWeight': 400,
                                    u'lineHeight': u'normal',
                                    u'minWidth': 20,
                                    u'opacity': 1,
                                    u'textAlign': u'center',
                                    u'textDecoration': u'none'},
                    u'Caption': {u'color': u'#3d3d3d',
                                 u'fontFamily': u'Open Sans',
                                 u'fontSize': 11,
                                 u'fontStyle': u'italic',
                                 u'fontWeight': 400,
                                 u'lineHeight': u'normal',
                                 u'minWidth': 20,
                                 u'opacity': 1,
                                 u'textAlign': u'center',
                                 u'textDecoration': u'none'},
                    u'Heading 1': {u'color': u'#3d3d3d',
                                   u'fontFamily': u'Open Sans',
                                   u'fontSize': 26,
                                   u'fontStyle': u'normal',
                                   u'fontWeight': 400,
                                   u'lineHeight': u'normal',
                                   u'minWidth': 20,
                                   u'opacity': 1,
                                   u'textAlign': u'center',
                                   u'textDecoration': u'none'},
                 u'Heading 2': {u'color': u'#3d3d3d',
                                u'fontFamily': u'Open Sans',
                                u'fontSize': 20,
                                u'fontStyle': u'normal',
                                u'fontWeight': 400,
                                u'lineHeight': u'normal',
                                u'minWidth': 20,
                                u'opacity': 1,
                                u'textAlign': u'center',
                                u'textDecoration': u'none'},
                 u'Heading 3': {u'color': u'#3d3d3d',
                                u'fontFamily': u'Open Sans',
                                u'fontSize': 11,
                                u'fontStyle': u'normal',
                                u'fontWeight': 700,
                                u'lineHeight': u'normal',
                                u'minWidth': 20,
                                u'opacity': 1,
                                u'textAlign': u'center',
                                u'textDecoration': u'none'}}

def _slide_template(id, transition):
    slide_temp = {'children': [],
                  'id': id,
                  'props': {'style': {}, 'transition': transition}}

pres_template = {
    'presentation': {
        'slide': [],
        'slidePreviews': [None for _ in range(496)],
        'version': '0.1.3',
        'paragraphStyles': paragraph_styles
    }
}
