class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((w / q, q, w)
                         for q, w in zip(quality, wage))

        result = float('inf')
        heap = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(heap, -q)
            sumq += q

            if len(heap) > K:
                sumq += heapq.heappop(heap)

            if len(heap) == K:
                result = min(result, ratio * sumq)

        return float(result)
