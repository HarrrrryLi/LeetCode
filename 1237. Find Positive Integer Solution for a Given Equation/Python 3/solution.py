"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        MAX_INT = 2 ** 32 - 1
        for x in range(1, MAX_INT + 1):
            if customfunction.f(x, 1) >= z:
                x_MAX = x
                break

        for y in range(1, MAX_INT + 1):
            if customfunction.f(1, y) >= z:
                y_MAX = y
                break

        result = []
        x, y = 1, y_MAX

        while x <= x_MAX and y > 0:
            current = customfunction.f(x, y)
            if current == z:
                result.append([x, y])
                x += 1
            elif current < z:
                x += 1
            else:
                y -= 1

        return result
