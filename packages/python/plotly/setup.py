import os
import sys
import platform
import json

from setuptools import setup, Command
from setuptools.command.egg_info import egg_info
from subprocess import check_call
from distutils import log

# ensure the current directory is on sys.path; so versioneer can be imported
# when pip uses PEP 517/518 build rules.
# https://github.com/python-versioneer/python-versioneer/issues/193
sys.path.append(os.path.dirname(__file__))

import versioneer


here = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(here)))
node_root = os.path.join(project_root, "packages", "javascript", "jupyterlab-plotly")
is_repo = os.path.exists(os.path.join(project_root, ".git"))

npm_path = os.pathsep.join(
    [
        os.path.join(node_root, "node_modules", ".bin"),
        os.environ.get("PATH", os.defpath),
    ]
)

labstatic = "jupyterlab_plotly/labextension/static"
if not os.path.exists(labstatic):
    # Ensure the folder exists when we will look for files in it
    os.makedirs(labstatic)

prebuilt_assets = [
    (
        "share/jupyter/labextensions/jupyterlab-plotly",
        [
            "jupyterlab_plotly/labextension/package.json",
        ],
    ),
    (
        "share/jupyter/labextensions/jupyterlab-plotly/static",
        [os.path.join(labstatic, f) for f in os.listdir(labstatic)],
    ),
    (
        "share/jupyter/nbextensions/jupyterlab-plotly",
        [
            "jupyterlab_plotly/nbextension/extension.js",
            "jupyterlab_plotly/nbextension/index.js",
            "jupyterlab_plotly/nbextension/index.js.LICENSE.txt",
        ],
    ),
]


if "--skip-npm" in sys.argv or os.environ.get("SKIP_NPM") is not None:
    print("Skipping npm install as requested.")
    skip_npm = True
    if "--skip-npm" in sys.argv:
        sys.argv.remove("--skip-npm")
else:
    skip_npm = False

# Load plotly.js version from js/package.json
def plotly_js_version():
    path = os.path.join(
        project_root, "packages", "javascript", "jupyterlab-plotly", "package.json"
    )
    with open(path, "rt") as f:
        package_json = json.load(f)
        version = package_json["dependencies"]["plotly.js"]
        version = version.replace("^", "")

    return version


def readme():
    with open(os.path.join(here, "README.md")) as f:
        return f.read()


def js_prerelease(command, strict=False):
    """decorator for building minified js/css prior to another command"""

    class DecoratedCommand(command):
        def run(self):
            jsdeps = self.distribution.get_command_obj("jsdeps")
            if not is_repo and all(os.path.exists(t) for t in jsdeps.targets):
                # sdist, nothing to do
                command.run(self)
                self.distribution.data_files.extend(prebuilt_assets)
                return

            try:
                self.distribution.run_command("jsdeps")
            except Exception as e:
                missing = [t for t in jsdeps.targets if not os.path.exists(t)]
                if strict or missing:
                    log.warn("rebuilding js and css failed")
                    if missing:
                        log.error("missing files: %s" % missing)
                    raise e
                else:
                    log.warn("rebuilding js and css failed (not a problem)")
                    log.warn(str(e))
            command.run(self)
            update_package_data(self.distribution)

    return DecoratedCommand


def update_package_data(distribution):
    """update package_data to catch changes during setup"""
    build_py = distribution.get_command_obj("build_py")

    # JS assets will not be present if we are skip npm build
    if not skip_npm:
        distribution.data_files.extend(prebuilt_assets)

    # re-init build_py options which load package_data
    build_py.finalize_options()


