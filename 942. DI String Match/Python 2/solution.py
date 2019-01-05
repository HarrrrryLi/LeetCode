class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        low, high = 0, len(S)
        result = []
        
        for c in S:
            if c == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        
        result.append(low)
        
        return result