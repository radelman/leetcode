from typing import List

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		n_heights = len(heights)
		
		if n_heights == 0:
			return 0
		elif n_heights == 1:
			return heights[0]
		
		widths = n_heights * [1]
		lefts = list(range(-1, n_heights - 1))
		rights = list(range(1, n_heights + 1))
		rights[-1] = -1
		
		to_be_sorted = [(heights[i], i) for i in range(n_heights)]
		to_be_sorted.sort(key = lambda x: x[0], reverse = True)
		to_be_sorted = [to_be_sorted[i][1] for i in range(n_heights)]
		
		max_area = heights[to_be_sorted[0]]
		
		for current in to_be_sorted:
			
			# this bar has already been devoured, so move on
			if widths[current] == 0:
				continue
			
			# keep devouring until the bar has fallen below its neighbors
			while True:
				
				left = lefts[current]
				right = rights[current]
				
				devour_left = False
				devour_right = False
				
				if left >= 0 and right >= 0:
					
					if heights[current] >= heights[left] and heights[current] >= heights[right]:
						if heights[left] > heights[right]:
							devour_left = True
						else:
							devour_right = True
							
				elif left >= 0:
					
					if heights[current] >= heights[left]:
						devour_left = True
						
				elif right >= 0:
					
					if heights[current] >= heights[right]:
						devour_right = True
						
				if devour_left:
					
					widths[current] = widths[current] + widths[left]
					heights[current] = min(heights[current], heights[left])
					lefts[current] = lefts[left]
					if lefts[current] >= 0:
						rights[lefts[current]] = current
					widths[left] = 0
					
				elif devour_right:
					
					widths[current] = widths[current] + widths[right]
					heights[current] = min(heights[current], heights[right])
					rights[current] = rights[right]
					if rights[current] >= 0:
						lefts[rights[current]] = current
					widths[right] = 0
					
				else:
					break
				
				max_area = max(max_area, widths[current] * heights[current])
				
		return max_area
	
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		m = len(matrix)
		n = len(matrix[0])
		
		ones_above = [n * [0] for i in range(m)];
		for j in range(n):
			count = 0
			for i in range(m):
				if matrix[i][j] == '0':
					count = 0
				else:
					count += 1
				ones_above[i][j] = count
		
		max_area = 0
		for i in range(m):
			max_area = max(max_area, self.largestRectangleArea(ones_above[i]))
			
		return max_area
	
def main() -> None:
	test_cases = [
	[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
	]
	
	solution = Solution()
	
	for inputs in test_cases:
		matrix = inputs
		
		test = solution.maximalRectangle(matrix)
		
		print(str(test))
		
if __name__ == '__main__':
	main()
	