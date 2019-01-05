Using sliding window. Keep the sliding window at maximum with length of s1.

transfer both string into arrays which value is the character - 'a'. For example, 'abcdefg' will be transformed into [0,1,2,3,4,5,6]

Then count the frequency of each character in s1, the result array is the target array.

Next, use sliding window, go through s2, when the index is larger than the length of s1, then the frequency of the leftest character minus 1 (window[s2[i - len(s1)]] -= 1).
If there is a moment current window equals target array, return True
return False, if there is no permutation.