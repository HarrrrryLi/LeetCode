class Solution:
    def numSpecialEquivGroups(self, A: list[str]) -> int:
        temp = set()
        for s in A:
            temp.add((''.join(sorted(s[::2])), ''.join(sorted(s[1::2]))))

        return len(temp)
