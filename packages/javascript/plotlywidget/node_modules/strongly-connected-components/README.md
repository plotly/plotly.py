strongly-connected-components
=============================
Given a directed graph, splits it into [strongly connected components](http://en.wikipedia.org/wiki/Strongly_connected_component).

## Example

```javascript
var scc = require("strongly-connected-components")

var adjacencyList = [
  [4], // 0
  [0,2], // 1
  [1,3], // 2
  [2], // 3
  [1], // 4
  [4,6], // 5
  [5,2], // 6
  [7,6,3], // 7
]

console.log(scc(adjacencyList))
```

## Install

    npm install strongly-connected-components

## API

### `require("strongly-connected-components")(adjacencyList)`
Computes the strongly connected components of a graph using Tarjan's algorithm.

* `adjacencyList` is an array of lists representing the directed edges of the graph

**Returns** An object containing:

* `components`: an array of arrays representing the partitioning of the vertices in the graph into connected components.
* `adjacencyList`: an array lists representing the directed edges of the directed acyclic graph between the strongly connected components

## Credits
(c) 2013 Mikola Lysenko. MIT License.  Based on the [implementation of Tarjan's algorithm on Wikipedia.](http://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm)
