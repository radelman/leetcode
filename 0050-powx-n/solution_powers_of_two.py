class Solution:
	def myPow(self, x: float, n: int) -> float:
		abs_x = abs(x)
		abs_n = abs(n)
		y = 1.0
		while abs_n > 0:
			if abs_n & 1 == 1:
				y = abs_x * y
			abs_x = abs_x * abs_x
			abs_n = abs_n >> 1
			
		if x < 0.0:
			if n % 2 == 1:
				y = -y
				
		if n < 0:
			y = 1.0 / y
			
		return y
	
def main() -> None:
	test_cases = [
	(2.0, 10),
	(-2.0, 11),
	(2.0, -12),
	(2.0, 0),
	(0.0, 10)
	]
	
	solution = Solution()
	
	for inputs in test_cases:
		x, n = inputs
		
		reference = pow(x, n)
		test = solution.myPow(x, n)
		
		print(str(test) + ' =? ' + str(reference))
		
if __name__ == '__main__':
	main()
	