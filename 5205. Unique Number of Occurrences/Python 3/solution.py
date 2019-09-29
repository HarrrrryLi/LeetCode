class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Cnter = collections.Counter(arr)

        return len(set(Cnter.values())) == len(list(Cnter.values()))
