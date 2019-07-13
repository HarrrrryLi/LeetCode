class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if M != 2:
            return month[M]

        if Y % 100 == 0:
            if Y % 400 == 0:
                return 29
            return 28

        if Y % 4 == 0:
            return 29

        return 28
