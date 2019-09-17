Split String with '\n' first.

For each line, if there are n '\t' at the beginning, it's at n level.

So for each line, just judge where it's a file or a directory. If it's a directory, calculate length and record it into a dictionary. If it's a file, just add all levels before, and update result.


Time Complexity O(N). Space Complexity O(N)