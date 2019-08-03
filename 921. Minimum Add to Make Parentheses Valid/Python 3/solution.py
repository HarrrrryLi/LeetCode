class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        result = 0
        stack = collections.deque()

        for c in S:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    result += 1
                else:
                    stack.pop()

        while stack:
            stack.pop()
            result += 1

        return result
