class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize a adjacency list
        pre_map = {i: [] for i in range(numCourses)}

        # append prerequisites to the course
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # use a set to keep track of the visited node
        visited = set()

        def dfs(course):
            # we find a cycle, which will be impossible to schedule the courses
            if course in visited:
                return False
            # we can finish the course if it does not have prerequisites
            if pre_map[course] == []:
                return True
            # now we need to traverse from course, so add it to visited
            visited.add(course)
            # run dfs on each of the prerequisites from pre_map
            for pre in pre_map[course]:
                # if there is a cycle, immediately return false
                if not dfs(pre):
                    return False
            # otherwise, it means course can be finished with prerequisites
            # so this course does not have to worry about prerequisite
            visited.remove(course)
            pre_map[course] = []
            return True
        
        # we need to go through every single course because they might be not
        # connected (eg. 1->2 3->4 where 2, 3 are not connected)
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
             
        
