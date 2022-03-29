from collections import deque
from typing import List, Tuple

class Solution:
	# is List[Tuple[int, int]] correct?
	def heapify_number_in_window(self, window: List[Tuple[int, int]], idxs: List[int], current: int) -> None:
		k = len(window)
		
		while (True):
			swap_up = False
			swap_left = False
			swap_right = False
			
			if current > 0:
				parent = (current - 1) // 2
				if window[current][1] > window[parent][1]:
					swap_up = True
					
			if not swap_up:
				if current < k:
					left_child = 2 * current + 1
					right_child = 2 * current  + 2
					if left_child < k and right_child < k:
						if window[left_child][1] > window[current][1] and window[left_child][1] >= window[right_child][1]:
							swap_left = True
						elif window[right_child][1] > window[current][1] and window[right_child][1] >= window[left_child][1]:
							swap_right = True
					elif left_child < k:
						if window[left_child][1] > window[current][1]:
							swap_left = True
					elif right_child < k:
						if window[right_child][1] > window[current][1]:
							swap_right = True
							
			if swap_up:
				swap_with = parent
			elif swap_left:
				swap_with = left_child
			elif swap_right:
				swap_with = right_child
			else:
				break
			
			idxs[window[current][0]], idxs[window[swap_with][0]] = idxs[window[swap_with][0]], idxs[window[current][0]] # this line must go ...
			window[current], window[swap_with] = window[swap_with], window[current] # before this one
			current = swap_with
			
	# my answer before reading the dicussion section
	def maxSlidingWindow_heap(self, nums: List[int], k: int) -> List[int]:
		n_nums = len(nums)
		
		window = []
		idxs = []
		
		for i in range(k):
			window.append((i, nums[i]))
			idxs.append(i)
			
			self.heapify_number_in_window(window, idxs, i)
			
		max_sliding_window = (n_nums - k + 1) * [0]
		for i in range(k, n_nums + 1):
			max_sliding_window[i - k] = window[0][1]
			
			if i == n_nums:
				break
			
			window[idxs[i - k]] = (i, nums[i])
			idxs.append(idxs[i - k])
			
			self.heapify_number_in_window(window, idxs, idxs[i])
			
		return max_sliding_window
	
	# my answer after reading the dicussion section
	def maxSlidingWindow_deque(self, nums: List[int], k: int) -> List[int]:
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
		
		test_heap = solution.maxSlidingWindow_heap(nums, k)
		test_deque = solution.maxSlidingWindow_deque(nums, k)
		
		print("heap: " + str(test_heap))
		print("deque: " + str(test_deque))
		
if __name__ == '__main__':
	main()
	