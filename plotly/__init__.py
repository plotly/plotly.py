import json
import warnings
from . version import __version__
import graph_objs
import plotly
import tools
import utils

from pkg_resources import resource_string


def _check_for_requirements():
    s = resource_string('plotly', 'requirements.json').decode('utf-8')

    reqs = json.loads(s)

    for req, version in reqs['core'].items():
        try:
            exec "import {}".format(req)
        except ImportError:
            warnings.warn(
                "{} is a core requirement, you'll have to install it "
                "on your machine before being able to use the plotly "
                "package.".format(req))
        else:
            our_version = version.split('.')
            exec "your_version = {}.__version__.split('.')".format(req)
            for ours, yours in zip(our_version, your_version):
                if int(ours) > int(yours):
                    warnings.warn(
                        "The core requirement, '{}', is on your "
                        "machine, but it may be out of date. If you run "
                        "into problems related to this package, "
                        "you should try updating to the version we test "
                        "with: '{}'. Your version: '{}'."
                        "".format(req, version, ".".join(your_version)))

    for req, version in reqs['optional'].items():
        try:
            exec "import {}".format(req)
        except ImportError:
            pass
        else:
            our_version = version.split('.')
            exec "your_version = {}.__version__.split('.')".format(req)
            for ours, yours in zip(our_version, your_version):
                if int(ours) > int(yours):
                    warnings.warn(
                        "The optional requirement, '{}', is on your "
                        "machine, but it may be out of date. If you run "
                        "into problems related to this package, "
                        "you should try updating to the version we test "
                        "with: '{}'. Your version: '{}'."
                        "".format(req, version, ".".join(your_version)))

_check_for_requirements()
