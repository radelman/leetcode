from typing import List

class Solution:
	def trap(self, height: List[int]) -> int:
		n_height = len(height)
		
		water_level = height.copy()
		for i in range(1, n_height):
			water_level[i] = max(water_level[i - 1], water_level[i])
			
		m = 0
		for i in range(n_height - 1, -1, -1):
			m = max(m, height[i])
			water_level[i] = min(water_level[i], m)
			
		water = 0
		for i in range(n_height):
			water += water_level[i] - height[i]
			
		return water
	
def main() -> None:
	test_cases = [
	[0,1,0,2,1,0,1,3,2,1,2,1],
	[4,2,0,3,2,5]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums = inputs
		
		test = solution.trap(nums)
		
		print(test)
		
if __name__ == '__main__':
	main()
	