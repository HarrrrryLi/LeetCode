class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        record = {}

        for queen in queens:
            if queen[0] == king[0]:
                row = king[0]
                if queen[1] > king[1]:
                    col = min(record.get(
                        'right', [float('inf'), float('inf')])[1], queen[1])
                    record['right'] = [row, col]
                else:
                    col = max(record.get(
                        'left', [float('inf'), float('-inf')])[1], queen[1])
                    record['left'] = [row, col]
            elif queen[1] == king[1]:
                col = king[1]
                if queen[0] > king[0]:
                    row = min(record.get(
                        'down', [float('inf'), float('inf')])[0], queen[0])
                    record['down'] = [row, col]
                else:
                    row = max(record.get(
                        'up', [float('-inf'), float('inf')])[0], queen[0])
                    record['up'] = [row, col]
            elif abs(queen[0] - king[0]) == abs(queen[1] - king[1]):
                if queen[0] > king[0]:
                    if queen[1] > king[1]:
                        pre = record.get(
                            'down-right', [float('inf'), float('inf')])
                        if pre[0] > queen[0]:
                            record['down-right'] = queen
                    else:
                        pre = record.get(
                            'down-left', [float('inf'), float('-inf')])
                        if pre[0] > queen[0]:
                            record['down-left'] = queen
                else:
                    if queen[1] > king[1]:
                        pre = record.get(
                            'up-right', [float('-inf'), float('inf')])
                        if pre[0] < queen[0]:
                            record['up-right'] = queen
                    else:
                        pre = record.get(
                            'up-left', [float('-inf'), float('-inf')])
                        if pre[0] < queen[0]:
                            record['up-left'] = queen

        result = []
        for key in record:
            result.append(record[key])

        return result
