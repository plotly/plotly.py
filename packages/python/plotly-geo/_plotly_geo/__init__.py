# https://packaging.python.org/guides/packaging-namespace-packages/
#         pkgutil-style-namespace-packages
__path__ = __import__("pkgutil").extend_path(__path__, __name__)
