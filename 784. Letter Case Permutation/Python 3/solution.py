class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S.isdigit():
            return [S]

        record = []
        for idx, c in enumerate(S):
            if c.isalpha():
                record.append(idx)

        size = len(record)
        result = []
        for comb in itertools.product(range(2), repeat=size):
            pre = 0
            temp = ''
            for idx, num in enumerate(comb):
                i = record[idx]
                temp += S[pre: i]
                pre = i + 1
                if num:
                    temp += S[i].upper()
                else:
                    temp += S[i].lower()
            temp += S[pre:]
            result.append(temp)

        return result
