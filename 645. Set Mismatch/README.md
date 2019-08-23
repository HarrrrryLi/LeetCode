For each number in the list, if nums[abs(num) - 1] < 0 means this one has been visited, this number is the repeated one, add it to result skip it. 
Else, nums[num] *= -1.

Go through the list, the missing one is idx + 1 where nums[idx] is positive.


Time Complexity O(N). Space Complexity O(1)