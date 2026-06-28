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
            elif nums[low] < temp:
                if nums[low] <= target < temp:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if temp < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
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
                
                
                    
                    
                