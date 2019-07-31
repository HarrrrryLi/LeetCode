class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        didx = 0
        obs = set()
        for ob in obstacles:
            obs.add((ob[0], ob[1]))

        current = (0, 0)
        result = 0
        for command in commands:
            if command == -1:
                didx = (didx - 1) % 4
            elif command == -2:
                didx = (didx + 1) % 4
            else:
                step = directions[didx]
                while command:
                    nxt_x, nxt_y = current[0] + step[0], current[1] + step[1]
                    if (nxt_x, nxt_y) in obs:
                        break
                    current = (nxt_x, nxt_y)
                    result = max(result, nxt_x ** 2 + nxt_y ** 2)
                    command -= 1

        return result
