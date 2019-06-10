# SVG arc to cubic bezier

A function that takes an SVG arc curve as input, and maps it to
one or more cubic bezier curves.

I extracted the `a2c` function from
[SVG path](https://github.com/fontello/svgpath), as I wanted to use it on its own.

All credit, thanks and respect goes to:

- Sergey Batishchev – [@snb2013](https://github.com/snb2013)
- Vitaly Puzrin – [@puzrin](https://github.com/puzrin)
- Alex Kocharin – [@rlidwka](https://github.com/rlidwka)

It blew my mind. Thank you!

## Installation

```
npm install svg-arc-to-cubic-bezier
```

## Usage

```js
import arcToBezier from 'svg-arc-to-cubic-bezier';

const previousPoint = { x: 100, y: 100 }

const currentPoint = {
  x: 700,
  y: 100,
  curve: {
    type: 'arc',
    rx: 300,
    ry: 200,
    largeArcFlag: 30,
    sweepFlag: 0,
    xAxisRotation: 0,
  },
};

const curves = arcToBezier({
  px: previousPoint.x,
  py: previousPoint.y,
  cx: currentPoint.x,
  cy: currentPoint.y,
  rx: currentPoint.curve.rx,
  ry: currentPoint.curve.ry,
  xAxisRotation: currentPoint.curve.xAxisRotation,
  largeArcFlag: currentPoint.curve.largeArcFlag,
  sweepFlag: currentPoint.curve.sweepFlag,
});

curves.forEach( c => console.log( c ));

// [
//   {
//     x1: 159.7865795437111,
//     y1: 244.97474575043722,
//     x2: 342.5677510865157,
//     y2: 362.49999701503634,
//     x: 508.253174689854,
//     y: 362.4999967447917,
//   },
//   {
//     x1: 673.9385982931924,
//     y1: 362.49999647454695,
//     x2: 759.7865756485664,
//     y2: 244.97474477179443,
//     x: 699.9999995964145,
//     y: 99.99999902135724,
//   },
// ]
```
