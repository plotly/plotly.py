---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.11.10
  plotly:
    description: Details about changes to static image generation in Plotly.py 6.1.
    display_as: file_settings
    language: python
    layout: base
    name: Static Image Generation Changes in Plotly.py 6.1
    order: 40
    page_type: u-guide
    permalink: python/static-image-generation-changes/
    thumbnail: thumbnail/static-image-export.png
---

<!-- #region -->
# Static Image Generation Changes in Plotly.py 6.1

Plotly.py 6.1 introduces support for Kaleido v1, which [improves static image generation](https://plotly.com/blog/kaleido-the-next-generation/) for Plotly figures.

While adding support for Kaleido v1, we are deprecating support for earlier versions of Kaleido and support for [Orca](/python/orca-management/). Support for Orca and earlier versions of Kaleido will be removed after September 2025, and we recommend updating to the latest Kaleido. This page documents how to migrate your Plotly code to Kaleido v1 and outlines the changes in functionality.

To migrate from either Orca or Kaleido v0, first install the latest Kaleido with:

```bash
pip install --upgrade kaleido
```

## Engine Parameter

The `engine` parameter on static image export methods and functions is deprecated in Plotly.py 6.1 and will be removed after September 2025. Once the `engine` parameter is removed, static image generation will use Kaleido v1 if it's installed, or raise an error if it isn't.

You'll need to update your code to remove references to `engine`. For example, `fig.to_image(format="png", engine="orca")` or `fig.to_image(format="png", engine="kaleido")` needs to be updated to `fig.to_image(format="png")`. This change applies to: `fig.to_image`, `fig.write_image`, `plotly.io.to_image`, and `plotly.io.write_image`.

## EPS Format

The `eps` format is no longer supported in Kaleido v1. If your existing code sets `format=eps`, you'll need to update it to use another format, for example `pdf`.

## Config Settings

Accessing Kaleido defaults and config settings via `plotly.io.kaleido.scope` is now deprecated and will be removed after September 2025. You'll need to update any code that uses `plotly.io.kaleido.scope` to instead use `plotly.io.defaults`. For example, to set the `default_format` to "jpeg":

~~~python
import plotly.io as pio
pio.defaults.default_format = "jpeg"
~~~

The `mapbox_access_token` config setting is not available on `plotly.io.defaults` because Mapbox maps are deprecated and will be removed in a future version of Plotly.py. See [MapLibre Migration ](https://plotly.com/python/mapbox-to-maplibre/) for more details.

If you are migrating from Orca, the following config settings do not apply to Kaleido: `server_url`, `port`, `timeout`, and `use_xvfb`, but other settings, such as `default_format`, can be accessed via `plotly.io.defaults`.
<!-- #endregion -->
