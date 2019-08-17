Using stack

Go through string, when we meet '(', push '(' to stack (if using Java/C++ push -1). when we meet ')', keep popping items, sum all numbers until we meet '(' or -1. If sum equal to 0, it means there is no elements between '()' then push 1 to stack, else push 2 * sum

Now in stack, there will be all numbers, just sum them as result.


Time Complexity O(N). Space Complexity O(N)