# Trigger the import of the plotly submodules that should be loaded
# before the rest of the chart_studio package.
#
# This avoids circular import problems during the deprecation phase where
# plotly modules will import the corresponding chart_studio modules in order
# to present backward compatible entry points
import plotly.tools as _tool
import plotly.utils as _utils
import plotly.files as _files