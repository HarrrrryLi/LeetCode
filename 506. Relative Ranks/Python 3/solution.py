class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        temp = [(score, idx) for idx, score in enumerate(nums)]
        temp.sort(reverse=True)
        result = [0] * len(nums)

        for idx, pair in enumerate(temp):
            if idx == 0:
                rank = 'Gold Medal'
            elif idx == 1:
                rank = 'Silver Medal'
            elif idx == 2:
                rank = 'Bronze Medal'
            else:
                rank = str(idx + 1)

            result[pair[1]] = rank

        return result
