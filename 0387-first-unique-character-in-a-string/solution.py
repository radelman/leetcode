from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = defaultdict(int)

        for c in s:
            char_counts[c] += 1

        for i, c in enumerate(s):
            if char_counts[c] == 1:
                return i

        return -1

def main() -> None:
	test_cases = [
        "leetcode",
        "loveleetcode",
        "aabb",
	]

	solution = Solution();

	for inputs in test_cases:
		s = inputs

		test = solution.firstUniqChar(s)

		print(test)

if __name__ == '__main__':
	main()
