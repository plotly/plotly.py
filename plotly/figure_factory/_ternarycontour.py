from __future__ import absolute_import
import plotly.colors as clrs
from plotly.graph_objs import graph_objs as go
from plotly import exceptions, optional_imports

np = optional_imports.get_module('numpy')
sk = optional_imports.get_module('skimage')
scipy_interp = optional_imports.get_module('scipy.interpolate')


def _replace_zero_coords(ternary_data, delta=0.0005):
    """
    Replaces zero ternary coordinates with delta and normalize the new
    triplets (a, b, c).

    Parameters
    ----------

    ternary_data : ndarray of shape (N, 3)

    delta : float
        Small float to regularize logarithm.

    Notes
    -----
    Implements a method
    by J. A. Martin-Fernandez,  C. Barcelo-Vidal, V. Pawlowsky-Glahn,
    Dealing with zeros and missing values in compositional data sets
    using nonparametric imputation, Mathematical Geology 35 (2003),
    pp 253-278.
    """
    zero_mask = (ternary_data == 0)
    info_row_zero = zero_mask.sum(axis=-1, keepdims=True)

    if delta is None:
        delta = 0.001
    unity_complement = 1 - delta * info_row_zero
    if np.any(unity_complement) < 0:
        raise ValueError('The provided value of delta led to negative'
                         'ternary coords.Set a smaller delta')
    ternary_data = np.where(zero_mask, delta, unity_complement * ternary_data)
    return ternary_data.squeeze()


def _ilr_transform(barycentric):
    """

    """
    barycentric = np.asarray(barycentric)
    x0 = np.log(barycentric[0] / barycentric[1]) / np.sqrt(2)
    x1 = 1. / np.sqrt(6) * np.log(barycentric[0] * barycentric[1] /
                                  barycentric[2] ** 2)
    ilr_tdata = np.stack((x0, x1))
    return ilr_tdata


def _ilr_inverse(x): #ilr: R^2 -->S^2 (2 simplex)
    #x an n  list of 2-lists or an array of shape (n,2),
    # implementation of a method presented in:
    # An algebraic method to compute isometric logratio transformation and back transformation of compositional data
    # Jarauta-Bragulat, E.; Buenestado, P.; Hervada-Sala, C.
    # in Proc of the Annual Conf of the Intl Assoc for Math Geology, 2003, pp 31-30
    #x should ne an array of shape (n,2)
    x = np.array(x)
    if x.shape[-1] != 2:
        raise ValueError(f'your data must be 2d points, not {x.shape[-1]}-points')
    if len(x.shape) == 1:
        x = x.reshape(1, 2)
    matrix = np.array([[ 0.5,  1 ,  1. ],
                       [-0.5,  1 ,  1. ],
                       [ 0. ,  0. ,  1. ]])
    s = np.sqrt(2)/2
    t = np.sqrt(3/2)
    Sk = np.einsum('ik, kj -> ij', np.array([[s, t],[-s, t]]), x.T)
    Z = -np.log(1+np.exp(Sk).sum(axis=0))
    log_barycentric = np.einsum('ik, kj -> ij', matrix, np.stack((2*s*x[:, 0], t*x[:, 1], Z)))
    iilr_tdata = np.exp(log_barycentric).T
    return iilr_tdata if x.shape[0] > 1 else iilr_tdata.squeeze()


def _transform_barycentric_cartesian():
    """
    Returns the transformation matrix from barycentric to cartesian
    coordinates and conversely.
    """
    # reference triangle
    tri_verts = np.array([[0.5, np.sqrt(3) / 2], [0, 0], [1, 0]])
    M = np.array([tri_verts[:, 0], tri_verts[:, 1], np.ones(3)])
    return M, np.linalg.inv(M)


