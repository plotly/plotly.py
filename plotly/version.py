__version__ = '3.0.0-rc.11'
__frontend_version__ = '^0.1.1'


def stable_semver():
    """
    Get the stable portion of the semantic version string (the first three
    numbers), without any of the trailing labels

    '3.0.0-rc.11' -> '3.0.0'
    """

    return __version__.split('-')[0]
