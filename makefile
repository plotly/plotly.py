all : readme

readme :
	@echo ""
	@less make_instructions.txt

setup_subs :
	@echo "Deleting old submodule locations, if they exist"
	rm -rf plotly/mplexporter
	rm -rf plotly/chunked_requests
	rm -rf plotly/plotly/chunked_requests
	rm -rf plotly/matplotlylib/mplexporter
	@echo "Initializing submodules listed in project"
	git submodule init
	@echo "Updating submodules to their respective commits"
	git submodule update
	make sync_subs

update_default_schema :
	@echo "Making sure the default-schema.json file is up to date"
	python -c "import json;\
               from plotly.graph_reference import GRAPH_REFERENCE;\
               f = open('plotly/graph_reference/default-schema.json', 'w');\
               json.dump(GRAPH_REFERENCE, f, indent=4, sort_keys=True,\
                   separators=(',', ': '));\
               f.close()"

install : sync_subs
	@echo ""
	@echo "Installing Python API with make"
	python setup.py install

sync_subs : sync_mpl sync_chunked
	@echo ""
	@echo "Submodules synced"

pull_subs : pull_mpl pull_chunked
	@echo ""
	@echo "Submodules pulled"

sync_mpl : submodules/mplexporter
	@echo ""
	@echo "Syncing mplexporter directories"
	rsync -r submodules/mplexporter/mplexporter plotly/matplotlylib/

sync_chunked : submodules/chunked_requests
	@echo ""
	@echo "Syncing chunked_requests directories"
	rsync -r submodules/chunked_requests/chunked_requests plotly/plotly/

pull_mpl : submodules/mplexporter
	@echo ""
	@echo "Pulling down updates from mplexporter"
	cd submodules/mplexporter; git pull origin master

pull_chunked : submodules/chunked_requests
	@echo ""
	@echo "Pulling down updates from chunked_requests"
	cd submodules/chunked_requests; git pull origin master
