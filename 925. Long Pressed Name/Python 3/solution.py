class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nsize, tsize = len(name), len(typed)

        ncnt, tcnt = 0, 0

        while ncnt < nsize and tcnt < tsize:
            if name[ncnt] != typed[tcnt]:
                return False

            ncur, tcur = ncnt, tcnt
            ncnt += 1
            tcnt += 1
            while ncnt < nsize and name[ncnt - 1] == name[ncnt]:
                ncnt += 1
            while tcnt < tsize and typed[tcnt - 1] == typed[tcnt]:
                tcnt += 1

            if tcnt - tcur < ncnt - ncur:
                return False

        return ncnt == nsize and tcnt == tsize
