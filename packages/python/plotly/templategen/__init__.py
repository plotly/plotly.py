from plotly.io.json import to_json_plotly
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
            f.write(to_json_plotly(template))
