class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W_max = int(math.sqrt(area))

        for W in range(W_max, 0, -1):
            if not area % W:
                return [area // W, W]
