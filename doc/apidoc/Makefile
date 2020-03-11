# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python3 -m sphinx
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
	sphinx-apidoc -o generated ../../packages/python/plotly/plotly ../../packages/python/plotly/plotly/validators ../../packages/python/plotly/plotly/tests ../../packages/python/plotly/plotly/matplotlylib/ ../../packages/python/plotly/plotly/offline ../../packages/python/plotly/plotly/api
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	rename 's/graph_objs/graph_objects/' _build/html/*.html _build/html/generated/*.html
	sed -i 's/graph_objs/graph_objects/g' _build/html/*.html _build/html/generated/*.html
