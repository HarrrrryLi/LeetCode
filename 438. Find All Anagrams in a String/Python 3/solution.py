import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        window_size = len(p)
        size = len(s)

        target = collections.Counter(p)
        result = []
        current = collections.Counter(s[:window_size])
        if current == target:
            result.append(0)
        for idx in range(1, size - window_size + 1):
            firstc = s[idx - 1]
            current[firstc] -= 1
            if current[firstc] == 0:
                del current[firstc]
            current[s[idx + window_size - 1]] += 1
            if current == target:
                result.append(idx)

        return result
