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

While adding support for Kaleido v1, we are deprecating support for earlier versions of Kaleido and support for orca, another static image generation library. Support for earlier verisons of Kaleido and orca will be removed after September 2025, and we recommend updating to the latest Kaleido. This page documents how to migrate to Kaleido v1 and outlines any changes in functionality. 

## Installing Kaleido

Install the latest kaleido with:

```bash
pip install -U kaleido
```

## Updating Existing Code

After September 2025, Kaleido v1 will  be the sole supported static image generator for Plotly.py. 
With this change, the `engine` parameter on Plotly figure methods and functions that generate static images will be removed. For example, `fig.to_image(format="png", engine="orca")` or `fig.to_image(format="png", engine="kaleido")` needs to be updted to `fig.to_image(format="png")`. 

This change applies to: `fig.to_image`, `fig.write_image`, `plotly.io.to_image`, and `plotly.io.write_image`.

<!-- #endregion -->
