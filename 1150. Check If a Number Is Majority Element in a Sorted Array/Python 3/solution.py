class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        cur = nums[0]

        temp = 1
        for idx in range(1, size):
            num = nums[idx]
            if num == cur:
                temp += 1
                if temp > size / 2:
                    return True
            else:
                temp = 1
                cur = num

        return False
