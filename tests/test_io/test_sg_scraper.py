"""Tests for the sphinx-gallery image scraper.

The scraper implements the interface described at
https://sphinx-gallery.github.io/stable/advanced.html#write-a-custom-image-scraper
so these tests drive it through sphinx-gallery itself rather than through a
copy of that interface.
"""

import functools
import importlib
import logging
import os
from pathlib import Path
from types import SimpleNamespace

import plotly.graph_objects as go
import plotly.io as pio
import pytest

pytest.importorskip("sphinx_gallery")

# The color of each successive image written during one test, so that the
# figure an image or thumbnail came from can be identified.
COLORS = ["red", "blue"]


def dummy_image_writer():
    """Return a pio.write_image stand-in, so the tests do not need Kaleido."""
    colors = iter(COLORS)

    def write_dummy_image(fig, file, format="png", **kwargs):
        color = next(colors)
        if format == "svg":
            with open(file, "w") as f:
                f.write(f'<svg xmlns="http://www.w3.org/2000/svg" fill="{color}"/>')
        else:
            from PIL import Image

            Image.new("RGB", (16, 16), color).save(file)

    return write_dummy_image


def assert_image_color(path, color, image_format):
    """Assert an image came from the figure that was written in `color`."""
    if image_format == "svg":
        assert f'fill="{color}"' in path.read_text()
    else:
        from PIL import Image, ImageColor

        # Sphinx-gallery pads thumbnails onto a white canvas, so only the
        # center is guaranteed to come from the scraped image.
        image = Image.open(path).convert("RGB")
        center = image.getpixel((image.width // 2, image.height // 2))
        assert center == ImageColor.getrgb(color)


@pytest.fixture
def gallery(tmp_path, monkeypatch):
    """Emulate a sphinx-gallery build of a single example.

    Calls into sphinx-gallery for everything that drives or consumes the
    scraper, so that the tests exercise the real API. Images are written by a
    stand-in for `pio.write_image`, so that the tests do not need Kaleido.
    """
    from sphinx_gallery.gen_gallery import DEFAULT_GALLERY_CONF
    from sphinx_gallery.gen_rst import save_thumbnail
    from sphinx_gallery.scrapers import ImagePathIterator, save_figures

    import plotly.io._sg_scraper as sg_scraper
    from plotly.io._base_renderers import sphinx_gallery_figures
    from plotly.io._sg_scraper import plotly_sg_scraper

    # Importing the scraper sets the renderer too, but only the first time it
    # is imported, which may have happened in another test already.
    monkeypatch.setattr(pio.renderers, "default", "sphinx_gallery_png")
    monkeypatch.setattr(pio, "write_image", dummy_image_writer())
    # Images come from the stand-in above, so the Kaleido probe must pass too
    monkeypatch.setattr(pio, "to_image", lambda *args, **kwargs: b"")
    sg_scraper._static_export_available.cache_clear()

    example_dir = tmp_path / "auto_examples"
    thumb_dir = example_dir / "images" / "thumb"
    thumb_dir.parent.mkdir(parents=True)
    template = str(example_dir / "images" / "sphx_glr_plot_example_{0:03}.png")
    src_file = str(example_dir / "plot_example.py")
    conf = {
        **DEFAULT_GALLERY_CONF,
        "src_dir": str(tmp_path),
        "image_scrapers": (plotly_sg_scraper,),
    }
    block_vars = {
        "image_path_iterator": ImagePathIterator(template),
        "src_file": src_file,
        "example_globals": {},
    }

    def scrape(content=""):
        """Scrape one code block, as sphinx-gallery does after executing it."""
        return save_figures(("code", content, 1), block_vars, conf)

    def thumbnail(**file_conf):
        """Generate the gallery thumbnail and return the one file produced."""
        save_thumbnail(template, src_file, block_vars, file_conf, conf)
        (thumb,) = thumb_dir.iterdir()
        return thumb

    yield SimpleNamespace(
        conf=conf,
        example_dir=example_dir,
        globals=block_vars["example_globals"],
        paths=block_vars["image_path_iterator"].paths,
        scraper=plotly_sg_scraper,
        scrape=scrape,
        thumbnail=thumbnail,
    )
    del sphinx_gallery_figures[:]
    sg_scraper._static_export_available.cache_clear()


@pytest.mark.parametrize("image_format", ["png", "svg"])
def test_scraper(gallery, image_format):
    """Each shown figure gets an embed and a static image, and can be a thumbnail."""
    # Selecting a format by wrapping the scraper is the approach documented at
    # https://sphinx-gallery.github.io/stable/advanced.html#example-3-matplotlib-with-svg-format
    gallery.conf["image_scrapers"] = (
        functools.partial(gallery.scraper, format=image_format),
    )
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 2, 1])])
    pio.show(fig)
    fig.show()  # both ways of showing a figure must be scraped

    rst = gallery.scrape()

    assert len(gallery.paths) == 2
    for path, color in zip(gallery.paths, COLORS):
        root = os.path.splitext(path)[0]
        assert_image_color(Path(f"{root}.{image_format}"), color, image_format)
    assert rst.count(".. raw:: html") == 2
    assert rst.count("plotly-graph-div") == 2
    # The wrapper sphinx-gallery uses for HTML reprs, so themes can style both
    assert rst.count('class="output_subarea') == 2

    # The thumbnail must be a scraped figure rather than a "no image" default,
    # and one image per figure in order is what makes `thumbnail_number` work
    for number, color in enumerate(COLORS, start=1):
        thumb = gallery.thumbnail(thumbnail_number=number)
        assert thumb.name == f"sphx_glr_plot_example_thumb.{image_format}"
        assert_image_color(thumb, color, image_format)

    # The figures have been consumed, so a block showing none scrapes nothing
    assert gallery.scrape() == ""
    assert len(gallery.paths) == 2


