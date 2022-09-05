from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = [[] for i in range(numCourses)]
        n_left = [0] * numCourses

        for ending, starting in prerequisites:
            edges[starting].append(ending)
            n_left[ending] += 1

        ready = [i for i in range(numCourses) if n_left[i] == 0]
        schedule = []

        for starting in ready:
            schedule.append(starting)

            for ending in edges[starting]:
                n_left[ending] -= 1

                if n_left[ending] == 0:
                    ready.append(ending)

        if len(schedule) < numCourses:
            return []

        return schedule

def main() -> None:
	test_cases = [
        (2, [[1,0]]),
        (4, [[1,0],[2,0],[3,1],[3,2]]),
	]

	solution = Solution();

	for inputs in test_cases:
		numCourses, prerequisites = inputs

		test = solution.findOrder(numCourses, prerequisites)

		print(test)

if __name__ == '__main__':
    main()
