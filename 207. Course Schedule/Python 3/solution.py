class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for course in range(numCourses):
            graph[course] = set()

        for course, pre in prerequisites:
            graph[course].add(pre)

        visited = collections.Counter()
        for course in range(numCourses):
            if not self.isAcyclic(course, visited, graph):
                return False

        return True

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
