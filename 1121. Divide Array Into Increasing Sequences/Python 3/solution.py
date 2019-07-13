# Space Complexity O(n) using Counter
return len(nums) >= K * max(collections.Counter(nums).values())