def _colors(ncontours, colormap=None):
    if colormap in clrs.PLOTLY_SCALES.keys():
        #cmap = clrs.validate_colors(colormap, colortype='rgb')
        cmap = clrs.PLOTLY_SCALES[colormap]
    else:
        raise exceptions.PlotlyError(
                "Colorscale must be a valid Plotly Colorscale."
                "The available colorscale names are {}".format(
                    clrs.PLOTLY_SCALES.keys()))
    values = np.linspace(0, 1, ncontours)
    keys = np.array([pair[0] for pair in cmap])
    cols = np.array([pair[1] for pair in cmap])
    inds = np.searchsorted(keys, values)
    if '#'in cols[0]:
        cols = [clrs.label_rgb(clrs.hex_to_rgb(col)) for col in cols]
    colors = [cols[0]]
    for ind, val in zip(inds[1:], values[1:]):
        key1, key2 = keys[ind - 1], keys[ind]
        interm = (val - key1) / (key2 - key1)
        col = clrs.find_intermediate_color(cols[ind - 1],
                                           cols[ind], interm,
                                           colortype='rgb')
        colors.append(col)
    return colors


def _contour_trace(x, y, z, ncontours=None,
                   colorscale='Electric',
                   linecolor='rgb(150,150,150)', interp_mode='cartesian',
                   coloring=None):
    """
    Contour trace in Cartesian coordinates.

    Parameters
    ==========

    x, y : array-like
        Cartesian coordinates
    z : array-like
        Field to be represented as contours.
    """
    if ncontours is None:
        ncontours = 5
    colors = _colors(ncontours, colorscale)
    traces = []
    mask_nan = np.isnan(z)
    mask_ok = np.logical_not(mask_nan)
    values = np.linspace(z[mask_ok].min(), z[mask_ok].max(), 
                            ncontours + 2)[1:-1]
    M, invM = _transform_barycentric_cartesian()
    dx = (x.max() - x.min())/x.size
    dy = (y.max() - y.min())/y.size
    zz = np.copy(z)
    zz[np.isnan(z)] = (z[mask_ok].min()
            - 10. * (z[mask_ok].max() - z[mask_ok].min()))
    for i, val in enumerate(values):
        contour_level = sk.measure.find_contours(zz, val)
        # stop
        for contour in contour_level:
            yy, xx = contour.T
            if interp_mode == 'cartesian':
                bar_coords = np.dot(invM,
                        np.stack((dx * xx, dy * yy, np.ones(xx.shape))))
            elif interp_mode == 'ilr':
                bar_coords = _ilr_inverse(np.stack((dx * xx + x.min(),
                                                    dy * yy + y.min())).T).T
            a, b, c = bar_coords
            tooltip = _tooltip(a, b, c, val)
            _col = colors[i] if coloring == 'lines' else linecolor
            trace = dict(
                type='scatterternary', text=tooltip,
                a=a, b=b, c=c, mode='lines',
                line=dict(color=_col, shape='spline', width=1),
                fill='toself',
                fillcolor=colors[i],
                hoverinfo='text',
                showlegend=True,
                name='%.2f' % val
            )
            if coloring == 'lines':
                trace['fill'] = None
            traces.append(trace)
    return traces


def _ternary_layout(title='Ternary contour plot', width=550, height=525,
                    fontfamily='Balto, sans-serif', colorbar_fontsize=14,
                    plot_bgcolor='rgb(240,240,240)',
                    pole_labels=['a', 'b', 'c'], label_fontsize=16):
    """
    Layout of ternary contour plot, to be passed to ``go.FigureWidget``
    object.

    Parameters
    ==========
    title : str or None
        Title of ternary plot
    width : int
        Figure width.
    height : int
        Figure height.
    fontfamily : str
        Family of fonts
    colorbar_fontsize : int
        Font size of colorbar.
    plot_bgcolor :
        color of figure background
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    label_fontsize : int
        Font size of pole labels.
    """
    return dict(title=title,
                width=width, height=height,
                font=dict(family=fontfamily, size=colorbar_fontsize),
                plot_bgcolor=plot_bgcolor,
                ternary=dict(sum=1,
                             aaxis=dict(title=pole_labels[0],
                                        min=0.01, linewidth=2,
                                        ticks='outside'),
                             baxis=dict(title=pole_labels[1],
                                        min=0.01, linewidth=2,
                                        ticks='outside'),
                             caxis=dict(title=pole_labels[2],
                                        min=0.01, linewidth=2,
                                        ticks='outside')),
                showlegend=False,
                )


