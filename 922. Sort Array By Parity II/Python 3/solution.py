class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_idx, odd_idx = 0, 1
        size = len(A)
        while even_idx < size and odd_idx < size:
            while odd_idx < size and A[odd_idx] % 2 == 1:
                odd_idx += 2
            while even_idx < size and A[even_idx] % 2 == 0:
                even_idx += 2
            if even_idx < size and odd_idx < size:
                A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]

        return A
