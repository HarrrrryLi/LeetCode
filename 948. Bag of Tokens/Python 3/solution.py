class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        result = temp = 0
        while deque and (P >= deque[0] or temp):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                temp += 1
            result = max(result, temp)

            if deque and temp:
                P += deque.pop()
                temp -= 1

        return result
