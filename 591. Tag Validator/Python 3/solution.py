class Solution:
    def isValid(self, code: str) -> bool:
        if code[0] != '<':
            return False
        stack = []
        i = 1
        state = 0
        curr = ''
        is_first = True
        while i < len(code):
            if state == 0 and code[i] != '>':
                if not is_first and not stack:
                    return False
                if 0 <= ord(code[i]) - ord('A') < 26:
                    curr += code[i]
                    i += 1
                else:
                    return False
            elif state == 0:
                if len(curr) == 0 or len(curr) > 9:
                    return False
                stack.append(curr)
                is_first = False
                curr = ''
                state = 1
                i += 1
            elif state == 1 and code[i] == '<':
                if code[i:i + 9] == '<![CDATA[':
                    curr = ''
                    state = 2
                    i += 9
                elif code[i + 1] != '/':
                    curr = ''
                    state = 0
                    i += 1
                else:
                    state = 3
                    curr = ''
                    i += 2
            elif state == 1:
                curr += code[i]
                i += 1
            elif state == 2 and code[i:i + 3] != ']]>':
                i += 1
            elif state == 2:
                if i + 3 >= len(code):
                    return False
                state = 1
                curr = ''
                i += 3
            elif state == 3 and code[i] != '>':
                curr += code[i]
                i += 1
            elif state == 3:
                if not stack or stack[-1] != curr:
                    return False
                stack.pop(-1)
                i += 1
                state = 1
                curr = ''
            else:
                print('False State Machine')
        return state == 1 and not stack and len(curr) == 0
