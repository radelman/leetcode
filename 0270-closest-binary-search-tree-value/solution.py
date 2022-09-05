from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_left = self.closestValue(root.left, target) if root.left is not None else 1e20
        closest_right = self.closestValue(root.right, target) if root.right is not None else 1e20

        distance_left = abs(closest_left - target)
        distance_center = abs(root.val - target)
        distance_right = abs(closest_right - target)

        if distance_left < distance_center and distance_left < distance_right:
            return closest_left
        elif distance_center < distance_right:
            return root.val
        else:
            return closest_right

def main() -> None:
    test_cases = [
        (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3.714286),
        (TreeNode(1), 4.428571),
    ]

    solution = Solution();

    for inputs in test_cases:
        root, target = inputs

        test = solution.closestValue(root, target)

        print(test)

if __name__ == '__main__':
    main()
