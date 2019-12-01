import inspect
import plotly.graph_objects as go

members = inspect.getmembers(go)

functions, classes, submodules = [], [], []

for m in members:
    print(m)
    if m[0] not in go.__all__:
        continue
    if m[1].__doc__ and "is deprecated" in m[1].__doc__:
        continue
    elif inspect.isfunction(m[1]):
        functions.append(m[0])
    elif inspect.isclass(m[1]):
        classes.append(m[0])
    elif inspect.ismodule(m[1]):
        submodules.append(m[0])

classes.sort()
submodules.sort()

classes_str = "\n".join(classes)
# print(classes_str)

submodules_str = "\n".join(submodules)
# print(submodules_str)

autosubmodule = ""

for submodule in submodules:
    autosubmodule += (
        ".. automodule:: plotly.graph_objects.%s\n    :members:\n\n" % submodule
    )
print(autosubmodule)
