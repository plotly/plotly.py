from templategen.ggplot2 import generate_ggplot2_template
from plotly.utils import PlotlyJSONEncoder
import json

if __name__ == '__main__':

    # ggplot2
    template = generate_ggplot2_template()
    with open('plotly/package_data/templates/ggplot2.json', 'w') as f:
        plotly_schema = json.dump(template, f, cls=PlotlyJSONEncoder)
