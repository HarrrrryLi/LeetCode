class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        record = {}
        start = 0
        result = 1

        for idx, c in enumerate(s):
            if c in record and record[c] >= start:
                result = max(result, idx - start)
                start = record[c] + 1
            record[c] = idx

        result = max(result, len(s) - start)
        return result
