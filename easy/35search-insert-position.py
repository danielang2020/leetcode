from typing import List
import unittest

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            temp = nums[mid]
            
            if temp == target:
                return mid
            elif temp > target:
                high = mid - 1
            else:
                low = mid + 1
            
        return low
    
              
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_search(self):
        self.assertEqual(self.instance.searchInsert([1,3,5,6],5),2)
        self.assertEqual(self.instance.searchInsert([1,3,5,6],2),1)
        self.assertEqual(self.instance.searchInsert([1,3,5,6],7),4)
        self.assertEqual(self.instance.searchInsert([1,3],2),1)


if __name__ == "__main__":
    unittest.main()