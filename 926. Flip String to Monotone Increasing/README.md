DP. Each element is a dictionary which contains two keys: True and False. True means all elements before (including this one) are 0.

So we can get 
'''
if S[cnt] == '0':
    nxt[True] = dp[True]
    nxt[False] = min(dp[False], dp[True]) + 1
else:
    nxt[False] = min(dp[False], dp[True])
    nxt[True] = dp[True] + 1
'''

Time Complexity O(N). Space Complexity O(1)