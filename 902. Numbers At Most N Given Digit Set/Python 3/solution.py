class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        size = len(D)
        candidates = set(int(d) for d in D)
        digits = len(str(N))
        result = 0
        record = {0: 0}

        for num in range(1, 10):
            record[num] = record[num - 1]
            if num - 1 in candidates:
                record[num] += 1

        for n in range(digits - 1, 0, -1):
            result += size ** n

        bit = digits
        inbound = True
        for c in str(N):
            digit = int(c)
            smaller = record[digit]
            if inbound:
                result += smaller * (size ** (bit - 1))
            else:
                break
            bit -= 1
            if digit not in candidates:
                inbound = False

        if inbound:
            result += 1

        return result
