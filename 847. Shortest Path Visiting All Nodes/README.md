Using heap.

If only have 1 node, return 0.

Find all nodes which has least neighbors, they will be start nodes. If number of least neighbors is equal to size - 1, it means it becomes a circle return size - 1. Push all start nodes into heap.  

Expanding heap with current strategy:
    1. Expand the path which has already expanded most unique nodes.
    2. If the first one are equal, expand shortest path length.

Objects need to be pushed into heap with node:
    1. Because we can visit a node multiple times, we need to use a set to record which nodes we visited.
    2. We also need to record visited edge with direction. For example, if we must go through node1 to node2 and node2 to node1. The optimal solution can not be cross node1 to node2 and node2 to node1 multiple times. It will be node1 -> node2 -> other nodes -> node2 -> node1 -> other nodes

For every expand, if a path expanded all nodes, update with result; if its current length is already greater or equal to current result, don't expand this node due to even if it finally expands all nodes, it won't be the shorest path.

If there is no such path, return 0.

Time Complexity O(EVlog(EV)). Space Complexity O(EV)
