We can't include the number which is larger than R. And we must include at least a number which is in [L, R].


Go through the list, store all numbers which are larger than R into a list called stop, store all numbers which are in [L, R] into a list called nums.
Add -1 to the left of stop list and add size of origin list to the right of stop list

For each nums(call it current), find it position in stop list called idx. Then we can get rightwall = stop[idx], leftwall = stop[idx - 1]. We can form subarrays in (leftwall, rightwall). Also we must include current, so we can calculate left and right which means how many numbers are in (leftwall, current) and (current, rightwall). Then in this area, we get  (left + 1) * (right + 1) subarrays. 


However, if in (leftwall, rightwall), there are two or more numbers which are in [L, R], we will calculate some subarrays multiple times. So after each calculation we need to add current to the stop list.


Time Complexity O(N logN). Space Complexity O(N)