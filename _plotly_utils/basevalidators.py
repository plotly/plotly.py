import base64
import numbers
import textwrap
import uuid
from importlib import import_module

import io
from copy import deepcopy

import re

# Optional imports
# ----------------
import sys
from six import string_types

np = None
pd = None

try:
    np = import_module('numpy')

    try:
        pd = import_module('pandas')
    except ImportError:
        pass

except ImportError:
    pass


# back-port of fullmatch from Py3.4+
def fullmatch(regex, string, flags=0):
    """Emulate python-3.4 re.fullmatch()."""
    if 'pattern' in dir(regex):
        regex_string = regex.pattern
    else:
        regex_string = regex
    return re.match("(?:" + regex_string + r")\Z", string, flags=flags)


# Utility functions
# -----------------
def to_scalar_or_list(v):
    if isinstance(v, (list, tuple)):
        return [to_scalar_or_list(e) for e in v]
    elif np and isinstance(v, np.ndarray):
        return [to_scalar_or_list(e) for e in v]
    elif pd and isinstance(v, (pd.Series, pd.Index)):
        return [to_scalar_or_list(e) for e in v]
    else:
        return v


def copy_to_readonly_numpy_array(v, dtype=None, force_numeric=False):
    """
    Convert an array-like value into a read-only numpy array

    Parameters
    ----------
    v : array like
        Array like value (list, tuple, numpy array, pandas series, etc.)
    dtype : str
        If specified, the numpy dtype that the array should be forced to
        have. If not specified then let numpy infer the datatype
    force_numeric : bool
        If true, raise an exception if the resulting numpy array does not
        have a numeric dtype (i.e. dtype.kind not in ['u', 'i', 'f'])
    Returns
    -------
    np.ndarray
        Numpy array with the 'WRITEABLE' flag set to False
    """

    assert np is not None

    # Copy to numpy array and handle dtype param
    # ------------------------------------------
    # If dtype was not specified then it will be passed to the numpy array
    # constructor as None and the data type will be inferred automatically

    # TODO: support datetime dtype here and in widget serialization
    # u: unsigned int, i: signed int, f: float
    numeric_kinds = ['u', 'i', 'f']

    # Unwrap data types that have a `values` property that might be a numpy
    # array. If this values property is a numeric numpy array then we
    # can take the fast path below
    if pd and isinstance(v, (pd.Series, pd.Index)):
        v = v.values

    if not isinstance(v, np.ndarray):
        v_list = [to_scalar_or_list(e) for e in v]
        new_v = np.array(v_list, order='C', dtype=dtype)
    elif v.dtype.kind in numeric_kinds:
        if dtype:
            new_v = np.ascontiguousarray(v.astype(dtype))
        else:
            new_v = np.ascontiguousarray(v.copy())
    else:
        new_v = v.copy()

    # Handle force numeric param
    # --------------------------
    if force_numeric and new_v.dtype.kind not in numeric_kinds:
        raise ValueError('Input value is not numeric and'
                         'force_numeric parameter set to True')

    if dtype != 'unicode':
        # Force non-numeric arrays to have object type
        # --------------------------------------------
        # Here we make sure that non-numeric arrays have the object
        # datatype. This works around cases like np.array([1, 2, '3']) where
        # numpy converts the integers to strings and returns array of dtype
        # '<U21'
        if new_v.dtype.kind not in ['u', 'i', 'f', 'O']:
            new_v = np.array(v, dtype='object')

    # Convert int64 arrays to int32
    # -----------------------------
    # JavaScript doesn't support int64 typed arrays
    if new_v.dtype == 'int64':
        new_v = new_v.astype('int32')

    # Set new array to be read-only
    # -----------------------------
    new_v.flags['WRITEABLE'] = False

    return new_v


def is_homogeneous_array(v):
    """
    Return whether a value is considered to be a homogeneous array
    """
    return ((np and isinstance(v, np.ndarray)) or
            (pd and isinstance(v, (pd.Series, pd.Index))))


def is_simple_array(v):
    """
    Return whether a value is considered to be an simple array
    """
    return isinstance(v, (list, tuple))


def is_array(v):
    """
    Return whether a value is considered to be an array
    """
    return is_simple_array(v) or is_homogeneous_array(v)


def type_str(v):
    """
    Return a type string of the form module.name for the input value v
    """
    if not isinstance(v, type):
        v = type(v)

    return "'{module}.{name}'".format(module=v.__module__, name=v.__name__)


# Validators
# ----------
class BaseValidator(object):
    """
    Base class for all validator classes
    """

    def __init__(self, plotly_name, parent_name, role=None, **_):
        """
        Construct a validator instance

        Parameters
        ----------
        plotly_name : str
            Name of the property being validated
        parent_name : str
            Names of all of the ancestors of this property joined on '.'
            characters. e.g.
            plotly_name == 'range' and parent_name == 'layout.xaxis'
        role : str
            The role string for the property as specified in
            plot-schema.json
        """
        self.parent_name = parent_name
        self.plotly_name = plotly_name
        self.role = role

    def description(self):
        """
        Returns a string that describes the values that are acceptable
        to the validator

        Should start with:
            The '{plotly_name}' property is a...

        For consistancy, string should have leading 4-space indent
        """
        raise NotImplementedError()

    def raise_invalid_val(self, v):
        """
        Helper method to raise an informative exception when an invalid
        value is passed to the validate_coerce method.

        Parameters
        ----------
        v :
            Value that was input to validate_coerce and could not be coerced
        Raises
        -------
        ValueError
        """
        raise ValueError("""
    Invalid value of type {typ} received for the '{name}' property of {pname}
        Received value: {v}

{valid_clr_desc}""".format(
            name=self.plotly_name,
            pname=self.parent_name,
            typ=type_str(v),
            v=repr(v),
            valid_clr_desc=self.description()))

    def raise_invalid_elements(self, invalid_els):
        if invalid_els:
            raise ValueError("""
    Invalid element(s) received for the '{name}' property of {pname}
        Invalid elements include: {invalid}

{valid_clr_desc}""".format(
                name=self.plotly_name,
                pname=self.parent_name,
                invalid=invalid_els[:10],
                valid_clr_desc=self.description()))

    def validate_coerce(self, v):
        """
        Validate whether an input value is compatible with this property,
        and coerce the value to be compatible of possible.

        Parameters
        ----------
        v
            The input value to be validated

        Raises
        ------
        ValueError
            if `v` cannot be coerced into a compatible form

        Returns
        -------
        The input `v` in a form that's compatible with this property
        """
        raise NotImplementedError()

    def present(self, v):
        """
        Convert output value of a previous call to `validate_coerce` into a
        form suitable to be returned to the user on upon property
        access.

        Note: The value returned by present must be either immutable or an
        instance of BasePlotlyType, otherwise the value could be mutated by
        the user and we wouldn't get notified about the change.

        Parameters
        ----------
        v
            A value that was the ouput of a previous call the
            `validate_coerce` method on the same object

        Returns
        -------

        """
        if is_homogeneous_array(v):
            # Note: numpy array was already coerced into read-only form so
            # we don't need to copy it here.
            return v
        elif is_simple_array(v):
            return tuple(v)
        else:
            return v


