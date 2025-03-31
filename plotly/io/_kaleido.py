import os
import json
from pathlib import Path
import importlib.metadata as importlib_metadata
from packaging.version import Version
import warnings

import plotly
from plotly.io._utils import validate_coerce_fig_to_dict, as_individual_args
from plotly.io import defaults

ENGINE_SUPPORT_TIMELINE = "September 2025"


# TODO: Remove --pre flag once Kaleido v1 full release is available
KALEIDO_DEPRECATION_MSG = f"""
Support for Kaleido versions less than 1.0.0 is deprecated and will be removed after {ENGINE_SUPPORT_TIMELINE}.
Please upgrade Kaleido to version 1.0.0 or greater (`pip install --upgrade --pre kaleido` or `pip install plotly[kaleido]`).
"""
ORCA_DEPRECATION_MSG = f"""
Support for the Orca engine is deprecated and will be removed after {ENGINE_SUPPORT_TIMELINE}.
Please install Kaleido (`pip install --upgrade --pre kaleido` or `pip install plotly[kaleido]`) to use the Kaleido engine.
"""
ENGINE_PARAM_DEPRECATION_MSG = f"""
Support for the 'engine' argument is deprecated and will be removed after {ENGINE_SUPPORT_TIMELINE}.
Kaleido will be the only supported engine at that time.
"""

_KALEIDO_AVAILABLE = None
_KALEIDO_MAJOR = None

kaleido_scope_default_warning_func = (
    lambda x: f"""
Use of plotly.io.kaleido.scope.{x} is deprecated and support will be removed after {ENGINE_SUPPORT_TIMELINE}.
Please use plotly.io.defaults.{x} instead.
"""
)
bad_attribute_error_msg_func = (
    lambda x: f"""
Attribute plotly.io.defaults.{x} is not valid.
Also, use of plotly.io.kaleido.scope.* is deprecated and support will be removed after {ENGINE_SUPPORT_TIMELINE}.
Please use plotly.io.defaults.* instead.
"""
)


def kaleido_available():
    global _KALEIDO_AVAILABLE
    global _KALEIDO_MAJOR
    if _KALEIDO_AVAILABLE is not None:
        return _KALEIDO_AVAILABLE
    try:
        import kaleido

        _KALEIDO_AVAILABLE = True
    except ImportError as e:
        _KALEIDO_AVAILABLE = False
    return _KALEIDO_AVAILABLE


def kaleido_major():
    global _KALEIDO_MAJOR
    if _KALEIDO_MAJOR is not None:
        return _KALEIDO_MAJOR
    if not kaleido_available():
        raise ValueError("Kaleido is not installed.")
    else:
        _KALEIDO_MAJOR = Version(importlib_metadata.version("kaleido")).major
    return _KALEIDO_MAJOR


try:
    if kaleido_available() and kaleido_major() < 1:
        # Kaleido v0
        import kaleido
        from kaleido.scopes.plotly import PlotlyScope

        # Show a deprecation warning if the old method of setting defaults is used
        class PlotlyScopeWithDeprecationWarnings(PlotlyScope):
            def __setattr__(self, name, value):
                if name in defaults.__dict__:
                    warnings.warn(
                        kaleido_scope_default_warning_func(name),
                        DeprecationWarning,
                        stacklevel=2,
                    )
                    setattr(defaults, name, value)
                super(PlotlyScopeWithDeprecationWarnings, self).__setattr__(name, value)

            def __getattr__(self, name):
                if name in defaults.__dict__:
                    warnings.warn(
                        kaleido_scope_default_warning_func(name),
                        DeprecationWarning,
                        stacklevel=2,
                    )
                return super(PlotlyScopeWithDeprecationWarnings, self).__getattr__(name)

        scope = PlotlyScopeWithDeprecationWarnings()
        # Compute absolute path to the 'plotly/package_data/' directory
        root_dir = os.path.dirname(os.path.abspath(plotly.__file__))
        package_dir = os.path.join(root_dir, "package_data")
        scope.plotlyjs = os.path.join(package_dir, "plotly.min.js")
        if scope.mathjax is None:
            scope.mathjax = (
                "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js"
            )
    else:
        # Kaleido v1
        import kaleido

        # Show a deprecation warning if the old method of setting defaults is used
        class DefaultsDeprecationWarning:
            def __getattr__(self, name):
                if name in defaults.__dict__:
                    warnings.warn(
                        kaleido_scope_default_warning_func(name),
                        DeprecationWarning,
                        stacklevel=2,
                    )
                    return getattr(defaults, name)
                else:
                    raise AttributeError(bad_attribute_error_msg_func(name))

            def __setattr__(self, name, value):
                if name in defaults.__dict__:
                    warnings.warn(
                        kaleido_scope_default_warning_func(name),
                        DeprecationWarning,
                        stacklevel=2,
                    )
                    setattr(defaults, name, value)
                else:
                    raise AttributeError(bad_attribute_error_msg_func(name))

        scope = DefaultsDeprecationWarning()

