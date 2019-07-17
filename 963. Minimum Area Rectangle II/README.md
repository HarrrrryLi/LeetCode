Using complex represent a vector.

Choosing 2 points, regard as diagonal points, calculate center and radius. Store them in a dictionary, key is center and radius, value is one point


Then for each center and radius, in the value list, choose 2 points, regard them as two points of on edge, then calculate the area by abs(P - Q) * abs(P - (2 * center - Q))


Time Complexity O(N^2) Space Complexity O(N ^ 2)


