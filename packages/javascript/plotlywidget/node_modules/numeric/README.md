Numeric Javascript by Sébastien Loisel
======================================

Numeric Javascript is a javascript library for doing numerical
analysis in the browser. Because Numeric Javascript uses only the
javascript programming language, it works in many browsers and does
not require powerful servers.

Numeric Javascript is for building "web 2.0" apps that can perform
complex calculations in the browser and thus avoid the latency of
asking a server to compute something. Indeed, you do not need a
powerful server (or any server at all) since your web app will perform
all its calculations in the client.

For further information, see http://www.numericjs.com/
Discussion forum: http://groups.google.com/group/numericjs

License
-------

Numeric Javascript is copyright by Sébastien Loisel and is distributed
under the MIT license. Details are found in the license.txt file.

Dependencies
------------

There are no dependencies for numeric.js.

Subdirectories
--------------

Here are some of the subdirectories and their contents:

* / holds the html/php files for the workshop/web site, license.txt, README, etc...

* /src holds the source files. The .js files are concatenated together to produce lib/numeric.js

* /lib holds numeric.js and numeric-min.js. These files aren't checked into the git tree because
they are created from the files in the /src subdirectory.

* /resources holds some small images, css files, etc...

* /tools contains build/test scripts. If you're going to patch or otherwise make tweaks to numeric,
you will need to use the /tools/build.sh script. There are also a bunch of scripts to deploy to
the numericjs.com web site, which you probably won't need.

Building and testing
--------------------

If you tweak the code, you can build and test the library by running the script /tools/build.sh. If you plan
to send me patches, please at least run this build script and check that all the tests pass.
