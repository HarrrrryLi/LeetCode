Go through each letter and each word. If pre are the same or we don't have pre, we do following check:
    If current column is not inorder we need to delete this. And go check next column
    If for current column there are two letters are the same, we need to check next column.
    If for current column it's already inorder and there aren't two same letters, means it's already sorted. break.


Time Complexity O(N ^ 2 * L). Space Complexity O(N). N is the length of each word, L is the length of word list.