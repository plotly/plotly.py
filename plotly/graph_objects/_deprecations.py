import warnings

warnings.filterwarnings(
    "default", r"plotly\.graph_objects\.\w+ is deprecated", DeprecationWarning
)


class Data(list):
    """
        plotly.graph_objects.Data is deprecated.
    Please replace it with a list or tuple of instances of the following types
      - plotly.graph_objects.Scatter
      - plotly.graph_objects.Bar
      - plotly.graph_objects.Area
      - plotly.graph_objects.Histogram
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Data is deprecated.
        Please replace it with a list or tuple of instances of the following types
          - plotly.graph_objects.Scatter
          - plotly.graph_objects.Bar
          - plotly.graph_objects.Area
          - plotly.graph_objects.Histogram
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.Data is deprecated.
Please replace it with a list or tuple of instances of the following types
  - plotly.graph_objects.Scatter
  - plotly.graph_objects.Bar
  - plotly.graph_objects.Area
  - plotly.graph_objects.Histogram
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Annotations(list):
    """
        plotly.graph_objects.Annotations is deprecated.
    Please replace it with a list or tuple of instances of the following types
      - plotly.graph_objects.layout.Annotation
      - plotly.graph_objects.layout.scene.Annotation

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Annotations is deprecated.
        Please replace it with a list or tuple of instances of the following types
          - plotly.graph_objects.layout.Annotation
          - plotly.graph_objects.layout.scene.Annotation

        """
        warnings.warn(
            """plotly.graph_objects.Annotations is deprecated.
