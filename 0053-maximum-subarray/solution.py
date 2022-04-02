from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		n_nums = len(nums)
		
		max_ending_here = nums[0]
		max_overall = nums[0]
		
		for i in range(1, n_nums):
			if max_ending_here > 0:
				max_ending_here = max_ending_here + nums[i]
			else:
				max_ending_here = nums[i]
			if max_ending_here > max_overall:
				max_overall = max_ending_here
			
		return max_overall
	
def main() -> None:
	test_cases = [
	[-2,1,-3,4,-1,2,1,-5,4],
	[1],
	[5,4,-1,7,8]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums = inputs
		
		test = solution.maxSubArray(nums)
		
		print(test)
		
if __name__ == '__main__':
	main()
	