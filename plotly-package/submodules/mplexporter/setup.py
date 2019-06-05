try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DESCRIPTION = "General Matplotlib Exporter"
LONG_DESCRIPTION = open('README.md').read()
NAME = "mplexporter"
AUTHOR = "Jake VanderPlas"
AUTHOR_EMAIL = "jakevdp@cs.washington.edu"
MAINTAINER = "Jake VanderPlas"
MAINTAINER_EMAIL = "jakevdp@cs.washington.edu"
DOWNLOAD_URL = 'https://github.com/mpld3/mplexporter'
URL = DOWNLOAD_URL
LICENSE = 'BSD 3-clause'
VERSION = '0.0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['mplexporter', 'mplexporter.renderers'],
     )