Please replace it with a list or tuple of instances of the following types
  - plotly.graph_objects.layout.Annotation
  - plotly.graph_objects.layout.scene.Annotation
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Frames(list):
    """
        plotly.graph_objects.Frames is deprecated.
    Please replace it with a list or tuple of instances of the following types
      - plotly.graph_objects.Frame

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Frames is deprecated.
        Please replace it with a list or tuple of instances of the following types
          - plotly.graph_objects.Frame

        """
        warnings.warn(
            """plotly.graph_objects.Frames is deprecated.
Please replace it with a list or tuple of instances of the following types
  - plotly.graph_objects.Frame
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class AngularAxis(dict):
    """
        plotly.graph_objects.AngularAxis is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.AngularAxis
      - plotly.graph_objects.layout.polar.AngularAxis

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.AngularAxis is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.AngularAxis
          - plotly.graph_objects.layout.polar.AngularAxis

        """
        warnings.warn(
            """plotly.graph_objects.AngularAxis is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.AngularAxis
  - plotly.graph_objects.layout.polar.AngularAxis
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Annotation(dict):
    """
        plotly.graph_objects.Annotation is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.Annotation
      - plotly.graph_objects.layout.scene.Annotation

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Annotation is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.Annotation
          - plotly.graph_objects.layout.scene.Annotation

        """
        warnings.warn(
            """plotly.graph_objects.Annotation is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.Annotation
  - plotly.graph_objects.layout.scene.Annotation
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class ColorBar(dict):
    """
        plotly.graph_objects.ColorBar is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter.marker.ColorBar
      - plotly.graph_objects.surface.ColorBar
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.ColorBar is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter.marker.ColorBar
          - plotly.graph_objects.surface.ColorBar
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.ColorBar is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter.marker.ColorBar
  - plotly.graph_objects.surface.ColorBar
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Contours(dict):
    """
        plotly.graph_objects.Contours is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.contour.Contours
      - plotly.graph_objects.surface.Contours
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Contours is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.contour.Contours
          - plotly.graph_objects.surface.Contours
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.Contours is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.contour.Contours
  - plotly.graph_objects.surface.Contours
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class ErrorX(dict):
    """
        plotly.graph_objects.ErrorX is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter.ErrorX
      - plotly.graph_objects.histogram.ErrorX
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.ErrorX is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter.ErrorX
          - plotly.graph_objects.histogram.ErrorX
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.ErrorX is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter.ErrorX
  - plotly.graph_objects.histogram.ErrorX
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class ErrorY(dict):
    """
        plotly.graph_objects.ErrorY is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter.ErrorY
      - plotly.graph_objects.histogram.ErrorY
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.ErrorY is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter.ErrorY
          - plotly.graph_objects.histogram.ErrorY
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.ErrorY is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter.ErrorY
  - plotly.graph_objects.histogram.ErrorY
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class ErrorZ(dict):
    """
        plotly.graph_objects.ErrorZ is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter3d.ErrorZ

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.ErrorZ is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter3d.ErrorZ

        """
        warnings.warn(
            """plotly.graph_objects.ErrorZ is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter3d.ErrorZ
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Font(dict):
    """
        plotly.graph_objects.Font is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.Font
      - plotly.graph_objects.layout.hoverlabel.Font
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Font is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.Font
          - plotly.graph_objects.layout.hoverlabel.Font
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.Font is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.Font
  - plotly.graph_objects.layout.hoverlabel.Font
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Legend(dict):
    """
        plotly.graph_objects.Legend is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.Legend

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Legend is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.Legend

        """
        warnings.warn(
            """plotly.graph_objects.Legend is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.Legend
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Line(dict):
    """
        plotly.graph_objects.Line is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter.Line
      - plotly.graph_objects.layout.shape.Line
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Line is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter.Line
          - plotly.graph_objects.layout.shape.Line
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.Line is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter.Line
  - plotly.graph_objects.layout.shape.Line
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Margin(dict):
    """
        plotly.graph_objects.Margin is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.Margin

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Margin is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.Margin

        """
        warnings.warn(
            """plotly.graph_objects.Margin is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.Margin
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Marker(dict):
    """
        plotly.graph_objects.Marker is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter.Marker
      - plotly.graph_objects.histogram.selected.Marker
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Marker is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter.Marker
          - plotly.graph_objects.histogram.selected.Marker
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.Marker is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter.Marker
  - plotly.graph_objects.histogram.selected.Marker
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class RadialAxis(dict):
    """
        plotly.graph_objects.RadialAxis is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.RadialAxis
      - plotly.graph_objects.layout.polar.RadialAxis

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.RadialAxis is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.RadialAxis
          - plotly.graph_objects.layout.polar.RadialAxis

        """
        warnings.warn(
            """plotly.graph_objects.RadialAxis is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.RadialAxis
  - plotly.graph_objects.layout.polar.RadialAxis
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Scene(dict):
    """
        plotly.graph_objects.Scene is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.Scene

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Scene is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.Scene

        """
        warnings.warn(
            """plotly.graph_objects.Scene is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.Scene
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Stream(dict):
    """
        plotly.graph_objects.Stream is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.scatter.Stream
      - plotly.graph_objects.area.Stream

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Stream is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.scatter.Stream
          - plotly.graph_objects.area.Stream

        """
        warnings.warn(
            """plotly.graph_objects.Stream is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.scatter.Stream
  - plotly.graph_objects.area.Stream
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class XAxis(dict):
    """
        plotly.graph_objects.XAxis is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.XAxis
      - plotly.graph_objects.layout.scene.XAxis

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.XAxis is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.XAxis
          - plotly.graph_objects.layout.scene.XAxis

        """
        warnings.warn(
            """plotly.graph_objects.XAxis is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.XAxis
  - plotly.graph_objects.layout.scene.XAxis
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class YAxis(dict):
    """
        plotly.graph_objects.YAxis is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.YAxis
      - plotly.graph_objects.layout.scene.YAxis

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.YAxis is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.YAxis
          - plotly.graph_objects.layout.scene.YAxis

        """
        warnings.warn(
            """plotly.graph_objects.YAxis is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.YAxis
  - plotly.graph_objects.layout.scene.YAxis
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class ZAxis(dict):
    """
        plotly.graph_objects.ZAxis is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.layout.scene.ZAxis

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.ZAxis is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.layout.scene.ZAxis

        """
        warnings.warn(
            """plotly.graph_objects.ZAxis is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.layout.scene.ZAxis
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class XBins(dict):
    """
        plotly.graph_objects.XBins is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.histogram.XBins
      - plotly.graph_objects.histogram2d.XBins

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.XBins is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.histogram.XBins
          - plotly.graph_objects.histogram2d.XBins

        """
        warnings.warn(
            """plotly.graph_objects.XBins is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.histogram.XBins
  - plotly.graph_objects.histogram2d.XBins
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class YBins(dict):
    """
        plotly.graph_objects.YBins is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.histogram.YBins
      - plotly.graph_objects.histogram2d.YBins

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.YBins is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.histogram.YBins
          - plotly.graph_objects.histogram2d.YBins

        """
        warnings.warn(
            """plotly.graph_objects.YBins is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.histogram.YBins
  - plotly.graph_objects.histogram2d.YBins
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Trace(dict):
    """
        plotly.graph_objects.Trace is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.Scatter
      - plotly.graph_objects.Bar
      - plotly.graph_objects.Area
      - plotly.graph_objects.Histogram
      - etc.

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Trace is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.Scatter
          - plotly.graph_objects.Bar
          - plotly.graph_objects.Area
          - plotly.graph_objects.Histogram
          - etc.

        """
        warnings.warn(
            """plotly.graph_objects.Trace is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.Scatter
  - plotly.graph_objects.Bar
  - plotly.graph_objects.Area
  - plotly.graph_objects.Histogram
  - etc.
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


class Histogram2dcontour(dict):
    """
        plotly.graph_objects.Histogram2dcontour is deprecated.
    Please replace it with one of the following more specific types
      - plotly.graph_objects.Histogram2dContour

    """

    def __init__(self, *args, **kwargs):
        """
                plotly.graph_objects.Histogram2dcontour is deprecated.
        Please replace it with one of the following more specific types
          - plotly.graph_objects.Histogram2dContour

        """
        warnings.warn(
            """plotly.graph_objects.Histogram2dcontour is deprecated.
Please replace it with one of the following more specific types
  - plotly.graph_objects.Histogram2dContour
""",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)
