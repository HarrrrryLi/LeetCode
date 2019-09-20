class Solution:
    def customSortString(self, S: str, T: str) -> str:
        letter2idx = {c: idx for idx, c in enumerate(S)}
        size = len(S)

        return ''.join(sorted(T, key=lambda x: letter2idx[x] if x in letter2idx else size))
