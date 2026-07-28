import os
import json
from pathlib import Path
from typing import Union, List
import importlib.metadata as importlib_metadata
from packaging.version import Version
import warnings

import plotly
from plotly.io._utils import validate_coerce_fig_to_dict, broadcast_args_to_dicts
from plotly.io._defaults import defaults
from _plotly_utils.optional_imports import get_module

kaleido = get_module("kaleido", should_load=True)

PLOTLY_GET_CHROME_ERROR_MSG = """

Kaleido requires Google Chrome to be installed.

Either download and install Chrome yourself following Google's instructions for your operating system,
or install it from your terminal by running:

    $ plotly_get_chrome

"""

KALEIDO_REQUIRED_MSG = """
Image export requires the Kaleido package, v1.0.0 or greater,
which can be installed using pip:

    $ pip install --upgrade "kaleido>=1"
"""


_KALEIDO_AVAILABLE = None


def kaleido_available() -> bool:
    """
    Returns True if Kaleido version 1.0.0 or greater is installed, otherwise False.
    """
    global _KALEIDO_AVAILABLE
    if _KALEIDO_AVAILABLE is not None:
        return _KALEIDO_AVAILABLE

    if kaleido is not None and Version(
        importlib_metadata.version("kaleido")
    ) >= Version("1.0.0"):
        _KALEIDO_AVAILABLE = True
    else:
        _KALEIDO_AVAILABLE = False
    return _KALEIDO_AVAILABLE


def as_path_object(file: Union[str, Path]) -> Union[Path, None]:
    """
    Cast the `file` argument, which may be either a string or a Path object,
    to a Path object.
    If `file` is neither a string nor a Path object, None will be returned.
    """
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
    return path


def infer_format(path: Union[Path, None], format: Union[str, None]) -> Union[str, None]:
    if path is not None and format is None:
        ext = path.suffix
        if ext:
            format = ext.lstrip(".")
        else:
            raise ValueError(
                f"""
Cannot infer image type from output path '{path}'.
Please specify the type using the format parameter, or add a file extension.
For example:

    >>> import plotly.io as pio
    >>> pio.write_image(fig, file_path, format='png')
"""
            )
    return format


def to_image(
    fig: Union[dict, plotly.graph_objects.Figure],
    format: Union[str, None] = None,
    width: Union[int, None] = None,
    height: Union[int, None] = None,
    scale: Union[int, float, None] = None,
    validate: bool = True,
) -> bytes:
    """
    Convert a figure to a static image bytes string

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    format: str
        (optional) The desired image format. One of:
            - 'png'
            - 'jpg' or 'jpeg'
            - 'webp'
            - 'svg'
            - 'pdf'
        Defaults to `plotly.io.defaults.default_format`.

    width: int
        (optional) The width of the exported image in layout pixels. If the
        `scale` property is 1.0, this will also be the width of the exported image
        in physical pixels. Defaults to `plotly.io.defaults.default_width`.

    height: int
        (optional) The height of the exported image in layout pixels. If the
        `scale` property is 1.0, this will also be the height of the exported image
        in physical pixels. Defaults to `plotly.io.defaults.default_height`.

    scale: int or float
        (optional) The scale factor to use when exporting the figure. A scale
        factor larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions, while a scale factor of
        less than 1.0 will decrease the image resolution. Defaults to
        `plotly.io.defaults.default_scale`.

    validate: bool
        (optional) True if the figure should be validated before being converted
        to an image, False otherwise. Defaults to True.

    Returns
    -------
    bytes
        The image data
    """
    if not kaleido_available():
        raise RuntimeError(KALEIDO_REQUIRED_MSG)

    # Convert figure to dict (and validate if requested)
    fig_dict = validate_coerce_fig_to_dict(fig, validate)

    # Check if trying to export to EPS format, which is not supported in Kaleido v1
    if format == "eps":
        raise ValueError(
            "EPS export is no longer supported by Kaleido. Please use SVG or PDF instead."
        )
    from kaleido.errors import ChromeNotFoundError

    try:
        kopts = {}
        if defaults.plotlyjs:
            kopts["plotlyjs"] = defaults.plotlyjs
        if defaults.mathjax:
            kopts["mathjax"] = defaults.mathjax
        if defaults.headers:
            kopts["headers"] = defaults.headers

        width = (
            width
            or fig_dict.get("layout", {}).get("width")
            or fig_dict.get("layout", {})
            .get("template", {})
            .get("layout", {})
            .get("width")
            or defaults.default_width
        )
        height = (
            height
            or fig_dict.get("layout", {}).get("height")
            or fig_dict.get("layout", {})
            .get("template", {})
            .get("layout", {})
            .get("height")
            or defaults.default_height
        )

        img_bytes = kaleido.calc_fig_sync(
            fig_dict,
            opts=dict(
                format=format or defaults.default_format,
                width=width,
                height=height,
                scale=scale or defaults.default_scale,
            ),
            topojson=defaults.topojson,
            kopts=kopts,
        )
    except ChromeNotFoundError:
        raise RuntimeError(PLOTLY_GET_CHROME_ERROR_MSG)

    return img_bytes


