class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        size1, size2 = len(num1), len(num2)
        cnt1, cnt2 = size1 - 1, size2 - 1
        c = 0
        result = ''
        while c or cnt1 >= 0 or cnt2 >= 0:
            _sum = c
            if cnt1 >= 0:
                _sum += ord(num1[cnt1]) - ord('0')
                cnt1 -= 1
                
            if cnt2 >= 0:
                _sum += ord(num2[cnt2]) - ord('0')
                cnt2 -= 1
            
            result = str(_sum % 10) + result
            c = _sum / 10
        
        
        return result