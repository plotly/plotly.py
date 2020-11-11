# %%
from random import triangular
import plotly.figure_factory as ff

z = [[round(triangular(0.01, 0.1), 3) for j in range(10)] for i in range(10)]
# ff.create_annotated_heatmap(z, colorscale='greens').show()
ff.create_annotated_heatmap(z, colorscale='RdBu', zmid=0).show()
# %%
ff.create_annotated_heatmap(z, colorscale='Greens', zmin=-0.3, zmax=0.1).show()

# %%
ff.create_annotated_heatmap(z, colorscale='greens', zmin=0, zmax=1).show()

# %%
