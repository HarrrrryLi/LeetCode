class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        size = len(nums)
        index_map = {}
        
        for i,num in enumerate(nums):
            if target-num in index_map:
                return [index_map[target-num],i]
            index_map[num] = i
        
        return []