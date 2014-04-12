all : pull_subs install

sync_mplexporter : plotly/mplexporter
	rsync -r plotly/mplexporter/mplexporter plotly/matplotlylib/

install : sync_mplexporter
	python setup.py install

pull_subs : plotly/mplexporter plotly/graph_reference
	git submodule foreach 'git pull origin master'
