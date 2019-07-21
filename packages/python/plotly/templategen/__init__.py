from plotly.utils import PlotlyJSONEncoder
import json
import os
from templategen.definitions import builders

here = os.path.dirname(os.path.abspath(__file__))
package_dir = os.path.dirname(here)
if __name__ == "__main__":

    for template_name in builders:
        template = builders[template_name]()

        with open(
            os.path.join(
                package_dir,
                "plotly",
                "package_data",
                "templates",
                "%s.json" % template_name,
            ),
            "w",
        ) as f:
            plotly_schema = json.dump(template, f, cls=PlotlyJSONEncoder)
