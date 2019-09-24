class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for course in range(numCourses):
            graph[course] = set()

        for course, pre in prerequisites:
            graph[pre].add(course)

        visited = collections.Counter()
        for course in range(numCourses):
            if course in visited:
                continue
            if not self.isAcyclic(course, visited, graph):
                return []

        visited = set()
        result = []
        for course in range(numCourses):
            if course not in visited:
                self.toposort(course, visited, graph, result)

        result.reverse()
        return result

    def isAcyclic(self, cur, visited, graph):
        if visited[cur] == 2:
            return False

        if visited[cur] == 1:
            return True

        visited[cur] = 2

        for pre in graph[cur]:
            if not self.isAcyclic(pre, visited, graph):
                return False

        visited[cur] = 1
        return True

    def toposort(self, cur, visited, graph, result):
        visited.add(cur)

        for nxt in graph[cur]:
            if nxt not in visited:
                self.toposort(nxt, visited, graph, result)

        result.append(cur)
