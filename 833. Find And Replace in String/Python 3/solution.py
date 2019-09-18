class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        record = []
        for idx, src, tar in zip(indexes, sources, targets):
            record.append((idx, src, tar))

        record.sort()

        size = len(record)
        result = list(S)
        for cnt in range(size - 1, -1, -1):
            idx, src, tar = record[cnt]
            src_size = len(src)
            if S[idx: idx + src_size] == src:
                result[idx: idx + src_size] = tar

        return ''.join(result)
