import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# this solution is *fast*, but kind of bad on memory.  i think one possible
# improvement is to create a new ListNode class that has a __lt__ method.  then
# there's no need for the (val, index, node) tuples in the heap
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        index = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, index, node))
                index += 1

        if not heap:
            return None

        head = None
        current = None

        while heap:
            val, index, node = heapq.heappop(heap)

            if val == 1000000:
                break

            if not current:
                current = node
            else:
                current.next = node
                current = current.next

            if not head:
                head = current

            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

        return head

def print_list(list1: Optional[ListNode]) -> None:
    vals = []
    while list1 is not None:
        vals.append(list1.val)
        list1 = list1.next
    print(vals)

def main() -> None:
    test_cases = [
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ],
        [
        ],
        [
            None,
        ]
	]

    solution = Solution();

    for inputs in test_cases:
        lists = inputs

        test = solution.mergeKLists(lists)

        print_list(test)

if __name__ == '__main__':
    main()
