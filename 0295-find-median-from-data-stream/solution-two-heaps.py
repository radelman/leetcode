# this solution is much better than the binary tree one.  a little faster, but
# really great on memory

import heapq

class Heap:
    def __init__(self, factor: int) -> None:
        """
        use factor = 1 for a min heap and -1 for a max heap.
        """

        self.nums = []
        self.factor = factor

    def push(self, num: int) -> None:
        heapq.heappush(self.nums, self.factor * num)

    def __len__(self) -> int:
        return len(self.nums)

    def peak(self) -> int:
        return self.nums[0] / self.factor

    def pop(self) -> int:
        return heapq.heappop(self.nums) / self.factor

    def pushpop(self, num: int) -> int:
        return heapq.heappushpop(self.nums, self.factor * num) / self.factor

class MedianFinder:
    def __init__(self):
        self.left = Heap(-1) # max heap
        self.left.push(-1000000)
        self.middle = 0.0
        self.right = Heap(1) # min heap
        self.right.push(1000000)

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if num < self.middle:
                self.left.push(num)
            else:
                self.right.push(num)

        elif len(self.left) > len(self.right):
            if num < self.middle:
                self.right.push(self.left.pushpop(num))
            else:
                self.right.push(num)

        else:
            if num < self.middle:
                self.left.push(num)
            else:
                self.left.push(self.right.pushpop(num))

        self.middle = (self.left.peak() + self.right.peak()) / 2.0

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return self.middle
        elif len(self.left) > len(self.right):
            return self.left.peak()
        else:
            return self.right.peak()

def main() -> None:
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())

if __name__ == '__main__':
    main()
