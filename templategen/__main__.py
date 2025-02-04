from plotly.io.json import to_json_plotly
import os
from templategen.definitions import builders

for template_name in builders:
    template = builders[template_name]()

    with open(
        os.path.join(
            "plotly",
            "package_data",
            "templates",
            "%s.json" % template_name,
        ),
        "w",
    ) as f:
        f.write(to_json_plotly(template))
