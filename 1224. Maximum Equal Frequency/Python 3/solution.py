class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        Cnter = collections.Counter()
        freq = collections.Counter()
        result = 1
        for idx, num in enumerate(nums):
            if num not in Cnter:
                Cnter[num] += 1
                freq[1] += 1
            else:
                freq[Cnter[num]] -= 1
                if freq[Cnter[num]] == 0:
                    del freq[Cnter[num]]
                Cnter[num] += 1
                freq[Cnter[num]] += 1

            if len(Cnter) == 1:
                result = max(idx + 1, result)
                continue
            if 1 in freq and freq[1] == 1 and len(freq) == 2:
                result = max(idx + 1, result)
                continue
            if 1 in freq and len(freq) == 1:
                result = max(idx + 1, result)
                continue
            min_key, max_key = min(freq.keys()), max(freq.keys())
            if max_key == min_key + 1 and freq[max_key] == 1:
                result = max(idx + 1, result)

        return result
