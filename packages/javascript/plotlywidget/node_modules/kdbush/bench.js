'use strict';

var kdbush = require('./src/kdbush');
var v8 = require('v8');

var randomPoint = (max) => { return {x: randomInt(max), y: randomInt(max)}; };
var randomInt = (max) => Math.floor(Math.random() * max);
var heapSize = () => v8.getHeapStatistics().used_heap_size / 1000 + ' KB';

for (var i = 0, points = []; i < 1000000; i++) points.push(randomPoint(1000));

console.log('memory: ' + heapSize());

console.time('index ' + points.length + ' points');
var index = kdbush(points, (p) => p.x, (p) => p.y, 64, Int32Array);
console.timeEnd('index ' + points.length + ' points');

console.log('memory: ' + heapSize());

console.time('10000 small bbox queries');
for (i = 0; i < 10000; i++) {
    var p = randomPoint(1000);
    index.range(p.x - 1, p.y - 1, p.x + 1, p.y + 1);
}
console.timeEnd('10000 small bbox queries');

console.time('10000 small radius queries');
for (i = 0; i < 10000; i++) {
    p = randomPoint(1000);
    index.within(p.x, p.y, 1);
}
console.timeEnd('10000 small radius queries');
