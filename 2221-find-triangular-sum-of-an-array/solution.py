from typing import List

class Solution:
	def triangularSum(self, nums: List[int]) -> int:
		result = 0
		
		# the number of times each number shows up in the final sum is equal
		# to its corresponding binomial coefficient.  to save time, though,
		# instead of calculating each coefficient from scratch, we'll use some
		# recursive identities
		for i, num in enumerate(nums):
			if i == 0:
				coeff = 1
			else:
				coeff = (((len(nums) - 1) - i + 1) * coeff) // i
			result += coeff * num
			
		# using the fact that (a + b) % n = a % n + b % n, we only need to do
		# the final mod at the very end
		result = result % 10
		
		return result
	
def main() -> None:
	test_cases = [
	[1,2,3,4,5],
	[5]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums = inputs
		
		test = solution.triangularSum(nums)
		
		print(test)
		
if __name__ == '__main__':
	main()
	