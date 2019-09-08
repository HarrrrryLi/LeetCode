class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        size = len(distance)

        for idx in range(start, destination + 1 + size):
            if idx % size == destination:
                break
            clockwise += distance[idx % size]

        counterclockwise = 0
        for idx in range(start - 1, destination - size - 2, -1):
            if idx % size == destination - 1:
                break
            counterclockwise += distance[idx % size]

        return min(counterclockwise, clockwise)
