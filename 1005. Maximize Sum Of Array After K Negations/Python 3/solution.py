class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)

        while K > 0:
            num = heapq.heappop(A)
            if num == 0:
                break
            elif num < 0:
                heapq.heappush(A, -num)
                K -= 1
            elif K % 2 == 0:
                heapq.heappush(A, num)
                K -= 2
            else:
                heapq.heappush(A, -num)
                K -= 1

        return sum(A)
