default : push

push : graph_objs_meta.json
	python graph_objs_meta.py
	git add -u
	git commit -m 'auto-commit and push from make'
	git push origin master:master