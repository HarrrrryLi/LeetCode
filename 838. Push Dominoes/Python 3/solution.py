class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ''
        size = len(dominoes)
        for idx, domino in enumerate(dominoes):
            if domino != '.':
                result += domino
            else:
                rfound, lfound = False, False
                for ltemp in range(idx + 1, size):
                    if dominoes[ltemp] == 'L':
                        lfound = True
                        llen = ltemp - idx
                        break
                    elif dominoes[ltemp] == 'R':
                        break
                for rtemp in range(idx - 1, -1, -1):
                    if dominoes[rtemp] == 'R':
                        rfound = True
                        rlen = idx - rtemp
                        break
                    elif dominoes[rtemp] == 'L':
                        break
                if rfound and lfound:
                    if rlen < llen:
                        result += 'R'
                    elif rlen > llen:
                        result += 'L'
                    else:
                        result += '.'
                elif rfound:
                    result += 'R'
                elif lfound:
                    result += 'L'
                else:
                    result += '.'

        return result
