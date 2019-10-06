class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        size = len(arr)
        record = {}

        for idx, num in enumerate(arr):
            pre = num - difference
            if pre in record:
                cur = record[pre] + 1
            else:
                cur = 1

            if num in record:
                record[num] = max(cur, record[num])
            else:
                record[num] = cur

        return max(record.values())
