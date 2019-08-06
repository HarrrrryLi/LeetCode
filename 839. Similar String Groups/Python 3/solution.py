class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        if not A:
            return 0

        Aset = set(A)
        stack = collections.deque()
        size = len(A[0])
        result = 0
        while Aset:
            stack.append(Aset.pop())
            result += 1

            while stack:
                word = stack.pop()
                temp = list(Aset)
                for nxt in temp:
                    diff = 0
                    for idx, c in enumerate(nxt):
                        if c != word[idx]:
                            diff += 1
                        if diff > 2:
                            break
                    else:
                        if diff == 2:
                            stack.append(nxt)
                            Aset.remove(nxt)

        return result
