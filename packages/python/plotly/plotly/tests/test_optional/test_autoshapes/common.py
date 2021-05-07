def _cmp_partial_dict(a, b):
    ret = True
    if len(list(b.keys())) == 0:
        return False
    for k in b.keys():
        try:
            v = a[k]
            ret &= v == b[k]
        except KeyError:
            return False
    return ret


def _check_figure_layout_objects(test_input, expected, fig, layout_key="shapes"):
    f, kwargs = test_input
    f(fig, **kwargs)
    ret = True
    if len(fig.layout[layout_key]) != len(expected):
        assert False
    for s, d in zip(fig.layout[layout_key], expected):
        ret &= _cmp_partial_dict(s, d)
    assert ret
