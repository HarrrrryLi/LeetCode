class Solution:
    def minimumDistance(self, word: str) -> int:
        KEY_LEN = 6
        dp = {}

        for c in word:
            nxt = {}
            if not dp:
                nxt[('', c)] = 0
                nxt[(c, '')] = 0
            else:
                for left, right in dp:
                    val = dp[(left, right)]
                    cur_pos = self.getPos(c, KEY_LEN)
                    left_pos = self.getPos(left, KEY_LEN) if left else cur_pos
                    right_pos = self.getPos(
                        right, KEY_LEN) if right else cur_pos

                    nxt[(left, c)] = min(nxt.get((left, c), float('inf')),
                                         val + self.getDist(cur_pos, right_pos))
                    nxt[(c, right)] = min(nxt.get((c, right), float('inf')),
                                          val + self.getDist(cur_pos, left_pos))
            dp = nxt

        return min(dp.values())

    def getPos(self, c, KEY_LEN):
        ascii_diff = ord(c) - ord('A')
        row = ascii_diff // KEY_LEN
        col = ascii_diff % KEY_LEN

        return (row, col)

    def getDist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
