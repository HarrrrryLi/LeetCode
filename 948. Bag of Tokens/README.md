Greedy.

Sort list first
Then:
    1. Keep adding scores/turning face down, result = max(result, temp). 
    2. Then turn the largest one face up
    3. go step 1 until the list is empty

Time Comlexity O(NlogN). Space Complexity O(N)