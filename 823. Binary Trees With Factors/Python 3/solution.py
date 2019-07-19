class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()

        dp = {num: 1 for num in A}

        for parent in A:
            for left_child in A:
                if left_child >= parent:
                    break
                if parent % left_child != 0:
                    continue
                right_child = parent / left_child
                if right_child in dp:
                    dp[parent] += dp[left_child] * dp[right_child]

        return sum(dp.values()) % (10 ** 9 + 7)
