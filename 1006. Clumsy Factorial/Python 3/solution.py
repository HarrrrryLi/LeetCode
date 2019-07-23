class Solution:
    def clumsy(self, N: int) -> int:
        # ops = ['*', '/', '+', '-']
        result = N
        op_idx = 0
        nums = collections.deque()
        ops = collections.deque()
        for num in range(N - 1, 0, -1):
            if op_idx == 0:
                result *= num
            elif op_idx == 1:
                result //= num
            elif op_idx == 2:
                nums.append(result)
                ops.append('+')
                result = num
            else:
                nums.append(result)
                ops.append('-')
                result = num
            op_idx += 1
            op_idx %= 4

        nums.append(result)

        result = nums.popleft()

        while nums:
            op = ops.popleft()
            num = nums.popleft()
            if op == '+':
                result += num
            else:
                result -= num

        return result
