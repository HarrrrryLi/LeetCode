class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        groups = [set(), set()]
        stack = collections.deque()
        dislike_dict = collections.defaultdict(list)

        for p1, p2 in dislikes:
            dislike_dict[p1].append(p2)
            dislike_dict[p2].append(p1)

        for person in range(1, N + 1):
            if person not in groups[0] and person not in groups[1]:
                stack.append((person, 0))
                groups[0].add(person)
                while stack:
                    p, g = stack.pop()
                    for dislike in dislike_dict[p]:
                        if dislike in groups[g]:
                            return False
                        if dislike not in groups[1 - g]:
                            groups[1 - g].add(dislike)
                            stack.append((dislike, 1 - g))

        return True
