Make left = 0, right = size - 1

Go through the word, find the letter equal to right, suppose that index is i.

If i == right means, no more palindrome word pairs. Then result += 1 return result
If text[left:i + 1] == text[right + 1 - (i - left):right + 1], these pair can be splited, result += 2.
If text[left:i + 1] != text[right + 1 - (i - left):right + 1], keep searching when meet next letter equal to right.



Time Complexity O(N ^ 2). Space Complexity O(N)