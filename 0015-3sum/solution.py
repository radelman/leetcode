from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		n_nums = len(nums)
		
		nums = sorted(nums)
		
		previous_nums = set()
		three_sums = set()
		
		for i in range(1, n_nums):
			previous_nums.add(nums[i - 1])
			
			for j in range(i + 1, n_nums):
				num_needed = -(nums[i] + nums[j])
				if num_needed in previous_nums:
					three_sum = (num_needed, nums[i], nums[j])
					three_sums.add(three_sum)
					
		three_sums = [list(x) for x in three_sums]
		
		return three_sums
	
def main() -> None:
	test_cases = [
	[-1,0,1,2,-1,-4],
	[],
	[0]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums = inputs
		
		test = solution.threeSum(nums)
		
		print(test)
		
if __name__ == '__main__':
	main()
	