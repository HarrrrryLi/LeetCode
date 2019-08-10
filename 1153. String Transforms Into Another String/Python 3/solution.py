class Solution:
    def canConvert(self, s1, s2):
        if s1 == s2:
            return True
        record = {}
        for c1, c2 in zip(s1, s2):
            if record.setdefault(c1, c2) != c2:
                return False
        return len(set(record.values())) < 26
