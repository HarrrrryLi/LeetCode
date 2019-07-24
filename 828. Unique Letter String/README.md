For each letter, store its indexes into a list. 

For each letter, add -1 to the beginning of the list, add size to the end of the list then result += (v[i] - v[i - 1]) * (v[i + 1] - v[i])


Time Complexity O(N). Space Complexity O(N)