"""
utils
=====

Low-level functionality NOT intended for users to EVER use.

"""
from __future__ import absolute_import

import os.path
import re
import threading
import warnings

import json as _json

from _plotly_utils.exceptions import PlotlyError
from _plotly_utils.optional_imports import get_module

# Optional imports, may be None for users that only use our core functionality.
numpy = get_module("numpy")
pandas = get_module("pandas")
sage_all = get_module("sage.all")


### incase people are using threading, we lock file reads
lock = threading.Lock()


http_msg = (
    "The plotly_domain and plotly_api_domain of your config file must start "
    "with 'https', not 'http'. If you are not using On-Premise then run the "
    "following code to ensure your plotly_domain and plotly_api_domain start "
    "with 'https':\n\n\n"
    "import plotly\n"
    "plotly.tools.set_config_file(\n"
    "    plotly_domain='https://plotly.com',\n"
    "    plotly_api_domain='https://api.plotly.com'\n"
    ")\n\n\n"
    "If you are using On-Premise then you will need to use your company's "
    "domain and api_domain urls:\n\n\n"
    "import plotly\n"
    "plotly.tools.set_config_file(\n"
    "    plotly_domain='https://plotly.your-company.com',\n"
    "    plotly_api_domain='https://plotly.your-company.com'\n"
    ")\n\n\n"
    "Make sure to replace `your-company.com` with the URL of your Plotly "
    "On-Premise server.\nSee "
    "https://plotly.com/python/getting-started/#special-instructions-for-plotly-onpremise-users "
    "for more help with getting started with On-Premise."
)


### general file setup tools ###


def load_json_dict(filename, *args):
    """Checks if file exists. Returns {} if something fails."""
    data = {}
    if os.path.exists(filename):
        lock.acquire()
        with open(filename, "r") as f:
            try:
                data = _json.load(f)
                if not isinstance(data, dict):
                    data = {}
            except:
                data = {}  # TODO: issue a warning and bubble it up
        lock.release()
        if args:
            return {key: data[key] for key in args if key in data}
    return data


def save_json_dict(filename, json_dict):
    """Save json to file. Error if path DNE, not a dict, or invalid json."""
    if isinstance(json_dict, dict):
        # this will raise a TypeError if something goes wrong
        json_string = _json.dumps(json_dict, indent=4)
        lock.acquire()
        with open(filename, "w") as f:
            f.write(json_string)
        lock.release()
    else:
        raise TypeError("json_dict was not a dictionary. not saving.")


def ensure_file_exists(filename):
    """Given a valid filename, make sure it exists (will create if DNE)."""
    if not os.path.exists(filename):
        head, tail = os.path.split(filename)
        ensure_dir_exists(head)
        with open(filename, "w") as f:
            pass  # just create the file


def ensure_dir_exists(directory):
    """Given a valid directory path, make sure it exists."""
    if dir:
        if not os.path.isdir(directory):
            os.makedirs(directory)


def get_first_duplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
        else:
            return item
    return None


### source key
def is_source_key(key):
    src_regex = re.compile(r".+src$")
    if src_regex.match(key) is not None:
        return True
    else:
        return False


### validation
def validate_world_readable_and_sharing_settings(option_set):
    if (
        "world_readable" in option_set
        and option_set["world_readable"] is True
        and "sharing" in option_set
        and option_set["sharing"] is not None
        and option_set["sharing"] != "public"
    ):
        raise PlotlyError(
            "Looks like you are setting your plot privacy to both "
            "public and private.\n If you set world_readable as True, "
            "sharing can only be set to 'public'"
        )
    elif (
        "world_readable" in option_set
        and option_set["world_readable"] is False
        and "sharing" in option_set
        and option_set["sharing"] == "public"
    ):
        raise PlotlyError(
            "Looks like you are setting your plot privacy to both "
            "public and private.\n If you set world_readable as "
            "False, sharing can only be set to 'private' or 'secret'"
        )
    elif "sharing" in option_set and option_set["sharing"] not in [
        "public",
        "private",
        "secret",
        None,
    ]:
        raise PlotlyError(
            "The 'sharing' argument only accepts one of the following "
            "strings:\n'public' -- for public plots\n"
            "'private' -- for private plots\n"
            "'secret' -- for private plots that can be shared with a "
            "secret url"
        )


def validate_plotly_domains(option_set):
    domains_not_none = []
    for d in ["plotly_domain", "plotly_api_domain"]:
        if d in option_set and option_set[d]:
            domains_not_none.append(option_set[d])

    if not all(d.lower().startswith("https") for d in domains_not_none):
        warnings.warn(http_msg, category=UserWarning)


def set_sharing_and_world_readable(option_set):
    if "world_readable" in option_set and "sharing" not in option_set:
        option_set["sharing"] = "public" if option_set["world_readable"] else "private"

    elif "sharing" in option_set and "world_readable" not in option_set:
        if option_set["sharing"] == "public":
            option_set["world_readable"] = True
        else:
            option_set["world_readable"] = False
