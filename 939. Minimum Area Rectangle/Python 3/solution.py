class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p = set()
        for x, y in points:
            p.add((x, y))

        result = float('inf')

        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            if x1 == x2 or y1 == y2:
                continue

            if (x1, y2) in p and (x2, y1) in p:
                area = abs(y2 - y1) * abs(x2 - x1)
                result = min(area, result)

        if result == float('inf'):
            return 0

        return result
