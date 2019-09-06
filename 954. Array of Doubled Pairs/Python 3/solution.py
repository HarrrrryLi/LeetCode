class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        Cnter = collections.Counter(A)
        if 0 in Cnter and Cnter[0] % 2 == 1:
            return False

        while Cnter:
            min_num = min(Cnter, key=lambda x: abs(x))
            nxt_num = 2 * min_num
            if nxt_num not in Cnter:
                return False

            Cnter[min_num] -= 1
            Cnter[nxt_num] -= 1

            if not Cnter[min_num]:
                del Cnter[min_num]
            if not Cnter[nxt_num]:
                del Cnter[nxt_num]

        return True
