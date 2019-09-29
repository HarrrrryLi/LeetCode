DP.

Because each substring can be rearranged/ reorded, we only need to consider how many letters have a odd frequency.

If only one letter or no letter has odd frequency, then it's palindrome. If there are more than one letter have odd frequency, we get number of those letters. If this odd_num // 2 is not greater than k, it can be convert to a palindrome.


Time Compelxity O(N). Space Complexity O(L). N is the length of query array. L is the length of string