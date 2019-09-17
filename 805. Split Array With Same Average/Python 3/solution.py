class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        l, total = len(A), sum(A)
        A.sort()
        for i in range(1, l // 2 + 1):
            if (total * i) % l:
                continue
            if self.dfs(A, total * i / l, i, 0):
                return True
        return False

    def dfs(self, A, target, k, index):
        if not target and not k:
            return True
        if target <= 0 or k == 0:
            return False
        for i in range(index, len(A)):
            if i > index and A[i - 1] == A[i]:
                continue
            if A[i] * k > target or A[-1] * k < target:
                break
            if self.dfs(A, target - A[i], k - 1, i + 1):
                return True
        return False
