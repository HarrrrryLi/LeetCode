Create two dictionaries store mine related info. Fisrt one, key is row, value is list, each element is col of mine, using bisect make sure it's sorted. Second is the similar, using col as key.

Then go through each grid in this graph, calculate each grid left, right, up, down distance. If row or col in those dictionaries, using bisect find index to calculate length



Time Complexity O(N^2logN) Space Complexity O(N^2)