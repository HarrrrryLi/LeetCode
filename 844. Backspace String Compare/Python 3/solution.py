class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_size, t_size = len(S), len(T)
        s_idx, t_idx = s_size - 1, t_size - 1

        while s_idx >= 0 or t_idx >= 0:
            bs_count = 0
            s_stored, t_stored = '', ''
            while True:
                if s_idx < 0:
                    break
                if S[s_idx] == '#':
                    bs_count += 1
                else:
                    if bs_count:
                        bs_count -= 1
                    else:
                        s_stored = S[s_idx]
                        break
                s_idx -= 1

            bs_count = 0
            while True:
                if t_idx < 0:
                    break
                if T[t_idx] == '#':
                    bs_count += 1
                else:
                    if bs_count:
                        bs_count -= 1
                    else:
                        t_stored = T[t_idx]
                        break
                t_idx -= 1
            if t_stored != s_stored:
                return False
            s_idx -= 1
            t_idx -= 1

        return True

#### O(N) Space Complexity Solution ####

# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         S_stack, T_stack = collections.deque(), collections.deque()

#         for c in S:
#             if c == '#':
#                 if S_stack:
#                     S_stack.pop()
#             else:
#                 S_stack.append(c)

#         for c in T:
#             if c == '#':
#                 if T_stack:
#                     T_stack.pop()
#             else:
#                 T_stack.append(c)

#         return S_stack == T_stack
