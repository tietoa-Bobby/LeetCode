class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:  
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visited[course] = 2
            return True

        for course in range(numCourses):
            if visited[course] == 0:  
                if not dfs(course):
                    return False
        
        return True
        