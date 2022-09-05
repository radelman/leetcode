from itertools import accumulate

# this solution works, but is slow.  i tried speeding things up with a hashmap
# of indices of matching first characters, and a comparison of character sums
# before doing a direct comparison of strings.  probably not the best choice of
# algorithms
class Solution:
    def countSubstrings(self, s: str) -> int:
        acc = [0] + [x for x in accumulate([ord(c) for c in s])]

        idxs = {c: [] for c in "abcdefghijklmnopqrstuvwxyz"}

        for i, c in enumerate(s):
            idxs[c].append(i)

        count = 0

        for i, a in enumerate(s):
            for z in idxs[a]:
                if z >= i:
                    k = z + 1

                    j = (i + k) // 2

                    if (k - i) % 2 == 0:
                        if acc[j] - acc[i] == acc[k] - acc[j]:
                            if s[i : j] == "".join(reversed(s[j : k])):
                                count += 1

                    else:
                        if acc[j] - acc[i] == acc[k] - acc[j + 1]:
                            if s[i : j] == "".join(reversed(s[j + 1 : k])):
                                count += 1

        return count

def main() -> None:
    test_cases = [
        "abc",
        "aaa",
	]

    solution = Solution();

    for inputs in test_cases:
        s = inputs

        test = solution.countSubstrings(s)

        print(test)

if __name__ == '__main__':
    main()
