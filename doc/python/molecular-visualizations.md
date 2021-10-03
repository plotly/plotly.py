---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
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
    version: 3.9.6
  plotly:
    # description:
    display_as: bio
    language: python
    layout: base
    name: Molecular visualizations
    order: 1
    page_type: u-guide
    permalink: python/molecular-visualizations/
    thumbnail: thumbnail/molecular_visualizations.png
---

## Molecular Visualizations


### Default Molecule3dViewer
An example of a default Molecule3dViewer component without any extra properties.

```python
import json
import urllib.request as urlreq

import dash_bio as dashbio
from jupyter_dash import JupyterDash

app = JupyterDash(__name__)

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()

model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

app.layout = dashbio.Molecule3dViewer(
    styles=styles_data,
    modelData=model_data,
    backgroundOpacity=0.2
)

app.run_server(mode="inline")
```

### Labels
Add labels corresponding to the atom of the molecule. Label styles can be set with additional parameters. For styling keys, see.

```python
import json
import urllib.request as urlreq

import dash_bio as dashbio
from jupyter_dash import JupyterDash

app = JupyterDash(__name__)

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()

model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

app.layout = dashbio.Molecule3dViewer(
    styles=styles_data,
    modelData=model_data,
    labels=[
        {'text': 'Residue Name: GLY1', 'fontColor': 'red', 'font': 'Courier New, monospace'},
        {'text': 'Residue Chain: A', 'position': {'x': 15.407, 'y': -8.432, 'z': 6.573}}
    ],
)

app.run_server(mode="inline")
```

### Isosurfaces
Render a 3D isosurface. Volumetric orbital data must be provided in the cube file format.

```python
import json
import urllib.request as urlreq

import dash_bio as dashbio
from jupyter_dash import JupyterDash

app = JupyterDash(__name__)

model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/benzene_model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/benzene_style_data.js').read()

cube_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/benzene-homo.cube').read().decode('utf-8')

model_data = json.loads(model_data)
styles_data = json.loads(styles_data)

app.layout = dashbio.Molecule3dViewer(
    styles=styles_data,
    modelData=model_data,
    selectionType='atom',
    orbital={
        'cube_file': cube_data,
        'iso_val': 0.1,
        'opacity': 1.0,
        'positiveVolumetricColor': 'red',
        'negativeVolumetricColor': 'blue',
    }
)

app.run_server(mode="inline")
```

### Molecule3dViewer Properties


> Access this documentation in your Python terminal with:
> ```
> >>> help(dash_bio.Molecule3dViewer)
> ```
> Our recommended IDE for writing Dash apps is Dash Enterprise's
> **[Data Science Workspaces](https://plotly.com/dash/workspaces)**,
> which has typeahead support for Dash Component Properties.
> **[Find out if your company is using
> Dash Enterprise](https://go.plotly.com/company-lookup)**.


**id** (_string_; optional): The ID used to identify this component in callbacks.

**atomLabelsShown** (_boolean_; optional): Property to either show or hide labels.

**backgroundColor** (_string_; default ```'#FFFFFF'```): Property to change the background color of the molecule viewer.

**backgroundOpacity** (_number_; default ```0```): Property to change the background opacity - ranges from 0 to 1.

**labels** (_list_ of dicts; optional): Labels corresponding to the atoms of the molecule. Each label has a ```text``` field, a string containing the label content, and can have many other styling fields as described in **https://3dmol.csb.pitt.edu/doc/types.html#LabelSpec**.

**modelData** (_dict_; optional): The data that will be used to display the molecule in 3D The data will be in JSON format and should have two main dictionaries - atoms, bonds.

```modelData``` is a dict with keys:
- **atoms** (_list_; optional)
- **bonds** (_list_; optional)

**orbital** (_dict_; optional): Add an isosurface from volumetric data provided in the ```cube_file```.

```orbital``` is a dict with keys:
- **cube_file** (_string_; optional): The filepath containing raw volumetric data for vertex coloring.
- **iso_val** (_number_; optional): The isovalue to draw the surface at.
- **negativeVolumetricColor** (_string_; optional): Color for the negative value of the isosurface orbital.
- **opacity** (_number_; optional): Transparency of the surface, between 0 and 1.
- **positiveVolumetricColor** (_string_; optional): Color for the positive value of the isosurface orbital.

**selectedAtomIds** (_list_; optional): Property that stores a list of all selected atoms.

**selectionType** (_a value equal to: 'atom', 'residue', 'chain'_; default ```'atom'```): The selection type - may be atom, residue or chain.

**shapes** (_list of dicts_; optional): Add a predefined renderable shape objects to the molecule. Valid shape types are Arrow, Sphere, and Cylinder.

**styles** (_list of dicts_; optional): Property that can be used to change the representation of the molecule. Options include sticks, cartoon and sphere.

```styles``` is a list of dicts with keys:
- **color** (_string_; optional)
- **visualization_type** (_a value equal to: 'cartoon', 'sphere', 'stick'_; optional)

**zoom** (_dict_; default ```{ factor: 0.8, animationDuration: 0, fixedPath: False,}```): Zoom the current view by a constant factor, with optional parameters to modify the duration and motion of the zoom animation.

```zoom``` is a dict with keys:
- **animationDuration** (_number_; optional): An optional parameter that denotes the duration of a zoom animation, in milliseconds.
- **factor** (_number_; optional): Magnification factor. Values greater than 1 will zoom, in, less than one will zoom out. Default 2.
- **fixedPath** (_boolean_; optional): If True, animation is constrained to requested motion, overriding updates that happen during the animation.

**zoomTo** (_dict_; default ```{ sel: {}, animationDuration: 0, fixedPath: False,}```): Zoom to center of atom selection.

```zoomTo``` is a dict with keys:
- **animationDuration** (_number_; optional): An optional parameter that denotes the duration of a zoom animation , in milliseconds.
- **fixedPath** (_boolean_; optional): If True, animation is constrained to requested motion, overriding updates that happen during the animation.
- **sel** (_dict_; optional): Selection specification specifying model and atom properties to select. Default: all atoms in viewer.<br>
  ```sel``` is a dict with keys:
    - **chain** (_string_; optional): Chain that the residue is located on.
    - **resi** (_number_; optional): The index value used to identify the residue; residues are numbered sequentially starting from 1.


