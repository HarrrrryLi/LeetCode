class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = collections.deque()

        for idx, c in enumerate(s):
            if stack and c == stack[-1][0]:
                _, freq = stack.pop()
                stack.append((c, freq + 1))
                if freq + 1 >= k:
                    stack.pop()
            else:
                stack.append((c, 1))

        result = ''
        while stack:
            c, freq = stack.popleft()
            while stack and c == stack[0][0]:
                _, f = stack.popleft()
                freq += f
            if freq < k:
                result += c * freq

        return result
