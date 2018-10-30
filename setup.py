from setuptools import setup, Command
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist
from subprocess import check_call
from distutils import log

import os
import sys
import platform
import json

exec(open('plotly/version.py').read())

here = os.path.dirname(os.path.abspath(__file__))
node_root = os.path.join(here, 'js')
is_repo = os.path.exists(os.path.join(here, '.git'))

npm_path = os.pathsep.join([
    os.path.join(node_root, 'node_modules', '.bin'),
                os.environ.get('PATH', os.defpath),
])


# Load plotly.js version from js/package.json
def plotly_js_version():
    with open('js/package.json', 'rt') as f:
        package_json = json.load(f)
        version = package_json['dependencies']['plotly.js']

    return version


def readme():
    with open('README.rst') as f:
        return f.read()


def js_prerelease(command, strict=False):
    """decorator for building minified js/css prior to another command"""
    class DecoratedCommand(command):
        def run(self):
            jsdeps = self.distribution.get_command_obj('jsdeps')
            if not is_repo and all(os.path.exists(t) for t in jsdeps.targets):
                # sdist, nothing to do
                command.run(self)
                return

            try:
                self.distribution.run_command('jsdeps')
            except Exception as e:
                missing = [t for t in jsdeps.targets if not os.path.exists(t)]
                if strict or missing:
                    log.warn('rebuilding js and css failed')
                    if missing:
                        log.error('missing files: %s' % missing)
                    raise e
                else:
                    log.warn('rebuilding js and css failed (not a problem)')
                    log.warn(str(e))
            command.run(self)
            update_package_data(self.distribution)
    return DecoratedCommand


def update_package_data(distribution):
    """update package_data to catch changes during setup"""
    build_py = distribution.get_command_obj('build_py')
    # distribution.package_data = find_package_data()
    # re-init build_py options which load package_data
    build_py.finalize_options()


class NPM(Command):
    description = 'install package.json dependencies using npm'

    user_options = []

    node_modules = os.path.join(node_root, 'node_modules')

    targets = [
        os.path.join(here, 'plotlywidget', 'static', 'extension.js'),
        os.path.join(here, 'plotlywidget', 'static', 'index.js')
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def get_npm_name(self):
        npmName = 'npm'
        if platform.system() == 'Windows':
            npmName = 'npm.cmd'

        return npmName

    def has_npm(self):
        npmName = self.get_npm_name();
        try:
            check_call([npmName, '--version'])
            return True
        except:
            return False

    def should_run_npm_install(self):
        package_json = os.path.join(node_root, 'package.json')
        node_modules_exists = os.path.exists(self.node_modules)
        return self.has_npm()

    def run(self):
        has_npm = self.has_npm()
        if not has_npm:
            log.error(
                "`npm` unavailable.  If you're running this command using sudo, make sure `npm` is available to sudo")

        env = os.environ.copy()
        env['PATH'] = npm_path

        if self.should_run_npm_install():
            log.info("Installing build dependencies with npm.  This may take a while...")
            npmName = self.get_npm_name();
            check_call([npmName, 'install'], cwd=node_root, stdout=sys.stdout, stderr=sys.stderr)
            os.utime(self.node_modules, None)

        for t in self.targets:
            if not os.path.exists(t):
                msg = 'Missing file: %s' % t
                if not has_npm:
                    msg += '\nnpm is required to build a development version of widgetsnbextension'
                raise ValueError(msg)

        # update package data in case this created new files
        update_package_data(self.distribution)


class CodegenCommand(Command):
    description = 'Generate class hierarchy from Plotly JSON schema'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if sys.version_info.major != 3 or sys.version_info.minor < 6:
            raise ImportError(
                'Code generation must be executed with Python >= 3.6')

        from codegen import perform_codegen
        perform_codegen()


class UpdateSchemaCommand(Command):
    description = 'Download latest version of the plot-schema JSON file'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if sys.version_info.major != 3:
            raise ImportError('Schema download must be executed with Python 3')

        import urllib.request
        url = ('https://raw.githubusercontent.com/plotly/plotly.js/'
               'v%s/dist/plot-schema.json' % plotly_js_version())
        with urllib.request.urlopen(url) as response:

            with open('plotly/package_data/plot-schema.json', 'wb') as f:
                f.write(response.read())


class UpdateBundleCommand(Command):
    description = 'Download latest version of the plot-schema JSON file'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if sys.version_info.major != 3:
            raise ImportError('Schema download must be executed with Python 3')

        import urllib.request
        url = ('https://raw.githubusercontent.com/plotly/plotly.js/'
               'v%s/dist/plotly.min.js' % plotly_js_version())
        with urllib.request.urlopen(url) as response:

            with open('plotly/package_data/plotly.min.js', 'wb') as f:
                f.write(response.read())

        # Write plotly.js version file
        with open('plotly/offline/_plotlyjs_version.py', 'w') as f:
            f.write("""\
# DO NOT EDIT
# This file is generated by the updatebundle setup.py command
__plotlyjs_version__ = '{plotlyjs_version}'
""".format(plotlyjs_version=plotly_js_version()))


class UpdatePlotlyJsCommand(Command):
    description = 'Update project to a new version of plotly.js'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_command('updatebundle')
        self.run_command('updateschema')
        self.run_command('codegen')


graph_objs_packages = [
    d[0] for d in os.walk('plotly/graph_objs')
    if not d[0].endswith('__pycache__')]


validator_packages = [
    d[0] for d in os.walk('plotly/validators')
    if not d[0].endswith('__pycache__')]


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
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Visualization',
      ],
      license='MIT',
      packages=['plotly',
                'plotlywidget',
                'plotly/api',
                'plotly/api/v1',
                'plotly/api/v2',
                'plotly/dashboard_objs',
                'plotly/presentation_objs',
                'plotly/plotly',
                'plotly/plotly/chunked_requests',
                'plotly/figure_factory',
                'plotly/grid_objs',
                'plotly/widgets',
                'plotly/offline',
                'plotly/io',
                'plotly/matplotlylib',
                'plotly/matplotlylib/mplexporter',
                'plotly/matplotlylib/mplexporter/renderers',
                '_plotly_utils'] + graph_objs_packages + validator_packages,
      package_data={'plotly': ['package_data/*', 'package_data/templates/*'],
                    'plotlywidget': ['static/*']},
      data_files=[
          ('share/jupyter/nbextensions/plotlywidget', [
              'plotlywidget/static/extension.js',
              'plotlywidget/static/index.js',
              'plotlywidget/static/index.js.map',
          ]),
          ('etc/jupyter/nbconfig/notebook.d', ['plotlywidget.json']),
      ],
      install_requires=['decorator>=4.0.6',
                        'nbformat>=4.2',
                        'pytz',
                        'requests',
                        'retrying>=1.3.3',
                        'six'],
      zip_safe=False,
      cmdclass={
          'build_py': js_prerelease(build_py),
          'egg_info': js_prerelease(egg_info),
          'sdist': js_prerelease(sdist, strict=True),
          'jsdeps': NPM,
          'codegen': CodegenCommand,
          'updateschema': UpdateSchemaCommand,
          'updatebundle': UpdateBundleCommand,
          'updateplotlyjs': js_prerelease(UpdatePlotlyJsCommand)
      },
)
