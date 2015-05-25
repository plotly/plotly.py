from setuptools import setup
from setuptools import setup, find_packages

exec (open('plotly/version.py').read())
exec (open('plotly/resources.py').read())


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
      url='https://plot.ly/api/python',
      description="Python plotting library for collaborative, "
                  "interactive, publication-quality graphs.",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Visualization',
      ],
      license='MIT',
      packages=find_packages(),
      data_files=[(GRAPH_REFERENCE_DIR, GRAPH_REFERENCE_FILES),
                  (WIDGETS_DIR, WIDGETS_FILES)],
      package_data={'plotly': ['graph_reference/*.json', 'widgets/*.js']},
      install_requires=['requests', 'six', 'pytz'],
      extras_require={"PY2.6": ['simplejson', 'ordereddict',
                                'requests[security]']},
      zip_safe=False)
