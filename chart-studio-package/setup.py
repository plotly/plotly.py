from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="chart_studio",
    version="4.0.0a1",
    author="Chris P",
    author_email="chris@plot.ly",
    maintainer="Jon Mease",
    maintainer_email="jon@plot.ly",
    url="https://plot.ly/python/",
    project_urls={"Github": "https://github.com/plotly/plotly.py"},
    description="An open-source, interactive graphing library for Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    license="MIT",
    packages=[
        "chart_studio",
        "chart_studio.api",
        "chart_studio.api.v1",
        "chart_studio.api.v2",
        "chart_studio.dashboard_objs",
        "chart_studio.grid_objs",
        "chart_studio.plotly",
        "chart_studio.plotly.chunked_requests",
        "chart_studio.presentation_objs",
        "chart_studio.widgets",
    ],
    install_requires=["plotly", "requests", "retrying>=1.3.3", "six"],
    zip_safe=False,
)
