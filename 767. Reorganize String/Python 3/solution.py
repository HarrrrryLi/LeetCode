class Solution:
    def reorganizeString(self, S: str) -> str:
        Cnter = collections.Counter(S)

        heap = []
        for key in Cnter:
            heapq.heappush(heap, (-Cnter[key], key))

        result = ''
        while heap:
            freq, c = heapq.heappop(heap)
            if result and c == result[-1]:
                if not heap:
                    return ''
                temp = (freq, c)
                freq, c = heapq.heappop(heap)
                heapq.heappush(heap, temp)

            result += c
            if -freq - 1:
                heapq.heappush(heap, (freq + 1, c))

        return result
