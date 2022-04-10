class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if len(needle) == 0:
			return 0
		
		cumsum = [ord(c) for c in haystack]
		for i in range(1, len(cumsum)):
			cumsum[i] = cumsum[i - 1] + cumsum[i]
			
		target = sum([ord(c) for c in needle])
		
		for i in range(len(haystack) - len(needle) + 1):
			first = cumsum[i - 1] if i > 0 else 0
			last = cumsum[i + len(needle) - 1]
			
			attempt = last - first
			
			if attempt == target:
				if haystack[i : i + len(needle)] == needle:
					return i
				
		return -1
	
def main() -> None:
	test_cases = [
	["hello", "ll"],
	["aaaaa", "bba"]
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		haystack, needle = inputs
		
		test = solution.strStr(haystack, needle)
		
		print(test)
		
if __name__ == '__main__':
	main()
	