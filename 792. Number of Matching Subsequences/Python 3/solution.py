class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        indices = collections.defaultdict(list)

        for idx, c in enumerate(S):
            indices[c].append(idx)

        result = 0
        for word in words:
            size = len(word)
            if word[0] not in indices:
                continue
            Count = True
            cur = indices[word[0]][0]
            for idx in range(1, size):
                c = word[idx]
                if c not in indices:
                    Count = False
                    break
                i = bisect.bisect(indices[c], cur)
                if i == len(indices[c]):
                    Count = False
                    break
                cur = indices[c][i]
            if Count:
                result += 1

        return result
