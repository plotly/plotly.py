all : readme

readme :
	@echo ""
	@less make_instructions.txt

install : sync_subs
	@echo ""
	@echo "Installing Python API with make"
	python setup.py install

sync_subs : sync_mpl sync_chunked sync_refs
	@echo ""
	@echo "Submodules synced"

pull_subs : pull_mpl pull_chunked pull_refs
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

sync_refs : submodules/graph_reference
	@echo ""
	@echo "Syncing graph_reference directories"
	rsync -r submodules/graph_reference plotly/

pull_refs : submodules/graph_reference
	@echo ""
	@echo "Pulling down updates from graph_reference"
	cd submodules/graph_reference; git pull origin master

pull_mpl : submodules/mplexporter
	@echo ""
	@echo "Pulling down updates from mplexporter"
	cd submodules/mplexporter; git pull origin master

pull_chunked : submodules/chunked_requests
	@echo ""
	@echo "Pulling down updates from chunked_requests"
	cd submodules/chunked_requests; git pull origin master
	
