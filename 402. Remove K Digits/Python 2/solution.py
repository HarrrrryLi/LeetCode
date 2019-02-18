class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        for number in num:
            while k and result and result[-1] > number:
                result.pop()
                k -= 1
            result.append(number)
        
        return ''.join(result[:-k or None]).lstrip('0') or '0'