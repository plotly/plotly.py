The ultimate reference of Plotly's JSON graph format.

Used as the help reference in [Plotly-Python library](https://github.com/plotly/python-api) and in [Plotly's web documentation](https://plot.ly/api/rest).

#### Files in this repo:

- For reference, see [graph_objs_meta.json](/graph_objs_meta.json)
- To contribute, edit [graph_objs_meta.py](/graph_objs_meta.py)


#### Format

A fully described `key` is an object with the keys: `val_types`, `required`, `type`, `description`. 
- `val_types`: Valid types (e.g. `array_like of strings`, `number: in [0, 1]`)
- `required`: Whether the key is required or not to create the chart type
- `type`: `style` | `plot_info` | `object` | `data`
- `description`: Self explanatory 

#### Contributing
1 - Add and modified keys in the `graph_objs_meta.py` file.  There are a bunch of shortcuts in that file, so you might have to hunt around a bit to check if something was already defined or not.

2 - Generate JSON
```bash
python graph_objs_meta.py
```

3 - Commit and push

Alternatively, if you're working directly in master, like a boss, you can do this:
1 - Add and modified keys in the `graph_objs_meta.py` file.

2 - MAKE SURE YOU PULL FIRST! (no one likes dealing with conflicts...)
```bash
git pull origin master
```

3 - Use the little makefile shortcut to generate the json, add, commit, and push
```bash
make push
```

#### Testing

When you upload to any branch, Nose is going to test the
test_graph_references.py file. To see if you're push passed, go to:
https://circleci.com/gh/plotly/graph_reference
