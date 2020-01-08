class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = collections.deque()
        size = len(arr)

        visited.add(start)
        queue.append(start)

        while queue:
            idx = queue.popleft()
            if not arr[idx]:
                return True
            left, right = idx - arr[idx], idx + arr[idx]
            if left >= 0 and left not in visited:
                visited.add(left)
                queue.append(left)
            if right < size and right not in visited:
                visited.add(right)
                queue.append(right)

        return False
