The test_init test the plotly.py initialization logic and must be run individually.

For example, run...
```
$ pytest test_init/test_lazy_imports.py
$ pytest test_init/test_dependencies_not_imported.py
``` 

instead of ...
```
$ pytest test_init
``` 
