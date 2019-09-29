class Solution:
    def countLetters(self, S: str) -> int:
        result = 0
        size = len(S)
        cur = S[0]
        cur_cnt = 1

        for idx in range(1, size):
            if S[idx] == cur:
                cur_cnt += 1
            else:
                result += (cur_cnt + 1) * cur_cnt // 2
                cur = S[idx]
                cur_cnt = 1

        result += (cur_cnt + 1) * cur_cnt // 2
        return result
