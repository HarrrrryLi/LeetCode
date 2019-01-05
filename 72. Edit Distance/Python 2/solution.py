class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        row_size = len(word1) + 1
        col_size = len(word2) + 1
        dp = [[0]*col_size for _ in range(row_size)]
        
        for row_cnt in range(row_size):
            dp[row_cnt][0] = row_cnt
            
        for col_cnt in range(col_size):
            dp[0][col_cnt] = col_cnt
            
        
        for row_cnt in range(1, row_size):
            for col_cnt in range(1, col_size):
                if word1[row_cnt - 1] == word2[col_cnt - 1]:
                    dp[row_cnt][col_cnt] = dp[row_cnt - 1][col_cnt - 1]
                else:
                    dp[row_cnt][col_cnt] = 1 + min(dp[row_cnt-1][col_cnt], dp[row_cnt][col_cnt - 1], dp[row_cnt - 1][col_cnt - 1])
                    
        
        return dp[-1][-1]