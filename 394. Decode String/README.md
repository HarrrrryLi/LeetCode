Use two stacks. One stores string, the other stores num.  
When we meet '[', we add the number(if number is 0,then add 1) into number stack. Then add '[' to string stack. When we meet ']', pop a number and keep pop string until meet '['. Then use num * string and add this string back into string stack.
After go through the whole string. we should keep poping string, concate them as a result string.

Time Complexity O(n). Space Complexity O(n)