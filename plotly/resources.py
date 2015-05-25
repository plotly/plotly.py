"""
This module defines where non-python source files are located.

All paths are relative to sys.prefix. This is why they are in a plotly-specific
'plotly-data' directory.

"""
import os

# This is relative to `sys.prefix`. We store non-python files here.
DATA_DIR = 'plotly-data'

# For graph object definitions and local error handling
GRAPH_REFERENCE_DIR = os.path.join(DATA_DIR, 'graph_reference')
GRAPH_REFERENCE_GRAPH_OBJS_META = 'plotly/graph_reference/graph_objs_meta.json'
GRAPH_REFERENCE_KEY_TO_NAME = 'plotly/graph_reference/KEY_TO_NAME.json'
GRAPH_REFERENCE_NAME_TO_KEY = 'plotly/graph_reference/NAME_TO_KEY.json'
GRAPH_REFERENCE_OBJ_MAP = 'plotly/graph_reference/OBJ_MAP.json'
GRAPH_REFERENCE_FILES = [GRAPH_REFERENCE_GRAPH_OBJS_META,
                         GRAPH_REFERENCE_KEY_TO_NAME,
                         GRAPH_REFERENCE_NAME_TO_KEY,
                         GRAPH_REFERENCE_OBJ_MAP]

# For IPython widget support
WIDGETS_DIR = os.path.join(DATA_DIR, 'widgets')
WIDGETS_MAIN_JS = 'plotly/widgets/graphWidget.js'
WIDGETS_FILES = [WIDGETS_MAIN_JS]
