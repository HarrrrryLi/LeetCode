DP.

Suppose we have left leg and right leg. 
Create a dictionary, key is right_leg_length - left_leg_length, value is right_leg_length + left_leg_length.
For each number, we can choose put it on left leg or right leg or neither. Every time update value using max.


Time Complexity O(R * 3 ^ N). Space Complexity O(3 ^ N)