class DataArrayValidator(BaseValidator):
    """
        "data_array": {
            "description": "An {array} of data. The value MUST be an
                            {array}, or we ignore it.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt"
            ]
        },
    """

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(DataArrayValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):
        return ("""\
    The '{plotly_name}' property is an array that may be specified as a tuple,
    list, numpy array, or pandas Series"""
                .format(plotly_name=self.plotly_name))

    def validate_coerce(self, v):

        if v is None:
            # Pass None through
            pass
        elif is_homogeneous_array(v):
            v = copy_to_readonly_numpy_array(v)
        elif is_simple_array(v):
            v = to_scalar_or_list(v)
        else:
            self.raise_invalid_val(v)
        return v


class EnumeratedValidator(BaseValidator):
    """
        "enumerated": {
            "description": "Enumerated value type. The available values are
                            listed in `values`.",
            "requiredOpts": [
                "values"
            ],
            "otherOpts": [
                "dflt",
                "coerceNumber",
                "arrayOk"
            ]
        },
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 values,
                 array_ok=False,
                 coerce_number=False,
                 **kwargs):
        super(EnumeratedValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        # Save params
        # -----------
        self.values = values
        self.array_ok = array_ok
        # coerce_number is rarely used and not implemented
        self.coerce_number = coerce_number

        # Handle regular expressions
        # --------------------------
        # Compiled regexs
        self.val_regexs = []

        # regex replacements that run before the matching regex
        # So far, this is only used to cast 'x1' -> 'x' for anchor-style
        # enumeration properties
        self.regex_replacements = []

        # Loop over enumeration values
        # ----------------------------
        # Look for regular expressions
        for v in self.values:
            if v and isinstance(v, string_types) and v[0] == '/' and v[-1] == '/':
                # String is a regex with leading and trailing '/' character
                regex_str = v[1:-1]
                self.val_regexs.append(re.compile(regex_str))
                self.regex_replacements.append(
                    EnumeratedValidator.build_regex_replacement(regex_str))
            else:
                self.val_regexs.append(None)
                self.regex_replacements.append(None)

    @staticmethod
    def build_regex_replacement(regex_str):
        # Example: regex_str == r"^y([2-9]|[1-9][0-9]+)?$"
        #
        # When we see a regular expression like the one above, we want to
        # build regular expression replacement params that will remove a
        # suffix of 1 from the input string ('y1' -> 'y' in this example)
        #
        # Why?: Regular expressions like this one are used in enumeration
        # properties that refer to subplotids (e.g. layout.annotation.xref)
        # The regular expressions forbid suffixes of 1, like 'x1'. But we
        # want to accept 'x1' and coerce it into 'x'
        #
        # To be cautious, we only perform this conversion for enumerated
        # values that match the anchor-style regex
        match = re.match(r"\^(\w)\(\[2\-9\]\|\[1\-9\]\[0\-9\]\+\)\?\$",
                         regex_str)

        if match:
            anchor_char = match.group(1)
            return '^' + anchor_char + '1$', anchor_char
        else:
            return None

    def perform_replacemenet(self, v):
        """
        Return v with any applicable regex replacements applied
        """
        if isinstance(v, string_types):
            for repl_args in self.regex_replacements:
                if repl_args:
                    v = re.sub(repl_args[0], repl_args[1], v)

        return v

    def description(self):

        # Separate regular values from regular expressions
        enum_vals = []
        enum_regexs = []
        for v, regex in zip(self.values, self.val_regexs):
            if regex is not None:
                enum_regexs.append(regex.pattern)
            else:
                enum_vals.append(v)
        desc = ("""\
    The '{name}' property is an enumeration that may be specified as:"""
                .format(name=self.plotly_name))

        if enum_vals:
            enum_vals_str = '\n'.join(
                textwrap.wrap(
                    repr(enum_vals),
                    initial_indent=' ' * 12,
                    subsequent_indent=' ' * 12,
                    break_on_hyphens=False))

            desc = desc + """
      - One of the following enumeration values:
{enum_vals_str}""".format(enum_vals_str=enum_vals_str)

        if enum_regexs:
            enum_regexs_str = '\n'.join(
                textwrap.wrap(
                    repr(enum_regexs),
                    initial_indent=' ' * 12,
                    subsequent_indent=' ' * 12,
                    break_on_hyphens=False))

            desc = desc + """
      - A string that matches one of the following regular expressions:
{enum_regexs_str}""".format(enum_regexs_str=enum_regexs_str)

        if self.array_ok:
            desc = desc + """
      - A tuple, list, or one-dimensional numpy array of the above"""

        return desc

    def in_values(self, e):
        """
        Return whether a value matches one of the enumeration options
        """
        is_str = isinstance(e, string_types)
        for v, regex in zip(self.values, self.val_regexs):
            if is_str and regex:
                in_values = fullmatch(regex, e) is not None
                #in_values = regex.fullmatch(e) is not None
            else:
                in_values = e == v

            if in_values:
                return True

        return False

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_array(v):
            v_replaced = [self.perform_replacemenet(v_el) for v_el in v]

            invalid_els = [e for e in v_replaced if (not self.in_values(e))]
            if invalid_els:
                self.raise_invalid_elements(invalid_els[:10])

            if is_homogeneous_array(v):
                v = copy_to_readonly_numpy_array(v)
            else:
                v = to_scalar_or_list(v)
        else:
            v = self.perform_replacemenet(v)
            if not self.in_values(v):
                self.raise_invalid_val(v)
        return v


class BooleanValidator(BaseValidator):
    """
        "boolean": {
            "description": "A boolean (true/false) value.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt"
            ]
        },
    """

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(BooleanValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):
        return ("""\
    The '{plotly_name}' property must be specified as a bool
    (either True, or False)""".format(plotly_name=self.plotly_name))

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif not isinstance(v, bool):
            self.raise_invalid_val(v)

        return v


class SrcValidator(BaseValidator):

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(SrcValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):
        return ("""\
    The '{plotly_name}' property must be specified as a string or
    as a plotly.grid_objs.Column object""".format(plotly_name=self.plotly_name))

    def validate_coerce(self, v):
        from plotly.grid_objs import Column
        if v is None:
            # Pass None through
            pass
        elif isinstance(v, string_types):
            pass
        elif isinstance(v, Column):
            # Convert to id string
            v = v.id
        else:
            self.raise_invalid_val(v)

        return v


class NumberValidator(BaseValidator):
    """
        "number": {
            "description": "A number or a numeric value (e.g. a number
                            inside a string). When applicable, values
                            greater (less) than `max` (`min`) are coerced to
                            the `dflt`.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt",
                "min",
                "max",
                "arrayOk"
            ]
        },
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 min=None,
                 max=None,
                 array_ok=False,
                 **kwargs):
        super(NumberValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        # Handle min
        if min is None and max is not None:
            # Max was specified, so make min -inf
            self.min_val = float('-inf')
        else:
            self.min_val = min

        # Handle max
        if max is None and min is not None:
            # Min was specified, so make min inf
            self.max_val = float('inf')
        else:
            self.max_val = max

        if min is not None or max is not None:
            self.has_min_max = True
        else:
            self.has_min_max = False

        self.array_ok = array_ok

    def description(self):
        desc = ("""\
    The '{plotly_name}' property is a number and may be specified as:"""
                .format(plotly_name=self.plotly_name))

        if not self.has_min_max:
            desc = desc + """
      - An int or float"""

        else:
            desc = desc + """
      - An int or float in the interval [{min_val}, {max_val}]""".format(
                min_val=self.min_val, max_val=self.max_val)

        if self.array_ok:
            desc = desc + """
      - A tuple, list, or one-dimensional numpy array of the above"""

        return desc

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_homogeneous_array(v):

            try:
                v_array = copy_to_readonly_numpy_array(v, force_numeric=True)
            except (ValueError, TypeError, OverflowError):
                self.raise_invalid_val(v)

            # Check min/max
            if self.has_min_max:
                v_valid = np.logical_and(self.min_val <= v_array,
                                         v_array <= self.max_val)

                if not np.all(v_valid):
                    # Grab up to the first 10 invalid values
                    v_invalid = np.logical_not(v_valid)
                    some_invalid_els = (np.array(v, dtype='object')
                                        [v_invalid][:10]
                                        .tolist())

                    self.raise_invalid_elements(some_invalid_els)

            v = v_array  # Always numeric numpy array
        elif self.array_ok and is_simple_array(v):
            # Check numeric
            invalid_els = [e for e in v if not isinstance(e, numbers.Number)]

            if invalid_els:
                self.raise_invalid_elements(invalid_els[:10])

            # Check min/max
            if self.has_min_max:
                invalid_els = [e for e in v if
                               not (self.min_val <= e <= self.max_val)]

                if invalid_els:
                    self.raise_invalid_elements(invalid_els[:10])

            v = to_scalar_or_list(v)
        else:
            # Check numeric
            if not isinstance(v, numbers.Number):
                self.raise_invalid_val(v)

            # Check min/max
            if self.has_min_max:
                if not (self.min_val <= v <= self.max_val):
                    self.raise_invalid_val(v)
        return v


class IntegerValidator(BaseValidator):
    """
        "integer": {
            "description": "An integer or an integer inside a string. When
                            applicable, values greater (less) than `max`
                            (`min`) are coerced to the `dflt`.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt",
                "min",
                "max",
                "arrayOk"
            ]
        },
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 min=None,
                 max=None,
                 array_ok=False,
                 **kwargs):
        super(IntegerValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        # Handle min
        if min is None and max is not None:
            # Max was specified, so make min -inf
            self.min_val = -sys.maxsize - 1
        else:
            self.min_val = min

        # Handle max
        if max is None and min is not None:
            # Min was specified, so make min inf
            self.max_val = sys.maxsize
        else:
            self.max_val = max

        if min is not None or max is not None:
            self.has_min_max = True
        else:
            self.has_min_max = False

        self.array_ok = array_ok

    def description(self):
        desc = ("""\
    The '{plotly_name}' property is a integer and may be specified as:"""
                .format(plotly_name=self.plotly_name))

        if not self.has_min_max:
            desc = desc + """
      - An int (or float that will be cast to an int)"""
        else:
            desc = desc + ("""
      - An int (or float that will be cast to an int)
        in the interval [{min_val}, {max_val}]""".format(
                min_val=self.min_val, max_val=self.max_val))

        if self.array_ok:
            desc = desc + """
      - A tuple, list, or one-dimensional numpy array of the above"""

        return desc

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_homogeneous_array(v):
            if v.dtype.kind not in ['i', 'u']:
                self.raise_invalid_val(v)

            v_array = copy_to_readonly_numpy_array(v, dtype='int32')

            # Check min/max
            if self.has_min_max:
                v_valid = np.logical_and(self.min_val <= v_array,
                                         v_array <= self.max_val)

                if not np.all(v_valid):
                    # Grab up to the first 10 invalid values
                    v_invalid = np.logical_not(v_valid)
                    some_invalid_els = (np.array(v, dtype='object')
                                   [v_invalid][:10].tolist())
                    self.raise_invalid_elements(some_invalid_els)

            v = v_array
        elif self.array_ok and is_simple_array(v):
            # Check integer type
            invalid_els = [e for e in v if not isinstance(e, int)]

            if invalid_els:
                self.raise_invalid_elements(invalid_els[:10])

            # Check min/max
            if self.has_min_max:
                invalid_els = [e for e in v if
                               not (self.min_val <= e <= self.max_val)]

                if invalid_els:
                    self.raise_invalid_elements(invalid_els[:10])

            v = to_scalar_or_list(v)
        else:
            # Check int
            if not isinstance(v, int):
                # don't let int() cast strings to ints
                self.raise_invalid_val(v)

            # Check min/max
            if self.has_min_max:
                if not (self.min_val <= v <= self.max_val):
                    self.raise_invalid_val(v)

        return v


class StringValidator(BaseValidator):
    """
        "string": {
            "description": "A string value. Numbers are converted to strings
                            except for attributes with `strict` set to true.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt",
                "noBlank",
                "strict",
                "arrayOk",
                "values"
            ]
        },
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 no_blank=False,
                 strict=False,
                 array_ok=False,
                 values=None,
                 **kwargs):
        super(StringValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)
        self.no_blank = no_blank
        self.strict = strict
        self.array_ok = array_ok
        self.values = values

    def description(self):
        desc = ("""\
    The '{plotly_name}' property is a string and must be specified as:"""
                .format(plotly_name=self.plotly_name))

        if self.no_blank:
            desc = desc + """
      - A non-empty string"""
        elif self.values:
            valid_str = '\n'.join(
                textwrap.wrap(
                    repr(self.values),
                    initial_indent=' ' * 12,
                    subsequent_indent=' ' * 12,
                    break_on_hyphens=False))

            desc = desc + """
      - One of the following strings:
{valid_str}""".format(valid_str=valid_str)
        else:
            desc = desc + """
      - A string"""

        if not self.strict:
            desc = desc + """
      - A number that will be converted to a string"""

        if self.array_ok:
            desc = desc + """
      - A tuple, list, or one-dimensional numpy array of the above"""

        return desc

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_array(v):

            # If strict, make sure all elements are strings.
            if self.strict:
                invalid_els = [e for e in v if not isinstance(e, string_types)]
                if invalid_els:
                    self.raise_invalid_elements(invalid_els)

            if is_homogeneous_array(v):
                # If not strict, let numpy cast elements to strings
                v = copy_to_readonly_numpy_array(v, dtype='unicode')

                # Check no_blank
                if self.no_blank:
                    invalid_els = v[v == ''][:10].tolist()
                    if invalid_els:
                        self.raise_invalid_elements(invalid_els)

                # Check values
                if self.values:
                    invalid_inds = np.logical_not(np.isin(v, self.values))
                    invalid_els = v[invalid_inds][:10].tolist()
                    if invalid_els:
                        self.raise_invalid_elements(invalid_els)

            elif is_simple_array(v):
                if not self.strict:
                    v = [str(e) for e in v]

                # Check no_blank
                if self.no_blank:
                    invalid_els = [e for e in v if e == '']
                    if invalid_els:
                        self.raise_invalid_elements(invalid_els)

                # Check values
                if self.values:
                    invalid_els = [e for e in v if v not in self.values]
                    if invalid_els:
                        self.raise_invalid_elements(invalid_els)

                v = to_scalar_or_list(v)

        else:
            if self.strict:
                if not isinstance(v, string_types):
                    self.raise_invalid_val(v)
            else:
                if not isinstance(v, string_types + (int, float)):
                    self.raise_invalid_val(v)

                # Convert value to a string
                v = str(v)

            if self.no_blank and len(v) == 0:
                self.raise_invalid_val(v)

            if self.values and v not in self.values:
                self.raise_invalid_val(v)

        return v


