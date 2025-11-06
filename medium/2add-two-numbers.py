from typing import Optional
import unittest

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode]) ->Optional[ListNode]:
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
            node = ListNode(n,node)
            total = total - n * (10 ** (length - i - 1))
        
        return node
        
        
        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_addTwoNumbers1(self):
        l1 = ListNode(2,ListNode(4,ListNode(3)))
        l2 = ListNode(5,ListNode(6,ListNode(4)))
        result = self.instance.addTwoNumbers(l1,l2)
        
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)
        
    def test_addTwoNumbers2(self):
        l1 = ListNode(0,None)
        l2 = ListNode(0,None)
        result = self.instance.addTwoNumbers(l1,l2)
        
        self.assertEqual(result.val, 0)
        self.assertEqual(result.next, None)   
        
    def test_addTwoNumbers3(self):
        l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
        l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
        result = self.instance.addTwoNumbers(l1,l2)
        
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
