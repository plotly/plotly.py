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
	python -c "import requests;\
               from requests.compat import json as _json;\
               response = requests.get('https://api.plot.ly/v2/plot-schema?sha1');\
               f = open('plotly/package_data/default-schema.json', 'w');\
               _json.dump(response.json()['schema'], f, indent=4,\
                          sort_keys=True, separators=(',', ': '));\
               f.close()"
	@echo "Auto-generating graph objects based on updated default-schema."
	python update_graph_objs.py

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

update_plotlyjs_for_offline :
	@echo "Updating plotly.js for Offline Mode"
	@echo "------------------"
	python -c "import urllib2;\
				cdn_url = 'https://cdn.plot.ly/plotly-latest.min.js';\
				response = urllib2.urlopen(cdn_url);\
				html = response.read();\
				f = open('./plotly/package_data/plotly.min.js', 'w');\
    		 	f.write(html);\
				f.close()"
	@echo "---------------------------------"
	@echo "Remember to update the CHANGELOG!"
