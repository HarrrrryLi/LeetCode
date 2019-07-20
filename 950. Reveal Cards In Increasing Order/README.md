Recursive.

odd index of result equals first half. 
For even index of result, calculate increasingorder(second half) first, mark as temp
if origin deck has even number of cards it equals temp, else it equals temp[-1] + temp[:-1]


Time Complexity O(n). Space Complexity O(n)