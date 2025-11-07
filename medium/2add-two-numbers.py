from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """convert to string to a valid number, this will cost some compute

        Args:
            l1 (Optional[ListNode]): _description_
            l2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """        
        multiple1 = 1
        multiple2 = 1
        value1 = l1.val
        value2 = l2.val
        total1 = value1 * multiple1
        total2 = value2 * multiple2

        while l1.next is not None:
            multiple1 = multiple1 * 10
            v1 = l1.next
            total1 = total1 + v1.val * multiple1
            l1 = v1

        while l2.next is not None:
            multiple2 = multiple2 * 10
            v2 = l2.next
            total2 = total2 + v2.val * multiple2
            l2 = v2

        total = total1 + total2

        length = len(str(total))

        node = None
        for i in range(length):
            n = int(total / (10 ** (length - i - 1)))
            node = ListNode(n, node)
            total = total - n * (10 ** (length - i - 1))

        return node

    def addTwoNumbers1(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """only compute current position number to get result, so save memory and compute.

        Args:
            l1 (Optional[ListNode]): _description_
            l2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """        
        dummy = ListNode
        curr = dummy
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            value = total % 10

            node = ListNode(value)
            curr.next = node
            curr = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_addTwoNumbers1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        result = self.instance.addTwoNumbers1(l1, l2)

        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)

    def test_addTwoNumbers2(self):
        l1 = ListNode(0, None)
        l2 = ListNode(0, None)
        result = self.instance.addTwoNumbers1(l1, l2)

        self.assertEqual(result.val, 0)
        self.assertEqual(result.next, None)

    def test_addTwoNumbers3(self):
        l1 = ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
            ),
        )
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        result = self.instance.addTwoNumbers1(l1, l2)

        self.assertEqual(result.val, 8)
        self.assertEqual(result.next.val, 9)
        self.assertEqual(result.next.next.val, 9)
        self.assertEqual(result.next.next.next.val, 9)
        self.assertEqual(result.next.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.next.next.val, 0)
        self.assertEqual(result.next.next.next.next.next.next.next.val, 1)


if __name__ == "__main__":
    unittest.main()
