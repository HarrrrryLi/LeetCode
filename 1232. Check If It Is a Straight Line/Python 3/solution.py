class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        diffy, diffx = coordinates[1][1] - \
            coordinates[0][1], coordinates[1][0] - coordinates[0][0]
        if diffx == 0:
            k = float('inf')
        else:
            k = diffy / diffx
        size = len(coordinates)
        for idx in range(2, size):
            dy, dx = coordinates[idx][1] - coordinates[idx -
                                                       1][1], coordinates[idx][0] - coordinates[idx - 1][0]
            if dx == 0:
                if k != float('inf'):
                    return False
                else:
                    return True
            if k != dy / dx:
                return False

        return True
