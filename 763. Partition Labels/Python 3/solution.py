class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        first = {}
        last = {}
        stack = collections.deque()
        
        for idx, c in enumerate(S):
            if c not in first:
                first[c] = idx
            last[c] = idx
        
        stack.append(0)
        for idx, c in enumerate(S):
            last_idx = last[c]
            first_idx = first[c]
            while stack and first_idx <= stack[-1]:
                stack.pop()
            stack.append(last_idx)

        result = []
        pre = -1
        while stack:
            current = stack.popleft()
            result.append(current - pre)
            pre = current
        
        return result
            