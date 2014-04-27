all : pull_subs install

sync_mplexporter : plotly/mplexporter
	rsync -r plotly/mplexporter/mplexporter plotly/matplotlylib/

sync_chunked_requests : plotly/chunked_requests
	rsync -r plotly/chunked_requests/chunked_requests plotly/plotly/

install : sync_mplexporter sync_chunked_requests
	python setup.py install

pull_subs : plotly/mplexporter plotly/graph_reference chriddyp/chunked_requests
	git submodule foreach 'git pull origin master'

html_nbs : notebooks
	cd notebooks; \
		ipython nbconvert 'Plotly and Python.ipynb'; \
		python add_some_css.py 'Plotly and Python.html'
	cd notebooks; \
		ipython nbconvert 'Plotly and mpld3.ipynb'; \
		python add_some_css.py 'Plotly and mpld3.html'
	cd notebooks; \
		ipython nbconvert Quickstart.ipynb; \
		python add_some_css.py Quickstart.html
