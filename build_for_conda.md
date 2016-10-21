Initial setup was done using:

`conda skeleton pypi plotly --version 1.12.4`

To test all imports, manually added following dependencies at runtime:
```
- matplotlib
- numpy
- ipython
- ipywidgets
```

I also had to change all `module/submodule` in the test imports to `module.submodule`.

Finally, build and test the created version:

`conda build plotly`

Currently, the updated (version 1.12.4) conda package sits at https://anaconda.org/chohner/plotly. There seems to be an old offial package at https://anaconda.org/plotly/plotly.
