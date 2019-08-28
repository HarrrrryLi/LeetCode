class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        s = str(N)
        size = len(s)
        target = collections.Counter(s)

        temp = 1
        temps = str(temp)

        while len(temps) <= size:
            if len(temps) < size:
                temp *= 2
                temps = str(temp)
            else:
                if collections.Counter(temps) == target:
                    return True
                else:
                    temp *= 2
                    temps = str(temp)

        return False
