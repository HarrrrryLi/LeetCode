class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        if K == 0:
            return 5

        temp = 5
        temp_cnt = 1
        while temp_cnt * 5 + 1 <= K:
            temp_cnt *= 5
            temp_cnt += 1

        if temp_cnt == K:
            return 5

        while True:
            if K % temp_cnt == 0:
                if K // temp_cnt == 5:
                    return 0
                else:
                    return 5
            K %= temp_cnt
            while temp_cnt > K:
                temp_cnt -= 1
                temp_cnt //= 5

        return 5
