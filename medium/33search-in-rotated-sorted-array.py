from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            temp = nums[mid]
            
            if temp == target:
                return mid
            elif nums[low] <= temp: # first check left if it's sorted (including single element)
                if nums[low] <= target < temp: # then check as usual in sorted range
                    high = mid - 1
                else:
                    low = mid + 1 # next go to unsorted part
            else: # first check right if it's sorted
                if temp < target <= nums[high]: # then check as usual in sorted range
                    low = mid + 1
                else:
                    high = mid - 1 # next go to unsorted part
                    
        return -1
                    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_search(self):
        self.assertEqual(self.instance.search([4,5,6,7,0,1,2],0),4)
        self.assertEqual(self.instance.search([4,5,6,7,0,1,2],3),-1)
        self.assertEqual(self.instance.search([1],0),-1)


if __name__ == "__main__":
    unittest.main()
                
                
                    
                    
                