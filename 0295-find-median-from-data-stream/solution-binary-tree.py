# this solution works, but is very slow and memory-intensive according to
# leetcode.  there is probably a better way

class Node:
    def __init__(self, num: int) -> None:
        self.num = num
        self.count = 1
        self.left = None
        self.left_count = 0
        self.right = None
        self.right_count = 0

    def addNum(self, num: int) -> "Node":
        if num == self.num:
            self.count += 1

        elif num < self.num:
            if self.left is not None:
                self.left = self.left.addNum(num)
            else:
                self.left = Node(num)

            self.left_count += 1

        else:
            if self.right is not None:
                self.right = self.right.addNum(num)
            else:
                self.right = Node(num)

            self.right_count += 1

        # balance the tree if necessary

        # A is heavier than B, so rotate right
        #
        #        node               A
        #      A      B   -->   C       node
        #    C   D                    D      B

        if self.left_count - self.right_count > 1:
            A = self.left
            self.left = A.right
            self.left_count = A.right_count
            A.right = self
            A.right_count = self.left_count + self.count + self.right_count
            return A

        # B is heavier than A, so rotate left
        #
        #        node                      B
        #      A      B     -->     node       D
        #           C   D         A      C

        if self.right_count - self.left_count > 1:
            B = self.right
            self.right = B.left
            self.right_count = B.left_count
            B.left = self
            B.left_count = self.left_count + self.count + self.right_count
            return B

        # balanced enough

        return self

    def findMedian(self, left_count, right_count) -> float:
        #        /       |       \
        # prev left     node     prev right
        #               /  \
        #              /    \
        #           left    right

        mid = (
              left_count       # <-- (1) } nodes to the left
            + self.left_count  # <-- (2) }
            + self.count       # <-- (3) } current node and children (the median should be in here)
            + self.right_count # <-- (4) }
            + right_count      # <-- (5) } nodes to the right
        ) // 2

        acc = left_count

        # (2)
        acc += self.left_count
        if acc > mid:
            return self.left.findMedian(
                left_count,
                self.count + self.right_count + right_count,
            )

        # (3)
        acc += self.count
        if acc > mid:
            return self.num

        # (4)
        acc += self.right_count
        if acc > mid:
            return self.right.findMedian(
                left_count + self.left_count + self.count,
                right_count,
            )

class MedianFinder:
    def __init__(self):
        self.root = None
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.root is None:
            self.root = Node(num)
        else:
            self.root = self.root.addNum(num)

    def findMedian(self) -> float:
        count = (
              self.root.left_count
            + self.root.count
            + self.root.right_count
        )

        if count % 2 == 1:
            return self.root.findMedian(0, 0)
        else:
            return (
                  self.root.findMedian(1, 0)
                + self.root.findMedian(0, 0)
            ) / 2.0

def main() -> None:
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())

if __name__ == '__main__':
    main()
