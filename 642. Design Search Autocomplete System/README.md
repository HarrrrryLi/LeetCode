use ditionary to store sentences and their frequency.

If input is '#', the make the frequency of input string +1. Then clear input string cache and match cache
If input is not '#', and there is no input before(or input was cleared), find all key in dictionary start with this input character. Then sort and store the list in match cache. If input is not '#', and there is some input before, find all string which the i-th letter is this input character where i - 1 is the length of before input. Then store all the strings into match cache.  return first three

Time Complexity O(nlogn). Space Complexity O(n)