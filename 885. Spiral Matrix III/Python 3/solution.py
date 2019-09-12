class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        pattern = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pidx, pcnt = 0, 0
        size = 1
        result = [(r0, c0)]
        cur = (r0, c0)
        while len(result) < R * C:
            rdir, cdir = pattern[pidx]
            for delta in range(1, size + 1):
                nxtr = cur[0] + delta * rdir
                nxtc = cur[1] + delta * cdir
                if nxtc < C and nxtc >= 0 and nxtr < R and nxtr >= 0:
                    result.append((nxtr, nxtc))
            cur = (cur[0] + size * rdir, cur[1] + size * cdir)
            pcnt += 1
            pidx += 1
            pidx %= 4
            if pcnt == 2:
                pcnt = 0
                size += 1

        return result
