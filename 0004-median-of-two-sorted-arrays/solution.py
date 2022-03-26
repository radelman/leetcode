from bisect import bisect_left
from statistics import median
from typing import List

class Solution:
	def findMedianSortedArraysOdd(self, nums1: List[int], nums2: List[int], extra_num: int) -> float:
		len1 = len(nums1)
		len2 = len(nums2)
		
		if extra_num is None:
			len3 = 0
			
			a = min(nums1[ 0], nums2[ 0])
			b = max(nums1[-1], nums2[-1])
		else:
			len3 = 1
			
			a = min(nums1[ 0], nums2[ 0], extra_num)
			b = max(nums1[-1], nums2[-1], extra_num)
			
		while (True):
			x = (a + b) / 2.0
			
			if b - a < 1.0:
				return round(x)
			
			idx1 = bisect_left(nums1, x)
			idx2 = bisect_left(nums2, x)
			
			if extra_num is None:
				idx3 = 0
			else:
				if x <= extra_num:
					idx3 = 0
				else:
					idx3 = 1
					
			n_left = idx1 + idx2 + idx3
			n_right = len1 + len2 + len3 - n_left
			
			if n_left > n_right:
				b = x
			else:
				a = x
				
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		len1 = len(nums1)
		len2 = len(nums2)
		
		if len1 == 0:
			if len2 % 2 == 0:
				return (nums2[len2 // 2 - 1] + nums2[len2 // 2]) / 2
			else:
				return nums2[(len2 - 1) // 2]
		elif len2 == 0:
			if len1 % 2 == 0:
				return (nums1[len1 // 2 - 1] + nums1[len1 // 2]) / 2
			else:
				return nums1[(len1 - 1) // 2]
		else:
			a = min(nums1[ 0], nums2[ 0])
			b = max(nums1[-1], nums2[-1])
			
			if (len1 + len2) % 2 == 0:
				left = self.findMedianSortedArraysOdd(nums1, nums2, a - 1)
				right = self.findMedianSortedArraysOdd(nums1, nums2, b + 1)
				return (left + right) / 2.0
			else:
				return self.findMedianSortedArraysOdd(nums1, nums2, None)
			
def main() -> None:
	test_cases = [
	[[], [1, 2]],
	[[], [1, 2, 3]],
	[[1, 2], []],
	[[1, 2, 3], []],
	[[1, 2, 3], [8, 9, 10, 11, 12, 13, 14]],
	[[1, 2, 3], [8, 9, 10, 11, 12, 13, 14, 15]]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		nums1 = inputs[0]
		nums2 = inputs[1]
		
		reference = median(sorted(nums1 + nums2))
		test = solution.findMedianSortedArrays(nums1, nums2)
		
		print(str(test) + ' =? ' + str(reference))
		
if __name__ == '__main__':
	main()
	