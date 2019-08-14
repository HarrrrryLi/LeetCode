class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True
        stack = collections.deque()

        pop_idx = 0
        push_idx = 0
        size = len(pushed)
        while pop_idx < size:
            while not stack or stack[-1] != popped[pop_idx]:
                if push_idx >= size:
                    return False
                stack.append(pushed[push_idx])
                push_idx += 1
            stack.pop()
            pop_idx += 1

        return True
