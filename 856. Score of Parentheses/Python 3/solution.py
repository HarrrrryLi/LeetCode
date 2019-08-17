class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = collections.deque()

        for c in S:
            if c == '(':
                stack.append(c)
            else:
                item = stack.pop()
                temp = 0
                while item != '(':
                    temp += item
                    item = stack.pop()
                if temp == 0:
                    stack.append(1)
                else:
                    stack.append(2 * temp)

        result = 0
        while stack:
            result += stack.pop()
        return result
