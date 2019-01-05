class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_stack = collections.deque()
        num_stack = collections.deque()
        num = 0
        
        for c in s:
            if c.isdigit():
                num *= 10
                num += int(c)
                continue
            elif c == '[':
                if not num:
                    num_stack.append(1)
                num_stack.append(num)
                num = 0
            elif c == ']':
                temp = ''
                temp_c = str_stack.pop()
                while temp_c != '[':
                    temp = temp_c + temp
                    temp_c = str_stack.pop()
                temp = num_stack.pop() * temp
                str_stack.append(temp)
                continue
            
            str_stack.append(c)
        
        
        result = ''
        while str_stack:
            string = str_stack.pop()
            result = string + result
        
        return result