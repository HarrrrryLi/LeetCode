class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        def backtracking(path, nums):
            if len(nums) == 1:
                if math.sqrt(nums[0] + path) % 1 == 0:
                    self.ans += 1
            else:
                visited2 = []
                for j in range(len(nums)):
                    if math.sqrt(nums[j] + path) % 1 == 0 and nums[j] not in visited2:
                        visited2.append(nums[j])
                        backtracking(nums[j], nums[:j] + nums[j + 1:])

        self.ans = 0
        visited = []
        for i in range(len(A)):
            if A[i] not in visited:
                visited.append(A[i])
                backtracking(A[i], A[:i] + A[i + 1:])

        return self.ans
