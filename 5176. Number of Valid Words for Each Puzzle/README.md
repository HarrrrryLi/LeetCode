Bit Compress

The conditions means: word should contain first letter of puzzle and word is a substring of a puzzle.

Then use bit compress for both word and puzzle. Use (sub - 1) & mask to create a substring. 


Time Complexity O(max(WL, PL)). Space Complexity O(WL)