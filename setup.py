from setuptools import setup

exec (open('plotly/version.py').read())


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='plotly',
      version=__version__,
      use_2to3=False,
      author='Chris P',
      author_email='chris@plot.ly',
      maintainer='Chris P',
      maintainer_email='chris@plot.ly',
      url='https://plot.ly/python/',
      description="Python plotting library for collaborative, "
                  "interactive, publication-quality graphs.",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Visualization',
      ],
      license='MIT',
      packages=['plotly',
                'plotly/plotly',
                'plotly/plotly/chunked_requests',
                'plotly/graph_objs',
                'plotly/grid_objs',
                'plotly/widgets',
                'plotly/offline',
                'plotly/matplotlylib',
                'plotly/matplotlylib/mplexporter',
                'plotly/matplotlylib/mplexporter/renderers'],
      package_data={'plotly': ['graph_reference/*.json', 'widgets/*.js', 'offline/*.js']},
      install_requires=['requests', 'six', 'pytz'],
      zip_safe=False)
