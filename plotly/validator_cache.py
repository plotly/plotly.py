from _plotly_utils.basevalidators import LiteralValidator
from plotly.validators._data import DataValidator
import _plotly_utils.basevalidators as basevalidators
import json
import os.path as opath

DERIVED_CLASSES = {
    "DataValidator": "data",
    "LayoutValidator": "layout",
}

class ValidatorCache(object):
    _cache = {}
    _json_cache = None

    @staticmethod
    def get_validator(parent_path, prop_name):
        if ValidatorCache._json_cache is None:
            # Load the JSON validator params from the file
            validator_json_path = opath.join(
                opath.dirname(__file__), "validators", "_validators.json"
            )
            if not opath.exists(validator_json_path):
                raise FileNotFoundError(
                    f"Validator JSON file not found: {validator_json_path}"
                )
            with open(validator_json_path, "r") as f:
                ValidatorCache._json_cache = json.load(f)

        key = (parent_path, prop_name)
        if key not in ValidatorCache._cache:

            if "." not in parent_path and prop_name == "type":
                # Special case for .type property of traces
                validator = LiteralValidator("type", parent_path, parent_path)
            elif parent_path == "" and prop_name == "data":
                # Special case for .data property of Figure
                validator = DataValidator
            else:
                lookup_name = None
                if parent_path == "layout":
                    from .graph_objects import Layout

                    match = Layout._subplotid_prop_re.match(prop_name)
                    if match:
                        lookup_name = match.group(1)

                lookup_name = lookup_name or prop_name
                lookup = f"{parent_path}.{lookup_name}" if parent_path else lookup_name
                validator_item = ValidatorCache._json_cache.get(lookup)
                validator_classname = validator_item["superclass"]
                if validator_classname in DERIVED_CLASSES:
                    # If the superclass is a derived class, we need to get the base class
                    # and pass the derived class name as a parameter
                    base_item = ValidatorCache._json_cache.get(
                        DERIVED_CLASSES[validator_classname]
                    )
                    validator_args = base_item["params"]
                    validator_args.update(validator_item["params"])
                    validator_classname = base_item["superclass"]
                else:
                    validator_args = validator_item["params"]

                validator_class = getattr(basevalidators, validator_classname)

                print("validator_item", key, validator_item)
                validator = validator_class(**validator_args)
            ValidatorCache._cache[key] = validator

        return ValidatorCache._cache[key]

def generate_validator(params: dict, superclass_name: str):
    superclass = getattr(basevalidators, superclass_name)
    return superclass(**params)