class ColorValidator(BaseValidator):
    """
        "color": {
            "description": "A string describing color. Supported formats:
                            - hex (e.g. '#d3d3d3')
                            - rgb (e.g. 'rgb(255, 0, 0)')
                            - rgba (e.g. 'rgb(255, 0, 0, 0.5)')
                            - hsl (e.g. 'hsl(0, 100%, 50%)')
                            - hsv (e.g. 'hsv(0, 100%, 100%)')
                            - named colors(full list:
                              http://www.w3.org/TR/css3-color/#svg-color)",
            "requiredOpts": [],
            "otherOpts": [
                "dflt",
                "arrayOk"
            ]
        },
    """
    re_hex = re.compile('#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})')
    re_rgb_etc = re.compile('(rgb|hsl|hsv)a?\([\d.]+%?(,[\d.]+%?){2,3}\)')

    named_colors = [
        "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige",
        "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown",
        "burlywood", "cadetblue", "chartreuse", "chocolate", "coral",
        "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue",
        "darkcyan", "darkgoldenrod", "darkgray", "darkgrey", "darkgreen",
        "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
        "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue",
        "darkslategray", "darkslategrey", "darkturquoise", "darkviolet",
        "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue",
        "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro",
        "ghostwhite", "gold", "goldenrod", "gray", "grey", "green",
        "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory",
        "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon",
        "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow",
        "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon",
        "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey",
        "lightsteelblue", "lightyellow", "lime", "limegreen", "linen",
        "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid",
        "mediumpurple", "mediumseagreen", "mediumslateblue",
        "mediumspringgreen", "mediumturquoise", "mediumvioletred",
        "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite",
        "navy", "oldlace", "olive", "olivedrab", "orange", "orangered",
        "orchid", "palegoldenrod", "palegreen", "paleturquoise",
        "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum",
        "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown",
        "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver",
        "skyblue", "slateblue", "slategray", "slategrey", "snow",
        "springgreen", "steelblue", "tan", "teal", "thistle", "tomato",
        "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow",
        "yellowgreen"
    ]

    def __init__(self,
                 plotly_name,
                 parent_name,
                 array_ok=False,
                 colorscale_path=None,
                 **kwargs):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        self.array_ok = array_ok

        # colorscale_path is the path to the colorscale associated with this
        # color property, or None if no such colorscale exists. Only colors
        # with an associated colorscale may take on numeric values
        self.colorscale_path = colorscale_path

    def numbers_allowed(self):
        return self.colorscale_path is not None

    def description(self):

        named_clrs_str = '\n'.join(
            textwrap.wrap(
                ', '.join(self.named_colors),
                width=79 - 16,
                initial_indent=' ' * 12,
                subsequent_indent=' ' * 12))

        valid_color_description = """\
    The '{plotly_name}' property is a color and may be specified as:
      - A hex string (e.g. '#ff0000')
      - An rgb/rgba string (e.g. 'rgb(255,0,0)')
      - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
      - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
      - A named CSS color:
{clrs}""".format(
            plotly_name=self.plotly_name, clrs=named_clrs_str)

        if self.colorscale_path:
            valid_color_description = valid_color_description + """
      - A number that will be interpreted as a color
        according to {colorscale_path}""".format(
                colorscale_path=self.colorscale_path)

        if self.array_ok:
            valid_color_description = valid_color_description + """
      - A list or array of any of the above"""

        return valid_color_description

    def validate_coerce(self, v, should_raise=True):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_homogeneous_array(v):

            v_array = copy_to_readonly_numpy_array(v)
            if (self.numbers_allowed() and
                    v_array.dtype.kind in ['u', 'i', 'f']):
                # Numbers are allowed and we have an array of numbers.
                # All good
                v = v_array
            else:
                validated_v = [
                    self.validate_coerce(e, should_raise=False)
                    for e in v]

                invalid_els = self.find_invalid_els(v, validated_v)

                if invalid_els and should_raise:
                    self.raise_invalid_elements(invalid_els)

                # ### Check that elements have valid colors types ###
                elif self.numbers_allowed() or invalid_els:
                    v = copy_to_readonly_numpy_array(
                        validated_v, dtype='object')
                else:
                    v = copy_to_readonly_numpy_array(
                        validated_v, dtype='unicode')
        elif self.array_ok and is_simple_array(v):
            validated_v = [
                self.validate_coerce(e, should_raise=False)
                for e in v]

            invalid_els = self.find_invalid_els(v, validated_v)

            if invalid_els and should_raise:
                self.raise_invalid_elements(invalid_els)
            else:
                v = validated_v
        else:
            # Validate scalar color
            validated_v = self.vc_scalar(v)
            if validated_v is None and should_raise:
                self.raise_invalid_val(v)

            v = validated_v

        return v

    def find_invalid_els(self, orig, validated, invalid_els=None):
        """
        Helper method to find invalid elements in orig array.
        Elements are invalid if their corresponding element in
        the validated array is None.

        This method handles deeply nested list structures
        """
        if invalid_els is None:
            invalid_els = []

        for orig_el, validated_el in zip(orig, validated):
            if is_array(orig_el):
                self.find_invalid_els(orig_el, validated_el, invalid_els)
            else:
                if validated_el is None:
                    invalid_els.append(orig_el)

        return invalid_els

    def vc_scalar(self, v):
        """ Helper to validate/coerce a scalar color """
        return ColorValidator.perform_validate_coerce(
            v, allow_number=self.numbers_allowed())

    @staticmethod
    def perform_validate_coerce(v, allow_number=None):
        """
        Validate, coerce, and return a single color value. If input cannot be
        coerced to a valid color then return None.

        Parameters
        ----------
        v : number or str
            Candidate color value

        allow_number : bool
            True if numbers are allowed as colors

        Returns
        -------
        number or str or None
        """

        if isinstance(v, numbers.Number) and allow_number:
            # If allow_numbers then any number is ok
            return v
        elif not isinstance(v, string_types):
            # If not allow_numbers then value must be a string
            return None
        else:
            # Remove spaces so regexes don't need to bother with them.
            v_normalized = v.replace(' ', '').lower()

            # if ColorValidator.re_hex.fullmatch(v_normalized):
            if fullmatch(ColorValidator.re_hex, v_normalized):
                # valid hex color (e.g. #f34ab3)
                return v
            elif fullmatch(ColorValidator.re_rgb_etc, v_normalized):
            # elif ColorValidator.re_rgb_etc.fullmatch(v_normalized):
                # Valid rgb(a), hsl(a), hsv(a) color
                # (e.g. rgba(10, 234, 200, 50%)
                return v
            elif v_normalized in ColorValidator.named_colors:
                # Valid named color (e.g. 'coral')
                return v
            else:
                # Not a valid color
                return None


