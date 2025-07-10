# Manage plotly.py project.

RUN = uv run
PACKAGE_DIRS = _plotly_utils plotly
CODE_DIRS = ${PACKAGE_DIRS} scripts

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

## sync: update Python packages
sync:
	uv sync --extra dev
