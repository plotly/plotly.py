### Stand Alone Distribution

**WARNING**: Use this as a last resort. We make no guarantees that the files here are the most up-to-date content.

If for reasons beyond your control, you cannot install the plotly package via pip (e.g., you need to install on a machine without an internet connection), you can install via a zip file we provide (see below).

Here we assume you're familiar with command-line tools and that you've got pip installed. Not the case? Check it out here:
[http://pip.readthedocs.org/en/latest/installing.html](http://pip.readthedocs.org/en/latest/installing.html)

#### Unix-y Folks, do this:
```bash
curl -O https://github.com/plotly/python-api/raw/tarball-link/stand_alone_dist/dist.zip
unzip dist.zip
cd dist
ls | xargs pip install -I
```

### Need Help?
<mailto:support@plot.ly>
