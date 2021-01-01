import pandas as pd
import numpy as np


def ols(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Ordinary Least Squares (OLS) trendline function

    Requires `statsmodels` to be installed.

    This trendline function causes fit results to be stored within the figure,
    accessible via the `plotly.express.get_trendline_results` function. The fit results
    are the output of the `statsmodels.api.OLS` function.

    Valid keys for the `trendline_options` dict are:

    - `add_constant` (`bool`, default `True`): if `False`, the trendline passes through
    the origin but if `True` a y-intercept is fitted.

    - `log_x` and `log_y` (`bool`, default `False`): if `True` the OLS is computed with
    respect to the base 10 logarithm of the input. Note that this means no zeros can
    be present in the input.
    """

    import statsmodels.api as sm

    add_constant = trendline_options.get("add_constant", True)
    log_x = trendline_options.get("log_x", False)
    log_y = trendline_options.get("log_y", False)

    if log_y:
        if np.any(y == 0):
            raise ValueError(
                "Can't do OLS trendline with `log_y=True` when `y` contains zeros."
            )
        y = np.log10(y)
        y_label = "log10(%s)" % y_label
    if log_x:
        if np.any(x == 0):
            raise ValueError(
                "Can't do OLS trendline with `log_x=True` when `x` contains zeros."
            )
        x = np.log10(x)
        x_label = "log10(%s)" % x_label
    if add_constant:
        x = sm.add_constant(x)
    fit_results = sm.OLS(y, x, missing="drop").fit()
    y_out = fit_results.predict()
    if log_y:
        y_out = np.power(10, y_out)
    hover_header = "<b>OLS trendline</b><br>"
    if len(fit_results.params) == 2:
        hover_header += "%s = %g * %s + %g<br>" % (
            y_label,
            fit_results.params[1],
            x_label,
            fit_results.params[0],
        )
    elif not add_constant:
        hover_header += "%s = %g * %s<br>" % (y_label, fit_results.params[0], x_label,)
    else:
        hover_header += "%s = %g<br>" % (y_label, fit_results.params[0],)
    hover_header += "R<sup>2</sup>=%f<br><br>" % fit_results.rsquared
    return y_out, hover_header, fit_results


def lowess(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """LOcally WEighted Scatterplot Smoothing (LOWESS) trendline function

    Requires `statsmodels` to be installed.

    Valid keys for the `trendline_options` dict are:

    - `frac` (`float`, default `0.6666666`): the `frac` parameter from the
    `statsmodels.api.nonparametric.lowess` function
    """
    import statsmodels.api as sm

    frac = trendline_options.get("frac", 0.6666666)
    y_out = sm.nonparametric.lowess(y, x, missing="drop", frac=frac)[:, 1]
    hover_header = "<b>LOWESS trendline</b><br><br>"
    return y_out, hover_header, None


def ma(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Moving Average (MA) trendline function

    Requires `pandas` to be installed.

    The `trendline_options` dict is passed as keyword arguments into the
    `pandas.Series.rolling` function.
    """
    y_out = pd.Series(y, index=x_raw).rolling(**trendline_options).mean()[non_missing]
    hover_header = "<b>MA trendline</b><br><br>"
    return y_out, hover_header, None


def ewma(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Exponentially Weighted Moving Average (EWMA) trendline function

    Requires `pandas` to be installed.

    The `trendline_options` dict is passed as keyword arguments into the
    `pandas.Series.ewma` function.
    """
    y_out = pd.Series(y, index=x_raw).ewm(**trendline_options).mean()[non_missing]
    hover_header = "<b>EWMA trendline</b><br><br>"
    return y_out, hover_header, None
