I'm excited to announce that Plotly.py 4.6 is now available for download via `pip` and `conda`! 
For up-to-date installation instructions (including the **extra required steps for JupyterLab**!) please 
see our [Getting Started](https://plot.ly/python/getting-started/) documentation page and
if you run into trouble, check out our [Troubleshooting Guide](https://plot.ly/python/troubleshooting/).

# What's new in Plotly.py 4.6

Our [changelog](https://github.com/plotly/plotly.py/releases/tag/v4.6.0) has links to individual pull requests, 
but here are the highlights:

### Unified Hover Labels

Until today hovering on plots resulted in either one more multiple hover labels, each always attached to a single point.
This release introduces two new values for `layout.hovermode`, namely `"x unified"` and `"y unified"`, which results in 
a single hover label that refers to multiple points at a single X or Y value (on 2D cartesian subplots). Here's what this looks
like:

IMGE


Check out our [expanded Hover Label documentation page](https://plotly.com/python/hover-text-and-formatting/)
for more examples of how to control and customize hover labels.

This feature was [anonymously *sponsored*](https://plotly.com/consulting-and-oem/) and we thank our benefactor on behalf of the community :heart:.

### Excluding Weekends and Holidays from Date Axes

A long-requested feature has been to add the ability to remove certain time periods from charts with date axes, 
for example removing weekends from charts that detail business processes or financial transactions. This is now implemented
for `date` axes using the new `rangebreaks` attribute (but unfortunately does not work with the `scattergl` trace type yet).

IMG

Using `rangebreaks` you can exclude weekends with `bounds=["sat", "mon"]` and individual dates with 
`values=["2020-01-01", "2020-01-12"]`. Check out our 
[reworked Time Series and Date Axes documentation page](https://plotly.com/python/time-series/) for information 
on how to use this feature.

This feature was  [anonymously *sponsored*](https://plotly.com/consulting-and-oem/) and we thank our benefactor on
behalf of the community :heart:.

### Labeling with `px.imshow()` plus `xarray` support

With this release, it's now possible to pass tick label data to `px.imshow()` and to control the x, y, and color axis titles. 
These labels are also automatically used for the hover label text.

IMG

The [`xarray` package](http://xarray.pydata.org/en/stable/) is designed to make it easy to work with labelled N-dimensional 
matrix data, and with this release, if you pass an `xarray` object into `px.imshow()` now, these labels are automatically set
based on the label information in the `xarray`. 

IMG

This is perfect for [using Plotly Express with Datashader](https://plotly.com/python/datashader/), as Datashader 
returns `xarray` objects by default.

### Documentation Rebranding and New Search

As you browse our documentation today, you might notice the fresh new colors and fonts, as well as the switch from the old `plot.ly`
domain name to the new `plotly.com` domain name. We love our new branding and hope that you do too!



This refresh is not just skin-deep, though: we've also reworked our documentation search system. The search box is now available on 
every page, in the left-hand sidebar, and search queries are now run against both the tutorial examples *and* the Figure Reference page, 
to make sure you can quickly find what you're looking for! We've also tuned the Figure Reference search result ordering, to ensure the
most useful hits show up higher in the rankings.

### Community

We've updated our [contributing notes](https://github.com/plotly/plotly.py/blob/master/contributing.md) and
[pull-request template](https://raw.githubusercontent.com/plotly/plotly.py/master/.github/pull_request_template.md) to make it easier for community
members to pitch in with Plotly.py.

We also heartily thank the community members who contributed to our code and documentation in this release: thank you 
[@SylwiaOliwia2](https://github.com/SylwiaOliwia2) and [@dangercrow](https://github.com/dangercrow) and
[@tvaucher](https://github.com/tvaucher)!

Even if you cannot contribute to Plotly.py yourself, if you work with an organization that uses Plotly.py and 
has a software budget, one of the best ways to give back to the open-source community is to 
[sponsor a feature](https://plotly.com/consulting-and-oem/) in any of our libraries!

### Powered by Plotly.js 1.53 and perfect for Dash 1.10

This release of Plotly.py inherits all of the improvements to the underlying Javascript library that powers it.
The full [Plotly.js 1.53 changelog](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1530----2020-03-31) 
contains more details about what changed under the hood.

The version of Plotly.js that Plotly.py 4.6 is built on is the same one that's bundled with 
the [recently-released Dash 1.10](https://community.plotly.com/t/dash-v1-10-0-release/37076) so we recommend that if
you're a Dash user you upgrade to both Dash 1.10 and Plotly.py 4.6 to get the full benefit of all of these 
libraries working together.

## Get it now!

To sum up: Plotly.py 4.6.0 is out and if you're excited about any of the above features, 
head on over to our [Getting Started](https://plot.ly/python/getting-started/) documentation page 
for full installation instructions, and don't forget to upgrade your JupyterLab extensions
if that is your environment of choice!

### Previous Announcements in the 4.x series

- [Plotly.py 4.5](https://community.plotly.com/t/announcing-plotly-py-4-5/34045)
- [Plotly.py 4.4](https://community.plotly.com/t/announcing-plotly-py-4-4-1/32514)
- [Plotly.py 4.3, 4.2, 4.1](https://community.plotly.com/t/announcing-plotly-py-4-3-and-4-2-and-4-1/31245)
- [Plotly.py 4.0](https://community.plotly.com/t/introducing-plotly-py-4-0-0/25639)
