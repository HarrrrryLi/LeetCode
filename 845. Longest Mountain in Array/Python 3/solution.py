class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        size = len(A)
        if size == 1:
            return 0
        result = 0

        temp = 1
        increasing = True
        for idx in range(1, size):
            if increasing:
                if A[idx] > A[idx - 1]:
                    temp += 1
                elif A[idx] == A[idx - 1]:
                    temp = 1
                    increasing = True
                else:
                    if temp == 1:
                        temp = 1
                        increasing = True
                    else:
                        temp += 1
                        increasing = False
            else:
                if A[idx] < A[idx - 1]:
                    temp += 1
                elif A[idx] == A[idx - 1]:
                    result = max(result, temp)
                    temp = 1
                    increasing = True
                else:
                    result = max(result, temp)
                    temp = 2
                    increasing = True
        if not increasing:
            result = max(result, temp)
        if result == 1:
            return 0

        return result
