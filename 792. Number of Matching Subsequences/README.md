Create a dictionary, key is letter value is a list of indices of this letter, we need to keep it sorted.

Suppose we have a letter 'a' with index [n, n + m], if we use n + m one and we can form a substring, means we can use n one to form the same substring. But If we use n to form a substring doesn't mean we can use n + m form a string.


So we go through each word. 
    If a letter doesn't in the dictionary, means we can't get this substring. 
    
    Record the first index of first letter as pre. For each letter, get right insert point of pre in this letter's list. If the insert point is the end of list, means after pre one, there is no this letter. Then we can't form a substring. If the insert point is not the end of list, means we can do that, and get the smallest index which is insert point. Then we record it and continue


Time Complexity O(N * l * logL). N is the length of words list, l is the average length for each word in the words list, L is the length of string.
Space Complexity O(L)


