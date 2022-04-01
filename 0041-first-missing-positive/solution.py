from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n_nums = len(nums)
		
		if n_nums == 0:
			return 1
		elif n_nums == 1:
			if nums[0] == 1:
				return 2
			else:
				return 1
			
		for i in range(n_nums):
			if nums[i] < 1 or nums[i] > n_nums:
				nums[i] = 0
				
		for i in range(n_nums):
			num = nums[i]
			if num > 0:
				nums[i] = 0
				start_from_next = i + 1
				break
		if num < 1:
			return 1
		
		while num > 0:
			loc = num - 1
			if nums[loc] != -num:
				nums[loc], num = -num, nums[loc]
			else:
				num = 0
				
			if num == 0:
				while start_from_next < n_nums:
					num = nums[start_from_next]
					if num > 0:
						nums[start_from_next] = 0
						start_from_next += 1
						break
					start_from_next += 1
				if num == 0:
					break
				
		for i in range(1, n_nums + 1):
			if nums[i - 1] != -i:
				return i
			
		return n_nums + 1
	
def main() -> None:
	test_cases = [
	[1,2,0],
	[3,4,-1,1],
	[7,8,9,11,12]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums = inputs
		
		test = solution.firstMissingPositive(nums)
		
		print(test)
		
if __name__ == '__main__':
	main()
	