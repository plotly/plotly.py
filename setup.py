from setuptools import setup, Command
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist
from subprocess import check_call
from distutils import log

import os
import sys
import platform

plotly_js_version = '1.38.2'

exec(open('plotly/version.py').read())

here = os.path.dirname(os.path.abspath(__file__))
node_root = os.path.join(here, 'js')
is_repo = os.path.exists(os.path.join(here, '.git'))

npm_path = os.pathsep.join([
    os.path.join(node_root, 'node_modules', '.bin'),
                os.environ.get('PATH', os.defpath),
])

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
            raise ImportError('Code generation must be executed with Python >= 3.6')

        from codegen import perform_codegen
        perform_codegen()


class DownloadSchemaCommand(Command):
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
               'v%s/dist/plot-schema.json' % plotly_js_version)
        with urllib.request.urlopen(url) as response:

            with open('plotly/package_data/plot-schema.json', 'wb') as f:
                f.write(response.read())


class DownloadPlotlyJsCommand(Command):
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
               'v%s/dist/plotly.min.js' % plotly_js_version)
        with urllib.request.urlopen(url) as response:

            with open('plotly/package_data/plotly.min.js', 'wb') as f:
                f.write(response.read())


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
                'plotly/graph_objs',
                'plotly/graph_objs/scatterternary',
                'plotly/graph_objs/scatterternary/unselected',
                'plotly/graph_objs/scatterternary/hoverlabel',
                'plotly/graph_objs/scatterternary/selected',
                'plotly/graph_objs/scatterternary/marker',
                'plotly/graph_objs/scatterternary/marker/colorbar',
                'plotly/graph_objs/scattergl',
                'plotly/graph_objs/scattergl/unselected',
                'plotly/graph_objs/scattergl/hoverlabel',
                'plotly/graph_objs/scattergl/selected',
                'plotly/graph_objs/scattergl/marker',
                'plotly/graph_objs/scattergl/marker/colorbar',
                'plotly/graph_objs/violin',
                'plotly/graph_objs/violin/box',
                'plotly/graph_objs/violin/unselected',
                'plotly/graph_objs/violin/hoverlabel',
                'plotly/graph_objs/violin/selected',
                'plotly/graph_objs/violin/marker',
                'plotly/graph_objs/sankey',
                'plotly/graph_objs/sankey/hoverlabel',
                'plotly/graph_objs/sankey/link',
                'plotly/graph_objs/sankey/node',
                'plotly/graph_objs/box',
                'plotly/graph_objs/box/unselected',
                'plotly/graph_objs/box/hoverlabel',
                'plotly/graph_objs/box/selected',
                'plotly/graph_objs/box/marker',
                'plotly/graph_objs/histogram2dcontour',
                'plotly/graph_objs/histogram2dcontour/hoverlabel',
                'plotly/graph_objs/histogram2dcontour/colorbar',
                'plotly/graph_objs/histogram2dcontour/contours',
                'plotly/graph_objs/area',
                'plotly/graph_objs/area/hoverlabel',
                'plotly/graph_objs/layout',
                'plotly/graph_objs/layout/ternary',
                'plotly/graph_objs/layout/ternary/aaxis',
                'plotly/graph_objs/layout/ternary/baxis',
                'plotly/graph_objs/layout/ternary/caxis',
                'plotly/graph_objs/layout/legend',
                'plotly/graph_objs/layout/polar',
                'plotly/graph_objs/layout/polar/radialaxis',
                'plotly/graph_objs/layout/polar/angularaxis',
                'plotly/graph_objs/layout/shape',
                'plotly/graph_objs/layout/geo',
                'plotly/graph_objs/layout/geo/projection',
                'plotly/graph_objs/layout/slider',
                'plotly/graph_objs/layout/slider/currentvalue',
                'plotly/graph_objs/layout/hoverlabel',
                'plotly/graph_objs/layout/annotation',
                'plotly/graph_objs/layout/annotation/hoverlabel',
                'plotly/graph_objs/layout/yaxis',
                'plotly/graph_objs/layout/mapbox',
                'plotly/graph_objs/layout/mapbox/layer',
                'plotly/graph_objs/layout/mapbox/layer/symbol',
                'plotly/graph_objs/layout/xaxis',
                'plotly/graph_objs/layout/xaxis/rangeslider',
                'plotly/graph_objs/layout/xaxis/rangeselector',
                'plotly/graph_objs/layout/scene',
                'plotly/graph_objs/layout/scene/camera',
                'plotly/graph_objs/layout/scene/annotation',
                'plotly/graph_objs/layout/scene/annotation/hoverlabel',
                'plotly/graph_objs/layout/scene/yaxis',
                'plotly/graph_objs/layout/scene/xaxis',
                'plotly/graph_objs/layout/scene/zaxis',
                'plotly/graph_objs/layout/updatemenu',
                'plotly/graph_objs/layout/grid',
                'plotly/graph_objs/ohlc',
                'plotly/graph_objs/ohlc/hoverlabel',
                'plotly/graph_objs/ohlc/decreasing',
                'plotly/graph_objs/ohlc/increasing',
                'plotly/graph_objs/mesh3d',
                'plotly/graph_objs/mesh3d/hoverlabel',
                'plotly/graph_objs/mesh3d/colorbar',
                'plotly/graph_objs/parcoords',
                'plotly/graph_objs/parcoords/hoverlabel',
                'plotly/graph_objs/parcoords/line',
                'plotly/graph_objs/parcoords/line/colorbar',
                'plotly/graph_objs/contour',
                'plotly/graph_objs/contour/hoverlabel',
                'plotly/graph_objs/contour/colorbar',
                'plotly/graph_objs/contour/contours',
                'plotly/graph_objs/scattermapbox',
                'plotly/graph_objs/scattermapbox/unselected',
                'plotly/graph_objs/scattermapbox/hoverlabel',
                'plotly/graph_objs/scattermapbox/selected',
                'plotly/graph_objs/scattermapbox/marker',
                'plotly/graph_objs/scattermapbox/marker/colorbar',
                'plotly/graph_objs/scatterpolargl',
                'plotly/graph_objs/scatterpolargl/unselected',
                'plotly/graph_objs/scatterpolargl/hoverlabel',
                'plotly/graph_objs/scatterpolargl/selected',
                'plotly/graph_objs/scatterpolargl/marker',
                'plotly/graph_objs/scatterpolargl/marker/colorbar',
                'plotly/graph_objs/histogram2d',
                'plotly/graph_objs/histogram2d/hoverlabel',
                'plotly/graph_objs/histogram2d/colorbar',
                'plotly/graph_objs/surface',
                'plotly/graph_objs/surface/hoverlabel',
                'plotly/graph_objs/surface/colorbar',
                'plotly/graph_objs/surface/contours',
                'plotly/graph_objs/surface/contours/z',
                'plotly/graph_objs/surface/contours/x',
                'plotly/graph_objs/surface/contours/y',
                'plotly/graph_objs/carpet',
                'plotly/graph_objs/carpet/aaxis',
                'plotly/graph_objs/carpet/baxis',
                'plotly/graph_objs/carpet/hoverlabel',
                'plotly/graph_objs/contourcarpet',
                'plotly/graph_objs/contourcarpet/hoverlabel',
                'plotly/graph_objs/contourcarpet/colorbar',
                'plotly/graph_objs/contourcarpet/contours',
                'plotly/graph_objs/pie',
                'plotly/graph_objs/pie/hoverlabel',
                'plotly/graph_objs/pie/marker',
                'plotly/graph_objs/choropleth',
                'plotly/graph_objs/choropleth/unselected',
                'plotly/graph_objs/choropleth/hoverlabel',
                'plotly/graph_objs/choropleth/colorbar',
                'plotly/graph_objs/choropleth/selected',
                'plotly/graph_objs/choropleth/marker',
                'plotly/graph_objs/scatter',
                'plotly/graph_objs/scatter/unselected',
                'plotly/graph_objs/scatter/hoverlabel',
                'plotly/graph_objs/scatter/selected',
                'plotly/graph_objs/scatter/marker',
                'plotly/graph_objs/scatter/marker/colorbar',
                'plotly/graph_objs/table',
                'plotly/graph_objs/table/cells',
                'plotly/graph_objs/table/hoverlabel',
                'plotly/graph_objs/table/header',
                'plotly/graph_objs/scatter3d',
                'plotly/graph_objs/scatter3d/hoverlabel',
                'plotly/graph_objs/scatter3d/marker',
                'plotly/graph_objs/scatter3d/marker/colorbar',
                'plotly/graph_objs/scatter3d/projection',
                'plotly/graph_objs/scatterpolar',
                'plotly/graph_objs/scatterpolar/unselected',
                'plotly/graph_objs/scatterpolar/hoverlabel',
                'plotly/graph_objs/scatterpolar/selected',
                'plotly/graph_objs/scatterpolar/marker',
                'plotly/graph_objs/scatterpolar/marker/colorbar',
                'plotly/graph_objs/scattergeo',
                'plotly/graph_objs/scattergeo/unselected',
                'plotly/graph_objs/scattergeo/hoverlabel',
                'plotly/graph_objs/scattergeo/selected',
                'plotly/graph_objs/scattergeo/marker',
                'plotly/graph_objs/scattergeo/marker/colorbar',
                'plotly/graph_objs/candlestick',
                'plotly/graph_objs/candlestick/hoverlabel',
                'plotly/graph_objs/candlestick/decreasing',
                'plotly/graph_objs/candlestick/increasing',
                'plotly/graph_objs/heatmapgl',
                'plotly/graph_objs/heatmapgl/hoverlabel',
                'plotly/graph_objs/heatmapgl/colorbar',
                'plotly/graph_objs/heatmap',
                'plotly/graph_objs/heatmap/hoverlabel',
                'plotly/graph_objs/heatmap/colorbar',
                'plotly/graph_objs/bar',
                'plotly/graph_objs/bar/unselected',
                'plotly/graph_objs/bar/hoverlabel',
                'plotly/graph_objs/bar/selected',
                'plotly/graph_objs/bar/marker',
                'plotly/graph_objs/bar/marker/colorbar',
                'plotly/graph_objs/scattercarpet',
                'plotly/graph_objs/scattercarpet/unselected',
                'plotly/graph_objs/scattercarpet/hoverlabel',
                'plotly/graph_objs/scattercarpet/selected',
                'plotly/graph_objs/scattercarpet/marker',
                'plotly/graph_objs/scattercarpet/marker/colorbar',
                'plotly/graph_objs/pointcloud',
                'plotly/graph_objs/pointcloud/hoverlabel',
                'plotly/graph_objs/pointcloud/marker',
                'plotly/graph_objs/histogram',
                'plotly/graph_objs/histogram/unselected',
                'plotly/graph_objs/histogram/hoverlabel',
                'plotly/graph_objs/histogram/selected',
                'plotly/graph_objs/histogram/marker',
                'plotly/graph_objs/histogram/marker/colorbar',
                'plotly/grid_objs',
                'plotly/validators',
                'plotly/validators/scatterternary',
                'plotly/validators/scatterternary/stream',
                'plotly/validators/scatterternary/unselected',
                'plotly/validators/scatterternary/unselected/textfont',
                'plotly/validators/scatterternary/unselected/marker',
                'plotly/validators/scatterternary/textfont',
                'plotly/validators/scatterternary/hoverlabel',
                'plotly/validators/scatterternary/hoverlabel/font',
                'plotly/validators/scatterternary/selected',
                'plotly/validators/scatterternary/selected/textfont',
                'plotly/validators/scatterternary/selected/marker',
                'plotly/validators/scatterternary/line',
                'plotly/validators/scatterternary/marker',
                'plotly/validators/scatterternary/marker/gradient',
                'plotly/validators/scatterternary/marker/colorbar',
                'plotly/validators/scatterternary/marker/colorbar/tickformatstop',
                'plotly/validators/scatterternary/marker/colorbar/tickfont',
                'plotly/validators/scatterternary/marker/colorbar/titlefont',
                'plotly/validators/scatterternary/marker/line',
                'plotly/validators/scattergl',
                'plotly/validators/scattergl/stream',
                'plotly/validators/scattergl/unselected',
                'plotly/validators/scattergl/unselected/marker',
                'plotly/validators/scattergl/hoverlabel',
                'plotly/validators/scattergl/hoverlabel/font',
                'plotly/validators/scattergl/selected',
                'plotly/validators/scattergl/selected/marker',
                'plotly/validators/scattergl/line',
                'plotly/validators/scattergl/error_y',
                'plotly/validators/scattergl/error_x',
                'plotly/validators/scattergl/marker',
                'plotly/validators/scattergl/marker/colorbar',
                'plotly/validators/scattergl/marker/colorbar/tickformatstop',
                'plotly/validators/scattergl/marker/colorbar/tickfont',
                'plotly/validators/scattergl/marker/colorbar/titlefont',
                'plotly/validators/scattergl/marker/line',
                'plotly/validators/violin',
                'plotly/validators/violin/box',
                'plotly/validators/violin/box/line',
                'plotly/validators/violin/meanline',
                'plotly/validators/violin/stream',
                'plotly/validators/violin/unselected',
                'plotly/validators/violin/unselected/marker',
                'plotly/validators/violin/hoverlabel',
                'plotly/validators/violin/hoverlabel/font',
                'plotly/validators/violin/selected',
                'plotly/validators/violin/selected/marker',
                'plotly/validators/violin/line',
                'plotly/validators/violin/marker',
                'plotly/validators/violin/marker/line',
                'plotly/validators/sankey',
                'plotly/validators/sankey/stream',
                'plotly/validators/sankey/textfont',
                'plotly/validators/sankey/hoverlabel',
                'plotly/validators/sankey/hoverlabel/font',
                'plotly/validators/sankey/link',
                'plotly/validators/sankey/link/line',
                'plotly/validators/sankey/node',
                'plotly/validators/sankey/node/line',
                'plotly/validators/sankey/domain',
                'plotly/validators/box',
                'plotly/validators/box/stream',
                'plotly/validators/box/unselected',
                'plotly/validators/box/unselected/marker',
                'plotly/validators/box/hoverlabel',
                'plotly/validators/box/hoverlabel/font',
                'plotly/validators/box/selected',
                'plotly/validators/box/selected/marker',
                'plotly/validators/box/line',
                'plotly/validators/box/marker',
                'plotly/validators/box/marker/line',
                'plotly/validators/histogram2dcontour',
                'plotly/validators/histogram2dcontour/ybins',
                'plotly/validators/histogram2dcontour/xbins',
                'plotly/validators/histogram2dcontour/stream',
                'plotly/validators/histogram2dcontour/hoverlabel',
                'plotly/validators/histogram2dcontour/hoverlabel/font',
                'plotly/validators/histogram2dcontour/colorbar',
                'plotly/validators/histogram2dcontour/colorbar/tickformatstop',
                'plotly/validators/histogram2dcontour/colorbar/tickfont',
                'plotly/validators/histogram2dcontour/colorbar/titlefont',
                'plotly/validators/histogram2dcontour/line',
                'plotly/validators/histogram2dcontour/contours',
                'plotly/validators/histogram2dcontour/contours/labelfont',
                'plotly/validators/histogram2dcontour/marker',
                'plotly/validators/area',
                'plotly/validators/area/stream',
                'plotly/validators/area/hoverlabel',
                'plotly/validators/area/hoverlabel/font',
                'plotly/validators/area/marker',
                'plotly/validators/layout',
                'plotly/validators/layout/ternary',
                'plotly/validators/layout/ternary/aaxis',
                'plotly/validators/layout/ternary/aaxis/tickformatstop',
                'plotly/validators/layout/ternary/aaxis/tickfont',
                'plotly/validators/layout/ternary/aaxis/titlefont',
                'plotly/validators/layout/ternary/baxis',
                'plotly/validators/layout/ternary/baxis/tickformatstop',
                'plotly/validators/layout/ternary/baxis/tickfont',
                'plotly/validators/layout/ternary/baxis/titlefont',
                'plotly/validators/layout/ternary/caxis',
                'plotly/validators/layout/ternary/caxis/tickformatstop',
                'plotly/validators/layout/ternary/caxis/tickfont',
                'plotly/validators/layout/ternary/caxis/titlefont',
                'plotly/validators/layout/ternary/domain',
                'plotly/validators/layout/legend',
                'plotly/validators/layout/legend/font',
                'plotly/validators/layout/polar',
                'plotly/validators/layout/polar/radialaxis',
                'plotly/validators/layout/polar/radialaxis/tickformatstop',
                'plotly/validators/layout/polar/radialaxis/tickfont',
                'plotly/validators/layout/polar/radialaxis/titlefont',
                'plotly/validators/layout/polar/angularaxis',
                'plotly/validators/layout/polar/angularaxis/tickformatstop',
                'plotly/validators/layout/polar/angularaxis/tickfont',
                'plotly/validators/layout/polar/domain',
                'plotly/validators/layout/shape',
                'plotly/validators/layout/shape/line',
                'plotly/validators/layout/radialaxis',
                'plotly/validators/layout/geo',
                'plotly/validators/layout/geo/center',
                'plotly/validators/layout/geo/lataxis',
                'plotly/validators/layout/geo/domain',
                'plotly/validators/layout/geo/lonaxis',
                'plotly/validators/layout/geo/projection',
                'plotly/validators/layout/geo/projection/rotation',
                'plotly/validators/layout/slider',
                'plotly/validators/layout/slider/transition',
                'plotly/validators/layout/slider/currentvalue',
                'plotly/validators/layout/slider/currentvalue/font',
                'plotly/validators/layout/slider/step',
                'plotly/validators/layout/slider/pad',
                'plotly/validators/layout/slider/font',
                'plotly/validators/layout/hoverlabel',
                'plotly/validators/layout/hoverlabel/font',
                'plotly/validators/layout/annotation',
                'plotly/validators/layout/annotation/hoverlabel',
                'plotly/validators/layout/annotation/hoverlabel/font',
                'plotly/validators/layout/annotation/font',
                'plotly/validators/layout/image',
                'plotly/validators/layout/titlefont',
                'plotly/validators/layout/yaxis',
                'plotly/validators/layout/yaxis/tickformatstop',
                'plotly/validators/layout/yaxis/tickfont',
                'plotly/validators/layout/yaxis/titlefont',
                'plotly/validators/layout/mapbox',
                'plotly/validators/layout/mapbox/center',
                'plotly/validators/layout/mapbox/layer',
                'plotly/validators/layout/mapbox/layer/fill',
                'plotly/validators/layout/mapbox/layer/symbol',
                'plotly/validators/layout/mapbox/layer/symbol/textfont',
                'plotly/validators/layout/mapbox/layer/line',
                'plotly/validators/layout/mapbox/layer/circle',
                'plotly/validators/layout/mapbox/domain',
                'plotly/validators/layout/xaxis',
                'plotly/validators/layout/xaxis/tickformatstop',
                'plotly/validators/layout/xaxis/rangeslider',
                'plotly/validators/layout/xaxis/rangeslider/yaxis',
                'plotly/validators/layout/xaxis/tickfont',
                'plotly/validators/layout/xaxis/titlefont',
                'plotly/validators/layout/xaxis/rangeselector',
                'plotly/validators/layout/xaxis/rangeselector/button',
                'plotly/validators/layout/xaxis/rangeselector/font',
                'plotly/validators/layout/angularaxis',
                'plotly/validators/layout/font',
                'plotly/validators/layout/margin',
                'plotly/validators/layout/scene',
                'plotly/validators/layout/scene/camera',
                'plotly/validators/layout/scene/camera/eye',
                'plotly/validators/layout/scene/camera/center',
                'plotly/validators/layout/scene/camera/up',
                'plotly/validators/layout/scene/aspectratio',
                'plotly/validators/layout/scene/annotation',
                'plotly/validators/layout/scene/annotation/hoverlabel',
                'plotly/validators/layout/scene/annotation/hoverlabel/font',
                'plotly/validators/layout/scene/annotation/font',
                'plotly/validators/layout/scene/yaxis',
                'plotly/validators/layout/scene/yaxis/tickformatstop',
                'plotly/validators/layout/scene/yaxis/tickfont',
                'plotly/validators/layout/scene/yaxis/titlefont',
                'plotly/validators/layout/scene/xaxis',
                'plotly/validators/layout/scene/xaxis/tickformatstop',
                'plotly/validators/layout/scene/xaxis/tickfont',
                'plotly/validators/layout/scene/xaxis/titlefont',
                'plotly/validators/layout/scene/zaxis',
                'plotly/validators/layout/scene/zaxis/tickformatstop',
                'plotly/validators/layout/scene/zaxis/tickfont',
                'plotly/validators/layout/scene/zaxis/titlefont',
                'plotly/validators/layout/scene/domain',
                'plotly/validators/layout/updatemenu',
                'plotly/validators/layout/updatemenu/pad',
                'plotly/validators/layout/updatemenu/button',
                'plotly/validators/layout/updatemenu/font',
                'plotly/validators/layout/grid',
                'plotly/validators/layout/grid/domain',
                'plotly/validators/ohlc',
                'plotly/validators/ohlc/stream',
                'plotly/validators/ohlc/hoverlabel',
                'plotly/validators/ohlc/hoverlabel/font',
                'plotly/validators/ohlc/line',
                'plotly/validators/ohlc/decreasing',
                'plotly/validators/ohlc/decreasing/line',
                'plotly/validators/ohlc/increasing',
                'plotly/validators/ohlc/increasing/line',
                'plotly/validators/mesh3d',
                'plotly/validators/mesh3d/stream',
                'plotly/validators/mesh3d/contour',
                'plotly/validators/mesh3d/hoverlabel',
                'plotly/validators/mesh3d/hoverlabel/font',
                'plotly/validators/mesh3d/colorbar',
                'plotly/validators/mesh3d/colorbar/tickformatstop',
                'plotly/validators/mesh3d/colorbar/tickfont',
                'plotly/validators/mesh3d/colorbar/titlefont',
                'plotly/validators/mesh3d/lighting',
                'plotly/validators/mesh3d/lightposition',
                'plotly/validators/parcoords',
                'plotly/validators/parcoords/stream',
                'plotly/validators/parcoords/rangefont',
                'plotly/validators/parcoords/hoverlabel',
                'plotly/validators/parcoords/hoverlabel/font',
                'plotly/validators/parcoords/tickfont',
                'plotly/validators/parcoords/line',
                'plotly/validators/parcoords/line/colorbar',
                'plotly/validators/parcoords/line/colorbar/tickformatstop',
                'plotly/validators/parcoords/line/colorbar/tickfont',
                'plotly/validators/parcoords/line/colorbar/titlefont',
                'plotly/validators/parcoords/labelfont',
                'plotly/validators/parcoords/domain',
                'plotly/validators/parcoords/dimension',
                'plotly/validators/contour',
                'plotly/validators/contour/stream',
                'plotly/validators/contour/hoverlabel',
                'plotly/validators/contour/hoverlabel/font',
                'plotly/validators/contour/colorbar',
                'plotly/validators/contour/colorbar/tickformatstop',
                'plotly/validators/contour/colorbar/tickfont',
                'plotly/validators/contour/colorbar/titlefont',
                'plotly/validators/contour/line',
                'plotly/validators/contour/contours',
                'plotly/validators/contour/contours/labelfont',
                'plotly/validators/scattermapbox',
                'plotly/validators/scattermapbox/stream',
                'plotly/validators/scattermapbox/unselected',
                'plotly/validators/scattermapbox/unselected/marker',
                'plotly/validators/scattermapbox/textfont',
                'plotly/validators/scattermapbox/hoverlabel',
                'plotly/validators/scattermapbox/hoverlabel/font',
                'plotly/validators/scattermapbox/selected',
                'plotly/validators/scattermapbox/selected/marker',
                'plotly/validators/scattermapbox/line',
                'plotly/validators/scattermapbox/marker',
                'plotly/validators/scattermapbox/marker/colorbar',
                'plotly/validators/scattermapbox/marker/colorbar/tickformatstop',
                'plotly/validators/scattermapbox/marker/colorbar/tickfont',
                'plotly/validators/scattermapbox/marker/colorbar/titlefont',
                'plotly/validators/scatterpolargl',
                'plotly/validators/scatterpolargl/stream',
                'plotly/validators/scatterpolargl/unselected',
                'plotly/validators/scatterpolargl/unselected/textfont',
                'plotly/validators/scatterpolargl/unselected/marker',
                'plotly/validators/scatterpolargl/hoverlabel',
                'plotly/validators/scatterpolargl/hoverlabel/font',
                'plotly/validators/scatterpolargl/selected',
                'plotly/validators/scatterpolargl/selected/textfont',
                'plotly/validators/scatterpolargl/selected/marker',
                'plotly/validators/scatterpolargl/line',
                'plotly/validators/scatterpolargl/marker',
                'plotly/validators/scatterpolargl/marker/colorbar',
                'plotly/validators/scatterpolargl/marker/colorbar/tickformatstop',
                'plotly/validators/scatterpolargl/marker/colorbar/tickfont',
                'plotly/validators/scatterpolargl/marker/colorbar/titlefont',
                'plotly/validators/scatterpolargl/marker/line',
                'plotly/validators/histogram2d',
                'plotly/validators/histogram2d/ybins',
                'plotly/validators/histogram2d/xbins',
                'plotly/validators/histogram2d/stream',
                'plotly/validators/histogram2d/hoverlabel',
                'plotly/validators/histogram2d/hoverlabel/font',
                'plotly/validators/histogram2d/colorbar',
                'plotly/validators/histogram2d/colorbar/tickformatstop',
                'plotly/validators/histogram2d/colorbar/tickfont',
                'plotly/validators/histogram2d/colorbar/titlefont',
                'plotly/validators/histogram2d/marker',
                'plotly/validators/surface',
                'plotly/validators/surface/stream',
                'plotly/validators/surface/hoverlabel',
                'plotly/validators/surface/hoverlabel/font',
                'plotly/validators/surface/colorbar',
                'plotly/validators/surface/colorbar/tickformatstop',
                'plotly/validators/surface/colorbar/tickfont',
                'plotly/validators/surface/colorbar/titlefont',
                'plotly/validators/surface/contours',
                'plotly/validators/surface/contours/z',
                'plotly/validators/surface/contours/z/project',
                'plotly/validators/surface/contours/x',
                'plotly/validators/surface/contours/x/project',
                'plotly/validators/surface/contours/y',
                'plotly/validators/surface/contours/y/project',
                'plotly/validators/surface/lighting',
                'plotly/validators/surface/lightposition',
                'plotly/validators/frame',
                'plotly/validators/carpet',
                'plotly/validators/carpet/aaxis',
                'plotly/validators/carpet/aaxis/tickformatstop',
                'plotly/validators/carpet/aaxis/tickfont',
                'plotly/validators/carpet/aaxis/titlefont',
                'plotly/validators/carpet/baxis',
                'plotly/validators/carpet/baxis/tickformatstop',
                'plotly/validators/carpet/baxis/tickfont',
                'plotly/validators/carpet/baxis/titlefont',
                'plotly/validators/carpet/stream',
                'plotly/validators/carpet/hoverlabel',
                'plotly/validators/carpet/hoverlabel/font',
                'plotly/validators/carpet/font',
                'plotly/validators/contourcarpet',
                'plotly/validators/contourcarpet/stream',
                'plotly/validators/contourcarpet/hoverlabel',
                'plotly/validators/contourcarpet/hoverlabel/font',
                'plotly/validators/contourcarpet/colorbar',
                'plotly/validators/contourcarpet/colorbar/tickformatstop',
                'plotly/validators/contourcarpet/colorbar/tickfont',
                'plotly/validators/contourcarpet/colorbar/titlefont',
                'plotly/validators/contourcarpet/line',
                'plotly/validators/contourcarpet/contours',
                'plotly/validators/contourcarpet/contours/labelfont',
                'plotly/validators/pie',
                'plotly/validators/pie/outsidetextfont',
                'plotly/validators/pie/stream',
                'plotly/validators/pie/textfont',
                'plotly/validators/pie/hoverlabel',
                'plotly/validators/pie/hoverlabel/font',
                'plotly/validators/pie/insidetextfont',
                'plotly/validators/pie/marker',
                'plotly/validators/pie/marker/line',
                'plotly/validators/pie/domain',
                'plotly/validators/choropleth',
                'plotly/validators/choropleth/stream',
                'plotly/validators/choropleth/unselected',
                'plotly/validators/choropleth/unselected/marker',
                'plotly/validators/choropleth/hoverlabel',
                'plotly/validators/choropleth/hoverlabel/font',
                'plotly/validators/choropleth/colorbar',
                'plotly/validators/choropleth/colorbar/tickformatstop',
                'plotly/validators/choropleth/colorbar/tickfont',
                'plotly/validators/choropleth/colorbar/titlefont',
                'plotly/validators/choropleth/selected',
                'plotly/validators/choropleth/selected/marker',
                'plotly/validators/choropleth/marker',
                'plotly/validators/choropleth/marker/line',
                'plotly/validators/scatter',
                'plotly/validators/scatter/stream',
                'plotly/validators/scatter/unselected',
                'plotly/validators/scatter/unselected/textfont',
                'plotly/validators/scatter/unselected/marker',
                'plotly/validators/scatter/textfont',
                'plotly/validators/scatter/hoverlabel',
                'plotly/validators/scatter/hoverlabel/font',
                'plotly/validators/scatter/selected',
                'plotly/validators/scatter/selected/textfont',
                'plotly/validators/scatter/selected/marker',
                'plotly/validators/scatter/line',
                'plotly/validators/scatter/error_y',
                'plotly/validators/scatter/error_x',
                'plotly/validators/scatter/marker',
                'plotly/validators/scatter/marker/gradient',
                'plotly/validators/scatter/marker/colorbar',
                'plotly/validators/scatter/marker/colorbar/tickformatstop',
                'plotly/validators/scatter/marker/colorbar/tickfont',
                'plotly/validators/scatter/marker/colorbar/titlefont',
                'plotly/validators/scatter/marker/line',
                'plotly/validators/table',
                'plotly/validators/table/cells',
                'plotly/validators/table/cells/fill',
                'plotly/validators/table/cells/line',
                'plotly/validators/table/cells/font',
                'plotly/validators/table/stream',
                'plotly/validators/table/hoverlabel',
                'plotly/validators/table/hoverlabel/font',
                'plotly/validators/table/domain',
                'plotly/validators/table/header',
                'plotly/validators/table/header/fill',
                'plotly/validators/table/header/line',
                'plotly/validators/table/header/font',
                'plotly/validators/scatter3d',
                'plotly/validators/scatter3d/error_z',
                'plotly/validators/scatter3d/stream',
                'plotly/validators/scatter3d/textfont',
                'plotly/validators/scatter3d/hoverlabel',
                'plotly/validators/scatter3d/hoverlabel/font',
                'plotly/validators/scatter3d/line',
                'plotly/validators/scatter3d/error_y',
                'plotly/validators/scatter3d/error_x',
                'plotly/validators/scatter3d/marker',
                'plotly/validators/scatter3d/marker/colorbar',
                'plotly/validators/scatter3d/marker/colorbar/tickformatstop',
                'plotly/validators/scatter3d/marker/colorbar/tickfont',
                'plotly/validators/scatter3d/marker/colorbar/titlefont',
                'plotly/validators/scatter3d/marker/line',
                'plotly/validators/scatter3d/projection',
                'plotly/validators/scatter3d/projection/z',
                'plotly/validators/scatter3d/projection/x',
                'plotly/validators/scatter3d/projection/y',
                'plotly/validators/scatterpolar',
                'plotly/validators/scatterpolar/stream',
                'plotly/validators/scatterpolar/unselected',
                'plotly/validators/scatterpolar/unselected/textfont',
                'plotly/validators/scatterpolar/unselected/marker',
                'plotly/validators/scatterpolar/textfont',
                'plotly/validators/scatterpolar/hoverlabel',
                'plotly/validators/scatterpolar/hoverlabel/font',
                'plotly/validators/scatterpolar/selected',
                'plotly/validators/scatterpolar/selected/textfont',
                'plotly/validators/scatterpolar/selected/marker',
                'plotly/validators/scatterpolar/line',
                'plotly/validators/scatterpolar/marker',
                'plotly/validators/scatterpolar/marker/gradient',
                'plotly/validators/scatterpolar/marker/colorbar',
                'plotly/validators/scatterpolar/marker/colorbar/tickformatstop',
                'plotly/validators/scatterpolar/marker/colorbar/tickfont',
                'plotly/validators/scatterpolar/marker/colorbar/titlefont',
                'plotly/validators/scatterpolar/marker/line',
                'plotly/validators/scattergeo',
                'plotly/validators/scattergeo/stream',
                'plotly/validators/scattergeo/unselected',
                'plotly/validators/scattergeo/unselected/textfont',
                'plotly/validators/scattergeo/unselected/marker',
                'plotly/validators/scattergeo/textfont',
                'plotly/validators/scattergeo/hoverlabel',
                'plotly/validators/scattergeo/hoverlabel/font',
                'plotly/validators/scattergeo/selected',
                'plotly/validators/scattergeo/selected/textfont',
                'plotly/validators/scattergeo/selected/marker',
                'plotly/validators/scattergeo/line',
                'plotly/validators/scattergeo/marker',
                'plotly/validators/scattergeo/marker/gradient',
                'plotly/validators/scattergeo/marker/colorbar',
                'plotly/validators/scattergeo/marker/colorbar/tickformatstop',
                'plotly/validators/scattergeo/marker/colorbar/tickfont',
                'plotly/validators/scattergeo/marker/colorbar/titlefont',
                'plotly/validators/scattergeo/marker/line',
                'plotly/validators/candlestick',
                'plotly/validators/candlestick/stream',
                'plotly/validators/candlestick/hoverlabel',
                'plotly/validators/candlestick/hoverlabel/font',
                'plotly/validators/candlestick/line',
                'plotly/validators/candlestick/decreasing',
                'plotly/validators/candlestick/decreasing/line',
                'plotly/validators/candlestick/increasing',
                'plotly/validators/candlestick/increasing/line',
                'plotly/validators/heatmapgl',
                'plotly/validators/heatmapgl/stream',
                'plotly/validators/heatmapgl/hoverlabel',
                'plotly/validators/heatmapgl/hoverlabel/font',
                'plotly/validators/heatmapgl/colorbar',
                'plotly/validators/heatmapgl/colorbar/tickformatstop',
                'plotly/validators/heatmapgl/colorbar/tickfont',
                'plotly/validators/heatmapgl/colorbar/titlefont',
                'plotly/validators/heatmap',
                'plotly/validators/heatmap/stream',
                'plotly/validators/heatmap/hoverlabel',
                'plotly/validators/heatmap/hoverlabel/font',
                'plotly/validators/heatmap/colorbar',
                'plotly/validators/heatmap/colorbar/tickformatstop',
                'plotly/validators/heatmap/colorbar/tickfont',
                'plotly/validators/heatmap/colorbar/titlefont',
                'plotly/validators/bar',
                'plotly/validators/bar/outsidetextfont',
                'plotly/validators/bar/stream',
                'plotly/validators/bar/unselected',
                'plotly/validators/bar/unselected/textfont',
                'plotly/validators/bar/unselected/marker',
                'plotly/validators/bar/textfont',
                'plotly/validators/bar/hoverlabel',
                'plotly/validators/bar/hoverlabel/font',
                'plotly/validators/bar/selected',
                'plotly/validators/bar/selected/textfont',
                'plotly/validators/bar/selected/marker',
                'plotly/validators/bar/error_y',
                'plotly/validators/bar/insidetextfont',
                'plotly/validators/bar/error_x',
                'plotly/validators/bar/marker',
                'plotly/validators/bar/marker/colorbar',
                'plotly/validators/bar/marker/colorbar/tickformatstop',
                'plotly/validators/bar/marker/colorbar/tickfont',
                'plotly/validators/bar/marker/colorbar/titlefont',
                'plotly/validators/bar/marker/line',
                'plotly/validators/scattercarpet',
                'plotly/validators/scattercarpet/stream',
                'plotly/validators/scattercarpet/unselected',
                'plotly/validators/scattercarpet/unselected/textfont',
                'plotly/validators/scattercarpet/unselected/marker',
                'plotly/validators/scattercarpet/textfont',
                'plotly/validators/scattercarpet/hoverlabel',
                'plotly/validators/scattercarpet/hoverlabel/font',
                'plotly/validators/scattercarpet/selected',
                'plotly/validators/scattercarpet/selected/textfont',
                'plotly/validators/scattercarpet/selected/marker',
                'plotly/validators/scattercarpet/line',
                'plotly/validators/scattercarpet/marker',
                'plotly/validators/scattercarpet/marker/gradient',
                'plotly/validators/scattercarpet/marker/colorbar',
                'plotly/validators/scattercarpet/marker/colorbar/tickformatstop',
                'plotly/validators/scattercarpet/marker/colorbar/tickfont',
                'plotly/validators/scattercarpet/marker/colorbar/titlefont',
                'plotly/validators/scattercarpet/marker/line',
                'plotly/validators/pointcloud',
                'plotly/validators/pointcloud/stream',
                'plotly/validators/pointcloud/hoverlabel',
                'plotly/validators/pointcloud/hoverlabel/font',
                'plotly/validators/pointcloud/marker',
                'plotly/validators/pointcloud/marker/border',
                'plotly/validators/histogram',
                'plotly/validators/histogram/ybins',
                'plotly/validators/histogram/xbins',
                'plotly/validators/histogram/stream',
                'plotly/validators/histogram/unselected',
                'plotly/validators/histogram/unselected/textfont',
                'plotly/validators/histogram/unselected/marker',
                'plotly/validators/histogram/hoverlabel',
                'plotly/validators/histogram/hoverlabel/font',
                'plotly/validators/histogram/selected',
                'plotly/validators/histogram/selected/textfont',
                'plotly/validators/histogram/selected/marker',
                'plotly/validators/histogram/error_y',
                'plotly/validators/histogram/error_x',
                'plotly/validators/histogram/cumulative',
                'plotly/validators/histogram/marker',
                'plotly/validators/histogram/marker/colorbar',
                'plotly/validators/histogram/marker/colorbar/tickformatstop',
                'plotly/validators/histogram/marker/colorbar/tickfont',
                'plotly/validators/histogram/marker/colorbar/titlefont',
                'plotly/validators/histogram/marker/line',
                'plotly/widgets',
                'plotly/offline',
                'plotly/matplotlylib',
                'plotly/matplotlylib/mplexporter',
                'plotly/matplotlylib/mplexporter/renderers',
                '_plotly_utils'],
      package_data={'plotly': ['package_data/*'], 'plotlywidget': ['static/*']},
      data_files=[
          ('share/jupyter/nbextensions/plotlywidget', [
              'plotlywidget/static/extension.js',
              'plotlywidget/static/index.js',
              'plotlywidget/static/index.js.map',
          ]),
      ],
      install_requires=['decorator>=4.0.6',
                        'nbformat>=4.2',
                        'pytz',
                        'requests',
                        'six'],
      zip_safe=False,
      cmdclass={
          'build_py': js_prerelease(build_py),
          'egg_info': js_prerelease(egg_info),
          'sdist': js_prerelease(sdist, strict=True),
          'jsdeps': NPM,
          'codegen': CodegenCommand,
          'updateschema': DownloadSchemaCommand,
          'updateplotlyjs': DownloadPlotlyJsCommand
      },
)
