# How to contribute?


## To add and/or modify keys in graph reference

Clone and/or pull the latest master version: 
```
$ git pull origin master
```

Make a new branch (for testing purposes) and checkout: 
```
$ git branch your_branch_name
$ git checkout your_branch_name
```

Add and modified keys in `graph_objs_meta.py`:

1. with special attention to existing shortcuts (search for key shortcuts with
   `@key@`),
1. if you are making a new shortcut function use `output` (see `@output@` to
   format the meta dictionary,
1. (more step-by-step info coming soon ...),
1. update the table content in `graph_objs_mets-toc.md` if keys were added or if
   the order was modified.

Generate the JSON files:
```
$ python graph_objs_meta.py
```

Add, commit and push to online repo:
```
$ git add .
$ git commit 
$ git push origin your_branch_name
```


## Testing

When you push any branch to the online repo, Nose is going to test the
`test_graph_references.py` file. 

To see if your push passed, go
[here](https://circleci.com/gh/plotly/graph_reference).


## To see the changes in the APIs' help function and online documentation

1. The `graph_reference` submodule in the
   [Python-API](https://github.com/plotly/python-api) needs to be updated and
   tests need to pass,
1. the [Python-API](https://github.com/plotly/python-api) needs to be pushed to
   pip,
1. our backend's `requirements.txt` needs to be updated with the new version of
   the Python-API.


