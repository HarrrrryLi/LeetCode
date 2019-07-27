class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        levels = [-1] * (N + 1)
        pres = collections.defaultdict(list)
        nxts = collections.defaultdict(list)
        for pre, nxt in relations:
            pres[nxt].append(pre)
            nxts[pre].append(nxt)

        stack = collections.deque()
        for course in range(1, N + 1):
            if not nxts[course]:
                stack.append((course, 1))
                levels[course] = 1

        if not stack:
            return -1

        result = 0
        while stack:
            course, depth = stack.pop()
            if not pres[course]:
                result = max(result, depth)
                if result == N:
                    break
                continue
            if depth == N:
                return -1
            for c in pres[course]:
                if levels[c] >= depth + 1:
                    continue
                levels[c] = depth + 1
                stack.append((c, depth + 1))

        return result