def _tooltip(a, b, c, z, mode='proportions'):
    """
    Tooltip annotations to be displayed on hover.

    Parameters
    ==========

    N : int
        Number of annotations along each axis.
    bar_coords : array-like
        Barycentric coordinates.
    grid_z : array
        Values (e.g. elevation values) at barycentric coordinates.
    xy1 : array-like
        Cartesian coordinates.
    mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    """
    N = len(a)
    if np.isscalar(z):
        z = z * np.ones(N)
    if mode == 'proportions' or mode == 'proportion':
        tooltip = [
         'a: %.2f' % round(a[i], 2) +
         '<br>b: %.2f' % round(b[i], 2) +
         '<br>c: %.2f' % round(c[i], 2) +
         '<br>z: %.2f' % round(z[i], 2) for i in range(N)]
    elif mode == 'percents' or mode == 'percent':
        tooltip = [
         'a: %d' % int(100 * a[i] + 0.5) +
         '<br>b: %d' % int(100 * b[i] + 0.5) +
         '<br>c: %d' % int(100 * c[i] + 0.5) +
         '<br>z: %.2f' % round(z[i], 2) for i in range(N)]
    else:
        raise ValueError("""tooltip mode must be either "proportions" or
                          "percents".""")
    return tooltip


def _prepare_barycentric_coord(b_coords):
    """
    Check ternary coordinates and return the right barycentric coordinates.
    """
    if not isinstance(b_coords, (list, np.ndarray)):
        raise ValueError('Data  should be either an array of shape (n,m), or a list of n m-lists, m=2 or 3')
    b_coords = np.asarray(b_coords)
    if b_coords.shape[0] not in (2, 3):
        raise ValueError('A point should have  2 (a, b) or 3 (a, b, c)  barycentric coordinates')
    if ((len(b_coords) == 3) and
         not np.allclose(b_coords.sum(axis=0), 1, rtol=0.01)):
        msg = "The sum of coordinates should be one for all data points"
        raise ValueError(msg)
    A, B = b_coords[:2]
    C = 1 - (A + B)
    if np.any(np.stack((A, B, C)) < 0):
        raise ValueError('Barycentric coordinates should be positive.')
    return A, B, C


def _central_proj(mdata):

    #array of shape(n,3) or a n-list of 3-lists of positive numbers,
    #returns for each row [a, b, c]--> np.array([a,b,c])/(a+b+c)

    mdata=np.asarray(mdata)
    if mdata.ndim > 2:
        raise ValueError("this function requires 2d arrays")
    if mdata.shape[-1] != 3:
        raise ValueError('data must have 3 coordinates')

    if mdata.ndim == 1:
         mdata = np.atleast_2d(mdata)

    if np.any(mdata < 0):
        raise ValueError("Data should be positive")

    if np.all(mdata == 0, axis=1).sum() > 0:
        raise ValueError("this projection can be applied only to non zero triplets")
    barycentric = mdata / mdata.sum(axis=1, keepdims=True)
    return barycentric.squeeze()



def _compute_grid(coordinates, values, tooltip_mode, interp_mode='cartesian'):
    """
    Compute interpolation of data points on regular grid in Cartesian
    coordinates.

    Parameters
    ==========

    coordinates : array-like
        Barycentric coordinates of data points.
    values : 1-d array-like
        Data points, field to be represented as contours.
    tooltip_mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    """
    A, B, C = _prepare_barycentric_coord(coordinates)
    if interp_mode == 'cartesian':
        M, invM = _transform_barycentric_cartesian()
        coord_points = np.einsum('ik, kj -> ij', M, np.stack((A, B, C)))
    elif interp_mode == 'ilr':
        mdata = _replace_zero_coords(np.stack((A, B, C)).T)
        coord_points = _ilr_transform(mdata.T)
    else:
        raise ValueError("interp_mode should be cartesian or ilr")
    xx, yy = coord_points[:2]
    x_min, x_max = xx.min(), xx.max()
    y_min, y_max = yy.min(), yy.max()
    n_interp = max(400, int(np.sqrt(len(values))))
    gr_x = np.linspace(x_min, x_max, n_interp)
    gr_y = np.linspace(y_min, y_max, n_interp)
    grid_x, grid_y = np.meshgrid(gr_x, gr_y)
    grid_z = scipy_interp.griddata(coord_points[:2].T, values,
                                   (grid_x, grid_y),
                                   method='cubic')
    return grid_z, gr_x, gr_y


