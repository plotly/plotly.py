var fs = require('fs')
var topojson = require('topojson')
var gju = require('geojson-utils')
var common = require('./common')

fs.readFile(common.pathToConfig, 'utf8', main)

function main (err, configFile) {
  if (err) throw err

  var config = JSON.parse(configFile)
  var toposToWrite = common.getToposToWrite(config)

  var barWrite = common.makeBar(
    'Writing into topojson: [:bar] :current/:total',
    [toposToWrite]
  )

  function propertyTransform (feature) { return feature.properties }

  toposToWrite.forEach(function (topo) {
    var r = topo.r

    var s = topo.s

    var collections = {}

    config.vectors.forEach(function (v) {
      var path = common.geojsonDir + common.tn(r, s.name, v.name, 'geo.json')

      var d = fs.readFileSync(path, 'utf8')

      var collection = JSON.parse(d)

      if (collection.features) formatProperties(collection, v)
      collections[v.name] = collection
    })

    // TODO experiment with simplification/quantization
    var topology = topojson.topology(collections, {
      'verbose': common.DEBUG,
      'property-transform': propertyTransform
    })

    pruneProperties(topology)

    var outPath = common.topojsonDir + common.out(r, s.name)

    fs.writeFile(outPath, JSON.stringify(topology), function (err) {
      if (err) throw err
      barWrite.tick()
    })
  })
}

function formatProperties (collection, v) {
  var features = collection.features

  var N = features.length

  var feature

  var id

  function getCentroid (feature) {
    var geometry = feature.geometry

    function getOne (polygon) {
      var coords = gju.centroid(polygon).coordinates
      return [ +coords[0].toFixed(2), +coords[1].toFixed(2) ]
    }

    if (geometry.type === 'MultiPolygon') {
      var coordinates = geometry.coordinates

      var N = coordinates.length

      var centroids = new Array(N)

      var areas = new Array(N)

      var polygon

      var indexOfMax

      // compute one centroid per polygon and
      // pick the one associated with the
      // largest area.

      for (var i = 0; i < N; i++) {
        polygon = {
          type: 'Polygon',
          coordinates: coordinates[i]
        }
        centroids[i] = getOne(polygon)
        areas[i] = gju.area(polygon)
      }

      // 'min' works best, not sure why
      indexOfMax = areas.indexOf(Math.min.apply(Math, areas))
      return centroids[indexOfMax]
    } else if (geometry.type === 'Polygon') {
      return getOne(geometry)
    }
  }

  for (var i = 0; i < N; i++) {
    feature = features[i]

    if (v.ids) {
      id = feature.properties[v.ids]

      if (id && id !== '-99') {
        feature.id = id
        feature.properties.ct = getCentroid(feature)
        feature.properties.gu = feature.properties['gu_a3']
        continue
      }
    }

    // Unfortunately, we need this to include Norway (IS0_A3=NOR)
    // from Natural Earth v4.1.0
    // - https://github.com/nvkelso/natural-earth-vector/issues/252
    if (v.ids && v.ids.indexOf('ISO_A3') === 0) {
      id = feature.properties['SOV_A3']

      if (id === 'NOR') {
        feature.id = id
        feature.properties.ct = getCentroid(feature)
        feature.properties.gu = feature.properties['gu_a3']
      }
    }

    // France (IS0_A3=FRA) is also acting weird using IS0_A3,
    // but using ISO_A3_EH seems to work ok
    // - https://github.com/nvkelso/natural-earth-vector/issues/284
  }
}

function pruneProperties (topology) {
  // keep 'gu' (aka governing unit A3 code, which necessary to identify
  // some subunits ids (e.g. 'WA' which can be Washington state and Western
  // Australia)
  var propsToKeep = ['ct', 'gu']

  var objects = topology.objects

  Object.keys(objects).forEach(function (objectName) {
    var obj = objects[objectName]

    delete obj.crs
    delete obj.name

    var geometries2 = []

    obj.geometries.forEach(function (geometry) {
      var properties = geometry.properties

      var newProperties = {}

      if (properties === undefined) return

      propsToKeep.forEach(function (prop) {
        if (properties[prop] !== undefined) {
          newProperties[prop] = properties[prop]
        }
      })

      if (Object.keys(newProperties).length) {
        geometry.properties = newProperties
      } else {
        delete geometry.properties
      }

      if (geometry.type !== null) {
        geometries2.push(geometry)
      }
    })

    obj.geometries = geometries2
  })
}
