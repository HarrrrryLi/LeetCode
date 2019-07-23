Find numbers appear in either top or bottom for every tile, put them in a set/list called candidates

Store top and bottom number in 2 counters.

result = min(result, size - top[num], size - bottom[num]) for every number in candidates

Time Complexity O(n). Space Complexity O(n)