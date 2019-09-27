Using DP.


First calcualte dp element, each number means the binary value from beginning to this one.

Then like three sum. set left and right pointer. Calculate 3 numbers, from left to right we call them as num1, num2 and num3. If all equals return [left, right]. Otherwise we compare num1 and num3 to see how to move pointers. If num1 is smaller than num3 then left += 1. Otherwise right += 1. Notice, if num1 equals to num3, we need to move right pointer left, because if we move left the number will change, but if we move right, the number may change(if the new included bit is 0, it won't change).


Time Complexity O(N). Space Complexity O(N). We could do space complexity O(1), but it will be harder to calculate numbers.