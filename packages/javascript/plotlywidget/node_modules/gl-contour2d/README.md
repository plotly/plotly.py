gl-contour2d
============
2D contour lines

To run the example, follow these steps:

```
git clone https://github.com/gl-vis/gl-contour2d.git
cd gl-contour2d
mkdir dist
browserify contour.js -o dist/bundle.js
browserify example/simple.js -o dist/simple_example_bundle.js
```
then open `simple.html` in the `example` directory.

To create your own visualization, copy the example files, modify them and run 
```
browserify example/yourExample.js -o dist/your_example_bundle.js
```

# License
(c) 2015 Mikola Lysenko. MIT License