def write_image(
    fig: Union[dict, plotly.graph_objects.Figure],
    file: Union[str, Path],
    format: Union[str, None] = None,
    scale: Union[int, float, None] = None,
    width: Union[int, None] = None,
    height: Union[int, None] = None,
    validate: bool = True,
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

    format: str
        (optional) The desired image format. One of:
          - 'png'
          - 'jpg' or 'jpeg'
          - 'webp'
          - 'svg'
          - 'pdf'
        Defaults to the file extension of `file`, if given; otherwise
        defaults to `plotly.io.defaults.default_format`.

    width: int
        (optional) The width of the exported image in layout pixels. If the
        `scale` property is 1.0, this will also be the width of the exported image
        in physical pixels. Defaults to `plotly.io.defaults.default_width`.

    height: int
        (optional) The height of the exported image in layout pixels. If the
        `scale` property is 1.0, this will also be the height of the exported image
        in physical pixels. Defaults to `plotly.io.defaults.default_height`.

    scale: int or float
        (optional) The scale factor to use when exporting the figure. A scale
        factor larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions, while a scale factor of
        less than 1.0 will decrease the image resolution. Defaults to
        `plotly.io.defaults.default_scale`.

    validate: bool
        (optional) True if the figure should be validated before being converted
        to an image, False otherwise. Defaults to True.

    Returns
    -------
    None
    """

    if not kaleido_available():
        raise RuntimeError(KALEIDO_REQUIRED_MSG)

    # Try to cast `file` as a pathlib object `path`.
    path = as_path_object(file)

    # Infer image format if not specified
    format = infer_format(path, format)

    # Request image
    # Do this first so we don't create a file if image conversion fails
    img_data = to_image(
        fig,
        format=format,
        scale=scale,
        width=width,
        height=height,
        validate=validate,
    )

    # Open file
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


def write_images(
    fig: Union[
        List[Union[dict, plotly.graph_objects.Figure]],
        Union[dict, plotly.graph_objects.Figure],
    ],
    file: Union[List[Union[str, Path]], Union[str, Path]],
    format: Union[List[Union[str, None]], Union[str, None]] = None,
    scale: Union[List[Union[int, float, None]], Union[int, float, None]] = None,
    width: Union[List[Union[int, None]], Union[int, None]] = None,
    height: Union[List[Union[int, None]], Union[int, None]] = None,
    validate: Union[List[bool], bool] = True,
) -> None:
    """
    Write multiple images to files or writeable objects. This is much faster than
    calling write_image() multiple times. This function can only be used with the Kaleido
    engine, v1.0.0 or greater.

    This function accepts the same arguments as write_image() (minus the `engine` argument),
    except that any of the arguments may be either a single value or an iterable of values.
    If multiple arguments are iterable, they must all have the same length.

    Parameters
    ----------
    fig:
        List of figure objects or dicts representing a figure.
        Also accepts a single figure or dict representing a figure.

    file: str, pathlib.Path, or list of (str or pathlib.Path)
        List of str or pathlib.Path objects representing local file paths to write to.
        Can also be a single str or pathlib.Path object if fig argument is
        a single figure or dict representing a figure.

    format: str or list of (str or None)
        (optional) The image format to use for exported images. One of:
          - 'png'
          - 'jpg' or 'jpeg'
          - 'webp'
          - 'svg'
          - 'pdf'
        Defaults to the file extension of `file`, if given; otherwise
        defaults to `plotly.io.defaults.default_format`.

        Pass a list to specify formats for each figure in the list passed to `fig`.
        Pass a str to apply the same format to all exported images.

    width: int or list of (int or None)
        (optional) The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels. Defaults to `plotly.io.defaults.default_width`.

        Pass a list to specify widths for each figure in the list passed to `fig`.
        Pass an int to apply the same width to all exported images.

    height: int or list of (int or None)
        (optional) The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels. Defaults to `plotly.io.defaults.default_height`.

        Pass a list to specify heights for each figure in the list passed to `fig`.
        Pass an int to apply the same height to all exported images.

    scale: int, float, or list of (int, float, or None)
        (optional) The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions, while a scale factor of
        less than 1.0 will decrease the image resolution. Defaults to
        `plotly.io.defaults.default_scale`.

        Pass a list to specify scale for each figure in the list passed to `fig`.
        Pass an int or float to apply the same scale to all exported images.

    validate: bool or list of bool
        (optional) True if the figure should be validated before being converted
        to an image, False otherwise. Defaults to True.

        Pass a list to specify validation for each figure in the list passed to `fig`.
        Pass a boolean to apply the same validation setting to all figures.

    Returns
    -------
    None
    """

    if not kaleido_available():
        raise RuntimeError(KALEIDO_REQUIRED_MSG)

    # Broadcast arguments into correct format for passing to Kaleido
    arg_dicts = broadcast_args_to_dicts(
        fig=fig,
        file=file,
        format=format,
        scale=scale,
        width=width,
        height=height,
        validate=validate,
    )

    # For each dict:
    #   - convert figures to dicts (and validate if requested)
    #   - try to cast `file` as a Path object
    for d in arg_dicts:
        d["fig"] = validate_coerce_fig_to_dict(d["fig"], d["validate"])
        d["file"] = as_path_object(d["file"])

    # Reshape arg_dicts into correct format for passing to Kaleido
    # We call infer_format() here rather than above so that the `file` argument
    # has already been cast to a Path object.
    # Also insert defaults for any missing arguments as needed
    kaleido_specs = [
        dict(
            fig=d["fig"],
            path=d["file"],
            opts=dict(
                format=infer_format(d["file"], d["format"]) or defaults.default_format,
                width=d["width"] or defaults.default_width,
                height=d["height"] or defaults.default_height,
                scale=d["scale"] or defaults.default_scale,
            ),
            topojson=defaults.topojson,
        )
        for d in arg_dicts
    ]

    from kaleido.errors import ChromeNotFoundError

    try:
        kopts = {}
        if defaults.plotlyjs:
            kopts["plotlyjs"] = defaults.plotlyjs
        if defaults.mathjax:
            kopts["mathjax"] = defaults.mathjax
        if defaults.headers:
            kopts["headers"] = defaults.headers
        kaleido.write_fig_from_object_sync(
            kaleido_specs,
            kopts=kopts,
        )
    except ChromeNotFoundError:
        raise RuntimeError(PLOTLY_GET_CHROME_ERROR_MSG)


def full_figure_for_development(
    fig: Union[dict, plotly.graph_objects.Figure],
    warn: bool = True,
    as_dict: bool = False,
) -> Union[plotly.graph_objects.Figure, dict]:
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

    if not kaleido_available():
        raise RuntimeError(KALEIDO_REQUIRED_MSG)

    if warn:
        warnings.warn(
            "full_figure_for_development is not recommended or necessary for "
            "production use in most circumstances. \n"
            "To suppress this warning, set warn=False"
        )

    bytes = kaleido.calc_fig_sync(
        fig,
        opts=dict(format="json"),
    )
    fig = json.loads(bytes.decode("utf-8"))

    if as_dict:
        return fig
    else:
        import plotly.graph_objects as go

        return go.Figure(fig, skip_invalid=True)


def plotly_get_chrome() -> None:
    """
    Install Google Chrome for Kaleido (Required for Plotly image export).
    This function is a command-line wrapper for `plotly.io.get_chrome()`.

    When running from the command line, use the command `plotly_get_chrome`;
    when calling from Python code, use `plotly.io.get_chrome()`.
    """

    usage = """
Usage: plotly_get_chrome [-y] [--path PATH]

Installs Google Chrome for Plotly image export.

Options:
  -y  Skip confirmation prompt
  --path PATH  Specify the path to install Chrome. Must be a path to an existing directory.
  --help  Show this message and exit.
"""

    # Handle command line arguments
    import sys

    cli_args = sys.argv

    # Handle "-y" flag
    cli_yes = "-y" in cli_args
    if cli_yes:
        cli_args.remove("-y")

    # Handle "--path" flag
    chrome_install_path = None
    if "--path" in cli_args:
        path_index = cli_args.index("--path") + 1
        if path_index < len(cli_args):
            chrome_install_path = cli_args[path_index]
            cli_args.remove("--path")
            cli_args.remove(chrome_install_path)
            chrome_install_path = Path(chrome_install_path)

    # If any arguments remain, command syntax was incorrect -- print usage and exit
    if len(cli_args) > 1:
        print(usage)
        sys.exit(1)

    if not cli_yes:
        print(
            f"""
Plotly will install a copy of Google Chrome to be used for generating static images of plots.
Chrome will be installed at: {chrome_install_path}"""
        )
        response = input("Do you want to proceed? [y/n] ")
        if not response or response[0].lower() != "y":
            print("Cancelled")
            return
    print("Installing Chrome for Plotly...")
    exe_path = get_chrome(chrome_install_path)
    print("Chrome installed successfully.")
    print(f"The Chrome executable is now located at: {exe_path}")


def get_chrome(path: Union[str, Path, None] = None) -> Path:
    """
    Get the path to the Chrome executable for Kaleido.
    This function is used by the `plotly_get_chrome` command line utility.

    Parameters
    ----------
    path: str or Path or None
        The path to the directory where Chrome should be installed.
        If None, the default download path will be used.
    """
    if not kaleido_available():
        raise RuntimeError(KALEIDO_REQUIRED_MSG)

    # Use default download path if no path was specified
    if path:
        user_specified_path = True
        chrome_install_path = Path(path)  # Ensure it's a Path object
    else:
        user_specified_path = False
        from choreographer.cli.defaults import default_download_path

        chrome_install_path = default_download_path

    # If install path was chosen by user, make sure there is an existing directory
    # located at chrome_install_path; otherwise fail
    if user_specified_path:
        if not chrome_install_path.exists():
            raise ValueError(
                f"""
The specified install path '{chrome_install_path}' does not exist.
Please specify a path to an existing directory using the --path argument,
or omit the --path argument to use the default download path.
"""
            )
        # Make sure the path is a directory
        if not chrome_install_path.is_dir():
            raise ValueError(
                f"""
The specified install path '{chrome_install_path}' already exists but is not a directory.
Please specify a path to an existing directory using the --path argument,
or omit the --path argument to use the default download path.
"""
            )

    return kaleido.get_chrome_sync(path=chrome_install_path)


__all__ = ["to_image", "write_image", "full_figure_for_development"]
