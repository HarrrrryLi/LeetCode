class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        Cnter = collections.Counter(s)
        record = {}

        result = self.helper(s, k, Cnter, 0, len(s) - 1, record)
        return result

    def helper(self, s, k, Cnter, left, right, record):
        if (left, right, k) in record:
            return record[(left, right, k)]

        if left >= right:
            return True

        if s[left] == s[right]:
            result = self.helper(s, k, Cnter, left + 1, right - 1, record)
        else:
            if k == 0:
                result = False
            else:
                result = self.helper(s, k - 1, Cnter, left, right - 1, record) or self.helper(
                    s, k - 1, Cnter, left + 1, right, record)

        record[(left, right, k)] = result
        return result
