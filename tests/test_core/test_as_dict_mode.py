import plotly.graph_objects as go


class TestTraceAsDict:
    """Test _as_dict=True on trace constructors."""

    def test_returns_dict_with_type(self):
        result = go.Scatter(x=[1, 2], y=[3, 4], mode="lines", _as_dict=True)
        assert isinstance(result, dict)
        assert result == {"type": "scatter", "x": [1, 2], "y": [3, 4], "mode": "lines"}

    def test_preserves_nested_dicts(self):
        result = go.Scatter(
            x=[1], y=[2], line=dict(color="red", width=2), _as_dict=True
        )
        assert result["line"] == {"color": "red", "width": 2}

    def test_default_unchanged(self):
        """Without _as_dict, constructors must return graph objects as before."""
        assert not isinstance(go.Scatter(x=[1], y=[2]), dict)
        assert not isinstance(go.Scatter(x=[1], y=[2], _as_dict=False), dict)


class TestFigureAsDict:
    """Test _as_dict=True on go.Figure construction and methods."""

    def test_construction(self):
        fig = go.Figure(
            data=[go.Scatter(x=[1], y=[2], _as_dict=True)],
            layout={"title": "T"},
            _as_dict=True,
        )
        assert isinstance(fig, go.Figure)
        assert fig._as_dict_mode is True
        # data stored as list of dicts, layout as raw dict
        assert fig._data == [{"type": "scatter", "x": [1], "y": [2]}]
        assert fig._layout == {"title": "T"}
        # Property getters return raw containers
        assert isinstance(fig.data, tuple)
        assert fig.layout is fig._layout

    def test_construction_from_dict(self):
        """Accept figure-like dict input (e.g. from to_dict())."""
        fig = go.Figure(
            data={"data": [{"type": "bar", "x": [1]}], "layout": {"height": 400}},
            _as_dict=True,
        )
        assert fig._data == [{"type": "bar", "x": [1]}]
        assert fig._layout == {"height": 400}

    def test_add_traces(self):
        fig = go.Figure(_as_dict=True)
        # Single item (not list)
        fig.add_traces(go.Scatter(x=[1], y=[2], _as_dict=True))
        # List of items
        fig.add_traces([go.Bar(x=["a"], y=[1], _as_dict=True)])
        assert len(fig._data) == 2
        assert fig._data[0]["type"] == "scatter"
        assert fig._data[1]["type"] == "bar"

    def test_update_layout(self):
        fig = go.Figure(_as_dict=True)
        # kwargs path
        fig.update_layout(title={"text": "Hello"})
        # dict1 path — recursive merge
        fig.update_layout({"title": {"font": {"size": 20}}})
        assert fig._layout["title"] == {"text": "Hello", "font": {"size": 20}}
        # overwrite=True
        fig.update_layout(title={"text": "New"}, overwrite=True)
        assert fig._layout["title"] == {"text": "New"}

    def test_add_annotation_and_shape(self):
        fig = go.Figure(_as_dict=True)
        fig.add_annotation(text="Note", x=1, y=2, showarrow=False)
        fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1)
        assert fig._layout["annotations"][0]["text"] == "Note"
        assert fig._layout["shapes"][0]["type"] == "rect"

    def test_add_vline_and_hline(self):
        fig = go.Figure(_as_dict=True)
        fig.add_vline(x=5)
        fig.add_hline(y=3)
        shapes = fig._layout["shapes"]
        assert len(shapes) == 2
        # vline: x fixed, yref is domain
        assert shapes[0]["x0"] == 5 and shapes[0]["x1"] == 5
        assert "y domain" in shapes[0]["yref"]
        # hline: y fixed, xref is domain
        assert shapes[1]["y0"] == 3 and shapes[1]["y1"] == 3
        assert "x domain" in shapes[1]["xref"]

    def test_add_vline_with_annotation(self):
        fig = go.Figure(_as_dict=True)
        fig.add_vline(x=5, annotation=dict(text="Limit"))
        assert len(fig._layout["shapes"]) == 1
        assert fig._layout["annotations"][0]["text"] == "Limit"

    def test_bulk_annotations(self):
        """Annotations use list.append (O(N)), not tuple concat."""
        fig = go.Figure(_as_dict=True)
        for i in range(100):
            fig.add_annotation(text=f"L{i}", x=i, y=i, showarrow=False)
        assert len(fig._layout["annotations"]) == 100

    def test_serialization(self):
        fig = go.Figure(
            data=[go.Scatter(x=[1, 2], y=[3, 4], _as_dict=True)],
            _as_dict=True,
        )
        fig.update_layout(title="Test")
        d = fig.to_dict()
        assert d["data"][0]["type"] == "scatter"
        assert d["layout"]["title"] == "Test"
        j = fig.to_json()
        assert isinstance(j, str) and '"scatter"' in j

    def test_default_figure_unchanged(self):
        """Without _as_dict, Figure must behave exactly as before."""
        fig = go.Figure(data=[go.Scatter(x=[1], y=[2])])
        assert hasattr(fig.data[0], "to_plotly_json")
        assert not getattr(fig, "_as_dict_mode", False)


class TestOutputEquivalence:
    """Fast-path output must match standard path for explicit properties."""

    def test_trace_equivalence(self):
        default = go.Scatter(x=[1], y=[2], mode="lines")
        fast = go.Scatter(x=[1], y=[2], mode="lines", _as_dict=True)
        for key in ["x", "y", "mode", "type"]:
            assert default.to_plotly_json()[key] == fast[key]

    def test_figure_data_equivalence(self):
        default = go.Figure(data=[go.Scatter(x=[1], y=[2])])
        fast = go.Figure(data=[go.Scatter(x=[1], y=[2], _as_dict=True)], _as_dict=True)
        dd, fd = default.to_dict()["data"][0], fast.to_dict()["data"][0]
        for key in ["type", "x", "y"]:
            assert dd[key] == fd[key]
