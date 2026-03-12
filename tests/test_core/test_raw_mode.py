import plotly.graph_objects as go


class TestTraceRaw:
    """Test raw=True on trace constructors."""

    def test_returns_dict_with_type(self):
        result = go.Scatter(x=[1, 2], y=[3, 4], mode="lines", raw=True)
        assert isinstance(result, dict)
        assert result == {"type": "scatter", "x": [1, 2], "y": [3, 4], "mode": "lines"}

    def test_preserves_nested_dicts(self):
        result = go.Scatter(x=[1], y=[2], line=dict(color="red", width=2), raw=True)
        assert result["line"] == {"color": "red", "width": 2}

    def test_default_unchanged(self):
        """Without raw, constructors must return graph objects as before."""
        assert not isinstance(go.Scatter(x=[1], y=[2]), dict)
        assert not isinstance(go.Scatter(x=[1], y=[2], raw=False), dict)


class TestFigureRaw:
    """Test raw=True on go.Figure construction and methods."""

    def test_construction(self):
        fig = go.Figure(
            data=[go.Scatter(x=[1], y=[2], raw=True)],
            layout={"title": "T"},
            raw=True,
        )
        assert isinstance(fig, go.Figure)
        assert fig._raw is True
        assert fig._data == [{"type": "scatter", "x": [1], "y": [2]}]
        assert fig._layout == {"title": "T"}
        assert isinstance(fig.data, tuple)
        assert fig.layout is fig._layout

    def test_construction_from_dict(self):
        """Accept figure-like dict input (e.g. from to_dict())."""
        fig = go.Figure(
            data={"data": [{"type": "bar", "x": [1]}], "layout": {"height": 400}},
            raw=True,
        )
        assert fig._data == [{"type": "bar", "x": [1]}]
        assert fig._layout == {"height": 400}

    def test_add_traces(self):
        fig = go.Figure(raw=True)
        fig.add_traces(go.Scatter(x=[1], y=[2], raw=True))
        fig.add_traces([go.Bar(x=["a"], y=[1], raw=True)])
        assert len(fig._data) == 2
        assert fig._data[0]["type"] == "scatter"
        assert fig._data[1]["type"] == "bar"

    def test_update_layout(self):
        fig = go.Figure(raw=True)
        fig.update_layout(title={"text": "Hello"})
        fig.update_layout({"title": {"font": {"size": 20}}})
        assert fig._layout["title"] == {"text": "Hello", "font": {"size": 20}}
        fig.update_layout(title={"text": "New"}, overwrite=True)
        assert fig._layout["title"] == {"text": "New"}

    def test_update_traces(self):
        fig = go.Figure(raw=True)
        fig.add_traces(
            [
                go.Scatter(x=[1], y=[2], mode="lines", raw=True),
                go.Bar(x=["a"], y=[1], raw=True),
            ]
        )
        fig.update_traces(patch={"opacity": 0.5})
        assert fig._data[0]["opacity"] == 0.5
        assert fig._data[1]["opacity"] == 0.5

    def test_update_traces_with_selector(self):
        fig = go.Figure(raw=True)
        fig.add_traces(
            [
                go.Scatter(x=[1], y=[2], raw=True),
                go.Bar(x=["a"], y=[1], raw=True),
            ]
        )
        fig.update_traces(patch={"opacity": 0.5}, selector={"type": "scatter"})
        assert fig._data[0]["opacity"] == 0.5
        assert "opacity" not in fig._data[1]

    def test_for_each_trace(self):
        fig = go.Figure(raw=True)
        fig.add_traces([go.Scatter(x=[1], y=[2], raw=True)])
        visited = []
        fig.for_each_trace(lambda t: visited.append(t["type"]))
        assert visited == ["scatter"]

    def test_add_annotation_and_shape(self):
        fig = go.Figure(raw=True)
        fig.add_annotation(text="Note", x=1, y=2, showarrow=False)
        fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1)
        assert fig._layout["annotations"][0]["text"] == "Note"
        assert fig._layout["shapes"][0]["type"] == "rect"

    def test_update_annotations(self):
        fig = go.Figure(raw=True)
        fig.add_annotation(text="A", x=0, y=0, showarrow=False)
        fig.add_annotation(text="B", x=1, y=1, showarrow=False)
        fig.update_annotations(patch={"font": {"size": 14}})
        for ann in fig._layout["annotations"]:
            assert ann["font"] == {"size": 14}

    def test_update_shapes(self):
        fig = go.Figure(raw=True)
        fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1)
        fig.update_shapes(patch={"opacity": 0.3})
        assert fig._layout["shapes"][0]["opacity"] == 0.3

    def test_add_vline_and_hline(self):
        fig = go.Figure(raw=True)
        fig.add_vline(x=5)
        fig.add_hline(y=3)
        shapes = fig._layout["shapes"]
        assert len(shapes) == 2
        assert shapes[0]["x0"] == 5 and shapes[0]["x1"] == 5
        assert "y domain" in shapes[0]["yref"]
        assert shapes[1]["y0"] == 3 and shapes[1]["y1"] == 3
        assert "x domain" in shapes[1]["xref"]

    def test_serialization(self):
        fig = go.Figure(
            data=[go.Scatter(x=[1, 2], y=[3, 4], raw=True)],
            raw=True,
        )
        fig.update_layout(title="Test")
        d = fig.to_dict()
        assert d["data"][0]["type"] == "scatter"
        assert d["layout"]["title"] == "Test"
        j = fig.to_json()
        assert isinstance(j, str) and '"scatter"' in j

    def test_default_figure_unchanged(self):
        """Without raw, Figure must behave exactly as before."""
        fig = go.Figure(data=[go.Scatter(x=[1], y=[2])])
        assert hasattr(fig.data[0], "to_plotly_json")
        assert not getattr(fig, "_raw", False)