class NPM(Command):
    description = "install package.json dependencies using npm"

    user_options = []

    node_modules = os.path.join(node_root, "node_modules")

    targets = [
        os.path.join(here, "jupyterlab_plotly", "nbextension", "extension.js"),
        os.path.join(here, "jupyterlab_plotly", "nbextension", "index.js"),
        os.path.join(here, "jupyterlab_plotly", "labextension", "package.json"),
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def get_npm_name(self):
        npmName = "npm"
        if platform.system() == "Windows":
            npmName = "npm.cmd"

        return npmName

    def has_npm(self):
        npmName = self.get_npm_name()
        try:
            check_call([npmName, "--version"])
            return True
        except:
            return False

    def should_run_npm_install(self):
        package_json = os.path.join(node_root, "package.json")
        node_modules_exists = os.path.exists(self.node_modules)
        return self.has_npm()

    def run(self):
        if skip_npm:
            log.info("Skipping npm-installation")
            return

        has_npm = self.has_npm()
        if not has_npm:
            log.error(
                "`npm` unavailable.  If you're running this command using sudo, make sure `npm` is available to sudo"
            )

        env = os.environ.copy()
        env["PATH"] = npm_path

        if self.should_run_npm_install():
            log.info(
                "Installing build dependencies with npm.  This may take a while..."
            )
            npmName = self.get_npm_name()
            check_call(
                [npmName, "install"],
                cwd=node_root,
                stdout=sys.stdout,
                stderr=sys.stderr,
            )
            check_call(
                [npmName, "run", "build:prod"],
                cwd=node_root,
                stdout=sys.stdout,
                stderr=sys.stderr,
            )
            os.utime(self.node_modules, None)

        for t in self.targets:
            if not os.path.exists(t):
                msg = "Missing file: %s" % t
                if not has_npm:
                    msg += "\nnpm is required to build a development version of jupyterlab-plotly"
                raise ValueError(msg)

        # update package data in case this created new files
        update_package_data(self.distribution)


class CodegenCommand(Command):
    description = "Generate class hierarchy from Plotly JSON schema"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if sys.version_info < (3, 6):
            raise ImportError("Code generation must be executed with Python >= 3.6")

        from codegen import perform_codegen

        perform_codegen()


def overwrite_schema(url):
    import requests

    req = requests.get(url)
    assert req.status_code == 200
    path = os.path.join(here, "codegen", "resources", "plot-schema.json")
    with open(path, "wb") as f:
        f.write(req.content)


def overwrite_bundle(url):
    import requests

    req = requests.get(url)
    assert req.status_code == 200
    path = os.path.join(here, "plotly", "package_data", "plotly.min.js")
    with open(path, "wb") as f:
        f.write(req.content)


def overwrite_plotlyjs_version_file(plotlyjs_version):
    path = os.path.join(here, "plotly", "offline", "_plotlyjs_version.py")
    with open(path, "w") as f:
        f.write(
            """\
# DO NOT EDIT
# This file is generated by the updatebundle setup.py command
__plotlyjs_version__ = "{plotlyjs_version}"
""".format(
                plotlyjs_version=plotlyjs_version
            )
        )


def overwrite_plotlywidget_version_file(version):
    path = os.path.join(here, "plotly", "_widget_version.py")
    with open(path, "w") as f:
        f.write(
            """\
# This file is generated by the updateplotlywidgetversion setup.py command
# for automated dev builds
#
# It is edited by hand prior to official releases
__frontend_version__ = "{version}"
""".format(
                version=version
            )
        )


def request_json(url):
    import requests

    req = requests.get(url)
    return json.loads(req.content.decode("utf-8"))


def get_latest_publish_build_info(repo, branch):

    url = (
        r"https://circleci.com/api/v1.1/project/github/"
        r"{repo}/tree/{branch}?limit=10000\&filter=completed"
    ).format(repo=repo, branch=branch)

    branch_jobs = request_json(url)

    # Get most recent successful publish build for branch
    builds = [
        j
        for j in branch_jobs
        if j.get("workflows", {}).get("job_name", None) == "publish-dist"
        and j.get("status", None) == "success"
    ]
    build = builds[0]

    # Extract build info
    return {p: build[p] for p in ["vcs_revision", "build_num", "committer_date"]}


def get_bundle_schema_urls(build_num):
    url = (
        "https://circleci.com/api/v1.1/project/github/"
        "plotly/plotly.js/{build_num}/artifacts"
    ).format(build_num=build_num)

    artifacts = request_json(url)

    # Find archive
    archives = [a for a in artifacts if a.get("path", None) == "plotly.js.tgz"]
    archive = archives[0]

    # Find bundle
    bundles = [a for a in artifacts if a.get("path", None) == "dist/plotly.min.js"]
    bundle = bundles[0]

    # Find schema
    schemas = [a for a in artifacts if a.get("path", None) == "dist/plot-schema.json"]
    schema = schemas[0]

    return archive["url"], bundle["url"], schema["url"]


class UpdateSchemaCommand(Command):
    description = "Download latest version of the plot-schema JSON file"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        url = (
            "https://raw.githubusercontent.com/plotly/plotly.js/"
            "v%s/dist/plot-schema.json" % plotly_js_version()
        )
        overwrite_schema(url)


class UpdateBundleCommand(Command):
    description = "Download latest version of the plot-schema JSON file"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        url = (
            "https://raw.githubusercontent.com/plotly/plotly.js/"
            "v%s/dist/plotly.min.js" % plotly_js_version()
        )
        overwrite_bundle(url)

        # Write plotly.js version file
        plotlyjs_version = plotly_js_version()
        overwrite_plotlyjs_version_file(plotlyjs_version)


class UpdatePlotlyJsCommand(Command):
    description = "Update project to a new version of plotly.js"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_command("updatebundle")
        self.run_command("updateschema")
        self.run_command("codegen")


class UpdateBundleSchemaDevCommand(Command):
    description = "Update the plotly.js schema and bundle from master"
    user_options = []

    def initialize_options(self):
        self.devrepo = None
        self.devbranch = None

    def finalize_options(self):
        self.set_undefined_options("updateplotlyjsdev", ("devrepo", "devrepo"))
        self.set_undefined_options("updateplotlyjsdev", ("devbranch", "devbranch"))

    def run(self):
        build_info = get_latest_publish_build_info(self.devrepo, self.devbranch)

        archive_url, bundle_url, schema_url = get_bundle_schema_urls(
            build_info["build_num"]
        )

        # Update bundle in package data
        overwrite_bundle(bundle_url)

        # Update schema in package data
        overwrite_schema(schema_url)

        # Update plotly.js url in package.json
        package_json_path = os.path.join(node_root, "package.json")
        with open(package_json_path, "r") as f:
            package_json = json.load(f)

        # Replace version with bundle url
        package_json["dependencies"]["plotly.js"] = archive_url
        with open(package_json_path, "w") as f:
            json.dump(package_json, f, indent=2)

        # update plotly.js version in _plotlyjs_version
        rev = build_info["vcs_revision"]
        date = build_info["committer_date"]
        version = "_".join([self.devrepo, self.devbranch, date[:10], rev[:8]])
        overwrite_plotlyjs_version_file(version)


class UpdatePlotlyJsDevCommand(Command):
    description = "Update project to a new development version of plotly.js"
    user_options = [
        ("devrepo=", None, "Repository name"),
        ("devbranch=", None, "branch or pull/number"),
    ]

    def initialize_options(self):
        self.devrepo = "plotly/plotly.js"
        self.devbranch = "master"

    def finalize_options(self):
        pass

    def run(self):
        self.run_command("updatebundleschemadev")
        self.run_command("jsdeps")
        self.run_command("codegen")


class UpdatePlotlywidgetVersionCommand(Command):
    description = "Update package.json version of jupyterlab-plotly"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from plotly._version import git_pieces_from_vcs, render

        # Update plotly.js url in package.json
        package_json_path = os.path.join(node_root, "package.json")

        with open(package_json_path, "r") as f:
            package_json = json.load(f)

        # Replace version with bundle url
        pieces = git_pieces_from_vcs("widget-v", project_root, False)
        pieces["dirty"] = False
        widget_ver = render(pieces, "pep440")["version"]

        package_json["version"] = widget_ver
        with open(package_json_path, "w") as f:
            json.dump(package_json, f, indent=2)

        # write _widget_version
        overwrite_plotlywidget_version_file(widget_ver)


graph_objs_packages = [
    d[0].replace("/", ".")
    for d in os.walk("plotly/graph_objs")
    if not d[0].endswith("__pycache__")
]


validator_packages = [
    d[0].replace("/", ".")
    for d in os.walk("plotly/validators")
    if not d[0].endswith("__pycache__")
]

versioneer_cmds = versioneer.get_cmdclass()
setup(
    name="plotly",
    version=versioneer.get_version(),
    use_2to3=False,
    author="Chris P",
    author_email="chris@plot.ly",
    maintainer="Nicolas Kruchten",
    maintainer_email="nicolas@plot.ly",
    url="https://plotly.com/python/",
    project_urls={"Github": "https://github.com/plotly/plotly.py"},
    description="An open-source, interactive data visualization library for Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.6",
    license="MIT",
    packages=[
        "jupyterlab_plotly",
        "plotly",
        "plotly.plotly",
        "plotly.offline",
        "plotly.io",
        "plotly.matplotlylib",
        "plotly.matplotlylib.mplexporter",
        "plotly.matplotlylib.mplexporter.renderers",
        "plotly.figure_factory",
        "plotly.data",
        "plotly.colors",
        "plotly.express",
        "plotly.express.data",
        "plotly.express.colors",
        "plotly.express.trendline_functions",
        "plotly.graph_objects",
        "_plotly_utils",
        "_plotly_utils.colors",
        "_plotly_future_",
    ]
    + graph_objs_packages
    + validator_packages,
    package_data={
        "plotly": [
            "package_data/*",
            "package_data/templates/*",
            "package_data/datasets/*",
        ],
        "jupyterlab_plotly": [
            "nbextension/*",
            "labextension/*",
            "labextension/static/*",
        ],
    },
    data_files=[
        ("etc/jupyter/nbconfig/notebook.d", ["jupyterlab-plotly.json"]),
    ],
    install_requires=["tenacity>=6.2.0"],
    zip_safe=False,
    cmdclass=dict(
        build_py=js_prerelease(versioneer_cmds["build_py"]),
        egg_info=js_prerelease(egg_info),
        sdist=js_prerelease(versioneer_cmds["sdist"], strict=True),
        jsdeps=NPM,
        codegen=CodegenCommand,
        updateschema=UpdateSchemaCommand,
        updatebundle=UpdateBundleCommand,
        updateplotlyjs=js_prerelease(UpdatePlotlyJsCommand),
        updatebundleschemadev=UpdateBundleSchemaDevCommand,
        updateplotlyjsdev=UpdatePlotlyJsDevCommand,
        updateplotlywidgetversion=UpdatePlotlywidgetVersionCommand,
        version=versioneer_cmds["version"],
    ),
)
