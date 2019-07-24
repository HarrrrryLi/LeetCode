class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        cur_c, cur_idx, cur_len = S[0], 0, 1
        size = len(S)
        result = []
        for cnt in range(1, size):
            c = S[cnt]
            if c == cur_c:
                cur_len += 1
            else:
                if cur_len >= 3:
                    result.append([cur_idx, cnt - 1])
                cur_c = c
                cur_idx = cnt
                cur_len = 1

        if cur_len >= 3:
            result.append([cur_idx, size - 1])

        return result
