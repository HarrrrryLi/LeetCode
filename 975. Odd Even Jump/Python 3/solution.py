import collections


class Solution:
    def oddEvenJumps(self, A: list[int]) -> int:
        size = len(A)

        def buildMonoStack(l):
            result = [None] * size
            stack = collections.deque()
            for ele in l:
                while stack and ele > stack[-1]:
                    result[stack.pop()] = ele
                stack.append(ele)
            return result

        sorted_idx = sorted(range(size), key=lambda idx: A[idx])
        oddnext = buildMonoStack(sorted_idx)
        sorted_idx.sort(key=lambda idx: -A[idx])
        evennext = buildMonoStack(sorted_idx)

        odd = [False] * size
        even = [False] * size
        odd[-1] = even[-1] = True

        for idx in range(size - 2, -1, -1):
            if oddnext[idx]:
                odd[idx] = even[oddnext[idx]]
            if evennext[idx]:
                even[idx] = odd[evennext[idx]]

        return sum(odd)
