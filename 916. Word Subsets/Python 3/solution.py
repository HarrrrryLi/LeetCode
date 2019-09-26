class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        Cnter = collections.Counter()

        for b in B:
            cnter = collections.Counter(b)
            for key in cnter:
                Cnter[key] = max(Cnter[key], cnter[key])

        result = []
        for a in A:
            CnterA = collections.Counter(a)
            for key in Cnter:
                if CnterA[key] < Cnter[key]:
                    break
            else:
                result.append(a)

        return result
