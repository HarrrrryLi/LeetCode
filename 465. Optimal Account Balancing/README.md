For each person, we define the positive number means the amount he/she will receive, the negative number means the amount he/she will pay.

If we sum everyone's amount, the person whose amount is zero won't do any transaction. Then what we should do is just calculate transaction times of non-zero amounts.

Then we just need to find how many minimum zero sum groups(the list/set which has least numbers and sum of all numbers is equal to zero) are there in amounts, then use total length - group numbers is the result

For example if there is a amounts list like [-2, -3 ,1 ,4], then it only need 4 - 1 = 3 transactions.  If there is a amounts list like [-2, -3, 3, 2] then it only need 4 -2 = 2 transactions.

The last part is using BFS to find minimum zero sum group. 

O(n^2) time complexity