def test_scraper_ignores_other_examples(gallery):
    """Files belonging to another example must be left alone (issue #4959).

    Sphinx-gallery can execute examples in parallel, so the directory holding
    the example being scraped may contain files from other examples.
    """
    others = [gallery.example_dir / f"plot_other.{ext}" for ext in ("png", "html")]
    for other in others:
        other.write_text("another example")
    pio.show(go.Figure())
    rst = gallery.scrape()

    for other in others:
        assert other.read_text() == "another example", f"{other.name} was scraped"
    assert len(gallery.paths) == 1
    assert rst.count(".. raw:: html") == 1


def test_scraper_repr_figure(gallery):
    """A figure displayed as a block's last expression still gets a thumbnail.

    Sphinx-gallery embeds the HTML of such figures itself (repr capture), so
    the scraper must contribute only the static image.
    """
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 2, 1])])
    gallery.globals["___"] = fig  # as sphinx-gallery's repr capture leaves it
    rst = gallery.scrape("fig.update_layout(title='hi')\nfig")

    assert rst == ""
    assert len(gallery.paths) == 1
    root = os.path.splitext(gallery.paths[0])[0]
    assert not os.path.isfile(f"{root}.html")
    assert_image_color(Path(f"{root}.png"), COLORS[0], "png")
    assert_image_color(gallery.thumbnail(), COLORS[0], "png")

    # ``___`` survives into blocks without a trailing expression; the stale
    # figure must not be scraped again
    assert gallery.scrape("x = 1") == ""
    assert len(gallery.paths) == 1


def test_scraper_repr_of_shown_figure_not_duplicated(gallery):
    """A figure that is both shown and the last expression is scraped once."""
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 2, 1])])
    fig.show()
    gallery.globals["___"] = fig
    rst = gallery.scrape("fig.show()\nfig")

    assert rst.count(".. raw:: html") == 1
    assert len(gallery.paths) == 1


def test_scraper_bad_format(gallery):
    gallery.conf["image_scrapers"] = (functools.partial(gallery.scraper, format="pdf"),)
    pio.show(go.Figure())
    with pytest.raises(ValueError, match="format must be one of"):
        gallery.scrape()


def test_scraper_no_static_export(gallery, monkeypatch, caplog):
    """Without static export, warn once and keep the interactive figures.

    Sphinx-gallery requires an image file for every image path taken, so no
    image paths may be consumed either; the examples then get sphinx-gallery's
    placeholder thumbnail.
    """
    import plotly.io._sg_scraper as sg_scraper

    def raise_no_browser(*args, **kwargs):
        raise ValueError("no browser")

    monkeypatch.setattr(pio, "to_image", raise_no_browser)
    sg_scraper._static_export_available.cache_clear()
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[3, 2, 1])])
    pio.show(fig)
    gallery.globals["___"] = fig

    with caplog.at_level(logging.WARNING):
        rst = gallery.scrape("fig.show()")

    # The shown figure is embedded inline instead of via files
    assert rst.count(".. raw:: html") == 1
    assert "Scatter" not in rst  # inlined as HTML, not as a repr
    assert "plotly-graph-div" in rst
    assert gallery.paths == []
    warnings = [r for r in caplog.records if "Kaleido" in r.getMessage()]
    assert len(warnings) == 1
    assert "no browser" in warnings[0].getMessage()

    # Only one warning per build, however many blocks follow; repr-displayed
    # figures are embedded by sphinx-gallery itself so they scrape to nothing
    with caplog.at_level(logging.WARNING):
        assert gallery.scrape("fig") == ""
    assert gallery.paths == []
    assert len([r for r in caplog.records if "Kaleido" in r.getMessage()]) == 1


def test_repr_html_fallback_size(monkeypatch):
    """The repr of a figure must have a usable pixel height, not "100%".

    With the (non-mimetype) sphinx_gallery_png renderer selected, sphinx-
    gallery captures ``_repr_html_``, whose output ends up in a container
    with no set height.
    """
    monkeypatch.setattr(pio.renderers, "default", "sphinx_gallery_png")
    assert 'style="height:525px; width:100%;"' in go.Figure()._repr_html_()
    fig = go.Figure(layout={"height": 400})
    assert 'style="height:400px; width:100%;"' in fig._repr_html_()


def test_image_scrapers_by_name(monkeypatch):
    """`image_scrapers=("plotly",)` must resolve through sphinx-gallery."""
    from sphinx_gallery.gen_rst import _get_callables

    from plotly.io._sg_scraper import plotly_sg_scraper

    monkeypatch.setattr(pio.renderers, "default", "browser")
    (scraper,) = _get_callables({"image_scrapers": ("plotly",)}, "image_scrapers")
    assert scraper is plotly_sg_scraper
    # Resolving the scraper must select the renderer that it knows how to
    # scrape, so that no other configuration is needed.
    assert pio.renderers.default == "sphinx_gallery_png"


def test_import_sets_default_renderer(monkeypatch):
    """Importing the scraper selects the renderer that it knows how to scrape."""
    monkeypatch.setattr(pio.renderers, "default", "browser")
    importlib.reload(importlib.import_module("plotly.io._sg_scraper"))
    assert pio.renderers.default == "sphinx_gallery_png"
