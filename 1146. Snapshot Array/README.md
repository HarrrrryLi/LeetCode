Just like truly snap shot, even a number will be modified, don't delete it.

Create a dictionary, key is (snap_id, index). Initial it with value 0.

When set a number, just put/update value of (snap_id, index)

When get a number, just go return (id, index) if this key pair in dictionary. id is from requested id to 0.


N is operate numbers
L is array length
Initial:
    Time Complexity O(L)
Put:
    Time Complexity O(1)
Get:
    Time Complexity O(N)

Space Complexity O(N). 