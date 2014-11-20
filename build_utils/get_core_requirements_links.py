"""Use requirements.txt file to generate dependency distribution links.

This file depends on the requirements package, which you can get via:
pip install requirements-parser

"""
import os
import requirements

file_dir = os.path.split(__file__)[0]
requirements_file = os.path.join(file_dir, '../requirements.txt')
pypi_base_url = "https://pypi.python.org/packages/source"

tarball_links = []
with open(requirements_file, 'r') as f:
    reqs = requirements.parse(f.read())

for req in reqs:
    name = req.name
    version = req.specs[0][1]
    tarball_links.append(
        "{base}/{name[0]}/{name}/{name}-{version}.tar.gz"
        .format(base=pypi_base_url, name=name, version=version)
    )

print ' '.join(tarball_links)
