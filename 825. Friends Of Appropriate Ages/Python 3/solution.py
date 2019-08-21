class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        result = 0
        Cnter = collections.Counter(ages)

        for candidate in Cnter:
            freq = Cnter[candidate]
            if freq > 1 and candidate > 14:
                result += freq * (freq - 1)

        for ageA, ageB in itertools.permutations(Cnter.keys(), 2):
            if (ageA < 100 and ageB > 100) or ((ageB - 7) * 2 <= ageA) or (ageB > ageA):
                continue
            result += Cnter[ageA] * Cnter[ageB]

        return result