class ColorlistValidator(BaseValidator):
    """
        "colorlist": {
          "description": "A list of colors. Must be an {array} containing
                          valid colors.",
          "requiredOpts": [],
          "otherOpts": [
            "dflt"
          ]
        }
    """

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(ColorlistValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):
        return ("""\
    The '{plotly_name}' property is a colorlist that may be specified
    as a tuple, list, one-dimensional numpy array, or pandas Series of valid
    color strings""".format(plotly_name=self.plotly_name))

    def validate_coerce(self, v):

        if v is None:
            # Pass None through
            pass
        elif is_array(v):
            validated_v = [
                ColorValidator.perform_validate_coerce(e, allow_number=False)
                for e in v
            ]

            invalid_els = [
                el for el, validated_el in zip(v, validated_v)
                if validated_el is None
            ]
            if invalid_els:
                self.raise_invalid_elements(invalid_els)

            v = to_scalar_or_list(v)
        else:
            self.raise_invalid_val(v)
        return v


class ColorscaleValidator(BaseValidator):
    """
        "colorscale": {
            "description": "A Plotly colorscale either picked by a name:
                            (any of Greys, YlGnBu, Greens, YlOrRd, Bluered,
                            RdBu, Reds, Blues, Picnic, Rainbow, Portland,
                            Jet, Hot, Blackbody, Earth, Electric, Viridis)
                            customized as an {array} of 2-element {arrays}
                            where the first element is the normalized color
                            level value (starting at *0* and ending at *1*),
                            and the second item is a valid color string.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt"
            ]
        },
    """

    named_colorscales = [
        'Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu', 'Reds',
        'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet', 'Hot', 'Blackbody',
        'Earth', 'Electric', 'Viridis', 'Cividis'
    ]

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(ColorscaleValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):
        desc = """\
    The '{plotly_name}' property is a colorscale and may be
    specified as:
      - A list of 2-element lists where the first element is the
        normalized color level value (starting at 0 and ending at 1), 
        and the second item is a valid color string.
        (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
      - One of the following named colorscales:
            ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
            'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
            'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']
        """.format(plotly_name=self.plotly_name)

        return desc

    def validate_coerce(self, v):
        v_valid = False

        if v is None:
            # Pass None through
            pass
        if v is None:
            v_valid = True
        elif isinstance(v, string_types):
            v_match = [
                el for el in ColorscaleValidator.named_colorscales
                if el.lower() == v.lower()
            ]
            if v_match:
                v_valid = True

        elif is_array(v) and len(v) > 0:
            invalid_els = [
                e for e in v
                if (not is_array(e) or
                    len(e) != 2 or
                    not isinstance(e[0], numbers.Number) or
                    not (0 <= e[0] <= 1) or
                    not isinstance(e[1], string_types) or
                    ColorValidator.perform_validate_coerce(e[1]) is None)]

            if len(invalid_els) == 0:
                v_valid = True

                # Convert to list of lists
                v = [[e[0],
                      ColorValidator.perform_validate_coerce(e[1])]
                     for e in v]

        if not v_valid:
            self.raise_invalid_val(v)

        return v

    def present(self, v):
        # Return-type must be immutable
        if v is None:
            return None
        elif isinstance(v, string_types):
            return v
        else:
            return tuple([tuple(e) for e in v])


