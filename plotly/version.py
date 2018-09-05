__version__ = '3.2.0'
__frontend_version__ = '^0.3.0'


def stable_semver():
    """
    Get the stable portion of the semantic version string (the first three
    numbers), without any of the trailing labels

    '3.0.0rc11' -> '3.0.0'
    """
    from distutils.version import LooseVersion
    version_components = LooseVersion(__version__).version
    stable_ver_str = '.'.join(str(s) for s in version_components[0:3])
    return stable_ver_str
