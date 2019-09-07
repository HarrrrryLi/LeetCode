Divide the grid into serval independent sideLength * sideLength grid. We will have some area are remained. 
Here we define add as put this area all for all areas.

First we add all right-bottom remain to each area. Then we add all bottom to each area. Next we add all right to each area. Last, we add other part to each area. If doing add will exceed the limit, we just reach the limit.


Time Complexity O(1). Space Complexity O(1)