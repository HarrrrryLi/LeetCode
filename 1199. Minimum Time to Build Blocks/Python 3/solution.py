class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        blocks.sort()
        heap = []
        heapq.heappush(heap, (len(blocks), 0, 0, 1))
        result = float('inf')
        while heap:
            size, time, cur_time, worker = heapq.heappop(heap)
            if size <= 0:
                result = min(time, result)
            if worker >= size:
                result = min(result, max(time, cur_time + blocks[size - 1]))
            if time >= result:
                continue
            lower = 1
            if blocks[size - 1] == blocks[0]:
                lower = min(worker, size - worker)
            for to_split in range(lower, min(worker, size - worker) + 1):
                to_work = worker - to_split
                nxt_time = max(time, blocks[size - 1] + cur_time)
                nxt_cur_time = cur_time + split
                nxt_worker = worker - to_work + to_split
                heapq.heappush(heap, (size - to_work, nxt_time,
                                      nxt_cur_time, nxt_worker))

        return result
