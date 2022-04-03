from collections import deque
from typing import List

class Solution:
	# my answer after reading the discussion section
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		n_nums = len(nums)
		
		d = deque()
		
		max_sliding_window = []
		
		for i in range(n_nums):
			while len(d) > 0 and d[0][0] < i - k + 1:
				d.popleft()
				
			while len(d) > 0 and d[-1][1] < nums[i]:
				d.pop()
				
			d.append((i, nums[i]))
			
			if i >= k - 1:
				max_sliding_window.append(d[0][1])
				
		return max_sliding_window
	
def main() -> None:
	test_cases = [
	[[1,3,-1,-3,5,3,6,7], 3],
	[[1], 1]
	]
	
	solution = Solution()
	
	for inputs in test_cases:
		nums, k = inputs
		
		test = solution.maxSlidingWindow(nums, k)
		
		print(test)
		
if __name__ == '__main__':
	main()
	