"""
dashboard_objs
==========

A module for creating and manipulating spectacle-presentation dashboards.
```
"""

import pprint

from plotly import exceptions, optional_imports
from plotly.utils import node_generator

IPython = optional_imports.get_module('IPython')

pres_template = {
    'presentation': {
        'slide': [],
        'slidePreviews': [None for _ in range(496)],
        'version': '0.1.3',
        'paragraphStyles': paragraph_styles
    }
}
