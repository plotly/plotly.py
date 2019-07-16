from setuptools import setup
import os


def readme():
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(parent_dir, "README.md")) as f:
        return f.read()


setup(
    name="plotly-geo",
    version="1.0.0",
    author="Chris P",
    author_email="chris@plot.ly",
    maintainer="Jon Mease",
    maintainer_email="jon@plot.ly",
    url="https://plot.ly/python/",
    project_urls={"Github": "https://github.com/plotly/plotly.py"},
    description="geo shape files for use with plotly.py",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    license="MIT",
    packages=["_plotly_geo"],
    package_data={"_plotly_geo": ["package_data/*"]},
)
