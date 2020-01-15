class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        record = collections.defaultdict(list)
        size = len(text)
        result = 0
        seen = set()
        for idx, c in enumerate(text):
            if c in record:
                for pre_idx in record[c]:
                    s = text[pre_idx: idx]
                    if idx + len(s) > size:
                        break
                    if s == text[idx: idx + len(s)]:
                        if s not in seen:
                            result += 1
                            seen.add(s)
            record[c].insert(0, idx)

        return result
