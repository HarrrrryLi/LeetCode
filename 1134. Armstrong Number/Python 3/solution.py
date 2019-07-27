class Solution:
    def isArmstrong(self, N: int) -> bool:
        score = 0
        order = len(str(N))
        temp = N
        while N:
            digit = N % 10
            score += digit ** order
            N //= 10

        return temp == score
