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
    name: Alignment Chart
    order: 1
    page_type: u-guide
    permalink: python/alignment-chart/
    thumbnail: thumbnail/alignment-chart.png
---

## Default AlignmentChart
An example of a default AlignmentChart component without any extra properties

```python
import urllib.request as urlreq

from jupyter_dash import JupyterDash
import dash_bio as dashbio

app = JupyterDash(__name__)

data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'alignment_viewer_p53.fasta'
).read().decode('utf-8')

app.layout = dashbio.AlignmentChart(
    id='my-default-alignment-viewer',
    data=data
)

app.run_server(mode="inline")
```

## Consensus Sequence
Toggle the display of the consensus sequence at the bottom of the heatmap.

```python
import urllib.request as urlreq

import dash_bio as dashbio
from jupyter_dash import JupyterDash

app = JupyterDash(__name__)

data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/alignment_viewer_p53.fasta').read().decode('utf-8')

app.layout = dashbio.AlignmentChart(
    data=data,
    showconsensus=False
)

app.run_server(mode="inline")
```

## Tile Size
Change the height and/or width of the tiles.


```python
import urllib.request as urlreq
import dash_bio as dashbio

data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/alignment_viewer_p53.fasta').read().decode('utf-8')

app.layout = dashbio.AlignmentChart(
    data=data,
    tilewidth=50
)
    
app.run_server(mode="inline")
```

## AlignmentChart Properties
> Access this documentation in your Python terminal with:
> 
> ```>>> help(dash_bio.AlignmentChart)```
> 
> Our recommended IDE for writing Dash apps is Dash Enterprise's Data Science Workspaces, which has typeahead support for Dash Component Properties. Find out if your company is using Dash Enterprise.

**id** (_string_; optional): The ID of this component, used to identify dash components in callbacks. The ID needs to be unique across all of the components in an app.

**colorscale** (_string_ | _dict_; default `'clustal2'`): Colorscale in 'buried', 'cinema', 'clustal', 'clustal2', 'helix', 'hydrophobicity' 'lesk', 'mae', 'nucleotide', 'purine', 'strand', 'taylor', 'turn', 'zappo', or your own colorscale as a {'nucleotide': COLOR} dict. Note that this is NOT a standard plotly colorscale.

**conservationcolor** (_string_; optional): Color of the conservation secondary barplot, in common name, hex, rgb or rgba format.

**conservationcolorscale** (_string_ | _list_; default `'Viridis'`): Colorscale of the conservation barplot, in Plotly colorscales (e.g. 'Viridis') or as custom Plotly colorscale under a list format. Note that this conservationcolorscale argument does NOT follow the same format as the colorscale argument.

**conservationmethod** (_a value equal to: 'conservation', 'entropy'_; default `'entropy'`): Whether to use most conserved ratio (MLE) 'conservation' or normalized entropy 'entropy' to determine conservation, which is a value between 0 and 1 where 1 is most conserved.

**conservationopacity** (_number_ | _string_; optional): Opacity of the conservation secondary barplot as a value between 0 and 1.

**correctgap** (_boolean_; default `True`): Whether to normalize the conservation barchart By multiplying it elementwise with the gap barchart, as to lower the conservation values across sequences regions with many gaps.

**data** (_string_; optional): Input data, either in FASTA or Clustal format.

**eventDatum** (_string_; optional): A Dash prop that returns data on clicking, hovering or resizing the viewer.

**extension** (_string_; default `'fasta'`): Format type of the input data, either in FASTA or Clustal.

**gapcolor** (_string_; default `'grey'`): Color of the gap secondary barplot, in common name, hex, rgb or rgba format.

**gapcolorscale** (_string_ | _list_; optional): Colorscale of the gap barplot, in Plotly colorscales (e.g. 'Viridis') or as custom Plotly colorscale under a list format. Note that this conservationcolorscale argument does NOT follow the same format as the colorscale argument.

**gapopacity** (_number_ | _string_; optional): Opacity of the gap secondary barplot as a value between 0 and 1.

**groupbars** (_boolean_; default `False`): If both conservation and gap are enabled, toggles whether to group bars or to stack them as separate subplots. No effect if not both gap and conservation are shown.

**height** (_number_ | _string_; default `900`): Width of the Viewer. Property takes precedence over tilesheight if both are set.

**numtiles** (_number_; optional): Sets how many tiles to display across horitontally. If enabled, overrides tilewidth and sets the amount of tiles directly based off that value.

**opacity** (_number_ | _string_; optional): Opacity of the main plot as a value between 0 and 1.

**overview** (_a value equal to: 'heatmap', 'slider', 'none'_; default `heatmap`): Toggles whether the overview should be a heatmap, a slider, or none.

**scrollskip** (_number_; default `10`): If overview is set to 'scroll', determines how many tiles to skip with each slider movement. Has no effect if scroll is not enabled (such as with overview or none).

**showconsensus** (_boolean_; default `True`): Displays toggling the consensus sequence, where each nucleotide in the consensus sequence is the argmax of its distribution at a set nucleotide.

**showconservation** (_boolean_; default `True`): Enables the display of conservation secondary barplot where the most conserved nucleotides or amino acids get greater bars.

**showgap** (_boolean_; default `True`): Enables the display of gap secondary barplot where the sequence regions with the fewest gaps get the greatest bars.

**showid** (_boolean_; default `True`): Toggles displaying sequence IDs at left of alignment.

**showlabel** (_boolean_; default `True`): Toggles displaying sequence labels at left of alignment.

**textcolor** (_string_; optional): Color of the nucleotide labels, in common name, hex, rgb or rgba format. If left blank, handled by the colorscale automatically.

**textsize** (_number_ | _string_; default `10`): Size of the nucleotide labels, as a number.

**tickstart** (_number_ | _string_; optional): Determines where to start annotating the first tile. If let blank will be automatically determined by Plotly. Equivalent to Plotly's tick0 property. Does not function if overview mode 'slider' is applied. (Current bug).

**ticksteps** (_number_ | _string_; optional): Determines at what interval to keep annotating the tiles. If left blank will be automatially determined by Plotly. Equivalent to Plotly's dtick property. Does not function if overview mode 'slider' is applied. (Current bug).

**tileheight** (_number_; default `16`): Sets how many pixels each nucleotide/amino acid on the Alignment Chart takes up vertically. If enabled, set height dynamically.

**tilewidth** (_number_; default `16`): Sets how many pixels each nucleotide/amino acid on the Alignment Chart takes up horizontally. The total number of tiles (numtiles) seen horizontally is automatically determined by rounding the Viewer width divided by the tile width. the Viewwer width divided by the tile witdth.

**width** (_number_ | _string_; optional): Width of the Viewer. Property takes precedence over tileswidth and numtiles if either of them is set.

```python

```
