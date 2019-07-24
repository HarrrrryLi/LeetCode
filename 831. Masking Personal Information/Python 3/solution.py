class Solution:
    def maskPII(self, S: str) -> str:
        S = S.lower()
        if '@' in S:
            idx = S.index('@')
            result = S[0] + '*' * 5 + S[idx - 1:]
            return result
        temp = []
        for c in S:
            if c.isdigit():
                temp.append(c)

        size = len(temp)
        if size == 10:
            result = '***-***-{}'.format(''.join(temp[-4:]))
        else:
            result = '+{}-***-***-{}'.format('*' *
                                             (size - 10), ''.join(temp[-4:]))

        return result
