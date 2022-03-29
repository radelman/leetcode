from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		indices = {}
		
		for i, num in enumerate(nums):
			if target - num in indices:
				return [indices[target - num], i]
			else:
				indices[num] = i
				
		return [] # shouldn't get here (the problem stated there's exactly one solution)
	
def main() -> None:
	test_cases = [
	[[2,7,11,15], 9],
	[[3,2,4], 6],
	[[3,3], 6]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums, target = inputs
		
		test = solution.twoSum(nums, target)
		
		print(test)
		
if __name__ == '__main__':
	main()
	