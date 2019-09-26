class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        size = len(A)
        maxdp = [0] * size
        mindp = [float('inf')] * size
        maxdp[0] = A[0]
        mindp[-1] = A[-1]

        for cnt in range(1, size):
            maxdp[cnt] = max(maxdp[cnt - 1], A[cnt])
            mindp[size - cnt - 1] = min(mindp[size - cnt], A[size - cnt - 1])

        for cnt in range(size - 1):
            if maxdp[cnt] <= mindp[cnt + 1]:
                return cnt + 1

        class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        size = len(A)
        maxdp = [0] * size
        mindp = [float('inf')] * size
        maxdp[0] = A[0]
        mindp[-1] = A[-1]

        for cnt in range(1, size):
            maxdp[cnt] = max(maxdp[cnt - 1], A[cnt])
            mindp[size - cnt - 1] = min(mindp[size - cnt], A[size - cnt - 1])

        for cnt in range(size - 1):
            if maxdp[cnt] <= mindp[cnt + 1]:
                return cnt + 1
