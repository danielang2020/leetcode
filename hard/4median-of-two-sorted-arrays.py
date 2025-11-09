from typing import List
import unittest


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            first = nums1[length // 2 - 1]
            second = nums1[length // 2]
            return (first + second) / 2
        else:
            index = length // 2
            return nums1[index]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_findMedianSortedArrays1(self):
        result = self.instance.findMedianSortedArrays([1,3],[2])

        self.assertEqual(result, 2)
        
    def test_findMedianSortedArrays2(self):
        result = self.instance.findMedianSortedArrays([1,2],[3,4])

        self.assertEqual(result, 2.5)     
        
    def test_findMedianSortedArrays3(self):
        result = self.instance.findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1])

        self.assertEqual(result, 0)                
    

     


if __name__ == "__main__":
    unittest.main()