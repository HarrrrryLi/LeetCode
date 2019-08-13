class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        result = ''
        neg = False
        if num < 0:
            num = -num
            neg = True
        while num:
            result = str(num % 7) + result
            num //= 7

        if neg:
            result = '-' + result
        return result