class TestOutputEquivalence:
    """Fast-path output must match standard path for explicit properties."""

    def test_trace_equivalence(self):
        default = go.Scatter(x=[1], y=[2], mode="lines")
        fast = go.Scatter(x=[1], y=[2], mode="lines", raw=True)
        for key in ["x", "y", "mode", "type"]:
            assert default.to_plotly_json()[key] == fast[key]

    def test_figure_data_equivalence(self):
        default = go.Figure(data=[go.Scatter(x=[1], y=[2])])
        fast = go.Figure(data=[go.Scatter(x=[1], y=[2], raw=True)], raw=True)
        dd, fd = default.to_dict()["data"][0], fast.to_dict()["data"][0]
        for key in ["type", "x", "y"]:
            assert dd[key] == fd[key]


class TestSubplotUpdateMethods:
    """Test update_xaxes/update_yaxes and other subplot update_* methods."""

    def test_update_xaxes(self):
        fig = go.Figure(raw=True)
        fig._layout["xaxis"] = {"title": {"text": "X"}}
        fig.update_xaxes(patch={"showgrid": False})
        assert fig._layout["xaxis"]["showgrid"] is False
        assert fig._layout["xaxis"]["title"] == {"text": "X"}

    def test_update_yaxes(self):
        fig = go.Figure(raw=True)
        fig._layout["yaxis"] = {"range": [0, 10]}
        fig.update_yaxes(patch={"showline": True})
        assert fig._layout["yaxis"]["showline"] is True
        assert fig._layout["yaxis"]["range"] == [0, 10]

    def test_update_xaxes_overwrite(self):
        fig = go.Figure(raw=True)
        fig._layout["xaxis"] = {"title": {"text": "X"}, "showgrid": True}
        fig.update_xaxes(patch={"title": {"text": "New"}}, overwrite=True)
        # overwrite=True does a flat update: title is replaced entirely, but
        # showgrid (not in patch) is preserved.
        assert fig._layout["xaxis"]["title"] == {"text": "New"}
        assert fig._layout["xaxis"]["showgrid"] is True

    def test_update_annotations_recursive(self):
        """update_annotations should recursively merge via _RawDictProxy."""
        fig = go.Figure(raw=True)
        fig.add_annotation(text="A", x=0, y=0, showarrow=False)
        fig._layout["annotations"][0]["font"] = {"size": 12, "color": "red"}
        fig.update_annotations(patch={"font": {"size": 18}})
        assert fig._layout["annotations"][0]["font"]["size"] == 18
        assert fig._layout["annotations"][0]["font"]["color"] == "red"

    def test_update_multiple_xaxes(self):
        fig = go.Figure(raw=True)
        fig._layout["xaxis"] = {"title": {"text": "X1"}}
        fig._layout["xaxis2"] = {"title": {"text": "X2"}}
        fig.update_xaxes(patch={"showgrid": False})
        assert fig._layout["xaxis"]["showgrid"] is False
        assert fig._layout["xaxis2"]["showgrid"] is False


class TestFigureUpdate:
    """Test fig.update() in raw mode."""

    def test_update_layout_via_update(self):
        fig = go.Figure(raw=True)
        fig.update(layout={"title": {"text": "Hello"}})
        assert fig._layout["title"] == {"text": "Hello"}

    def test_update_layout_recursive(self):
        fig = go.Figure(
            layout={"xaxis": {"title": {"text": "X"}, "showgrid": True}}, raw=True
        )
        fig.update(layout={"xaxis": {"color": "red"}})
        assert fig._layout["xaxis"]["title"] == {"text": "X"}
        assert fig._layout["xaxis"]["color"] == "red"
        assert fig._layout["xaxis"]["showgrid"] is True

    def test_update_data_via_update(self):
        fig = go.Figure(
            data=[go.Scatter(x=[1], y=[2], raw=True)],
            raw=True,
        )
        fig.update(data=[{"type": "bar", "x": ["a"], "y": [3]}])
        assert len(fig._data) == 2
        assert fig._data[1]["type"] == "bar"

    def test_update_layout_overwrite(self):
        fig = go.Figure(layout={"title": {"text": "Old"}, "showlegend": True}, raw=True)
        fig.update(layout={"title": {"text": "New"}}, overwrite=True)
        assert fig._layout == {"title": {"text": "New"}}


class TestGlobalConfig:
    """Test plotly.config.raw global flag."""

    def setup_method(self):
        from plotly import config

        self._original = config.raw
        config.raw = True

    def teardown_method(self):
        from plotly import config

        config.raw = self._original

    def test_figure_defaults_to_raw(self):
        fig = go.Figure()
        assert fig._raw is True

    def test_scatter_defaults_to_raw(self):
        result = go.Scatter(x=[1], y=[2])
        assert isinstance(result, dict)
        assert result["type"] == "scatter"

    def test_explicit_override(self):
        fig = go.Figure(raw=False)
        assert fig._raw is False

    def test_add_scatter_produces_raw_trace(self):
        fig = go.Figure()
        fig.add_scatter(x=[1, 2], y=[3, 4])
        assert len(fig._data) == 1
        assert isinstance(fig._data[0], dict)
