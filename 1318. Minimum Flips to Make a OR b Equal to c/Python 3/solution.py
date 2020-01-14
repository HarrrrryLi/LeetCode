class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_str, b_str, c_str = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        a_size, b_size, c_size = len(a_str), len(b_str), len(c_str)
        a_cnt, b_cnt, c_cnt = a_size - 1, b_size - 1, c_size - 1

        result = 0

        while c_cnt >= 0 or b_cnt >= 0 or a_cnt >= 0:
            a_bit = '0' if a_cnt < 0 else a_str[a_cnt]
            b_bit = '0' if b_cnt < 0 else b_str[b_cnt]
            c_bit = '0' if c_cnt < 0 else c_str[c_cnt]

            if c_bit == '0':
                if a_bit != '0':
                    result += 1
                if b_bit != '0':
                    result += 1
            else:
                if a_bit == '0' and b_bit == '0':
                    result += 1

            if a_cnt >= 0:
                a_cnt -= 1
            if b_cnt >= 0:
                b_cnt -= 1
            if c_cnt >= 0:
                c_cnt -= 1

        return result
