class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        taken = 0
        while queue:
            curr = queue.pop(0)
            taken += 1
            for neighbour in adj[curr]:
                indegree[neighbour] -=1 
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return taken == numCourses
        

            