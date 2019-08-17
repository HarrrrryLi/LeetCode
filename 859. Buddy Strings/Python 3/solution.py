class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        sizeA, sizeB = len(A), len(B)
        if sizeA != sizeB:
            return False

        temp = []
        Cnter = collections.Counter()
        for c1, c2 in zip(A, B):
            if c1 != c2:
                temp.append((c1, c2))
            Cnter[c1] += 1

        if len(temp) == 2:
            if (temp[0][1], temp[0][0]) == temp[1]:
                return True
            else:
                return False
        elif len(temp) == 0:
            for key in Cnter:
                if Cnter[key] >= 2:
                    return True
        return False
