"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
var iter_1 = require("./iter");
/**
 * Topologically sort an iterable of edges.
 *
 * @param edges - The iterable or array-like object of edges to sort.
 *   An edge is represented as a 2-tuple of `[fromNode, toNode]`.
 *
 * @returns The topologically sorted array of nodes.
 *
 * #### Notes
 * If a cycle is present in the graph, the cycle will be ignored and
 * the return value will be only approximately sorted.
 *
 * #### Example
 * ```typescript
 * import { topologicSort } from '@phosphor/algorithm';
 *
 * let data = [
 *   ['d', 'e'],
 *   ['c', 'd'],
 *   ['a', 'b'],
 *   ['b', 'c']
 * ];
 *
 * topologicSort(data);  // ['a', 'b', 'c', 'd', 'e']
 */
function topologicSort(edges) {
    // Setup the shared sorting state.
    var sorted = [];
    var visited = new Set();
    var graph = new Map();
    // Add the edges to the graph.
    iter_1.each(edges, addEdge);
    // Visit each node in the graph.
    graph.forEach(function (v, k) { visit(k); });
    // Return the sorted results.
    return sorted;
    // Add an edge to the graph.
    function addEdge(edge) {
        var fromNode = edge[0], toNode = edge[1];
        var children = graph.get(toNode);
        if (children) {
            children.push(fromNode);
        }
        else {
            graph.set(toNode, [fromNode]);
        }
    }
    // Recursively visit the node.
    function visit(node) {
        if (visited.has(node)) {
            return;
        }
        visited.add(node);
        var children = graph.get(node);
        if (children) {
            children.forEach(visit);
        }
        sorted.push(node);
    }
}
exports.topologicSort = topologicSort;