except ImportError as e:
    PlotlyScope = None
    scope = None


def to_image(
    fig,
    format=None,
    width=None,
    height=None,
    scale=None,
    validate=True,
    engine=None,
):
    """
    Convert a figure to a static image bytes string

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    format: str or None
        The desired image format. One of
            - 'png'
            - 'jpg' or 'jpeg'
            - 'webp'
            - 'svg'
            - 'pdf'
            - 'eps' (deprecated) (Requires the poppler library to be installed and on the PATH)

        If not specified, will default to:
            - `plotly.io.defaults.default_format` if engine is "kaleido"
            - `plotly.io.orca.config.default_format` if engine is "orca" (deprecated)

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to:
            - `plotly.io.defaults.default_width` if engine is "kaleido"
            - `plotly.io.orca.config.default_width` if engine is "orca" (deprecated)

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to:
            - `plotly.io.defaults.default_height` if engine is "kaleido"
            - `plotly.io.orca.config.default_height` if engine is "orca" (deprecated)

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to:
            - `plotly.io.defaults.default_scale` if engine is "kaliedo"
            - `plotly.io.orca.config.default_scale` if engine is "orca" (deprecated)

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    engine (deprecated): str
        Image export engine to use. This parameter is deprecated and Orca engine support will be
        dropped in the next major Plotly version. Until then, the following values are supported:
          - "kaleido": Use Kaleido for image export
          - "orca": Use Orca for image export
          - "auto" (default): Use Kaleido if installed, otherwise use Orca

    Returns
    -------
    bytes
        The image data
    """

    # Handle engine
    # -------------
    if engine is not None:
        warnings.warn(ENGINE_PARAM_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
    else:
        engine = "auto"

    if engine == "auto":
        if kaleido_available():
            # Default to kaleido if available
            engine = "kaleido"
        else:
            # See if orca is available
            from ._orca import validate_executable

            try:
                validate_executable()
                engine = "orca"
            except:
                # If orca not configured properly, make sure we display the error
                # message advising the installation of kaleido
                engine = "kaleido"

    if engine == "orca":
        warnings.warn(ORCA_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
        # Fall back to legacy orca image export path
        from ._orca import to_image as to_image_orca

        return to_image_orca(
            fig,
            format=format,
            width=width,
            height=height,
            scale=scale,
            validate=validate,
        )
    elif engine != "kaleido":
        raise ValueError(f"Invalid image export engine specified: {repr(engine)}")

    # Raise informative error message if Kaleido is not installed
    if not kaleido_available():
        raise ValueError(
            """
Image export using the "kaleido" engine requires the kaleido package,
which can be installed using pip:
    $ pip install -U kaleido
"""
        )

    # Convert figure to dict (and validate if requested)
    fig_dict = validate_coerce_fig_to_dict(fig, validate)

    # Request image bytes
    if kaleido_major() > 0:
        # Kaleido v1
        # Check if trying to export to EPS format, which is not supported in Kaleido v1
        if format == "eps":
            raise ValueError(
                f"""
EPS export is not supported by Kaleido v1. Please use SVG or PDF instead.
You can also downgrade to Kaleido v0, but support for Kaleido v0 will be removed after {ENGINE_SUPPORT_TIMELINE}.
To downgrade to Kaleido v0, run:
    $ pip install kaleido<1.0.0
"""
            )
        import choreographer

        try:
            # TODO: Refactor to make it possible to use a shared Kaleido instance here
            img_bytes = kaleido.calc_fig_sync(
                fig_dict,
                opts=dict(
                    format=format or defaults.default_format,
                    width=width or defaults.default_width,
                    height=height or defaults.default_height,
                    scale=scale or defaults.default_scale,
                ),
            )
        except choreographer.errors.ChromeNotFoundError:
            raise RuntimeError(
                """

Kaleido requires Google Chrome to be installed. Install it by running:
    $ plotly_get_chrome
"""
            )

    else:
        # Kaleido v0
        warnings.warn(KALEIDO_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
        img_bytes = scope.transform(
            fig_dict, format=format, width=width, height=height, scale=scale
        )

    return img_bytes


def write_image(
    fig,
    file,
    format=None,
    scale=None,
    width=None,
    height=None,
    validate=True,
    engine="auto",
):
    """
    Convert a figure to a static image and write it to a file or writeable
    object

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    file: str or writeable
        A string representing a local file path or a writeable object
        (e.g. a pathlib.Path object or an open file descriptor)

    format: str or None
        The desired image format. One of
          - 'png'
          - 'jpg' or 'jpeg'
          - 'webp'
          - 'svg'
          - 'pdf'
          - 'eps' (deprecated) (Requires the poppler library to be installed and on the PATH)

        If not specified and `file` is a string then this will default to the
        file extension. If not specified and `file` is not a string then this
        will default to:
            - `plotly.io.defaults.default_format` if engine is "kaleido"
            - `plotly.io.orca.config.default_format` if engine is "orca" (deprecated)

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to:
            - `plotly.io.defaults.default_width` if engine is "kaleido"
            - `plotly.io.orca.config.default_width` if engine is "orca" (deprecated)

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to:
            - `plotly.io.defaults.default_height` if engine is "kaleido"
            - `plotly.io.orca.config.default_height` if engine is "orca" (deprecated)

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to:
            - `plotly.io.defaults.default_scale` if engine is "kaleido"
            - `plotly.io.orca.config.default_scale` if engine is "orca" (deprecated)

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    engine (deprecated): str
        Image export engine to use. This parameter is deprecated and Orca engine support will be
        dropped in the next major Plotly version. Until then, the following values are supported:
          - "kaleido": Use Kaleido for image export
          - "orca": Use Orca for image export
          - "auto" (default): Use Kaleido if installed, otherwise use Orca

    Returns
    -------
    None
    """
    # Show Kaleido deprecation warning if needed
    # ------------------------------------------
    if (
        engine in {None, "auto", "kaleido"}
        and kaleido_available()
        and kaleido_major() < 1
    ):
        warnings.warn(KALEIDO_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
    if engine == "orca":
        warnings.warn(ORCA_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
    if engine not in {None, "auto"}:
        warnings.warn(ENGINE_PARAM_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)

    # Try to cast `file` as a pathlib object `path`.
    # ----------------------------------------------
    if isinstance(file, str):
        # Use the standard Path constructor to make a pathlib object.
        path = Path(file)
    elif isinstance(file, Path):
        # `file` is already a Path object.
        path = file
    else:
        # We could not make a Path object out of file. Either `file` is an open file
        # descriptor with a `write()` method or it's an invalid object.
        path = None

    # Infer format if not specified
    # -----------------------------
    if path is not None and format is None:
        ext = path.suffix
        if ext:
            format = ext.lstrip(".")
        else:
            raise ValueError(
                f"""
Cannot infer image type from output path '{file}'.
Please add a file extension or specify the type using the format parameter.
For example:

    >>> import plotly.io as pio
    >>> pio.write_image(fig, file_path, format='png')
"""
            )

    # Request image
    # -------------
    # Do this first so we don't create a file if image conversion fails
    img_data = to_image(
        fig,
        format=format,
        scale=scale,
        width=width,
        height=height,
        validate=validate,
        engine=engine,
    )

    # Open file
    # ---------
    if path is None:
        # We previously failed to make sense of `file` as a pathlib object.
        # Attempt to write to `file` as an open file descriptor.
        try:
            file.write(img_data)
            return
        except AttributeError:
            pass
        raise ValueError(
            f"""
The 'file' argument '{file}' is not a string, pathlib.Path object, or file descriptor.
"""
        )
    else:
        # We previously succeeded in interpreting `file` as a pathlib object.
        # Now we can use `write_bytes()`.
        path.write_bytes(img_data)


def to_images(*args, **kwargs):
    """
    Convert multiple figures to static images and return a list of image bytes

    Parameters
    ----------
    Accepts the same parameters as pio.to_image(), but any parameter may be either
    a single value or a list of values. If more than one parameter is a list,
    all must be the same length.

    Returns
    -------
    list of bytes
        The image data
    """
    individual_args, individual_kwargs = as_individual_args(*args, **kwargs)

    if kaleido_available() and kaleido_major() > 0:
        # Kaleido v1
        # TODO: Use a single shared kaleido instance for all images
        return [to_image(*a, **kw) for a, kw in zip(individual_args, individual_kwargs)]
    else:
        # Kaleido v0, or orca
        return [to_image(*a, **kw) for a, kw in zip(individual_args, individual_kwargs)]


def write_images(*args, **kwargs):
    """
    Write multiple images to files or writeable objects. This is much faster than
    calling write_image() multiple times.

    Parameters
    ----------
    Accepts the same parameters as pio.write_image(), but any parameter may be either
    a single value or a list of values. If more than one parameter is a list,
    all must be the same length.

    Returns
    -------
    None
    """

    # Get individual arguments
    individual_args, individual_kwargs = as_individual_args(*args, **kwargs)

    if kaleido_available() and kaleido_major() > 0:
        # Kaleido v1
        # TODO: Use a single shared kaleido instance for all images
        for a, kw in zip(individual_args, individual_kwargs):
            write_image(*a, **kw)
    else:
        # Kaleido v0, or orca
        for a, kw in zip(individual_args, individual_kwargs):
            write_image(*a, **kw)


def full_figure_for_development(fig, warn=True, as_dict=False):
    """
    Compute default values for all attributes not specified in the input figure and
    returns the output as a "full" figure. This function calls Plotly.js via Kaleido
    to populate unspecified attributes. This function is intended for interactive use
    during development to learn more about how Plotly.js computes default values and is
    not generally necessary or recommended for production use.

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    warn: bool
        If False, suppress warnings about not using this in production.

    as_dict: bool
        If True, output is a dict with some keys that go.Figure can't parse.
        If False, output is a go.Figure with unparseable keys skipped.

    Returns
    -------
    plotly.graph_objects.Figure or dict
        The full figure
    """

    # Raise informative error message if Kaleido is not installed
    if not kaleido_available():
        raise ValueError(
            """
Full figure generation requires the kaleido package,
which can be installed using pip:
    $ pip install -U kaleido
"""
        )

    if warn:
        warnings.warn(
            "full_figure_for_development is not recommended or necessary for "
            "production use in most circumstances. \n"
            "To suppress this warning, set warn=False"
        )

    if kaleido_available() and kaleido_major() > 0:
        # Kaleido v1
        bytes = kaleido.calc_fig_sync(
            fig,
            opts=dict(format="json"),
        )
        fig = json.loads(bytes.decode("utf-8"))
    else:
        # Kaleido v0
        warnings.warn(
            f"Support for Kaleido versions less than 1.0.0 is deprecated and will be removed after {ENGINE_SUPPORT_TIMELINE}. "
            + "Please upgrade Kaleido to version 1.0.0 or greater (`pip install --upgrade kaleido`).",
            DeprecationWarning,
        )
        fig = json.loads(scope.transform(fig, format="json").decode("utf-8"))

    if as_dict:
        return fig
    else:
        import plotly.graph_objects as go

        return go.Figure(fig, skip_invalid=True)


def get_chrome():
    """
    Install Google Chrome for Kaleido
    This function can be run from the command line using the command `plotly_get_chrome`
    defined in pyproject.toml
    """
    if not kaleido_available() or kaleido_major() < 1:
        raise ValueError(
            "This command requires Kaleido v1.0.0 or greater. Install it using `pip install kaleido`."
        )
    import sys

    cli_yes = len(sys.argv) > 1 and sys.argv[1] == "-y"
    if not cli_yes:
        print(
            "\nPlotly will install a copy of Google Chrome to be used for generating static images of plots.\n"
        )
        # TODO: Print path where Chrome will be installed
        # print(f"Chrome will be installed at {chrome_download_path}\n")
        response = input("Do you want to proceed? [y/n] ")
        if not response or response[0].lower() != "y":
            print("Cancelled")
            return
    print("Installing Chrome for Plotly...")
    kaleido.get_chrome_sync()
    print("Chrome installed successfully.")


__all__ = ["to_image", "write_image", "scope", "full_figure_for_development"]
