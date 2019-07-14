First find sequence in nums2, store them in a dictionary. Then go through nums1.

How to Find sequence in nums2:

Using monotone stack. Reverse go throught nums2, for each number, keeping popping if the top element of stack is not greater than current number.  If stack is not empty and this number not in dictionary, then store it.


Time Complexity O(n), Space Complexity O(n)