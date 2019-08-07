class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        def count(tar):
            res, tmp = 0, [0, A[-1]]
            for i in range(len(A)):
                loc = bisect.bisect_left(A, A[i] / tar)
                res += len(A) - loc
                if loc < len(A) and A[i] / A[loc] > tmp[0] / tmp[1]:
                    tmp = [A[i], A[loc]]
            return res, tmp
        l, m, r = 0, 0.5, 1
        cur, _ = count(m)
        while cur != K:
            if cur < K:
                l = m
            else:
                r = m
            m = (l + r) / 2
            cur, _ = count(m)
        return _
