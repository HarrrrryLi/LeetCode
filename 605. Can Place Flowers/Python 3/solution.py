class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        for idx in range(size):
            if n == 0:
                break
            if flowerbed[idx] == 0:
                if (idx - 1 < 0 or flowerbed[idx - 1] == 0) and (idx == size - 1 or flowerbed[idx + 1] == 0):
                    flowerbed[idx] = 1
                    n -= 1
        return n == 0