def create_ternarycontour(coordinates, values, pole_labels=['a', 'b', 'c'],
                          tooltip_mode='proportions', width=500, height=500,
                          ncontours=None,
                          showscale=False, coloring=None,
                          colorscale='Greens',
                          reversescale=False,
                          plot_bgcolor='rgb(240,240,240)',
                          title=None,
                          interp_mode='ilr',
                          showmarkers=False):
    """
    Ternary contour plot.

    Parameters
    ----------

    coordinates : list or ndarray
        Barycentric coordinates of shape (2, N) or (3, N) where N is the
        number of data points. The sum of the 3 coordinates is expected
        to be 1 for all data points.
    values : array-like
        Data points of field to be represented as contours.
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    tooltip_mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    width : int
        Figure width.
    height : int
        Figure height.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    showscale : bool, default False
        If True, a colorbar showing the color scale is displayed.
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    showlabels : bool, default False
        For line contours (coloring='lines'), the value of the contour is
        displayed if showlabels is True.
    colorscale : None or array-like
        colorscale of the contours.
    reversescale : bool
        Reverses the color mapping if true. If true, `zmin`
        will correspond to the last color in the array and
        `zmax` will correspond to the first color.
    plot_bgcolor :
        color of figure background
    title : str or None
        Title of ternary plot
    smoothing : bool
        If True, contours are smoothed.

    Examples
    ========

    Example 1: ternary contour plot with filled contours

    # Define coordinates
    a, b = np.mgrid[0:1:20j, 0:1:20j]
    mask = a + b <= 1
    a = a[mask].ravel()
    b = b[mask].ravel()
    c = 1 - a - b
    # Values to be displayed as contours
    z = a * b * c
    fig = ff.create_ternarycontour(np.stack((a, b, c)), z)

    It is also possible to give only two barycentric coordinates for each
    point, since the sum of the three coordinates is one:

    fig = ff.create_ternarycontour(np.stack((a, b)), z)

    Example 2: ternary contour plot with line contours

    fig = ff.create_ternarycontour(np.stack((a, b)), z, coloring='lines')

    Labels of contour plots can be displayed on the contours:

    fig = ff.create_ternarycontour(np.stack((a, b)), z, coloring='lines',
                                   showlabels=True)

    """
    grid_z, gr_x, gr_y = _compute_grid(coordinates, values,
                                       tooltip_mode,
                                       interp_mode=interp_mode)

    layout = _ternary_layout(pole_labels=pole_labels,
                             width=width, height=height, title=title,
                             plot_bgcolor=plot_bgcolor)

    contour_trace = _contour_trace(gr_x, gr_y, grid_z,
                                   ncontours=ncontours,
                                   colorscale=colorscale,
                                   interp_mode=interp_mode,
                                   coloring=coloring)
    fig = go.Figure(data=contour_trace, layout=layout)

    if showmarkers:
        a, b, c = coordinates
        tooltip = _tooltip(a, b, c, values)
        fig.add_scatterternary(a=a, b=b, c=c,
                               mode='markers',
                               marker={'color': values,
                                       'colorscale': colorscale},
                               text=tooltip,
                               hoverinfo='text')
    if showscale:
        colorbar = dict({'type': 'scatterternary',
                         'a': [None], 'b': [None],
                         'c': [None],
                         'marker': {'cmin': values.min(),
                                    'cmax': values.max(),
                                    'colorscale': colorscale,
                                    'showscale': True},
                         'mode': 'markers'})
        fig.add_trace(colorbar)

    return fig
