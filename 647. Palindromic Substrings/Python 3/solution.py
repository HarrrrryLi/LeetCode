class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        result = 0
        for idx, c in enumerate(s):
            result += 1
            left, right = idx - 1, idx + 1
            while left >= 0 and right < size:
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break

            if idx + 1 < size and s[idx + 1] == c:
                result += 1
                left, right = idx - 1, idx + 2
                while left >= 0 and right < size:
                    if s[left] == s[right]:
                        result += 1
                        left -= 1
                        right += 1
                    else:
                        break
        return result
