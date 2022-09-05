from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            ret = list1
            ret.next = self.mergeTwoLists(list1.next, list2)
        else:
            ret = list2
            ret.next = self.mergeTwoLists(list1, list2.next)

        return ret

class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head

        while list1 is not None or list2 is not None:
            if list1 is None:
                current.next = list2
                break

            if list2 is None:
                current.next = list1
                break

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        return head

def print_list(list1: Optional[ListNode]) -> None:
    vals = []
    while list1 is not None:
        vals.append(list1.val)
        list1 = list1.next
    print(vals)

def main() -> None:
    test_cases = [
        (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))),
        (None, None),
        (None, ListNode(0)),
    ]

    # solution = Solution1();
    solution = Solution2();

    for inputs in test_cases:
        list1, list2 = inputs

        test = solution.mergeTwoLists(list1, list2)

        print_list(test)

if __name__ == '__main__':
    main()
