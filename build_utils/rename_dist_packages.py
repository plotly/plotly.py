"""Rename enclosing package directories to give them a natural order.

This file depends on the requirements package, which you can get via:
pip install requirements-parser

"""
import shutil
import os
import requirements
from plotly.version import __version__

plotly_name = 'plotly'
file_dir = os.path.split(__file__)[0]
dist_dir = os.path.join(file_dir, '..', 'stand_alone_dist', 'dist')
requirements_file = os.path.join(file_dir, '..', 'requirements.txt')
dependency_packages = os.listdir(dist_dir)

# get ordered dependencies
with open(requirements_file, 'r') as f:
    contents = f.read()
num_deps = sum(1 for _ in requirements.parse(contents))
reqs = requirements.parse(contents)

# for each dependency, find the uncompressed package and rename it (order it)
for req_num, req in enumerate(reqs):
    for package_name in dependency_packages:
        if req.name == package_name.split('-')[0]:
            src = os.path.join(dist_dir, package_name)
            dst = os.path.join(dist_dir, "{}_{}-{}".format(
                req_num, req.name, req.specs[0][1]
            ))
            shutil.move(src, dst)

# rename plotly to be the last thing installed
for package_name in dependency_packages:
    if plotly_name == package_name.split('-')[0]:
        src = os.path.join(dist_dir, package_name)
        dst = os.path.join(dist_dir, "{}_{}-{}".format(
            num_deps, plotly_name, __version__
        ))
        shutil.move(src, dst)
