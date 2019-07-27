Build the tree first, for each subtree, root is the course, childern are the prerequisites. If there is no root in this tree, return -1

Then go through the tree, when meet leaf node, update result. If a node is not leaf node but its depth is N, means this tree has at least a cycle, return -1. For each node, record its depth, if next time try to expand the same node and the depth is not greater then recorded depth, then skip it, because the final result won't be larger.


Time Complexity O(N). Space Complexity O(N)