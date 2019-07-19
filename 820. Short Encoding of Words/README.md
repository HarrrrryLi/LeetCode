First, reverse every word store them in a list. Secondly, sort the new list. Then go through the whole list, if next one starts with current one, then remove current one.  Result will be number of remain words plus sum of the length of all word.

Time Complexity O(nlogn). Space Complexity O(n)