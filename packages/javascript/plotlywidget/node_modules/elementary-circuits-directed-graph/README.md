# elementary-circuits-directed-graph

An implementation of the Johnson's circuit finding algorithm [1].

[1] Donald B. Johnson, Finding all the elementary circuits of a directed
    graph, SIAM Journal on Computing, 1975.

## Example

```javascript
var findCircuits = require("elementary-circuits-directed-graph");

//   V4      V2
// +-<---o---<---o---<--+
// |             |      |
// V0 o             ^      o V3
// |           V1|      |
// +------>------o--->--+

var adjacencyList = [
  [1],
  [2, 3],
  [4],
  [2],
  [0]
]

console.log(findCircuits(adjacencyList))

// returns [[0, 1, 2, 4, 0], [0, 1, 3, 2, 4, 0]]
```

## Install

npm install elementary-circuits-directed-graph

## API

### `require("elementary-circuits-directed-graph")(adjacencyList)`
Finds all the elementary circuits of a directed graph using

* `adjacencyList` is an array of lists representing the directed edges of the graph

**Returns** An array of arrays representing the elementary circuits

## Credits
(c) 2018 Antoine Roy-Gobeil. MIT License.
