For A[idx], left[idx] means how many contiguous number are bigger than A[idx] on its left, right[idx] means how many contiguous numbers are not smaller than A[idx] on its right.

Then result will be the sum of A[idx] * left[idx] * right[idx]

Time Complexity O(N). Space Complexity O(N)