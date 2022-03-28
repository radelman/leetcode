from dataclasses import dataclass
from typing import List

@dataclass
class Bar:
	width: int = 1
	height: int = 0
	left: 'Bar' = None # better way to do this?
	right: 'Bar' = None # better way to do this?
	
class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		n_heights = len(heights)
		
		if n_heights == 0:
			return 0
		elif n_heights == 1:
			return heights[0]
		
		bars = [Bar(height = heights[i]) for i in range(n_heights)]
		bars[0].right = bars[1]
		for i in range(1, n_heights - 1):
			bars[i].left = bars[i - 1]
			bars[i].right = bars[i + 1]
		bars[-1].left = bars[-2]
		
		bars.sort(key = lambda bar: bar.height, reverse = True)
		
		max_area = bars[0].height
		
		for bar in bars:
			
			# this bar has already been devoured, so move on
			if bar.width == 0:
				continue
			
			# keep devouring until the bar has fallen below its neighbors
			while True:
				
				left = bar.left
				right = bar.right
				
				devour_left = False
				devour_right = False
				
				if left is not None and right is not None:
					if bar.height >= left.height and bar.height >= right.height:
						if left.height >= right.height:
							devour_left = True
						else:
							devour_right = True
							
				elif left is not None:
					if bar.height >= left.height:
						devour_left = True
						
				elif right is not None:
					if bar.height >= right.height:
						devour_right = True
						
				if devour_left:
					bar.width = bar.width + left.width
					bar.height = min(bar.height, left.height)
					bar.left = left.left
					if bar.left is not None:
						bar.left.right = bar
					left.width = 0
					
				elif devour_right:
					bar.width = bar.width + right.width
					bar.height = min(bar.height, right.height)
					bar.right = right.right
					if bar.right is not None:
						bar.right.left = bar
					right.width = 0
					
				else:
					break # nothing left to devour :(
				
				max_area = max(max_area, bar.width * bar.height)
				
		return max_area
	
def main() -> None:
	test_cases = [
	[],
	[1],
	[2,1,5,6,2,3],
	[2,4]
	]
	
	solution = Solution()
	
	for inputs in test_cases:
		heights = inputs
		
		test = solution.largestRectangleArea(heights)
		
		print(str(test))
		
if __name__ == '__main__':
	main()
	