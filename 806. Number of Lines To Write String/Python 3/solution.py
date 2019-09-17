class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 1
        width = 0

        for c in S:
            idx = ord(c) - ord('a')
            length = widths[idx]
            if width + length > 100:
                width = length
                lines += 1
            else:
                width += length

        return [lines, width]
