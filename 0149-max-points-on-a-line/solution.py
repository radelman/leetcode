from math import atan2
from statistics import mode
from typing import List

class Solution:
	def maxPoints(self, points: List[List[int]]) -> int:
		n_points = len(points)
		
		if n_points == 0:
			return 0
		elif n_points == 1:
			return 1
		
		max_count = 0
		for center_point in range(n_points):
			angles = [atan2(points[i][0] - points[center_point][0],
			                points[i][1] - points[center_point][1]) for i in range(n_points)]
			del angles[center_point]
			md = mode(angles)
			count = len([x for x in angles if abs(x - md) < 1.0e-9])
			count += 1 # the center point is on the line
			max_count = max(max_count, count)
			
		return max_count
	
def main() -> None:
	test_cases = [
	[[1,1],[2,2],[3,3]],
	[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		points = inputs
		
		test = solution.maxPoints(points)
		
		print(str(test))
		
if __name__ == '__main__':
	main()
	