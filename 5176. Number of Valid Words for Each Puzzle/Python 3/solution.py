class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        freq = collections.Counter()
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            freq[mask] += 1

        result = []
        for puzzle in puzzles:
            mask = 0
            for c in puzzle:
                mask |= 1 << (ord(c) - ord('a'))

            first = ord(puzzle[0]) - ord('a')
            sub = mask
            cnt = 0

            while True:
                if (sub >> first) & 1:
                    cnt += freq[sub]

                if not sub:
                    break

                sub = (sub - 1) & mask

            result.append(cnt)
        return result
