# supercluster [![Simply Awesome](https://img.shields.io/badge/simply-awesome-brightgreen.svg)](https://github.com/mourner/projects) [![Build Status](https://travis-ci.org/mapbox/supercluster.svg?branch=master)](https://travis-ci.org/mapbox/supercluster)

A very fast JavaScript library for geospatial point clustering for browsers and Node.

```html
<script src="https://unpkg.com/supercluster@2.2.0/dist/supercluster.min.js"></script>
```

```js
var index = supercluster({
    radius: 40,
    maxZoom: 16
});
index.load(points);
index.getClusters([-180, -85, 180, 85], 2);
```

Clustering 6 million points in Leaflet:

![clusters2](https://cloud.githubusercontent.com/assets/25395/11857351/43407b46-a40c-11e5-8662-e99ab1cd2cb7.gif)

## Methods

* load(`points`) : `this`

Loads an array of [GeoJSON.Feature](http://geojson.org/geojson-spec.html#feature-objects) objects. Each feature's `geometry` must be a [GeoJSON.Point](http://geojson.org/geojson-spec.html#point). Once loaded, index is immutable.

* getClusters(`bbox`, `zoom`) : Array<[GeoJSON.Feature](http://geojson.org/geojson-spec.html#feature-objects)>

For the given `bbox` array (`[westLng, southLat, eastLng, northLat]`) and integer `zoom`, returns an array of clusters as [GeoJSON.Feature](http://geojson.org/geojson-spec.html#feature-objects) objects.

## Options

| Option   | Default | Description                                                       |
|----------|---------|-------------------------------------------------------------------|
| minZoom  | 0       | Minimum zoom level at which clusters are generated.               |
| maxZoom  | 16      | Maximum zoom level at which clusters are generated.               |
| radius   | 40      | Cluster radius, in pixels.                                        |
| extent   | 512     | (Tiles) Tile extent. Radius is calculated relative to this value. |
| nodeSize | 64      | Size of the KD-tree leaf node. Affects performance.               |
| log      | false   | Whether timing info should be logged.                             |

## Developing Supercluster

```
npm install       # install dependencies
npm run build-dev # generate dist/supercluster.js
npm run build-min # generate dist/supercluster.min.js
npm test          # run tests
```
