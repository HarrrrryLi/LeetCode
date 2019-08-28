class Solution(object):
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        stations.append((target, float('inf')))

        result = 0
        pre = 0
        tank = startFuel
        for position, fuel in stations:
            tank -= position - pre
            while heap and tank < 0:  # must refuel in past
                tank -= heapq.heappop(heap)
                result += 1
            if tank < 0:
                return -1
            heapq.heappush(heap, -fuel)
            pre = position

        return result
