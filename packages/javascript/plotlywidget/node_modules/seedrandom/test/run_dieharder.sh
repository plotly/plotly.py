#!/bin/sh
# http://www.phy.duke.edu/~rgb/General/dieharder.php
# How to run dieharder against seedrandom:

node bitgen.js | dieharder -g 200 -a | tee out/dieharder-report.txt
