class Solution:
    def longestDecomposition(self, text: str) -> int:
        size = len(text)
        left, right = 0, size - 1
        result = 0

        while left < right:
            temp = left
            temps = ''
            while True:
                while temp < right and text[temp] != text[right]:
                    temps += text[temp]
                    temp += 1
                temps += text[temp]
                if temp == right:
                    result += 1
                    return result
                length = temp - left + 1
                if temps == text[right + 1 - length: right + 1]:
                    result += 2
                    left = temp + 1
                    right = right - length
                    break
                else:
                    temp += 1
        if left == right:
            result += 1

        return result
