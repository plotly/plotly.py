# Manage plotly.py project.

RUN = uv run
PACKAGE_DIRS = _plotly_utils plotly
CODE_DIRS = ${PACKAGE_DIRS} scripts

ifdef MKDOCS_ALL
EXAMPLE_SRC =  $(wildcard doc/python/*.md)
else
EXAMPLE_SRC = doc/python/cone-plot.md doc/python/strip-charts.md
endif

EXAMPLE_DST = $(patsubst doc/python/%.md,pages/examples/%.md,${EXAMPLE_SRC})

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## docs: rebuild documentation
.PHONY: docs
docs:
	${RUN} mkdocs build

## docs-lint: check documentation
docs-lint:
	${RUN} pydoclint ${PACKAGE_DIRS}

## docs-tmp: rebuild documentation saving Markdown in ./tmp
docs-tmp:
	MKDOCS_TEMP_DIR=./docs_tmp ${RUN} mkdocs build

## examples-batch: generate Markdown for all doc/python
examples-batch:
	${RUN} bin/run_markdown.py --outdir pages/examples --inline --verbose 1 ${EXAMPLE_SRC}

## examples: generate Markdown for individual doc/python
examples: ${EXAMPLE_DST}

pages/examples/%.md: doc/python/%.md
	${RUN} bin/run_markdown.py --outdir pages/examples --inline --verbose 2 $<

## format: reformat code
format:
	${RUN} ruff format ${CODE_DIRS}

## generate: generate code
generate:
	${RUN} bin/generate_code.py --codedir plotly
	${RUN} ruff format plotly

## lint: check the code
lint:
	${RUN} ruff check ${CODE_DIRS}

## test: run tests
test:
	${RUN} pytest tests

## updatejs: update JavaScript bundle
updatejs:
	${RUN} bin/updatejs.py --codedir plotly

## --: --

## clean: clean up repository
clean:
	@find . -name '*~' -delete
	@find . -name '.DS_Store' -delete
	@rm -rf .coverage
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -rf dist
	@rm -rf docs
	@rm -rf pages/examples

## sync: update Python packages
sync:
	uv sync --extra dev
