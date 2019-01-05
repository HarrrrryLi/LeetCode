class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(c) - ord('a') for c in s1]
        B = [ord(c) - ord('a') for c in s2]
        size = len(A)
        target = [0] * 26
        
        for num in A:
            target[num] += 1
        
        window = [0] * 26
        for i, num in enumerate(B):
            window[num] += 1
            if i >= size:
                window[B[i - size]] -= 1
            if window == target:
                return True
        
        return False
            