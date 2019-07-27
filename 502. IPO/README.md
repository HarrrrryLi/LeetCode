sort (profit, capital) first with key -profit, capital.

Then when k > 0 and sorted list is not empty, go through sorted list, find the first element whose c is smaller or equal then W. Then W += p, remove this pair. k -= 1.

Time Complexity O(N * max(logN, k)) Space Complexity O(N)


