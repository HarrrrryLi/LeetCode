class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = - 2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        str = str.strip()
        num = 0
        sign = 1
        start = 0
        size = len(str)
        if size == 0:
            return 0
        
        if str[0] == '-':
            sign = -1
            start = 1
        elif str[0] == '+':
            sign = 1
            start = 1
            
        for cnt in range(start, size):
            c = str[cnt]
            if c.isdigit():
                num *= 10
                num += ord(c) - ord('0')
            else:
                break
        
        result = sign * num
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result