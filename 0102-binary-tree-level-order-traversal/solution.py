from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = [[root]]

        for prev in levels:
            current = []

            for i, node in enumerate(prev):
                if node.left:
                    current.append(node.left)

                if node.right:
                    current.append(node.right)

                prev[i] = node.val

            if len(current) > 0:
                levels.append(current)
            else:
                break

        return levels

def main() -> None:
    test_cases = [
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(1),
        None,
    ]

    solution = Solution();

    for inputs in test_cases:
        root = inputs

        test = solution.levelOrder(root)

        print(test)

if __name__ == '__main__':
    main()
