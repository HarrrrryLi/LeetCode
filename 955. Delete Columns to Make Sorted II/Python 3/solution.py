class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        N = len(A[0])
        size = len(A)
        if size == 1:
            return 0

        result = 0
        pre = []
        for n in range(N):
            nxt_needed = False
            for idx in range(1, size):
                word1, word2 = A[idx - 1], A[idx]
                pre_cnt = len(pre) - 1
                while pre_cnt >= 0:
                    p = pre[pre_cnt]
                    if word1[p] != word2[p]:
                        break
                    pre_cnt -= 1
                    p = pre[pre_cnt]
                if pre_cnt == -1:
                    if word1[n] > word2[n]:
                        result += 1
                        nxt_needed = True
                        break
                if pre_cnt == -1 and word1[n] == word2[n]:
                    nxt_needed = True
            else:
                pre.append(n)
            if not nxt_needed:
                break

        return result
