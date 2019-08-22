class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        left, right = int(L), int(R)
        bound = 100000
        result = 0
        for half in range(1, bound):
            num = int(str(half) + str(half)[::-1])
            square = num * num
            if square > right:
                break
            if square >= left and self.isPalindrome(square):
                result += 1

        for half in range(1, bound):
            num = int(str(half) + str(half)[-2::-1])
            square = num * num
            if square > right:
                break
            if square >= left and self.isPalindrome(square):
                result += 1

        return result

    def isPalindrome(self, x):
        s = str(x)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
