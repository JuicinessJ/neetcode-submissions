class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_lst = {}

        for course, req in prerequisites:
            if course not in adj_lst:
                adj_lst[course] = []

            adj_lst[course].append(req)

        seen = set()

        def dfs(course):
            if course in seen:
                return False

            if course not in adj_lst:
                return True

            seen.add(course)

            for pre in adj_lst[course]:
                if not dfs(pre):
                    return False
            
            seen.remove(course)
            adj_lst[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True




        


"""
I am given a nested list of integers or [[a, b]]:
where "a" represents the course I need to take,
and "b" represents the course I need to take before "a".

So for example: [0, 1], where 0 is the course I want to take,
and 1 is the course I need to take first.

However, if I was given [[0, 1], [1, 0]], this would be feasible impossible.
Since if I wanted to take course 0, I need to take course 1.
To take course 1, I need to take course 0.

I am also given another integer, which represents the total number of courses I can expect.

I am asked to return if its possible to complete these combinations of courses.
Where I return true, if the pre-reqs I am given is possible to take,
and false, if the pre-reqs given are impossible to complete.

Since our impossible case is caused by an overlap of two courses that require one another to take each other.
I am looking to prevent an overlap, for if we have an overlap, then the combination is impossible,
and if there is no overlap, then it is possible.

This means, I am looking to test for cycle by traversing the graph, if we have a cycle, then its a overlap, meaning bad.
If I can traverse the graph without a cycle, then we don't have an overlap, means good.

Since we are looking to test for overlap, we just need to compare courses for similarities.
We could try using a backtrack approach where if we have a course we want to take, and it requires a course that we are already taking.
Such as checking if b of [a, b] exist inside the hashmap.

Using this example: [[0,1], [1,2], [2,0]].
We'd have a hashmap where the key is "a" of [a, b],
and the value is "b", or a is courses we want to take, and b is what we need to take.

We start with [0, 1], we first check if 1 exist in the hashmap,
if it doesn't we add 0 as key and 1 as value.

We then check [1, 2], we check if 2 exist in the hashmap,
if not we then add 1 as key, and 2 as value.

Then we check [2, 0], we check if 0 exist in the hashmap, which it does.
So we call the backtrack, which iterates through, starting at 0,
sees 0 points to 1, checks 1, see its points to 2, and if it points to 0,
we return False, unless its easier to check earlier.
"""