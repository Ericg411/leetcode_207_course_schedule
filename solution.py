from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_degree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            in_degree[prereq[0]] += 1
            adjacency[prereq[1]].append(prereq[0])

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0

        while queue:
            current = queue.popleft()
            courses_taken += 1
            print(current)
            next_courses = adjacency[current]
            for course in next_courses:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return courses_taken == numCourses
