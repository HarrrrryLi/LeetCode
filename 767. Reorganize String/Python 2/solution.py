class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        size = len(S)
        counter = collections.Counter(S)
        for key in counter:
            if counter[key] > (size + 1) / 2:
                return ""
        temp = list(S)    
        temp.sort(key=lambda x: (counter[x], x))
        result = [0] * size
        
        result[::2], result[1::2] = temp[size / 2:], temp[:size / 2]
        
        return "".join(result)