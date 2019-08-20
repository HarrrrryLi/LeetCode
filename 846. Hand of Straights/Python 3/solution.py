class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        Cnter = collections.Counter(hand)
        candidates = sorted(Cnter.keys())

        for num in candidates:
            freq = Cnter[num]
            if not freq:
                continue
            for delta in range(W):
                nxt = delta + num
                if nxt not in candidates or Cnter[nxt] < freq:
                    return False
                Cnter[nxt] -= freq

        return True
