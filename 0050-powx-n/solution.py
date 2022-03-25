from math import exp, log

class Solution:
	def myPow(self, x: float, n: int) -> float:
		try:
			y = exp(abs(n) * log(abs(x)))
			
			if x < 0.0:
				if n % 2 == 1:
					y = -y
					
			if n < 0:
				y = 1.0 / y
				
		except:
			y = 0.0
			
		return y
	
if __name__ == '__main__':
	test_cases = [(2.0, 10), (-2.0, 11), (2.0, -12), (2.0, 0), (0.0, 10)]
	
	sol = Solution()
	
	for i, inputs in enumerate(test_cases):
		print(str(sol.myPow(inputs[0], inputs[1])) + ' =? ' + str(pow(inputs[0], inputs[1])))
		