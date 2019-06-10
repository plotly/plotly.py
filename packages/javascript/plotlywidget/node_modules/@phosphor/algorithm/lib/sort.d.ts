import { IterableOrArrayLike } from './iter';
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
export declare function topologicSort<T>(edges: IterableOrArrayLike<[T, T]>): T[];
