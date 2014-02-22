from setuptools import setup
exec(open('plotly/version.py').read())
def readme():
	with open('plotly/pypi_description.txt') as f:
		return f.read()

setup(name='plotly',
      version=__version__,
      author='Chris P',
      author_email='chris@plot.ly',
      maintainer='Chris P',
      maintainer_email='chris@plot.ly',
      url='https://plot.ly/api/python',
      description='Python plotting library for collaborative, interactive, web-based, publication-quality graphs.', 
      long_description=readme(),
      classifiers=['Development Status :: 4 - Beta',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.3',      
      'Topic :: Scientific/Engineering :: Visualization',
	  ],
      license='MIT',
      packages=['plotly'],
      install_requires=[
      	'requests'
      ],
      zip_safe=False)
