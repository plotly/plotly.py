---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
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
    version: 3.6.5
  plotly:
    description: Discussion of key differences between IPython and Python
    display_as: file_settings
    language: python
    layout: base
    name: IPython vs Python
    order: 25
    permalink: python/ipython-vs-python/
    thumbnail: thumbnail/venn.jpg
---

#### What is the difference between IPython and Python?
While these two names are quite similar, they refer to entirely different things.<br>
<br>
[**Python**](https://www.python.org/) is a general-purpose programming language. It was created in the late 1980s by Guido van Rossum. It is now one of the most popular languages in the world. It is routinely used by system administrators and web developers. Also, many scientists are using Python thanks to libraries such as NumPy, SciPy, pandas, and matplotlib. The ease of use of Python and its dynamic nature make it a very productive language.<br>
<br>
[**IPython**](https://ipython.org/) is an interactive command-line terminal for Python. It was created by Fernando Perez in 2001. IPython offers an enhanced read-eval-print loop (REPL) environment particularly well adapted to scientific computing.


![IPython terminal](https://s3-us-west-1.amazonaws.com/plotly-tutorials/plotly-documentation/images/ipython-console.png)


In other words, IPython is a powerful *interface* to the Python language. But it is certainly not the only one. Besides IPython, the most common way to use Python is to write *scripts*, files with the `.py` extension.<br>
<br>
A script contains a list of commands to execute in order. It runs from start to finish and display some output. On the contrary, with IPython, you generally write one command at a time and you get the results instantly. This is a completely different way of working with Python. When analyzing data or running computational models, you need this sort of interactivity to explore them efficiently.


#### Jupyter Notebook


In 2011, IPython introduced a new tool named the **Notebook**. Inspired by scientific programs like Mathematica or Sage, the Notebook offers a modern and powerful web interface to Python.


![IPython Notebook](https://s3-us-west-1.amazonaws.com/plotly-tutorials/plotly-documentation/images/notebook.png)


Compared to the original IPython terminal, the Notebook offers a more convenient text editor, the possibility to write rich text, and improved graphical capabilities. Also, since it is a web interface, it can integrate many of the existing web libraries for data visualization, including *plotly.js*.<br>
<br>
In 2015, the IPython developers made a major code reorganization of their ever-growing project. The Notebook is now called the Jupyter Notebook. This interface can be used not only with Python but with dozens of other languages such as R and Julia. IPython is now the name of the Python backend (aka kernel).<br>
<br>
In conclusion, IPython and Jupyter are great interfaces to the Python language. If you're learning Python, using the IPython terminal or the Jupyter Notebook is highly recommended.<br>
<br>
This was a guest article written by Cyrille Rossant, author of Learning IPython for Interactive Computing and Data Visualization, second edition and IPython Interactive Computing and Visualization Cookbook.
