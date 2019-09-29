class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        record = collections.defaultdict(list)

        for idx, color in enumerate(colors):
            record[color].append(idx)

        result = []

        for start, target in queries:
            if target not in record:
                result.append(-1)
            else:
                idx = bisect.bisect(record[target], start)
                dist = len(colors)
                if idx != 0:
                    dist = min(dist, start - record[target][idx - 1])
                if idx != len(record[target]):
                    dist = min(dist, record[target][idx] - start)
                result.append(dist)

        return result
