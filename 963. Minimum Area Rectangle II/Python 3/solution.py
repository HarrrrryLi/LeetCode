class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = [complex(*point) for point in points]
        seen = collections.defaultdict(list)

        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        result = float('inf')

        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                result = min(result, abs(P - Q) * abs(P - (2 * center - Q)))

        return result if result < float('inf') else 0
