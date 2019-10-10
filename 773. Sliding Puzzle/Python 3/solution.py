class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def boardToTuple(board):
            return tuple(board[0]) + tuple(board[1])

        def switch(current, zeroIndex, TargetIndex):
            temp = list(current)
            temp[zeroIndex] = temp[TargetIndex]
            temp[TargetIndex] = 0
            return tuple(temp)

        candidates = [boardToTuple(board)]
        moves = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        count = 0
        nextLevelCandidates = []
        used = set(candidates)

        while candidates:
            current = candidates.pop()

            if current == (1, 2, 3, 4, 5, 0):
                return count

            zeroIndex = current.index(0)

            for m in moves[zeroIndex]:
                newCandidate = switch(current, zeroIndex, m)
                if newCandidate not in used:
                    used.add(newCandidate)
                    nextLevelCandidates.append(newCandidate)

            if not candidates:
                candidates = nextLevelCandidates
                nextLevelCandidates = []
                count += 1
        return -1