class AngleValidator(BaseValidator):
    """
        "angle": {
            "description": "A number (in degree) between -180 and 180.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt"
            ]
        },
    """

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(AngleValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):
        desc = """\
    The '{plotly_name}' property is a angle (in degrees) that may be
    specified as a number between -180 and 180. Numeric values outside this
    range are converted to the equivalent value
    (e.g. 270 is converted to -90).
        """.format(plotly_name=self.plotly_name)

        return desc

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif not isinstance(v, numbers.Number):
            self.raise_invalid_val(v)
        else:
            # Normalize v onto the interval [-180, 180)
            v = (v + 180) % 360 - 180

        return v


class SubplotidValidator(BaseValidator):
    """
        "subplotid": {
            "description": "An id string of a subplot type (given by dflt),
                            optionally followed by an integer >1. e.g. if
                            dflt='geo', we can have 'geo', 'geo2', 'geo3',
                            ...",
            "requiredOpts": [
                "dflt"
            ],
            "otherOpts": [
                "regex"
            ]
        }
    """

    def __init__(self, plotly_name,
                 parent_name,
                 dflt=None,
                 regex=None,
                 **kwargs):

        if dflt is None and regex is None:
            raise ValueError(
                'One or both of regex and deflt must be specified'
            )

        super(SubplotidValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        if dflt is not None:
            self.base = dflt
        else:
            # e.g. regex == '/^y([2-9]|[1-9][0-9]+)?$/'
            self.base = re.match('/\^(\w+)',
                                 regex).group(1)

        if regex is not None:
            # Remove leading/trailing '/' characters
            self.regex = regex[1:-1]
        else:
            self.regex = dflt + "(\d*)"

    def description(self):

        desc = """\
    The '{plotly_name}' property is an identifier of a particular
    subplot, of type '{base}', that may be specified as the string '{base}'
    optionally followed by an integer >= 1
    (e.g. '{base}', '{base}1', '{base}2', '{base}3', etc.)
        """.format(
            plotly_name=self.plotly_name, base=self.base)
        return desc

    def validate_coerce(self, v):
        if v is None:
            pass
        elif not isinstance(v, string_types):
            self.raise_invalid_val(v)
        else:
            # match = re.fullmatch(self.regex, v)
            match = fullmatch(self.regex, v)
            if not match:
                is_valid = False
            else:
                digit_str = match.group(1)
                if len(digit_str) > 0 and int(digit_str) == 0:
                    is_valid = False
                elif len(digit_str) > 0 and int(digit_str) == 1:
                    # Remove 1 suffix (e.g. x1 -> x)
                    v = self.base
                    is_valid = True
                else:
                    is_valid = True

            if not is_valid:
                self.raise_invalid_val(v)
        return v


class FlaglistValidator(BaseValidator):
    """
        "flaglist": {
            "description": "A string representing a combination of flags
                            (order does not matter here). Combine any of the
                            available `flags` with *+*.
                            (e.g. ('lines+markers')). Values in `extras`
                            cannot be combined.",
            "requiredOpts": [
                "flags"
            ],
            "otherOpts": [
                "dflt",
                "extras",
                "arrayOk"
            ]
        },
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 flags,
                 extras=None,
                 array_ok=False,
                 **kwargs):
        super(FlaglistValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)
        self.flags = flags
        self.extras = extras if extras is not None else []
        self.array_ok = array_ok

        self.all_flags = self.flags + self.extras

    def description(self):

        desc = ("""\
    The '{plotly_name}' property is a flaglist and may be specified
    as a string containing:""").format(plotly_name=self.plotly_name)

        # Flags
        desc = desc + ("""
      - Any combination of {flags} joined with '+' characters
        (e.g. '{eg_flag}')""").format(
            flags=self.flags, eg_flag='+'.join(self.flags[:2]))

        # Extras
        if self.extras:
            desc = desc + ("""
        OR exactly one of {extras} (e.g. '{eg_extra}')""").format(
                extras=self.extras, eg_extra=self.extras[-1])

        if self.array_ok:
            desc = desc + """
      - A list or array of the above"""

        return desc

    def vc_scalar(self, v):
        if not isinstance(v, string_types):
            return None

        # To be generous we accept flags separated on plus ('+'),
        # or comma (',')
        split_vals = [e.strip() for e in re.split('[,+]', v)]

        # Are all flags valid names?
        all_flags_valid = all([f in self.all_flags for f in split_vals])

        # Are any 'extras' flags present?
        has_extras = any([f in self.extras for f in split_vals])

        # For flaglist to be valid all flags must be valid, and if we have
        # any extras present, there must be only one flag (the single extras
        # flag)
        is_valid = (all_flags_valid and
                    (not has_extras or len(split_vals) == 1))
        if is_valid:
            return '+'.join(split_vals)
        else:
            return None

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_array(v):

            # Coerce individual strings
            validated_v = [self.vc_scalar(e) for e in v]

            invalid_els = [
                el for el, validated_el in zip(v, validated_v)
                if validated_el is None
            ]
            if invalid_els:
                self.raise_invalid_elements(invalid_els)

            if is_homogeneous_array(v):
                v = copy_to_readonly_numpy_array(validated_v, dtype='unicode')
            else:
                v = to_scalar_or_list(v)
        else:

            validated_v = self.vc_scalar(v)
            if validated_v is None:
                self.raise_invalid_val(v)

            v = validated_v

        return v


class AnyValidator(BaseValidator):
    """
        "any": {
            "description": "Any type.",
            "requiredOpts": [],
            "otherOpts": [
                "dflt",
                "values",
                "arrayOk"
            ]
        },
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 values=None,
                 array_ok=False,
                 **kwargs):
        super(AnyValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)
        self.values = values
        self.array_ok = array_ok

    def description(self):

        desc = """\
    The '{plotly_name}' property accepts values of any type
        """.format(plotly_name=self.plotly_name)
        return desc

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif self.array_ok and is_homogeneous_array(v):
            v = copy_to_readonly_numpy_array(v, dtype='object')
        elif self.array_ok and is_simple_array(v):
            v = to_scalar_or_list(v)
        return v


