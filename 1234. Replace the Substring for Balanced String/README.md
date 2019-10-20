Two pointers/ Sliding window. 


First use counter to count and calculate which letters need to be replaced(store it into a target_sub dictionary). Then the problem becomes, find a shortest substring contains those letters with at least a specific frequency. 

Then using sliding window, to make sure in the windows that for each letter c in the target_sub dictionary at least target_sub[c] times. 


Time Complexity O(N). Space Complexity O(1)/ O(L). L is how many letters we need to take care, (in this problem L is 4)