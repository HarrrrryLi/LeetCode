Use two heaps, leftheap and rightheap. For each heap go left or right, until this height is smaller than next one, push height and -index(for left) or index(for right) into heap. return the index.
For each water, first judge can it go left,(leftheap not empty and the shallowest one is smaller than height K). If it can, the shallowest one add 1 and repush to the heap. If the shallowest one is the leftest one, then try to extend left part into leftheap. If not, judge can it go right, do the same thing as mentioned before. Else, add 1 to heights[K], then if left == k, add left to leftheap, if right == k ,add right to rightheap.

Time Complexity O(max(N, V*logN))