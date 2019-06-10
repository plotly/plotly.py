# parse-rect [![experimental](https://img.shields.io/badge/stability-unstable-green.svg)](http://github.com/badges/stability-badges) [![Build Status](https://travis-ci.org/dfcreative/parse-rect.png)](https://travis-ci.org/dfcreative/parse-rect)

Take any rectangle-like argument and return rectangle values.

[![npm install parse-rect](https://nodei.co/npm/parse-rect.png?mini=true)](https://npmjs.org/package/parse-rect/)

```js
const parseRect = require('parse-rect')

// {x: 10, y: 20, width: 90, height: 80}
parseRect('10 20 100 100')
parseRect(10, 20, 100, 100)
parseRect([10, 20, 100, 100])
parseRect({ x: 10, y: 20, width: 90, height: 80 })
parseRect({ x: 10, y: 20, w: 90, h: 80 })
parseRect({ l: 10, t: 20, r: 100, b: 100 })
parseRect({ left: 10, top: 20, right: 100, bottom: 100 })

// {x: 0, y: 0, width: 90, height: 80}
parseRect({ width: 90, height: 80 })
parseRect([ 90, 80 ])

// {x: 0, y: 0, width: 90, height: 90}
parseRect(90)
parseRect([90])
```

## License

(c) 2018 Dmitry Yv. MIT License
