import plotly.graph_objects as go
from plotly import basedatatypes

# Search down an object's composition tree and find fields with a given name


def find_field(obj, field, basepath="", max_path_len=80, forbidden=["parent"]):
    if obj is not None and len(basepath) < max_path_len:
        for f in dir(obj):
            joined_path = ".".join([basepath, f])
            if f == field:
                print(joined_path)
            if (
                (f not in forbidden)
                and (not f.startswith("_"))
                and (not f.endswith("_"))
            ):
                find_field(eval("obj.%s" % (f,)), field, joined_path)


def find_all_xy_traces():
    for field in dir(go):
        call_str = "go.%s" % (field,)
        call = eval(call_str)
        try:
            if issubclass(call, basedatatypes.BaseTraceType):
                obj = call()
                if "xaxis" in obj and "yaxis" in obj:
                    yield (call_str)
        except TypeError:
            pass


# s=go.Scatter()
# s=go.Bar()
# find_field(s,"color",basepath="scatter")
# print()
# find_field(s,"color",basepath="bar")

for call_str in find_all_xy_traces():
    call = eval(call_str)
    find_field(call(), "color", basepath=call_str)
    print()
