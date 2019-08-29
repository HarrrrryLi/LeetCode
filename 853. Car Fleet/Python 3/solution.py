class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        info = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        curp, curs = info[0]
        size = len(info)
        result = 1
        for idx in range(1, size):
            nxtp, nxts = info[idx]
            if nxts > curs:
                t = (curp - nxtp) / (nxts - curs)
                if t * nxts + nxtp > target:
                    curp, curs = nxtp, nxts
                    result += 1
            elif nxts == curs:
                if curp != nxtp:
                    curp, curs = nxtp, nxts
                    result += 1
            else:
                curp, curs = nxtp, nxts
                result += 1
        return result
