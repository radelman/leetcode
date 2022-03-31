from typing import List

class Solution:
	def inHash(self, nums: List[int], num) -> bool:
		n_nums = len(nums)
		
		loc = num % n_nums
		loc_orig = loc
		
		while nums[loc] != -num:
			loc = (loc + 1) % n_nums
			if loc == loc_orig:
				return False
			
		return True
	
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
			if nums[i] < 0:
				nums[i] = 0
				
		for i in range(n_nums):
			num = nums[i]
			if num > 0:
				nums[i] = 0
				start_from_next = i + 1
				break
		if num == 0:
			return 1
		
		while num > 0:
			loc = num % n_nums
			while nums[loc] < 0:
				loc = (loc + 1) % n_nums
				
			nums[loc], num = -num, nums[loc]
			
			if num == 0:
				while start_from_next < n_nums:
					num = nums[start_from_next]
					if num > 0:
						nums[start_from_next] = 0
						break
					start_from_next += 1
				if num == 0:
					break
				
		for i in range(1, n_nums + 2):
			if not self.inHash(nums, i):
				return i
			
		return 0 # should never get here
	
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
	