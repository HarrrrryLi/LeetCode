class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        stack = collections.deque()
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c == stack[0]:
                    stack.append(c)
                else:
                    stack.pop()
                    if not stack:
                        result += 1
        return result
