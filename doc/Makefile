# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
PYTHON        ?= python3
SPHINXOPTS    ?= -j $(shell nproc || getconf _NPROCESSORS_ONLN || 1)
SPHINXBUILD   ?= $(PYTHON) -m sphinx
SPHINXPROJ    = plotly
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


clean:
	rm -rf $(BUILDDIR)/*
	rm -rf auto_examples/
	rm -rf gen_modules/

