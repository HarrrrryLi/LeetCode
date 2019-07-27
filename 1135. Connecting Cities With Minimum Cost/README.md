MST problem.

Build graph first. Then randomly choosing a start city. Add all connected cities to heap as (cost, city). for each time pop out one, if this city not in MST, add it to MST and add cost to result.

If final MST doesn't contain all cities, return -1 else return result


Time Complexity O(n). Space Complexity O(n). n is the length of list