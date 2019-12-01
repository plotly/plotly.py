---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.7
  plotly:
    description: How to make Ternary Contour Plots in Python with plotly
    display_as: scientific
    language: python
    layout: base
    name: Ternary contours
    order: 19
    page_type: u-guide
    permalink: python/ternary-contour/
    thumbnail: thumbnail/ternary-contour.jpg
---

## Ternary contour plots


A ternary contour plots represents isovalue lines of a quantity defined inside a [ternary diagram](https://en.wikipedia.org/wiki/Ternary_plot), i.e. as a function of three variables which sum is constant. Coordinates of the ternary plot often correspond to concentrations of three species, and the quantity represented as contours is some property (e.g., physical, chemical, thermodynamical) varying with the composition.

For ternary contour plots, use the figure factory ``create_ternary_contour``. The figure factory interpolates between given data points in order to compute the contours.

Below we represent an example from metallurgy, where the mixing enthalpy is represented as a contour plot for aluminum-copper-yttrium (Al-Cu-Y) alloys.

#### Simple ternary contour plot with plotly

```python
import plotly.figure_factory as ff
import numpy as np
Al = np.array([0. , 0. , 0., 0., 1./3, 1./3, 1./3, 2./3, 2./3, 1.])
Cu = np.array([0., 1./3, 2./3, 1., 0., 1./3, 2./3, 0., 1./3, 0.])
Y = 1 - Al - Cu
# synthetic data for mixing enthalpy
# See https://pycalphad.org/docs/latest/examples/TernaryExamples.html
enthalpy = (Al - 0.01) * Cu * (Al - 0.52) * (Cu - 0.48) * (Y - 1)**2
fig = ff.create_ternary_contour(np.array([Al, Y, Cu]), enthalpy,
                                pole_labels=['Al', 'Y', 'Cu'],
                                interp_mode='cartesian')
fig.show()
```

#### Customized ternary contour plot

```python
import plotly.figure_factory as ff
import numpy as np
Al = np.array([0. , 0. , 0., 0., 1./3, 1./3, 1./3, 2./3, 2./3, 1.])
Cu = np.array([0., 1./3, 2./3, 1., 0., 1./3, 2./3, 0., 1./3, 0.])
Y = 1 - Al - Cu
# synthetic data for mixing enthalpy
# See https://pycalphad.org/docs/latest/examples/TernaryExamples.html
enthalpy = 2.e6 * (Al - 0.01) * Cu * (Al - 0.52) * (Cu - 0.48) * (Y - 1)**2 - 5000
fig = ff.create_ternary_contour(np.array([Al, Y, Cu]), enthalpy,
                                pole_labels=['Al', 'Y', 'Cu'],
                                interp_mode='cartesian',
                                ncontours=20,
                                colorscale='Viridis',
                                showscale=True,
                                title='Mixing enthalpy of ternary alloy')
fig.show()
```

#### Ternary contour plot with lines only

```python
import plotly.figure_factory as ff
import numpy as np
Al = np.array([0. , 0. , 0., 0., 1./3, 1./3, 1./3, 2./3, 2./3, 1.])
Cu = np.array([0., 1./3, 2./3, 1., 0., 1./3, 2./3, 0., 1./3, 0.])
Y = 1 - Al - Cu
# synthetic data for mixing enthalpy
# See https://pycalphad.org/docs/latest/examples/TernaryExamples.html
enthalpy = 2.e6 * (Al - 0.01) * Cu * (Al - 0.52) * (Cu - 0.48) * (Y - 1)**2 - 5000
fig = ff.create_ternary_contour(np.array([Al, Y, Cu]), enthalpy,
                                pole_labels=['Al', 'Y', 'Cu'],
                                interp_mode='cartesian',
                                ncontours=20,
                                coloring='lines')
fig.show()
```

#### Ternary contour plot with data points

With `showmarkers=True`, data points used to compute the contours are also displayed. They are best visualized for contour lines (no solid coloring). At the moment data points lying on the edges of the diagram are not displayed, this will be improved in future versions.

```python
import plotly.figure_factory as ff
import numpy as np
Al, Cu = np.mgrid[0:1:7j, 0:1:7j]
Al, Cu = Al.ravel(), Cu.ravel()
mask = Al + Cu <= 1
Al, Cu = Al[mask], Cu[mask]
Y = 1 - Al - Cu

enthalpy = (Al - 0.5) * (Cu - 0.5) * (Y - 1)**2
fig = ff.create_ternary_contour(np.array([Al, Y, Cu]), enthalpy,
                                pole_labels=['Al', 'Y', 'Cu'],
                                ncontours=20,
                                coloring='lines',
                                showmarkers=True)
fig.show()
```

#### Interpolation mode

Two modes are available in order to interpolate between data points: interpolation in Cartesian space (`interp_mode='cartesian'`) or interpolation using the [isometric log-ratio transformation](https://link.springer.com/article/10.1023/A:1023818214614) (see also [preprint](https://www.researchgate.net/profile/Leon_Parent2/post/What_is_the_best_approach_for_diagnosing_nutrient_disorders_and_formulating_fertilizer_recommendations/attachment/59d62a69c49f478072e9cf3f/AS%3A272541220835360%401441990298625/download/Egozcue+et+al+2003.pdf)),  `interp_mode='ilr'`. The `ilr` transformation preserves metrics in the [simplex](https://en.wikipedia.org/wiki/Simplex) but is not defined on its edges.

```python
a, b = np.mgrid[0:1:20j, 0:1:20j]
mask = a + b <= 1
a, b = a[mask], b[mask]
coords = np.stack((a, b, 1 - a - b))
value = np.sin(3.2 * np.pi * (a + b)) + np.sin(3 * np.pi * (a - b))
fig = ff.create_ternary_contour(coords, value, ncontours=9)
fig.show()
```

```python
a, b = np.mgrid[0:1:20j, 0:1:20j]
mask = a + b <= 1
a, b = a[mask], b[mask]
coords = np.stack((a, b, 1 - a - b))
value = np.sin(3.2 * np.pi * (a + b)) + np.sin(3 * np.pi * (a - b))
fig = ff.create_ternary_contour(coords, value, interp_mode='cartesian',
                                ncontours=9)
fig.show()
```
