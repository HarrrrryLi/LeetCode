class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        videos = collections.Counter()
        visited = set()
        queue = collections.deque()

        visited.add(id)
        queue.append((id, 0))

        while queue:
            usrid, l = queue.popleft()
            if l == level:
                for v in watchedVideos[usrid]:
                    videos[v] += 1
            else:
                for f in friends[usrid]:
                    if f not in visited:
                        visited.add(f)
                        queue.append((f, l + 1))

        return sorted(videos.keys(), key=lambda x: (videos[x], x))