class InfoArrayValidator(BaseValidator):
    """
        "info_array": {
            "description": "An {array} of plot information.",
            "requiredOpts": [
                "items"
            ],
            "otherOpts": [
                "dflt",
                "freeLength"
            ]
        }
    """

    def __init__(self,
                 plotly_name,
                 parent_name,
                 items,
                 free_length=None,
                 **kwargs):
        super(InfoArrayValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)
        self.items = items

        # Instantiate validators for each info array element
        self.item_validators = []
        info_array_items = (self.items
                            if isinstance(self.items, list) else [self.items])

        for i, item in enumerate(info_array_items):
            element_name = '{name}[{i}]'.format(name=plotly_name, i=i)
            item_validator = InfoArrayValidator.build_validator(
                item, element_name, parent_name)
            self.item_validators.append(item_validator)

        self.free_length = free_length

    def description(self):
        upto = ' up to' if self.free_length else ''
        desc = """\
    The '{plotly_name}' property is an info array that may be specified as a
    list or tuple of{upto} {N} elements where:
""".format(plotly_name=self.plotly_name,
           upto=upto,
           N=len(self.item_validators))

        for i, item_validator in enumerate(self.item_validators):
            el_desc = item_validator.description().strip()
            desc = desc + """
({i}) {el_desc}""".format(i=i, el_desc=el_desc)

        return desc

    @staticmethod
    def build_validator(validator_info, plotly_name, parent_name):
        datatype = validator_info['valType']  # type: str
        validator_classname = datatype.title().replace('_', '') + 'Validator'
        validator_class = eval(validator_classname)

        kwargs = {
            k: validator_info[k]
            for k in validator_info
            if k not in ['valType', 'description', 'role']
        }

        return validator_class(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def validate_coerce(self, v):
        if v is None:
            # Pass None through
            pass
        elif not is_array(v):
            self.raise_invalid_val(v)
        elif not self.free_length and len(v) != len(self.item_validators):
            self.raise_invalid_val(v)
        elif self.free_length and len(v) > len(self.item_validators):
            self.raise_invalid_val(v)
        else:
            # We have an array of the correct length
            v = to_scalar_or_list(v)
            for i, (el, validator) in enumerate(zip(v, self.item_validators)):
                # Validate coerce elements
                v[i] = validator.validate_coerce(el)

        return v

    def present(self, v):
        if v is None:
            return None
        else:
            # Call present on each of the item validators
            for i, (el, validator) in enumerate(zip(v, self.item_validators)):
                # Validate coerce elements
                v[i] = validator.present(el)

            # Return tuple form of
            return tuple(v)


class LiteralValidator(BaseValidator):
    """
    Validator for readonly literal values
    """
    def __init__(self, plotly_name, parent_name, val, **kwargs):
        super(LiteralValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            **kwargs)
        self.val = val

    def validate_coerce(self, v):
        if v != self.val:
            raise ValueError("""\
    The '{plotly_name}' property of {parent_name} is read-only""".format(
                plotly_name=self.plotly_name, parent_name=self.parent_name
            ))
        else:
            return v


class DashValidator(EnumeratedValidator):
    """
    Special case validator for handling dash properties that may be specified
    as lists of dash lengths.  These are not currently specified in the
    schema.

    "dash": {
        "valType": "string",
        "values": [
            "solid",
            "dot",
            "dash",
            "longdash",
            "dashdot",
            "longdashdot"
        ],
        "dflt": "solid",
        "role": "style",
        "editType": "style",
        "description": "Sets the dash style of lines. Set to a dash type
        string (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
        *longdashdot*) or a dash length list in px (eg *5px,10px,2px,2px*)."
    },
    """
    def __init__(self,
                 plotly_name,
                 parent_name,
                 values,
                 **kwargs):

        # Add regex to handle dash length lists
        dash_list_regex = \
            r"/^\d+(\.\d+)?(px|%)?((,|\s)\s*\d+(\.\d+)?(px|%)?)*$/"

        values = values + [dash_list_regex]

        # Call EnumeratedValidator superclass
        super(DashValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            values=values, **kwargs)

    def description(self):

            # Separate regular values from regular expressions
            enum_vals = []
            enum_regexs = []
            for v, regex in zip(self.values, self.val_regexs):
                if regex is not None:
                    enum_regexs.append(regex.pattern)
                else:
                    enum_vals.append(v)
            desc = ("""\
    The '{name}' property is an enumeration that may be specified as:"""
                    .format(name=self.plotly_name))

            if enum_vals:
                enum_vals_str = '\n'.join(
                    textwrap.wrap(
                        repr(enum_vals),
                        initial_indent=' ' * 12,
                        subsequent_indent=' ' * 12,
                        break_on_hyphens=False,
                        width=80))

                desc = desc + """
      - One of the following dash styles:
{enum_vals_str}""".format(enum_vals_str=enum_vals_str)

            desc = desc + """
      - A string containing a dash length list in pixels or percentages
            (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)
"""
            return desc


class ImageUriValidator(BaseValidator):
    _PIL = None

    try:
        _PIL = import_module('PIL')
    except ImportError:
        pass

    def __init__(self, plotly_name, parent_name, **kwargs):
        super(ImageUriValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

    def description(self):

        desc = """\
    The '{plotly_name}' property is an image URI that may be specified as:
      - A remote image URI string
        (e.g. 'http://www.somewhere.com/image.png')
      - A data URI image string
        (e.g. 'data:image/png;base64,iVBORw0KGgoAAAANSU')
      - A PIL.Image.Image object which will be immediately converted
        to a data URI image string
        See http://pillow.readthedocs.io/en/latest/reference/Image.html
        """.format(plotly_name=self.plotly_name)
        return desc

    def validate_coerce(self, v):
        if v is None:
            pass
        elif isinstance(v, string_types):
            # Future possibilities:
            #   - Detect filesystem system paths and convert to URI
            #   - Validate either url or data uri
            pass
        elif self._PIL and isinstance(v, self._PIL.Image.Image):
            # Convert PIL image to png data uri string
            in_mem_file = io.BytesIO()
            v.save(in_mem_file, format="PNG")
            in_mem_file.seek(0)
            img_bytes = in_mem_file.read()
            base64_encoded_result_bytes = base64.b64encode(img_bytes)
            base64_encoded_result_str = (
                base64_encoded_result_bytes.decode('ascii'))
            v = 'data:image/png;base64,{base64_encoded_result_str}'.format(
                base64_encoded_result_str=base64_encoded_result_str)
        else:
            self.raise_invalid_val(v)

        return v


class CompoundValidator(BaseValidator):

    def __init__(self, plotly_name, parent_name, data_class_str, data_docs,
                 **kwargs):
        super(CompoundValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        # Save element class string
        self.data_class_str = data_class_str
        self._data_class = None
        self.data_docs = data_docs
        self.module_str = CompoundValidator.compute_graph_obj_module_str(
            self.data_class_str, parent_name)

    @staticmethod
    def compute_graph_obj_module_str(data_class_str, parent_name):
        if parent_name == 'frame' and data_class_str in ['Data', 'Layout']:
            # Special case. There are no graph_objs.frame.Data or
            # graph_objs.frame.Layout classes. These are remapped to
            # graph_objs.Data and graph_objs.Layout

            parent_parts = parent_name.split('.')
            module_str = '.'.join(['plotly.graph_objs'] + parent_parts[1:])
        elif parent_name:
            module_str = 'plotly.graph_objs.' + parent_name
        else:
            module_str = 'plotly.graph_objs'

        return module_str

    @property
    def data_class(self):
        if self._data_class is None:
            module = import_module(self.module_str)
            self._data_class = getattr(module, self.data_class_str)

        return self._data_class

    def description(self):

        desc = ("""\
    The '{plotly_name}' property is an instance of {class_str}
    that may be specified as:
      - An instance of {module_str}.{class_str}
      - A dict of string/value properties that will be passed
        to the {class_str} constructor

        Supported dict properties:
            {constructor_params_str}""").format(
            plotly_name=self.plotly_name,
            class_str=self.data_class_str,
            module_str=self.module_str,
            constructor_params_str=self.data_docs)

        return desc

    def validate_coerce(self, v):
        if v is None:
            v = self.data_class()

        elif isinstance(v, dict):
            v = self.data_class(**v)

        elif isinstance(v, self.data_class):
            # Copy object
            v = self.data_class(**v.to_plotly_json())
        else:
            self.raise_invalid_val(v)

        v._plotly_name = self.plotly_name
        return v


class CompoundArrayValidator(BaseValidator):

    def __init__(self, plotly_name, parent_name, data_class_str, data_docs,
                 **kwargs):
        super(CompoundArrayValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        # Save element class string
        self.data_class_str = data_class_str
        self._data_class = None

        self.data_docs = data_docs
        self.module_str = CompoundValidator.compute_graph_obj_module_str(
            self.data_class_str, parent_name)

    def description(self):

        desc = ("""\
    The '{plotly_name}' property is a tuple of instances of
    {class_str} that may be specified as:
      - A list or tuple of instances of {module_str}.{class_str}
      - A list or tuple of dicts of string/value properties that
        will be passed to the {class_str} constructor

        Supported dict properties:
            {constructor_params_str}""").format(
            plotly_name=self.plotly_name,
            class_str=self.data_class_str,
            module_str=self.module_str,
            constructor_params_str=self.data_docs)

        return desc

    @property
    def data_class(self):
        if self._data_class is None:
            module = import_module(self.module_str)
            self._data_class = getattr(module, self.data_class_str)

        return self._data_class

    def validate_coerce(self, v):

        if v is None:
            v = []

        elif isinstance(v, (list, tuple)):
            res = []
            invalid_els = []
            for v_el in v:
                if isinstance(v_el, self.data_class):
                    res.append(v_el)
                elif isinstance(v_el, dict):
                    res.append(self.data_class(**v_el))
                else:
                    res.append(None)
                    invalid_els.append(v_el)

            if invalid_els:
                self.raise_invalid_elements(invalid_els)

            v = to_scalar_or_list(res)
        else:
            self.raise_invalid_val(v)

        return v


class BaseDataValidator(BaseValidator):

    def __init__(self,
                 class_strs_map,
                 plotly_name,
                 parent_name,
                 set_uid=False,
                 **kwargs):
        super(BaseDataValidator, self).__init__(
            plotly_name=plotly_name, parent_name=parent_name, **kwargs)

        self.class_strs_map = class_strs_map
        self._class_map = None
        self.set_uid = set_uid

    def description(self):

        trace_types = str(list(self.class_strs_map.keys()))

        trace_types_wrapped = '\n'.join(
            textwrap.wrap(
                trace_types,
                initial_indent='            One of: ',
                subsequent_indent=' ' * 21,
                width=79 - 12))

        desc = ("""\
    The '{plotly_name}' property is a tuple of trace instances
    that may be specified as:
      - A list or tuple of trace instances
        (e.g. [Scatter(...), Bar(...)])
      - A list or tuple of dicts of string/value properties where:
        - The 'type' property specifies the trace type
{trace_types}

        - All remaining properties are passed to the constructor of
          the specified trace type

        (e.g. [{{'type': 'scatter', ...}}, {{'type': 'bar, ...}}])""").format(
            plotly_name=self.plotly_name, trace_types=trace_types_wrapped)

        return desc

    @property
    def class_map(self):
        if self._class_map is None:

            # Initialize class map
            self._class_map = {}

            # Import trace classes
            trace_module = import_module('plotly.graph_objs')
            for k, class_str in self.class_strs_map.items():
                self._class_map[k] = getattr(trace_module, class_str)

        return self._class_map

    def validate_coerce(self, v):

        # Import Histogram2dcontour, this is the deprecated name of the
        # Histogram2dContour trace.
        from plotly.graph_objs import Histogram2dcontour

        if v is None:
            v = []
        elif isinstance(v, (list, tuple)):
            trace_classes = tuple(self.class_map.values())

            res = []
            invalid_els = []
            for v_el in v:

                if isinstance(v_el, trace_classes):
                    # Clone input traces
                    v_el = v_el.to_plotly_json()

                if isinstance(v_el, dict):
                    v_copy = deepcopy(v_el)

                    if 'type' in v_copy:
                        trace_type = v_copy.pop('type')
                    elif isinstance(v_el, Histogram2dcontour):
                        trace_type = 'histogram2dcontour'
                    else:
                        trace_type = 'scatter'

                    if trace_type not in self.class_map:
                        res.append(None)
                        invalid_els.append(v_el)
                    else:
                        trace = self.class_map[trace_type](**v_copy)
                        res.append(trace)
                else:
                    res.append(None)
                    invalid_els.append(v_el)

            if invalid_els:
                self.raise_invalid_elements(invalid_els)

            v = to_scalar_or_list(res)

            # Set new UIDs
            if self.set_uid:
                for trace in v:
                    trace.uid = str(uuid.uuid1())

        else:
            self.raise_invalid_val(v)

        return v
