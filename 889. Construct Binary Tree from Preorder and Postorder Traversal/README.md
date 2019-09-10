Recursive.

pre[0] is the root. pre[1] is left child. Suppose idx is index of pre[1] in post. Then post[:L] and pre[1: 1 + L] is left subtree.


Time Complexity O(N). Space Complexity O(N)