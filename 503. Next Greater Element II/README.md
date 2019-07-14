Using monotone stack.

Reverse go through range(size * 2), for each number, keeping popping if the top element of stack is not greater than current number.  If stack is not empty and the next greater element of this number haven't been found, then update it.


Time Complexity O(n), Space Complexity O(n)