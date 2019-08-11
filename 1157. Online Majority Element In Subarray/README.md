Using Binary search.
for each number, store it indices into a list. For each query, binary search left and right in each number's indices list. If different is at least threshold, return this number.



PS: THIS METHOD WILL BE TLE FOR PYTHON 3. ACCORDING TO [@lee215](https://leetcode.com/problems/online-majority-element-in-subarray/discuss/355848/Python-Random-Draft-%2B-Binary-Search) USING 20 TIMES RANDOM CAN HIGHLY PASS ALL TEST CASE


Time Complexity:
    Init: O(L)
    Query: O(N log L)

Space Complexity O(N)