all : pull_all install

sync_mplexporter : plotly/mplexporter
	rsync -r plotly/mplexporter/mplexporter plotly/matplotlylib/

sync_chunked_requests : plotly/chunked_requests
	rsync -r plotly/chunked_requests/chunked_requests plotly/plotly/

install : sync_mplexporter sync_chunked_requests
	python setup.py install

pull_refs : plotly/graph_reference
	cd plotly/graph_reference; git pull origin master

pull_mpl : plotly/mplexporter
	cd plotly/mplexporter; git pull origin master

pull_chunked : plotly/chunked_requests
	cd plotly/chunked_requests; git pull origin master

pull_all : pull_refs pull_mpl pull_chunked

pull_subs : 
	echo separated submodule pulls, run pull_refs, pull_chunked, or pull_mpl

show_subs : plotly/graph_reference plotly/chunked_requests plotly/mplexporter
	git for each ‘git remote -v’

html_nbs : notebooks
	cd notebooks; \
		ipython nbconvert 'Plotly and Python.ipynb'; \
		python add_some_css.py 'Plotly and Python.html'
	cd notebooks; \
		ipython nbconvert 'Plotly and matplotlib and mpld3.ipynb'; \
		python add_some_css.py 'Plotly and matplotlib and mpld3.html'
	cd notebooks; \
		ipython nbconvert Quickstart.ipynb; \
		python add_some_css.py Quickstart.html
