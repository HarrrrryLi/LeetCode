class Solution:
    def lastSubstring(self, s: str) -> str:
        size = len(s)
        max_c = 'a'
        candidates = []

        for idx, c in enumerate(s):
            if c == max_c:
                if idx == 0 or s[idx - 1] != c:
                    candidates.append((idx, idx))
            elif c > max_c:
                candidates = []
                candidates.append((idx, idx))
                max_c = c

        while len(candidates) > 1:
            temp = []
            tempc = 'a'
            for start, cur in candidates:
                if cur + 1 < size:
                    if s[cur + 1] == tempc:
                        temp.append((start, cur + 1))
                    elif s[cur + 1] > tempc:
                        temp = []
                        temp.append((start, cur + 1))
                        tempc = s[cur + 1]
            candidates = temp

        return s[candidates[0][0]:]
