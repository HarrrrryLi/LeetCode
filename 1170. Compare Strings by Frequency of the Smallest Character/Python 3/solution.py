class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query_record = self.flist(queries)
        words_record = self.flist(words)
        words_record.sort()

        result = []
        size = len(words_record)
        for freq in query_record:
            idx = bisect.bisect_right(words_record, freq)
            result.append(size - idx)

        return result

    def flist(self, s_list):
        result = []
        for s in s_list:
            sc = 'z'
            freq = 0
            for c in s:
                if c < sc:
                    freq = 1
                    sc = c
                elif c == sc:
                    freq += 1
            result.append(freq)
        return result
