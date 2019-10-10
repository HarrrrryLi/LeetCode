class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def cannot_add(distances, K, max_dist):
            add_stations = 0
            for d in distances:
                n = d // max_dist
                add_stations += n
                if d == n * max_dist:
                    add_stations -= 1
            return add_stations > K

        n = len(stations)
        distances = [stations[i+1] - stations[i] for i in range(n - 1)]
        d_min, d_max = min(distances), max(distances)
        low, high = d_min / (K + 1), d_max
        while low < high - 10 ** (-6):
            mid = low + (high - low) / 2
            if cannot_add(distances, K, mid):
                low = mid
            else:
                high = mid
        return low
