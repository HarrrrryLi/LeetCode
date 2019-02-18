class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for new in asteroids:
            while result and new < 0 < result[-1]:
                if result[-1] < -new:
                    result.pop()
                    continue
                elif result[-1] == -new:
                    result.pop()
                break
            else:
                result.append(new)
        return result