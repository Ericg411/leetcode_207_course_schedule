from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            in_degree[prereq[0]] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed_courses = 0

        while queue:
            course = queue.popleft()
            processed_courses += 1
            for next_course in adj[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return processed_courses == numCourses