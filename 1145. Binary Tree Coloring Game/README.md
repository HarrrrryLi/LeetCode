First of all, if choose one node can win, choose its parent node(father node) can win this. Just like example one, if choose 2 can win this game, choose 1 can also win this game.

So record all nodes depth, rank and whether it's parent of player1 selected node.

If it's not parent, just assume, player one can select all other nodes except nodes in the subtree of chosen node, can make comparision.

If it's parent, then the optimal way to win is color nodes where will lead to player1 selected node first, which will be half of (depth different - 1). Then color others. We can get following formula.
'''
extra = (player1_depth - depth - 1) // 2
player2 can get: extra + rank - player1_rank
player1 can get: (player1_depth - depth) // 2 + player1_rank
'''
Time Complexity O(N). Space Complexity O(N)