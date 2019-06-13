from plotly.utils import PlotlyJSONEncoder
import json
from templategen.definitions import builders

if __name__ == '__main__':

    for template_name in builders:
        template = builders[template_name]()

        with open('plotly/package_data/templates/%s.json' % template_name,
                  'w') as f:
            plotly_schema = json.dump(template, f, cls=PlotlyJSONEncoder)
