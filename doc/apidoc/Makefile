# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -m sphinx
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# For sphinx-apidoc the first positional path is the module to document
# then all the other ones are paths to exclude for the doc generation
%: Makefile
	sed -i 's/:class:`plotly.graph_objects/:class:`plotly.graph_objs/g' ../../plotly/graph_objs/*.py
	sed -i 's/:class:`plotly.graph_objects/:class:`plotly.graph_objs/g' ../../plotly/graph_objs/*/*.py
	sed -i 's/:class:`plotly.graph_objects/:class:`plotly.graph_objs/g' ../../plotly/graph_objs/*/*/*.py
	sed -i 's/:class:`plotly.graph_objects/:class:`plotly.graph_objs/g' ../../plotly/graph_objs/*/*/*/*.py
	# Copy _plotly_utils file so that they appear in the API doc
	cp ../../_plotly_utils/colors/sequential.py ../../_plotly_utils/colors/diverging.py ../../_plotly_utils/colors/qualitative.py ../../_plotly_utils/colors/cyclical.py ../../_plotly_utils/colors/colorbrewer.py ../../_plotly_utils/colors/carto.py ../../_plotly_utils/colors/cmocean.py ../../plotly/colors
	cp ../../_plotly_utils/colors/sequential.py ../../_plotly_utils/colors/diverging.py ../../_plotly_utils/colors/qualitative.py ../../_plotly_utils/colors/cyclical.py ../../_plotly_utils/colors/colorbrewer.py ../../_plotly_utils/colors/carto.py ../../_plotly_utils/colors/cmocean.py ../../plotly/express/colors
	# Run sphinx-apidoc script to create hierarchy of rst files to generate
	# docstrings. The first path is the one to process, the following ones
	# are excluded from the search.
	rm -rf _build generated
	sphinx-apidoc -M -o generated ../../plotly ../../plotly/validators ../../plotly/tests ../../plotly/matplotlylib/ ../../plotly/offline ../../plotly/api
	# Run sphinx-build to build html pages from the rst pages
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	git checkout -- ../../plotly/graph_objs
	# Remove files which were added only for docstring generation
	rm ../../plotly/colors/diverging.py ../../plotly/colors/sequential.py ../../plotly/colors/qualitative.py ../../plotly/colors/cyclical.py ../../plotly/colors/colorbrewer.py ../../plotly/colors/carto.py ../../plotly/colors/cmocean.py
	rm ../../plotly/express/colors/diverging.py ../../plotly/express/colors/sequential.py ../../plotly/express/colors/qualitative.py ../../plotly/express/colors/cyclical.py ../../plotly/express/colors/colorbrewer.py ../../plotly/express/colors/carto.py ../../plotly/express/colors/cmocean.py
	rename 's/graph_objs/graph_objects/' _build/html/*.html _build/html/generated/*.html _build/html/generated/generated/*.html
	mv _build/html/generated/plotly.graph_objs.html _build/html/generated/plotly.graph_objects.html
	sed -i 's/graph_objs/graph_objects/g' _build/html/*.html
	sed -i 's/graph_objs/graph_objects/g' _build/html/*.inv
	sed -i 's/graph_objs/graph_objects/g' _build/html/*.js
	sed -i 's/graph_objs/graph_objects/g' _build/html/generated/*.html
	sed -i 's/graph_objs/graph_objects/g' _build/html/generated/generated/*.html
